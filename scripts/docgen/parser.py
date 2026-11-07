"""
Source code parser for C++, C#, and Python files.
Extracts function definitions, declarations, namespaces, classes, and comments.
"""
import os
import re
from typing import List, Dict, Tuple, Optional
from .models import FunctionInfo
from .config import REPO_ROOT, SUBSYSTEM_RULES, CORE_MODULES, VENDOR_DIRS, SOURCE_EXTENSIONS

class SourceParser:
    def __init__(self, repo_root: str = REPO_ROOT):
        self.repo_root = repo_root

    def discover_files(self, modules: List[str] = CORE_MODULES) -> List[str]:
        """Discovers all source files to scan."""
        found_files = []
        for mod in modules:
            mod_path = os.path.join(self.repo_root, mod)
            if not os.path.exists(mod_path):
                continue
            for root, dirs, files in os.walk(mod_path):
                # Filter out vendor dirs
                rel_root = os.path.relpath(root, self.repo_root)
                parts = rel_root.split(os.sep)
                if any(p in VENDOR_DIRS for p in parts):
                    continue
                for f in files:
                    ext = os.path.splitext(f)[1].lower()
                    if ext in SOURCE_EXTENSIONS:
                        found_files.append(os.path.join(rel_root, f))
        return sorted(found_files)

    def determine_subsystem(self, file_path: str) -> Tuple[str, str]:
        """Returns (module, subsystem_name) based on file path."""
        norm_path = file_path.replace('\\', '/')
        parts = norm_path.split('/')
        module = parts[0]
        
        for rule, sub_name in SUBSYSTEM_RULES:
            if f"/{rule}/" in norm_path or norm_path.startswith(f"{rule}/") or norm_path.endswith(f"/{rule}") or rule == module:
                return module, sub_name
        return module, "App - Engine Core"

    def parse_file(self, rel_path: str) -> List[FunctionInfo]:
        """Parses a single file and returns all functions found."""
        abs_path = os.path.join(self.repo_root, rel_path)
        try:
            with open(abs_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception:
            return []

        ext = os.path.splitext(rel_path)[1].lower()
        if ext in ('.cpp', '.c', '.h', '.hpp', '.mm', '.m'):
            return self._parse_cpp_file(rel_path, content)
        elif ext == '.cs':
            return self._parse_csharp_file(rel_path, content)
        elif ext == '.py':
            return self._parse_python_file(rel_path, content)
        return []

    def _extract_docstring(self, content: str, start_idx: int) -> str:
        """Extracts comment immediately preceding start_idx."""
        prefix = content[:start_idx].rstrip()
        lines = prefix.splitlines()
        if not lines:
            return ""
        
        doc_lines = []
        i = len(lines) - 1
        while i >= 0:
            line = lines[i].strip()
            if line.startswith('//') or line.startswith('*') or line.startswith('/*') or line.endswith('*/'):
                cleaned = line.lstrip('/*').rstrip('*/').strip().lstrip('//').strip()
                if cleaned:
                    doc_lines.insert(0, cleaned)
                i -= 1
            else:
                break
            if len(doc_lines) > 15:
                break
        return " ".join(doc_lines).strip()

    def _parse_cpp_file(self, rel_path: str, content: str) -> List[FunctionInfo]:
        module, subsystem = self.determine_subsystem(rel_path)
        functions = []

        # Regex to locate candidate function definition headers
        # Matches: [modifiers] [ReturnType] [ClassName::]FunctionName(params) [const] {
        func_regex = re.compile(
            r'(?:^|\n)\s*'
            r'(?P<template>template\s*<[^>]*>\s*)?'
            r'(?P<modifiers>(?:(?:static|inline|virtual|explicit|friend|const|unsigned|extern|__forceinline|RBX_DEPRECATED)\s+)*)'
            r'(?P<return>(?:[\w:~<>*&]+(?:\s+[\w:~<>*&]+)?))\s+'
            r'(?P<name>[\w~]+(?:::[a-zA-Z0-9_~]+)*)\s*'
            r'\((?P<params>[^)]*)\)\s*'
            r'(?P<const>const\s*)?'
            r'(?P<volatile>volatile\s*)?'
            r'(?P<throw>throw\s*\([^)]*\)\s*)?'
            r'(?P<noexcept>noexcept\s*)?'
            r'\{',
            re.MULTILINE
        )

        for match in func_regex.finditer(content):
            name = match.group('name').strip()
            ret_type = match.group('return').strip()
            params = match.group('params').strip()
            modifiers_str = (match.group('modifiers') or '').strip()
            modifiers = [m for m in modifiers_str.split() if m]
            if match.group('const'):
                modifiers.append('const')

            # Filter out C++ control structures that might match
            if name in ('if', 'for', 'while', 'switch', 'catch', 'do', 'BOOST_AUTO_TEST_CASE', 'BOOST_FIXTURE_TEST_CASE'):
                continue
            if ret_type in ('if', 'for', 'while', 'switch', 'return', 'typedef', 'else'):
                continue

            # Calculate line number
            line_no = content[:match.start()].count('\n') + 1

            # Extract balanced brace body
            brace_count = 1
            pos = match.end()
            body_start = pos
            n = len(content)
            while pos < n and brace_count > 0:
                ch = content[pos]
                if ch == '{':
                    brace_count += 1
                elif ch == '}':
                    brace_count -= 1
                elif ch == '"':
                    # Skip string literal
                    pos += 1
                    while pos < n and content[pos] != '"':
                        if content[pos] == '\\':
                            pos += 1
                        pos += 1
                elif ch == '\'':
                    pos += 1
                    while pos < n and content[pos] != '\'':
                        if content[pos] == '\\':
                            pos += 1
                        pos += 1
                pos += 1

            body = content[body_start:pos-1].strip()
            docstring = self._extract_docstring(content, match.start())

            short_name = name.split('::')[-1]
            qualified_name = name

            func_info = FunctionInfo(
                name=short_name,
                qualified_name=qualified_name,
                return_type=ret_type,
                params=params,
                modifiers=modifiers,
                file_path=rel_path,
                line_number=line_no,
                module=module,
                subsystem=subsystem,
                docstring=docstring,
                body=body,
                is_definition=True
            )
            functions.append(func_info)

        return functions

    def _parse_csharp_file(self, rel_path: str, content: str) -> List[FunctionInfo]:
        module, subsystem = self.determine_subsystem(rel_path)
        functions = []

        cs_method_regex = re.compile(
            r'(?:^|\n)\s*'
            r'(?P<modifiers>(?:(?:public|private|protected|internal|static|virtual|override|abstract|async)\s+)*)'
            r'(?P<return>[\w<>[\]?]+)\s+'
            r'(?P<name>\w+)\s*'
            r'\((?P<params>[^)]*)\)\s*'
            r'\{',
            re.MULTILINE
        )

        for match in cs_method_regex.finditer(content):
            name = match.group('name').strip()
            ret_type = match.group('return').strip()
            params = match.group('params').strip()
            modifiers = [m for m in (match.group('modifiers') or '').split() if m]

            if name in ('if', 'for', 'while', 'switch', 'catch', 'using', 'lock'):
                continue

            line_no = content[:match.start()].count('\n') + 1

            # Extract body
            brace_count = 1
            pos = match.end()
            body_start = pos
            n = len(content)
            while pos < n and brace_count > 0:
                ch = content[pos]
                if ch == '{':
                    brace_count += 1
                elif ch == '}':
                    brace_count -= 1
                pos += 1

            body = content[body_start:pos-1].strip()
            docstring = self._extract_docstring(content, match.start())

            functions.append(FunctionInfo(
                name=name,
                qualified_name=name,
                return_type=ret_type,
                params=params,
                modifiers=modifiers,
                file_path=rel_path,
                line_number=line_no,
                module=module,
                subsystem=subsystem,
                docstring=docstring,
                body=body,
                is_definition=True
            ))

        return functions

    def _parse_python_file(self, rel_path: str, content: str) -> List[FunctionInfo]:
        module, subsystem = self.determine_subsystem(rel_path)
        functions = []

        py_def_regex = re.compile(
            r'(?:^|\n)\s*def\s+(?P<name>\w+)\s*\((?P<params>[^)]*)\)\s*(?:->\s*(?P<return>[^:]+))?:',
            re.MULTILINE
        )

        for match in py_def_regex.finditer(content):
            name = match.group('name').strip()
            params = match.group('params').strip()
            ret_type = (match.group('return') or 'Any').strip()
            line_no = content[:match.start()].count('\n') + 1

            docstring = self._extract_docstring(content, match.start())

            functions.append(FunctionInfo(
                name=name,
                qualified_name=name,
                return_type=ret_type,
                params=params,
                modifiers=[],
                file_path=rel_path,
                line_number=line_no,
                module=module,
                subsystem=subsystem,
                docstring=docstring,
                body="",
                is_definition=True
            ))

        return functions

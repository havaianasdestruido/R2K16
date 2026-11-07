"""
Test suite analyzer and test-to-function coverage mapper.
Parses BOOST and MSUnit test cases, assertions, and maps them to codebase functions.
"""
import os
import re
from typing import List, Dict, Set, Tuple
from collections import defaultdict
from .models import FunctionInfo, TestCaseInfo, TestUsageInfo
from .config import REPO_ROOT, TEST_MODULES, TEST_EXTENSIONS, VENDOR_DIRS

class TestMapper:
    def __init__(self, repo_root: str = REPO_ROOT):
        self.repo_root = repo_root
        self.test_cases: List[TestCaseInfo] = []
        # Mapping from function short name -> list of test cases
        self.func_to_tests: Dict[str, List[TestCaseInfo]] = defaultdict(list)

    def scan_tests(self) -> None:
        """Discovers and parses all test cases across the repository."""
        self.test_cases.clear()
        self.func_to_tests.clear()

        for test_mod in TEST_MODULES:
            mod_path = os.path.join(self.repo_root, test_mod)
            if not os.path.exists(mod_path):
                continue

            for root, dirs, files in os.walk(mod_path):
                rel_root = os.path.relpath(root, self.repo_root)
                parts = rel_root.split(os.sep)
                if any(p in VENDOR_DIRS for p in parts):
                    continue

                for f in files:
                    ext = os.path.splitext(f)[1].lower()
                    if ext in TEST_EXTENSIONS:
                        rel_path = os.path.join(rel_root, f)
                        self._parse_test_file(rel_path)

        # Build index from called function tokens to test cases
        for tc in self.test_cases:
            for token in tc.called_functions:
                self.func_to_tests[token].append(tc)

    def _parse_test_file(self, rel_path: str) -> None:
        abs_path = os.path.join(self.repo_root, rel_path)
        try:
            with open(abs_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception:
            return

        ext = os.path.splitext(rel_path)[1].lower()
        if ext == '.cs':
            self._parse_csharp_tests(rel_path, content)
        else:
            self._parse_cpp_tests(rel_path, content)

    def _parse_cpp_tests(self, rel_path: str, content: str) -> None:
        # Determine suite name
        suite_match = re.search(r'BOOST_AUTO_TEST_SUITE\s*\(\s*(\w+)\s*\)', content)
        default_suite = suite_match.group(1) if suite_match else os.path.splitext(os.path.basename(rel_path))[0]

        # Case pattern
        case_regex = re.compile(
            r'(?:BOOST_AUTO_TEST_CASE|BOOST_FIXTURE_TEST_CASE)\s*\(\s*(?P<name>\w+)(?:\s*,\s*(?P<fixture>\w+))?\s*\)\s*\{',
            re.MULTILINE
        )

        for match in case_regex.finditer(content):
            case_name = match.group('name')
            fixture = match.group('fixture') or ""
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

            # Extract called functions
            called_tokens = set(re.findall(r'(?:->|\.|\b)([a-zA-Z_]\w*)\s*\(', body))
            # Also extract namespaces/class scoped calls like RBX::format or TaskScheduler::singleton
            scoped_tokens = set(re.findall(r'\b([a-zA-Z_]\w*)::([a-zA-Z_]\w*)\b', body))
            for cls, fn in scoped_tokens:
                called_tokens.add(fn)

            # Extract assertions
            assertions = re.findall(r'(BOOST_\w+)\s*\(([^;]+)\)', body)
            formatted_asserts = [f"{m[0]}({m[1].strip()})" for m in assertions[:5]]

            tc = TestCaseInfo(
                suite_name=default_suite,
                test_name=case_name,
                file_path=rel_path,
                line_number=line_no,
                fixture=fixture,
                body=body,
                called_functions=called_tokens,
                assertions=formatted_asserts
            )
            self.test_cases.append(tc)

    def _parse_csharp_tests(self, rel_path: str, content: str) -> None:
        default_suite = os.path.splitext(os.path.basename(rel_path))[0]
        method_regex = re.compile(
            r'\[TestMethod\]\s*(?:public\s+)?void\s+(?P<name>\w+)\s*\([^)]*\)\s*\{',
            re.MULTILINE
        )

        for match in method_regex.finditer(content):
            case_name = match.group('name')
            line_no = content[:match.start()].count('\n') + 1

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
            called_tokens = set(re.findall(r'(?:->|\.|\b)([a-zA-Z_]\w*)\s*\(', body))
            assertions = re.findall(r'(Assert\.\w+)\s*\(([^;]+)\)', body)
            formatted_asserts = [f"{m[0]}({m[1].strip()})" for m in assertions[:5]]

            tc = TestCaseInfo(
                suite_name=default_suite,
                test_name=case_name,
                file_path=rel_path,
                line_number=line_no,
                fixture="",
                body=body,
                called_functions=called_tokens,
                assertions=formatted_asserts
            )
            self.test_cases.append(tc)

    def map_tests_to_function(self, func: FunctionInfo) -> List[TestUsageInfo]:
        """Finds all test usages of a given function."""
        test_usages = []
        matching_cases = self.func_to_tests.get(func.name, [])

        for tc in matching_cases:
            # Check how func is used in this test
            is_asserted = any(func.name in a for a in tc.assertions)
            is_benchmark = "1000000" in tc.body or "perf" in tc.test_name.lower() or "benchmark" in tc.test_name.lower()
            is_fixture = tc.fixture != "" and (func.name in tc.fixture or "fixture" in tc.test_name.lower())

            if is_asserted:
                kind = "direct_assertion"
            elif is_benchmark:
                kind = "performance_benchmark"
            elif is_fixture:
                kind = "fixture_setup"
            else:
                kind = "direct_call"

            relevant_asserts = [a for a in tc.assertions if func.name in a]
            if not relevant_asserts and tc.assertions:
                relevant_asserts = tc.assertions[:2]

            snippet = ""
            for line in tc.body.splitlines():
                if func.name in line:
                    snippet = line.strip()
                    break

            test_usages.append(TestUsageInfo(
                test_file=tc.file_path,
                suite_name=tc.suite_name,
                test_name=tc.test_name,
                line_number=tc.line_number,
                usage_kind=kind,
                assertions=relevant_asserts,
                context_snippet=snippet
            ))

        return test_usages

#!/usr/bin/env python3
"""Generate a browsable, best-effort syntax index of tracked source files."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

from tree_sitter import Language, Parser
import tree_sitter_c, tree_sitter_cpp, tree_sitter_python, tree_sitter_lua
import tree_sitter_javascript, tree_sitter_c_sharp, tree_sitter_java

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'website/static/generated'
LANGUAGES = {
    '.c': tree_sitter_c, '.h': tree_sitter_cpp, '.cc': tree_sitter_cpp,
    '.cpp': tree_sitter_cpp, '.cxx': tree_sitter_cpp, '.hpp': tree_sitter_cpp,
    '.hh': tree_sitter_cpp, '.hxx': tree_sitter_cpp, '.ipp': tree_sitter_cpp,
    '.py': tree_sitter_python, '.lua': tree_sitter_lua, '.js': tree_sitter_javascript,
    '.jsx': tree_sitter_javascript, '.cs': tree_sitter_c_sharp, '.java': tree_sitter_java,
}
DEFS = {'function_definition', 'function_declaration', 'method_declaration',
        'constructor_declaration', 'local_function_statement', 'generator_function_declaration'}
CALLS = {'call_expression', 'call', 'method_invocation', 'function_call', 'invocation_expression'}
TEST_PATH = re.compile(r'(test|spec)', re.I)
IDENT = re.compile(r'[A-Za-z_$~][\w$~]*')

def walk(node):
    stack = [node]
    while stack:
        n = stack.pop()
        yield n
        stack.extend(reversed(n.children))

def text(source, node):
    return source[node.start_byte:node.end_byte].decode('utf-8', 'replace')

def name_of(node, source):
    # Field names vary by grammar; follow declarators to the identifier, but
    # never descend into parameters, where identifiers are argument names.
    n = node.child_by_field_name('name') or node.child_by_field_name('declarator')
    while n:
        if n.type in ('identifier', 'field_identifier', 'property_identifier', 'destructor_name', 'operator_name'):
            return text(source, n)
        if n.type in ('qualified_identifier', 'scoped_identifier'):
            n = n.child_by_field_name('name') or n.named_children[-1]
        else:
            n = n.child_by_field_name('declarator') or n.child_by_field_name('name')
    return None

def bucket(name):
    return hashlib.sha256(name.encode()).hexdigest()[:2]

def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=True, separators=(',', ':')), encoding='utf-8')

def generate(root=ROOT, out=OUT):
    # Only tracked files, including tracked changes. Avoid parsing build outputs.
    paths = subprocess.check_output(['git', '-C', str(root), 'ls-files', '-z']).decode('utf-8', 'surrogateescape').split('\0')
    parsers = {ext: Parser(Language(mod.language())) for ext, mod in LANGUAGES.items()}
    groups, lookup = {}, {}
    counts = {'files': 0, 'functions': 0, 'test_calls': 0, 'parse_errors': 0, 'unreadable': 0}
    for path in paths:
        ext = Path(path).suffix.lower()
        if not path or ext not in parsers or path.startswith('website/static/generated/'):
            continue
        try:
            source = (root / path).read_bytes()
        except OSError:
            counts['unreadable'] += 1
            continue
        tree = parsers[ext].parse(source)
        lines = source.splitlines() if TEST_PATH.search(path) else []
        counts['files'] += 1
        counts['parse_errors'] += int(tree.root_node.has_error)
        parts = path.split('/')
        group = '/'.join(parts[:4]) if parts[0] == 'Library' and len(parts) > 4 else '/'.join(parts[:-1]) if parts[0] == 'Library' and len(parts) > 1 else parts[0] if len(parts) > 1 else '(root)'
        is_test = bool(TEST_PATH.search(path))
        for n in walk(tree.root_node):
            if n.type in DEFS:
                name = name_of(n, source)
                body = n.child_by_field_name('body')
                if not name or not body:  # declarations alone do not define behavior
                    continue
                signature = source[n.start_byte:body.start_byte].decode('utf-8', 'replace').strip()
                calls = []
                controls = set()
                for child in walk(body):
                    if child.type in CALLS:
                        target = child.child_by_field_name('function') or child.child_by_field_name('name')
                        if target:
                            identifiers = IDENT.findall(text(source, target))
                            if identifiers and identifiers[-1] not in calls:
                                calls.append(identifiers[-1])
                    if child.type in ('if_statement', 'for_statement', 'while_statement', 'switch_statement', 'return_statement', 'throw_statement', 'try_statement'):
                        controls.add(child.type.replace('_statement', ''))
                normalized = re.sub(rb'\s+', b' ', source[body.start_byte:body.end_byte]).strip()
                item = {'name': name, 'path': path, 'line': n.start_point.row + 1,
                        'end': n.end_point.row + 1, 'signature': signature[:1000],
                        'calls': calls[:30], 'controls': sorted(controls),
                        'hash': hashlib.sha256(normalized).hexdigest()[:16]}
                groups.setdefault(group, []).append(item)
                lookup.setdefault(bucket(name), {}).setdefault(name, {'definitions': [], 'tests': []})['definitions'].append([path, item['line'], item['hash']])
                counts['functions'] += 1
            if is_test and n.type in CALLS:
                target = n.child_by_field_name('function') or n.child_by_field_name('name')
                if target:
                    identifiers = IDENT.findall(text(source, target))
                    if identifiers:
                        name = identifiers[-1]
                        parent = n.parent
                        while parent and parent.type not in DEFS:
                            parent = parent.parent
                        context = name_of(parent, source) if parent else None
                        line_text = lines[n.start_point.row].decode('utf-8', 'replace').strip()[:240] if n.start_point.row < len(lines) else ''
                        lookup.setdefault(bucket(name), {}).setdefault(name, {'definitions': [], 'tests': []})['tests'].append([path, n.start_point.row + 1, context, line_text])
                        counts['test_calls'] += 1
    out.mkdir(parents=True, exist_ok=True)
    # Remove only files owned by this generator, so obsolete shards cannot linger.
    for folder in ('groups', 'names'):
        target = out / folder
        if target.exists():
            for f in target.glob('*.json'):
                f.unlink()
    manifest = []
    for group, items in sorted(groups.items()):
        key = hashlib.sha256(group.encode()).hexdigest()[:16]
        write_json(out / 'groups' / (key + '.json'), items)
        manifest.append({'name': group, 'key': key, 'count': len(items)})
    for key, items in lookup.items():
        write_json(out / 'names' / (key + '.json'), items)
    revision = os.getenv('GITHUB_SHA') or subprocess.check_output(['git', '-C', str(root), 'rev-parse', 'HEAD'], text=True).strip()
    write_json(out / 'manifest.json', {'revision': revision, 'counts': counts, 'groups': manifest, 'extensions': sorted(LANGUAGES)})
    print(json.dumps(counts, indent=2))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT, help='Git checkout to scan')
    parser.add_argument('--out', type=Path, default=OUT, help='Output directory')
    args = parser.parse_args()
    generate(args.root.resolve(), args.out.resolve())

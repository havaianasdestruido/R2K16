#!/usr/bin/env python3
"""
R2K16 Codebase Documentation Generator CLI.
Automatically scans the codebase, extracts all functions, maps test usages,
analyzes internal logic, identifies platform divergences, and generates
the complete Docusaurus documentation website.
"""
import sys
import os
import argparse
import time

# Ensure scripts/ directory is in sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from scripts.docgen.config import REPO_ROOT, CODEBASE_DOCS_DIR, CORE_MODULES, TEST_MODULES
from scripts.docgen.parser import SourceParser
from scripts.docgen.analyzer import FunctionAnalyzer
from scripts.docgen.test_mapper import TestMapper
from scripts.docgen.divergence_detector import DivergenceDetector
from scripts.docgen.markdown_generator import MarkdownGenerator

def main():
    parser = argparse.ArgumentParser(description="Generate R2K16 Codebase Documentation")
    parser.add_argument("--output-dir", default=CODEBASE_DOCS_DIR, help="Destination directory for Docusaurus docs")
    parser.add_argument("--stats-only", action="store_true", help="Print codebase statistics without generating docs")
    parser.add_argument("--check", action="store_true", help="Validate documentation generator without writing files")
    args = parser.parse_args()

    start_time = time.time()
    print("=" * 70)
    print("R2K16 Codebase Documentation Generator")
    print(f"Repository Root: {REPO_ROOT}")
    print(f"Target Output:   {args.output_dir}")
    print("=" * 70)

    # 1. Discover and parse test cases
    print("[1/5] Scanning test suites and extracting test cases...")
    test_mapper = TestMapper(repo_root=REPO_ROOT)
    test_mapper.scan_tests()
    print(f"      -> Parsed {len(test_mapper.test_cases):,} test cases across {len(TEST_MODULES)} test modules.")

    # 2. Discover and parse source files
    print("[2/5] Discovering source files across core engine modules...")
    source_parser = SourceParser(repo_root=REPO_ROOT)
    source_files = source_parser.discover_files(CORE_MODULES)
    print(f"      -> Discovered {len(source_files):,} source files to analyze.")

    print("[3/5] Extracting function declarations and definitions...")
    all_functions = []
    for sf in source_files:
        funcs = source_parser.parse_file(sf)
        all_functions.extend(funcs)
    print(f"      -> Extracted {len(all_functions):,} functions across all subsystems.")

    # 3. Index and detect platform divergences
    print("[4/5] Analyzing internal implementation, test usages, and platform divergences...")
    divergence_detector = DivergenceDetector(repo_root=REPO_ROOT)
    divergence_detector.index_functions(all_functions)

    function_analyzer = FunctionAnalyzer()

    tested_count = 0
    divergent_count = 0

    for func in all_functions:
        # Internal analysis
        func.internal_analysis = function_analyzer.analyze(func)

        # Test mapping
        func.test_usage = test_mapper.map_tests_to_function(func)
        if func.test_usage:
            tested_count += 1

        # Divergence analysis
        func.divergence = divergence_detector.analyze_divergence(func)
        if func.divergence.has_platform_guards or func.divergence.multi_file_variants:
            divergent_count += 1

    print(f"      -> Analyzed {len(all_functions):,} functions:")
    print(f"         - Directly exercised in tests: {tested_count:,}")
    print(f"         - Platform-divergent implementations: {divergent_count:,}")

    if args.stats_only:
        print("Done (--stats-only specified).")
        return 0

    if args.check:
        print("Done (--check specified, no files written).")
        return 0

    # 4. Generate Docusaurus Markdown files
    print("[5/5] Generating Docusaurus Markdown documentation pages...")
    md_gen = MarkdownGenerator(output_dir=args.output_dir)
    md_gen.generate_all(all_functions, test_mapper.test_cases)
    
    elapsed = time.time() - start_time
    print("=" * 70)
    print(f"Documentation generation completed successfully in {elapsed:.2f}s!")
    print(f"Generated pages available under: {args.output_dir}")
    print("=" * 70)

    return 0

if __name__ == "__main__":
    sys.exit(main())

"""
Data models for codebase function and test representation.
"""
from dataclasses import dataclass, field
from typing import List, Dict, Set, Optional, Any

@dataclass
class TestUsageInfo:
    test_file: str
    suite_name: str
    test_name: str
    line_number: int
    usage_kind: str  # 'direct_assertion', 'direct_call', 'fixture_setup', 'performance_benchmark'
    assertions: List[str] = field(default_factory=list)
    context_snippet: str = ""

@dataclass
class DivergenceInfo:
    has_platform_guards: bool = False
    platform_guards: List[str] = field(default_factory=list)
    multi_file_variants: List[str] = field(default_factory=list)
    caller_divergences: List[str] = field(default_factory=list)
    summary: str = "Uniform behavior across all target platforms."

@dataclass
class InternalAnalysis:
    summary: str = ""
    control_flow: str = "Linear execution flow"
    memory_management: str = "Standard stack allocation"
    concurrency_thread_safety: str = "Unsynchronized / single-threaded context"
    error_handling_invariants: str = "Standard return value verification"
    called_functions: List[str] = field(default_factory=list)
    external_libraries: List[str] = field(default_factory=list)
    state_mutation: str = "Stateless or local modification"

@dataclass
class FunctionInfo:
    name: str
    qualified_name: str
    return_type: str
    params: str
    modifiers: List[str]
    file_path: str
    line_number: int
    module: str
    subsystem: str
    docstring: str = ""
    body: str = ""
    is_definition: bool = True
    internal_analysis: Optional[InternalAnalysis] = None
    test_usage: List[TestUsageInfo] = field(default_factory=list)
    divergence: Optional[DivergenceInfo] = None

@dataclass
class TestCaseInfo:
    suite_name: str
    test_name: str
    file_path: str
    line_number: int
    fixture: str = ""
    body: str = ""
    called_functions: Set[str] = field(default_factory=set)
    assertions: List[str] = field(default_factory=list)

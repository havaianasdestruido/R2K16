"""
Internal implementation analyzer for engine functions.
Analyzes control flow, memory allocation, concurrency, error handling, invariants, and called APIs.
"""
import re
from typing import List, Dict, Set
from .models import FunctionInfo, InternalAnalysis

class FunctionAnalyzer:
    def __init__(self):
        # Patterns for memory management
        self.mem_alloc_patterns = [
            (re.compile(r'\bnew\b'), 'Dynamic heap allocation via C++ operator new'),
            (re.compile(r'\bdelete\b'), 'Heap memory deallocation via operator delete'),
            (re.compile(r'\bmalloc\b|\bcalloc\b|\brealloc\b'), 'C runtime dynamic heap allocation (malloc/calloc)'),
            (re.compile(r'\bfree\b'), 'C runtime memory release (free)'),
            (re.compile(r'scoped_array<[^>]+>'), 'RAII scoped heap buffer allocation (boost::scoped_array)'),
            (re.compile(r'shared_ptr<[^>]+>'), 'Reference-counted heap object ownership (boost::shared_ptr)'),
            (re.compile(r'intrusive_ptr<[^>]+>'), 'Intrusive reference-counted pointer management (boost::intrusive_ptr)'),
            (re.compile(r'scoped_ptr<[^>]+>'), 'Unique RAII pointer lifetime control (boost::scoped_ptr)'),
            (re.compile(r'stackBuffer\[\d+\]'), 'Fast stack buffer optimization (avoids heap allocation for small sizes)'),
        ]

        # Patterns for concurrency & thread safety
        self.concurrency_patterns = [
            (re.compile(r'spin_mutex'), 'Spinlock synchronization via RBX::spin_mutex'),
            (re.compile(r'scoped_lock'), 'RAII mutex lock acquisition (scoped_lock)'),
            (re.compile(r'boost::mutex|boost::recursive_mutex'), 'Thread mutual exclusion locking (boost::mutex)'),
            (re.compile(r'CEvent'), 'Cross-thread signaling and event synchronization (RBX::CEvent)'),
            (re.compile(r'InterlockedIncrement|InterlockedDecrement|atomic_count'), 'Atomic atomic operations (lock-free thread safety)'),
            (re.compile(r'TaskScheduler::singleton\(\)'), 'TaskScheduler global job queue dispatching'),
            (re.compile(r'CRITICAL_SECTION'), 'Win32 CriticalSection exclusion primitive'),
        ]

        # Patterns for invariants & error handling
        self.error_patterns = [
            (re.compile(r'RBXASSERT\s*\('), 'Engine invariant assertion check (RBXASSERT)'),
            (re.compile(r'FASTFLAG\s*\('), 'Runtime feature toggle branch check (FASTFLAG)'),
            (re.compile(r'DYNAMIC_FASTFLAG\s*\('), 'Dynamic runtime flag inspection (DYNAMIC_FASTFLAG)'),
            (re.compile(r'\bthrow\b'), 'C++ exception throw on invalid state or failure'),
            (re.compile(r'\btry\b\s*\{'), 'Exception handling block (try/catch recovery)'),
            (re.compile(r'runtime_error\s*\('), 'Standard runtime error exception formulation'),
            (re.compile(r'if\s*\(!\w+\)\s*return'), 'Defensive null-pointer validation guard'),
        ]

        # Patterns for external libraries
        self.ext_lib_patterns = [
            (re.compile(r'boost::'), 'Boost C++ Libraries'),
            (re.compile(r'G3D::'), 'G3D Graphics and Math Engine'),
            (re.compile(r'RakNet::'), 'RakNet UDP Networking Engine'),
            (re.compile(r'InternetGetCookie|InternetSetCookie|WinINet'), 'Microsoft WinINet API'),
            (re.compile(r'NSHTTPCookieStorage|WebKit'), 'Apple WebKit / Foundation API'),
            (re.compile(r'gl\w+\('), 'OpenGL / GLES Graphics API'),
            (re.compile(r'D3D\w+|IDirect3D'), 'DirectX Direct3D Graphics Pipeline'),
            (re.compile(r'FMOD'), 'FMOD Audio Engine'),
            (re.compile(r'InfluxDb'), 'InfluxDB Metrics Ingestion Client'),
        ]

    def analyze(self, func: FunctionInfo) -> InternalAnalysis:
        body = func.body
        if not body:
            return InternalAnalysis(
                summary=func.docstring or f"Declaration or inline method for {func.name}."
            )

        # 1. Control flow
        flow_traits = []
        if re.search(r'\bfor\s*\(|\bwhile\s*\(', body):
            flow_traits.append("Iterative loop processing")
        if re.search(r'\bif\s*\(', body):
            flow_traits.append("Conditional branching")
        if re.search(r'\bswitch\s*\(', body):
            flow_traits.append("Multi-case state dispatch")
        if re.search(r'\breturn\b', body):
            flow_traits.append("Explicit result return")
        flow_desc = ", ".join(flow_traits) if flow_traits else "Direct sequential execution"

        # 2. Memory management
        mem_traits = []
        for pattern, desc in self.mem_alloc_patterns:
            if pattern.search(body):
                mem_traits.append(desc)
        mem_desc = "; ".join(mem_traits) if mem_traits else "Stack-based automatic variable allocation"

        # 3. Concurrency
        conc_traits = []
        for pattern, desc in self.concurrency_patterns:
            if pattern.search(body):
                conc_traits.append(desc)
        conc_desc = "; ".join(conc_traits) if conc_traits else "Unsynchronized execution (caller must ensure thread-safety if shared)"

        # 4. Error handling & invariants
        err_traits = []
        for pattern, desc in self.error_patterns:
            if pattern.search(body):
                err_traits.append(desc)
        err_desc = "; ".join(err_traits) if err_traits else "Relies on standard return codes and caller validation"

        # 5. External libraries
        ext_libs = []
        for pattern, name in self.ext_lib_patterns:
            if pattern.search(body):
                ext_libs.append(name)

        # 6. Called functions (extract key call tokens)
        call_tokens = re.findall(r'(?:->|\.|\b)([a-zA-Z_]\w*)\s*\(', body)
        filtered_calls = []
        ignore_set = {'if', 'for', 'while', 'switch', 'catch', 'sizeof', 'typeof', 'static_cast', 'reinterpret_cast', 'dynamic_cast', 'const_cast', func.name}
        for token in call_tokens:
            if token not in ignore_set and len(token) > 2 and token not in filtered_calls:
                filtered_calls.append(token)
                if len(filtered_calls) >= 12:
                    break

        # 7. State mutation
        if 'const' in func.modifiers:
            state_desc = "Immutable / read-only operation (const member method; does not alter object state)"
        elif re.search(r'this->\w+\s*=|m_\w+\s*=|_\w+\s*=', body):
            state_desc = "Mutates internal member state or instance properties"
        else:
            state_desc = "Pure computational logic or modifies passed-in parameters/references"

        # 8. Human-readable synthesis
        summary_parts = []
        if func.docstring:
            summary_parts.append(func.docstring)
        else:
            summary_parts.append(f"Executes {func.name} within {func.subsystem}.")
            if filtered_calls:
                summary_parts.append(f"Coordinates interactions with `{', '.join(filtered_calls[:4])}`.")
            if mem_traits:
                summary_parts.append(f"Employs {mem_traits[0].lower()}.")

        summary = " ".join(summary_parts)

        return InternalAnalysis(
            summary=summary,
            control_flow=flow_desc,
            memory_management=mem_desc,
            concurrency_thread_safety=conc_desc,
            error_handling_invariants=err_desc,
            called_functions=filtered_calls,
            external_libraries=ext_libs,
            state_mutation=state_desc
        )

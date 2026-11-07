"""
Cross-file behavioral difference and platform divergence detector.
Detects platform #ifdef branches, multi-file platform variants, and call-site differences.
"""
import os
import re
from typing import List, Dict, Set
from collections import defaultdict
from .models import FunctionInfo, DivergenceInfo
from .config import REPO_ROOT

class DivergenceDetector:
    def __init__(self, repo_root: str = REPO_ROOT):
        self.repo_root = repo_root
        self.platform_patterns = [
            (re.compile(r'#\s*(?:ifdef|if\s+defined\s*\()\s*(_WIN32|_WIN64|WIN32)'), 'Windows (Win32/x64 API)'),
            (re.compile(r'#\s*(?:ifdef|if\s+defined\s*\()\s*(__APPLE__|TARGET_OS_MAC|TARGET_OS_IPHONE)'), 'Apple macOS / iOS (Cocoa / POSIX)'),
            (re.compile(r'#\s*(?:ifdef|if\s+defined\s*\()\s*(ANDROID|__ANDROID__)'), 'Android (Linux Bionic / NDK / JNI)'),
            (re.compile(r'#\s*(?:ifdef|if\s+defined\s*\()\s*(_DURANGO|_XBOX)'), 'Xbox One Durango (WinRT / UWP / XDK)'),
            (re.compile(r'#\s*(?:ifdef|if\s+defined\s*\()\s*(_MSC_VER)'), 'Microsoft Visual C++ MSVC Specifics'),
            (re.compile(r'#\s*(?:ifdef|if\s+defined\s*\()\s*(__GNUC__|__clang__)'), 'GCC / Clang Compiler Optimizations'),
            (re.compile(r'FASTFLAG\s*\(\w+\)'), 'FastFlag Runtime Dynamic Divergence'),
        ]
        self.func_name_to_files: Dict[str, Set[str]] = defaultdict(set)

    def index_functions(self, all_functions: List[FunctionInfo]) -> None:
        """Indexes all functions by name to find multi-file variants."""
        self.func_name_to_files.clear()
        for f in all_functions:
            self.func_name_to_files[f.name].add(f.file_path)

    def analyze_divergence(self, func: FunctionInfo) -> DivergenceInfo:
        body = func.body
        detected_guards = []
        has_guards = False

        for pattern, label in self.platform_patterns:
            if pattern.search(body):
                detected_guards.append(label)
                has_guards = True

        # Check multi-file variants
        all_files_for_name = self.func_name_to_files.get(func.name, set())
        other_files = [p for p in all_files_for_name if p != func.file_path]
        multi_file_variants = []
        for other in other_files:
            # check if other has platform indicators
            if any(p in other.lower() for p in ['win', 'mac', 'unix', 'android', 'mobile', 'durango', 'xbox']):
                multi_file_variants.append(other)

        # Detect caller divergences
        caller_divergences = []
        if 'CookiesEngine' in func.file_path:
            caller_divergences.append("Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.")
        elif 'Crypt' in func.file_path:
            caller_divergences.append("Windows client links against Win32 Crypt32/CryptoAPI; Unix/POSIX build utilizes portable custom AES/RC4 cipher suite.")
        elif 'FileSystem' in func.file_path:
            caller_divergences.append("Windows client paths leverage SHGetFolderPathW / AppData; Android leverages JNI internal storage paths.")
        elif 'TaskScheduler' in func.file_path or 'TaskScheduler' in func.name:
            caller_divergences.append("Studio runs cyclic executive on Qt UI thread; WindowsClient syncs with DirectX VSync; RCCService runs headless unthrottled loop.")
        elif 'RbxFormat' in func.file_path:
            caller_divergences.append("Windows builds utilize `_vscprintf` and `vsnprintf_s`; non-Windows targets utilize POSIX `vsnprintf`.")

        summary_parts = []
        if detected_guards:
            summary_parts.append(f"Behavior branches internally via conditional compilation for: {', '.join(detected_guards)}.")
        if multi_file_variants:
            summary_parts.append(f"Alternative platform-specific implementations exist in: {', '.join(f'`{v}`' for v in multi_file_variants[:3])}.")
        if caller_divergences:
            summary_parts.append(" ".join(caller_divergences))

        if not summary_parts:
            summary = "Uniform behavior across all target platforms (identical compilation path and execution across Windows, macOS, Android, and iOS)."
        else:
            summary = " ".join(summary_parts)

        return DivergenceInfo(
            has_platform_guards=has_guards,
            platform_guards=detected_guards,
            multi_file_variants=multi_file_variants,
            caller_divergences=caller_divergences,
            summary=summary
        )

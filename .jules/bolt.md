## 2024-05-18 - Avoid unnecessary std::shared_ptr copying in range-based loops
**Learning:** In C++ codebases processing large amounts of network data, range-based `for` loops iterating by value (`for (auto item : vec)`) over containers of `std::shared_ptr` cause atomic reference counting operations for every element. This is surprisingly expensive in a hot path.
**Action:** Always prefer `for (const auto& item : vec)` when iterating over containers of smart pointers unless a copy is explicitly required.

## 2023-10-25 - [Atomic Ref-Count Overhead in Range-Based For Loops]
**Learning:** In C++ codebases processing large amounts of network data or relying heavily on C++/CX WinRT reference counting (`T^` hat pointers), range-based `for` loops iterating by value (`for (auto item : vec)`) over containers of ref-counted types cause atomic reference counting operations (`AddRef` and `Release`) for every single element. This is surprisingly expensive in a hot path.
**Action:** Use `const auto&` or `auto&` to iterate over containers holding ref-counted pointers to avoid this overhead. However, note that for standard C++ raw pointers (e.g., `SimBody*`), passing by value (`auto`) is sufficient and often faster since no ref-counting is involved.

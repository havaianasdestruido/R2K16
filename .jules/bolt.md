## 2024-05-18 - Avoid unnecessary std::shared_ptr copying in range-based loops
**Learning:** In C++ codebases processing large amounts of network data, range-based `for` loops iterating by value (`for (auto item : vec)`) over containers of `std::shared_ptr` cause atomic reference counting operations for every element. This is surprisingly expensive in a hot path.
**Action:** Always prefer `for (const auto& item : vec)` when iterating over containers of smart pointers unless a copy is explicitly required.

## 2024-05-18 - Avoid unnecessary std::shared_ptr copying in range-based loops
**Learning:** In C++ codebases processing large amounts of network data, range-based `for` loops iterating by value (`for (auto item : vec)`) over containers of `std::shared_ptr` cause atomic reference counting operations for every element. This is surprisingly expensive in a hot path.
**Action:** Always prefer `for (const auto& item : vec)` when iterating over containers of smart pointers unless a copy is explicitly required.
## 2024-05-18 - C++/CX WinRT Ref-Counting Performance Penalty
**Learning:** In legacy Windows/Xbox C++ projects using C++/CX (WinRT components with `^` hat pointers), iterating over collections of `^` pointers by value (e.g., `for(auto user : GetChatUsers())`) is extremely expensive. Each iteration triggers an atomic COM `AddRef()` and `Release()` behind the scenes.
**Action:** ALWAYS iterate over C++/CX collections using `const auto&` to avoid these invisible performance bottlenecks.

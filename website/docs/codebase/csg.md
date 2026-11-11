---
sidebar_position: 19
title: CSG Geometric Kernel
description: Constructive Solid Geometry boolean operations (Union, Subtract, Intersect).
---

# CSG Geometric Kernel

Constructive Solid Geometry boolean operations (Union, Subtract, Intersect).


## FAQ

### How can I validate a CSG operation?

Read its implementation and test representative inputs, including invalid or degenerate geometry. A generated function description is not a geometric correctness proof.

### How can I investigate this in the repository?

From the repository root, search the relevant tracked files for a starting point (results are leads, not proof of behavior):

```bash
git grep -n -i -F -- 'union' -- CSG
```

Read the surrounding implementation and callers, and check relevant tests before making changes. A search may return no matches when terminology or tracked files change.

## Subsystem Metrics

- **Total Documented Functions:** `63`
- **Functions Exercised in Tests:** `3`
- **Platform-Divergent Implementations:** `1`
- **Component Source Files:** `2`

## Source Files

<details>
<summary>View all 2 source files in this subsystem</summary>

| Source File | Path |
| :--- | :--- |
| `CSGKernel.cpp` | `CSG/CSGKernel.cpp` |
| `CSGKernel.h` | `CSG/CSGKernel.h` |

</details>

---

## Function Reference

### 1. `CSGMeshFactorySgCore::createMesh`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
CSGMesh* CSGMeshFactorySgCore::createMesh();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `CSGMesh*` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:39` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes createMesh within CSG Geometric Kernel. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `createMesh`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 2. `CSGMeshSgCore::weldMesh`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CSGMeshSgCore::weldMesh(bool positionOnly);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:44` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes weldMesh within CSG Geometric Kernel. Coordinates interactions with `resize, size, swap, reserve`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `resize`, `size`, `swap`, `reserve`, `length`, `push_back`, `unsigned`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `weldMesh`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 3. `CSGMeshSgCore::EditData::clone`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
sgCObject* CSGMeshSgCore::EditData::clone() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `sgCObject*` |
| **Modifiers** | `const` |
| **Source Location** | `CSG/CSGKernel.cpp:116` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes clone within CSG Geometric Kernel. Coordinates interactions with `brepFromBinaryString, getBRepBinaryString`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `brepFromBinaryString`, `getBRepBinaryString`.

#### How it is Used in Tests

This function is exercised in **7 test case(s)**:

- **`CustomEvents::CloneEventAndReceiver`** (`App.UnitTest/CustomEvents.cpp:491`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_REQUIRE(clonedEvent)`, `BOOST_REQUIRE(clonedReceiver)`, `BOOST_REQUIRE_EQUAL(1, clonedEvent-&gt;getAttachedReceivers()-&gt;size())`, `BOOST_REQUIRE_EQUAL(clonedEvent.get(), clonedReceiver-&gt;getSource())`
  - **Callsite Snippet:** `shared_ptr&lt;Instance&gt; clone(partParent-&gt;clone(RBX::ScriptingCreator));`
- **`Instance::Clone`** (`App.UnitTest/Instance.cpp:86`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(count, RBX::Diagnostics::Countable&lt;RBX::Instance&gt;::getCount())`
  - **Callsite Snippet:** `i-&gt;clone(RBX::ScriptingCreator);`
- **`Instance::Clone`** (`App.UnitTest/InstanceTest.cpp:18`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(count, RBX::Diagnostics::Countable&lt;RBX::Instance&gt;::getCount())`
  - **Callsite Snippet:** `i-&gt;clone(RBX::ScriptingCreator);`
- **`LuaReflection::PerfClone`** (`App.UnitTest/LuaReflection.cpp:1088`)
  - **Usage Pattern:** `Performance Benchmark`
  - **Callsite Snippet:** `root-&gt;clone(ScriptingCreator);`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 4. `CSGMeshSgCore::EditData::destroy`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CSGMeshSgCore::EditData::destroy();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:123` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes destroy within CSG Geometric Kernel. Coordinates interactions with `sgDeleteObject`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `sgDeleteObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `destroy`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 5. `CSGMeshSgCore::EditData::setShape`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CSGMeshSgCore::EditData::setShape(sgCObject* shapeIn);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:130` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes setShape within CSG Geometric Kernel. Coordinates interactions with `destroy`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `destroy`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setShape`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 6. `initKernelOnce`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void initKernelOnce();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:136` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes initKernelOnce within CSG Geometric Kernel. Coordinates interactions with `sgInitKernel, AutoTriangulate`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `sgInitKernel`, `AutoTriangulate`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `initKernelOnce`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 7. `initKernel`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void initKernel();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:142` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes initKernel within CSG Geometric Kernel. Coordinates interactions with `call_once`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `call_once`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `initKernel`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 8. `editData`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
: editData(this);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `:` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:150` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes editData within CSG Geometric Kernel. Coordinates interactions with `initKernel`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `initKernel`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `editData`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 9. `editData`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
: editData(this);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `:` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:156` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes editData within CSG Geometric Kernel. Coordinates interactions with `initKernel`.

- **Control Flow & Execution:** Iterative loop processing.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `initKernel`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `editData`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 10. `removeAllDXFFiles`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void removeAllDXFFiles();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:186` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes removeAllDXFFiles within CSG Geometric Kernel. Coordinates interactions with `getUserDirectory, empty, iter, path`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getUserDirectory`, `empty`, `iter`, `path`, `extension`, `compare`, `remove`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `removeAllDXFFiles`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 11. `removePreviousErrorFiles`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void removePreviousErrorFiles();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:201` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes removePreviousErrorFiles within CSG Geometric Kernel. Coordinates interactions with `empty, remove, c_str, removeAllDXFFiles`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `empty`, `remove`, `c_str`, `removeAllDXFFiles`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `removePreviousErrorFiles`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 12. `logError`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void logError(sgCObject* obj1, sgCObject* obj2, bool unionOperation = true);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:216` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes logError within CSG Geometric Kernel. Coordinates interactions with `defined, removePreviousErrorFiles, getMainLogManager, MakeLogFileName`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `defined`, `removePreviousErrorFiles`, `getMainLogManager`, `MakeLogFileName`, `substr`, `size`, `sgGetScene`, `AttachObject`, `ExportDXF`, `c_str`, `DetachObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `logError`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Behavior branches internally via conditional compilation for: Windows (Win32/x64 API). Alternative platform-specific implementations exist in: `Win/VideoControl.cpp`.

- **Platform Preprocessor Guards:** `Windows (Win32/x64 API)`
- **Alternative Implementation Files:** `Win/VideoControl.cpp`

---

### 13. `gatherGroup`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void gatherGroup(sgCGroup* group, std::vector<sgC3DObject*>& objects);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:237` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes gatherGroup within CSG Geometric Kernel. Coordinates interactions with `GetChildrenList, GetHead, gather3DObjects, GetNext`.

- **Control Flow & Execution:** Iterative loop processing.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `GetChildrenList`, `GetHead`, `gather3DObjects`, `GetNext`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `gatherGroup`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 14. `gather3DObjects`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void gather3DObjects(sgCObject* obj, std::vector<sgC3DObject*>& objects);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:247` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes gather3DObjects within CSG Geometric Kernel. Coordinates interactions with `GetType, gatherGroup, push_back, Clone`.

- **Control Flow & Execution:** Multi-case state dispatch.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `GetType`, `gatherGroup`, `push_back`, `Clone`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `gather3DObjects`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 15. `applyMatrixToGroup`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void applyMatrixToGroup(sgCGroup* group, const sgCMatrix& matrix);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:268` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes applyMatrixToGroup within CSG Geometric Kernel. Coordinates interactions with `GetChildrenList, GetHead, applyMatrixTo3DObjects, GetNext`.

- **Control Flow & Execution:** Iterative loop processing.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `GetChildrenList`, `GetHead`, `applyMatrixTo3DObjects`, `GetNext`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `applyMatrixToGroup`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 16. `applyMatrixTo3DObjects`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void applyMatrixTo3DObjects(sgCObject* obj, const sgCMatrix& matrix);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:278` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes applyMatrixTo3DObjects within CSG Geometric Kernel. Coordinates interactions with `GetType, applyMatrixToGroup, Transform`.

- **Control Flow & Execution:** Multi-case state dispatch.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `GetType`, `applyMatrixToGroup`, `Transform`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `applyMatrixTo3DObjects`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 17. `applyColorToGroup`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void applyColorToGroup(sgCGroup* group, const Vector3& value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:301` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes applyColorToGroup within CSG Geometric Kernel. Coordinates interactions with `GetChildrenList, GetHead, applyColorTo3DObjects, GetNext`.

- **Control Flow & Execution:** Iterative loop processing.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `GetChildrenList`, `GetHead`, `applyColorTo3DObjects`, `GetNext`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `applyColorToGroup`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 18. `applyColorTo3DObjects`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void applyColorTo3DObjects(sgCObject* obj, const Vector3& value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:311` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes applyColorTo3DObjects within CSG Geometric Kernel. Coordinates interactions with `GetType, applyColorToGroup, SetColor`.

- **Control Flow & Execution:** Multi-case state dispatch.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `GetType`, `applyColorToGroup`, `SetColor`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `applyColorTo3DObjects`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 19. `applyScaleToGroup`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void applyScaleToGroup(sgCGroup* group, const Vector3& scale);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:337` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes applyScaleToGroup within CSG Geometric Kernel. Coordinates interactions with `GetChildrenList, GetHead, applyScaleTo3DObjects, GetNext`.

- **Control Flow & Execution:** Iterative loop processing.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `GetChildrenList`, `GetHead`, `applyScaleTo3DObjects`, `GetNext`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `applyScaleToGroup`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 20. `applyScaleTo3DObjects`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void applyScaleTo3DObjects(sgCObject* obj, const Vector3& scale);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:347` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes applyScaleTo3DObjects within CSG Geometric Kernel. Coordinates interactions with `GetType, applyScaleToGroup, Scale`.

- **Control Flow & Execution:** Multi-case state dispatch.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `GetType`, `applyScaleToGroup`, `Scale`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `applyScaleTo3DObjects`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 21. `applyTranslationToGroup`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void applyTranslationToGroup(sgCGroup* group, const Vector3& translation);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:373` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes applyTranslationToGroup within CSG Geometric Kernel. Coordinates interactions with `GetChildrenList, GetHead, applyTranslationTo3DObjects, GetNext`.

- **Control Flow & Execution:** Iterative loop processing.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `GetChildrenList`, `GetHead`, `applyTranslationTo3DObjects`, `GetNext`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `applyTranslationToGroup`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 22. `applyTranslationTo3DObjects`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void applyTranslationTo3DObjects(sgCObject* obj, const Vector3& translation);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:383` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes applyTranslationTo3DObjects within CSG Geometric Kernel. Coordinates interactions with `GetType, applyTranslationToGroup, Translate`.

- **Control Flow & Execution:** Multi-case state dispatch.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `GetType`, `applyTranslationToGroup`, `Translate`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `applyTranslationTo3DObjects`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 23. `calcFlatNormal`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void calcFlatNormal(CSGVertex& vertA, CSGVertex& vertB, CSGVertex& vertC);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:407` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes calcFlatNormal within CSG Geometric Kernel. Coordinates interactions with `cross`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `cross`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `calcFlatNormal`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 24. `calcFlatTangent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void calcFlatTangent(CSGVertex& vertA, CSGVertex& vertB, CSGVertex& vertC);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:417` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes calcFlatTangent within CSG Geometric Kernel. Coordinates interactions with `Vector3`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `Vector3`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `calcFlatTangent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 25. `averageNormal`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void averageNormal(Vector3& resultNormal,
                   const Vector3& posA,
                   const Vector3& posB,
                   const Vector3& normalA,
                   const Vector3& normalB);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:448` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes averageNormal within CSG Geometric Kernel. Coordinates interactions with `cos, toRadians, fabs, unit`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `cos`, `toRadians`, `fabs`, `unit`, `dot`.
- **External Library Dependencies:** `G3D Graphics and Math Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `averageNormal`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 26. `calcSmoothNormal`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void calcSmoothNormal(CSGVertex& vert, Vector3& normal, const std::vector<CSGVertex>& vertices, std::vector<unsigned int>& indices);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:471` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes calcSmoothNormal within CSG Geometric Kernel. Coordinates interactions with `size, averageNormal`.

- **Control Flow & Execution:** Iterative loop processing.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `size`, `averageNormal`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `calcSmoothNormal`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 27. `calcSmoothTangent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void calcSmoothTangent(CSGVertex& vert, Vector3& tangent, const std::vector<CSGVertex>& vertices, std::vector<unsigned int>& indices);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:480` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes calcSmoothTangent within CSG Geometric Kernel. Coordinates interactions with `size, averageNormal`.

- **Control Flow & Execution:** Iterative loop processing.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `size`, `averageNormal`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `calcSmoothTangent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 28. `calcUV`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void calcUV(CSGVertex& vert);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:489` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes calcUV within CSG Geometric Kernel. Coordinates interactions with `unit, fabs, generateUv`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `unit`, `fabs`, `generateUv`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `calcUV`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 29. `calcFlat`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void calcFlat(Vector3& normal, unsigned int& uvr,
              CSGVertex& vertA, CSGVertex& vertB, CSGVertex& vertC);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:511` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes calcFlat within CSG Geometric Kernel. Coordinates interactions with `cross, fabs`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `cross`, `fabs`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `calcFlat`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 30. `calcFlatTangent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void calcFlatTangent(Vector3& tangent, CSGVertex& vertA, CSGVertex& vertB, CSGVertex& vertC);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:531` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes calcFlatTangent within CSG Geometric Kernel. Coordinates interactions with `Vector3`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `Vector3`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `calcFlatTangent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 31. `triangulateGroup`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool triangulateGroup(sgCGroup* group, unsigned int& counter, std::vector<CSGVertex>& vertices, std::vector<unsigned int>& indices);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:562` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes triangulateGroup within CSG Geometric Kernel. Coordinates interactions with `GetChildrenList, GetHead, triangulateObject, GetNext`.

- **Control Flow & Execution:** Iterative loop processing, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `GetChildrenList`, `GetHead`, `triangulateObject`, `GetNext`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `triangulateGroup`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 32. `triangulate3D`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool triangulate3D(sgC3DObject* object, unsigned int& index, std::vector<CSGVertex>& vertices, std::vector<unsigned int>& indices);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:573` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes triangulate3D within CSG Geometric Kernel. Coordinates interactions with `Triangulate, SetMaterial, GetTriangles, Color4uint8`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `Triangulate`, `SetMaterial`, `GetTriangles`, `Color4uint8`, `Vector3`, `push_back`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `triangulate3D`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 33. `triangulateObject`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool triangulateObject(sgCObject* obj, unsigned int& counter, std::vector<CSGVertex>& vertices, std::vector<unsigned int>& indices);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:621` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes triangulateObject within CSG Geometric Kernel. Coordinates interactions with `GetType, triangulateGroup, triangulate3D`.

- **Control Flow & Execution:** Multi-case state dispatch, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `GetType`, `triangulateGroup`, `triangulate3D`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `triangulateObject`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 34. `CSGMeshSgCore::newTriangulate`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool CSGMeshSgCore::newTriangulate();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:635` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes newTriangulate within CSG Geometric Kernel. Coordinates interactions with `clear, getShape, triangulateObject, size`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new; Heap memory deallocation via operator delete.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `clear`, `getShape`, `triangulateObject`, `size`, `resize`, `clusterVertices`, `begin`, `end`, `erase`, `makeHalfEdges`, `calcFlat`, `cos`.
- **External Library Dependencies:** `G3D Graphics and Math Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `newTriangulate`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 35. `CSGMeshSgCore::triangulate`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CSGMeshSgCore::triangulate();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:900` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes triangulate within CSG Geometric Kernel. Coordinates interactions with `clear, getShape, triangulateObject, resize`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `clear`, `getShape`, `triangulateObject`, `resize`, `size`, `calcFlatNormal`, `calcUV`, `calcFlatTangent`, `calcSmoothNormal`, `calcSmoothTangent`, `length`, `unit`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `triangulate`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 36. `CSGMeshSgCore::sgCoreUnion`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool CSGMeshSgCore::sgCoreUnion(const CSGMeshSgCore& a, const CSGMeshSgCore& b);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:947` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes sgCoreUnion within CSG Geometric Kernel. Coordinates interactions with `getShape, gather3DObjects, size, logError`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getShape`, `gather3DObjects`, `size`, `logError`, `Union`, `GetChildrenList`, `GetCount`, `allChildren`, `BreakGroup`, `sgDeleteObject`, `push_back`, `resize`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `sgCoreUnion`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 37. `CSGMeshSgCore::sgCoreSubtract`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool CSGMeshSgCore::sgCoreSubtract(const CSGMeshSgCore& a, const CSGMeshSgCore& b);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:1022` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes sgCoreSubtract within CSG Geometric Kernel. Coordinates interactions with `getShape, gather3DObjects, size, logError`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getShape`, `gather3DObjects`, `size`, `logError`, `Sub`, `sgDeleteObject`, `GetChildrenList`, `GetCount`, `allChildren`, `BreakGroup`, `push_back`, `resize`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `sgCoreSubtract`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 38. `CSGMeshSgCore::unionMesh`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool CSGMeshSgCore::unionMesh(const CSGMesh* a, const CSGMesh* b);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:1110` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes unionMesh within CSG Geometric Kernel. Coordinates interactions with `sgCoreUnion`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `sgCoreUnion`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `unionMesh`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 39. `CSGMeshSgCore::intersectMesh`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool CSGMeshSgCore::intersectMesh(const CSGMesh* a, const CSGMesh* b);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:1121` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes intersectMesh within CSG Geometric Kernel.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `intersectMesh`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 40. `CSGMeshSgCore::subractMesh`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool CSGMeshSgCore::subractMesh(const CSGMesh* a, const CSGMesh* b);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:1127` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes subractMesh within CSG Geometric Kernel. Coordinates interactions with `sgCoreSubtract`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `sgCoreSubtract`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `subractMesh`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 41. `CSGMeshSgCore::applyCoordinateFrame`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CSGMeshSgCore::applyCoordinateFrame(CoordinateFrame cFrame);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:1138` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes applyCoordinateFrame within CSG Geometric Kernel. Coordinates interactions with `getShape, matrix, applyMatrixTo3DObjects, applyTranslationTo3DObjects`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getShape`, `matrix`, `applyMatrixTo3DObjects`, `applyTranslationTo3DObjects`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `applyCoordinateFrame`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 42. `CSGMeshSgCore::applyTranslation`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CSGMeshSgCore::applyTranslation(const G3D::Vector3& trans);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:1171` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes applyTranslation within CSG Geometric Kernel. Coordinates interactions with `getShape, applyTranslationTo3DObjects`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getShape`, `applyTranslationTo3DObjects`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `applyTranslation`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 43. `CSGMeshSgCore::applyScale`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CSGMeshSgCore::applyScale(const G3D::Vector3& scale);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:1178` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes applyScale within CSG Geometric Kernel. Coordinates interactions with `getShape, applyScaleTo3DObjects`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getShape`, `applyScaleTo3DObjects`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `applyScale`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 44. `CSGMeshSgCore::applyColor`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CSGMeshSgCore::applyColor(const G3D::Vector3& color);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:1186` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes applyColor within CSG Geometric Kernel. Coordinates interactions with `getShape, applyColorTo3DObjects`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getShape`, `applyColorTo3DObjects`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `applyColor`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 45. `CSGMeshSgCore::buildBRep`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CSGMeshSgCore::buildBRep();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:1194` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes buildBRep within CSG Geometric Kernel. Coordinates interactions with `size, float, push_back, setShape`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `size`, `float`, `push_back`, `setShape`, `ObjectFromTriangles`, `int`, `getShape`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `buildBRep`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 46. `CSGMeshSgCore::getBRepBinaryString`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string CSGMeshSgCore::getBRepBinaryString() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | `const` |
| **Source Location** | `CSG/CSGKernel.cpp:1229` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes getBRepBinaryString within CSG Geometric Kernel. Coordinates interactions with `getShape, ObjectToBitArray, write, str`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getShape`, `ObjectToBitArray`, `write`, `str`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getBRepBinaryString`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 47. `CSGMeshSgCore::brepFromBinaryString`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
sgCObject* CSGMeshSgCore::brepFromBinaryString(const std::string& str) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `sgCObject*` |
| **Modifiers** | `const` |
| **Source Location** | `CSG/CSGKernel.cpp:1248` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes brepFromBinaryString within CSG Geometric Kernel. Coordinates interactions with `empty, stream, read, resize`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `empty`, `stream`, `read`, `resize`, `BitArrayToObject`, `c_str`, `size`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `brepFromBinaryString`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 48. `CSGMeshSgCore::setBRepFromBinaryString`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CSGMeshSgCore::setBRepFromBinaryString(const std::string& str);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:1270` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes setBRepFromBinaryString within CSG Geometric Kernel. Coordinates interactions with `empty, brepFromBinaryString, setShape`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `empty`, `brepFromBinaryString`, `setShape`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setBRepFromBinaryString`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 49. `CSGMeshSgCore::isValid`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool CSGMeshSgCore::isValid() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `CSG/CSGKernel.cpp:1284` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes isValid within CSG Geometric Kernel. Coordinates interactions with `getShape`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getShape`.

#### How it is Used in Tests

This function is exercised in **3 test case(s)**:

- **`URLParser::Split`** (`App.UnitTest/URLParserTest.cpp:7`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(url.isValid())`
  - **Callsite Snippet:** `BOOST_CHECK(url.isValid());`
- **`URLParser::Normalization`** (`App.UnitTest/URLParserTest.cpp:76`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(url.isValid())`
  - **Callsite Snippet:** `BOOST_CHECK(url.isValid());`
- **`URLParser::Invalid`** (`App.UnitTest/URLParserTest.cpp:128`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(!url.isValid())`, `BOOST_CHECK(!url.isValid())`, `BOOST_CHECK(!url.isValid())`
  - **Callsite Snippet:** `BOOST_CHECK(!url.isValid());`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 50. `CSGMeshSgCore::clone`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
CSGMesh* CSGMeshSgCore::clone() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `CSGMesh*` |
| **Modifiers** | `const` |
| **Source Location** | `CSG/CSGKernel.cpp:1289` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes clone within CSG Geometric Kernel. Coordinates interactions with `CSGMeshSgCore`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `CSGMeshSgCore`.

#### How it is Used in Tests

This function is exercised in **7 test case(s)**:

- **`CustomEvents::CloneEventAndReceiver`** (`App.UnitTest/CustomEvents.cpp:491`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_REQUIRE(clonedEvent)`, `BOOST_REQUIRE(clonedReceiver)`, `BOOST_REQUIRE_EQUAL(1, clonedEvent-&gt;getAttachedReceivers()-&gt;size())`, `BOOST_REQUIRE_EQUAL(clonedEvent.get(), clonedReceiver-&gt;getSource())`
  - **Callsite Snippet:** `shared_ptr&lt;Instance&gt; clone(partParent-&gt;clone(RBX::ScriptingCreator));`
- **`Instance::Clone`** (`App.UnitTest/Instance.cpp:86`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(count, RBX::Diagnostics::Countable&lt;RBX::Instance&gt;::getCount())`
  - **Callsite Snippet:** `i-&gt;clone(RBX::ScriptingCreator);`
- **`Instance::Clone`** (`App.UnitTest/InstanceTest.cpp:18`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(count, RBX::Diagnostics::Countable&lt;RBX::Instance&gt;::getCount())`
  - **Callsite Snippet:** `i-&gt;clone(RBX::ScriptingCreator);`
- **`LuaReflection::PerfClone`** (`App.UnitTest/LuaReflection.cpp:1088`)
  - **Usage Pattern:** `Performance Benchmark`
  - **Callsite Snippet:** `root-&gt;clone(ScriptingCreator);`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 51. `CSGClustering::addPos`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
CSGClustering::IPosClassMap::iterator CSGClustering::addPos(uint64 key, int indx);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `CSGClustering::IPosClassMap::iterator` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:1305` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes addPos within CSG Geometric Kernel. Coordinates interactions with `find, end, insert, size`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `find`, `end`, `insert`, `size`, `push_back`, `value_type`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `addPos`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 52. `CSGClustering::mergeClasses`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CSGClustering::mergeClasses(IPosClassMap::iterator it[8]);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:1325` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes mergeClasses within CSG Geometric Kernel. Coordinates interactions with `insert, size, begin, end`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `insert`, `size`, `begin`, `end`, `clear`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `mergeClasses`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 53. `CSGClustering::addPosClasses`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CSGClustering::addPosClasses(G3D::uint64 key[8], int indx);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:1356` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes addPosClasses within CSG Geometric Kernel. Coordinates interactions with `addPos, mergeClasses`.

- **Control Flow & Execution:** Iterative loop processing.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `addPos`, `mergeClasses`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `addPosClasses`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 54. `CSGClustering::makeKey`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
uint64 CSGClustering::makeKey(const v3i2& v, unsigned int ii);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `uint64` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:1366` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes makeKey within CSG Geometric Kernel. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `makeKey`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 55. `CSGClustering::cluster`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CSGClustering::cluster();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:1379` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes cluster within CSG Geometric Kernel. Coordinates interactions with `size, floor, makeKey, addPosClasses`.

- **Control Flow & Execution:** Iterative loop processing.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `size`, `floor`, `makeKey`, `addPosClasses`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `cluster`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 56. `CSGClustering::extractVertices`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
size_t CSGClustering::extractVertices();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `size_t` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:1397` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes extractVertices within CSG Geometric Kernel. Coordinates interactions with `size, empty, begin, push_back`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `size`, `empty`, `begin`, `push_back`, `max`, `end`, `swap`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `extractVertices`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 57. `CSGMeshSgCore::clusterVertices`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
size_t CSGMeshSgCore::clusterVertices(float resolution);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `size_t` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:1420` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes clusterVertices within CSG Geometric Kernel. Coordinates interactions with `makeExtents, min, size, max`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `makeExtents`, `min`, `size`, `max`, `clustering`, `cluster`, `extractVertices`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `clusterVertices`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 58. `CSGMeshSgCore::makeExtents`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CSGMeshSgCore::makeExtents();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:1436` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes makeExtents within CSG Geometric Kernel. Coordinates interactions with `negativeMaxExtents, begin, end, expandToContain`.

- **Control Flow & Execution:** Iterative loop processing.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `negativeMaxExtents`, `begin`, `end`, `expandToContain`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `makeExtents`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 59. `CSGMeshSgCore::translate`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CSGMeshSgCore::translate(const G3D::Vector3& translation);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:1444` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes translate within CSG Geometric Kernel. Coordinates interactions with `size, shift`.

- **Control Flow & Execution:** Iterative loop processing.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `size`, `shift`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `translate`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 60. `CSGMeshSgCore::makeHalfEdges`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool CSGMeshSgCore::makeHalfEdges(std::vector< int>& vertexEdges);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `CSG/CSGKernel.cpp:1464` |
| **Subsystem** | `CSG Geometric Kernel` |

#### How it Works Internally

Executes makeHalfEdges within CSG Geometric Kernel. Coordinates interactions with `size, resize, insert, value_type`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `size`, `resize`, `insert`, `value_type`, `find`, `end`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `makeHalfEdges`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---


:::tip Additional Functions
There are **3 additional internal and inline functions** in this subsystem. All functions are indexed and cross-referenced in the **[Complete Function Catalog](./function-catalog.md)**.
:::

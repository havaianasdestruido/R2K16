---
sidebar_position: 2
title: Base Foundations
description: Base foundations, TaskScheduler, signals, time, memory, assertions, and string formatting.
---

# Base Foundations

Base foundations, TaskScheduler, signals, time, memory, assertions, and string formatting.

## Subsystem Metrics

- **Total Documented Functions:** `906`
- **Functions Exercised in Tests:** `155`
- **Platform-Divergent Implementations:** `110`
- **Component Source Files:** `65`

## Source Files

<details>
<summary>View all 65 source files in this subsystem</summary>

| Source File | Path |
| :--- | :--- |
| `HardwareInfo.cpp` | `Base/HardwareInfo.cpp` |
| `RbxAssert.cpp` | `Base/RbxAssert.cpp` |
| `RbxFormat.cpp` | `Base/RbxFormat.cpp` |
| `cpucount.cpp` | `Base/cpucount.cpp` |
| `RbxFormat.h` | `Base/include/RbxFormat.h` |
| `microprofile.h` | `Base/include/microprofile/microprofile.h` |
| `microprofiledraw.h` | `Base/include/microprofile/microprofiledraw.h` |
| `microprofileui.h` | `Base/include/microprofile/microprofileui.h` |
| `ArrayDynamic.h` | `Base/include/rbx/ArrayDynamic.h` |
| `BaldPtr.h` | `Base/include/rbx/BaldPtr.h` |
| `Boost.hpp` | `Base/include/rbx/Boost.hpp` |
| `CEvent.h` | `Base/include/rbx/CEvent.h` |
| `Countable.h` | `Base/include/rbx/Countable.h` |
| `Debug.h` | `Base/include/rbx/Debug.h` |
| `DenseHash.h` | `Base/include/rbx/DenseHash.h` |
| `GlobalVectorItem.h` | `Base/include/rbx/GlobalVectorItem.h` |
| `Set.h` | `Base/include/rbx/Intrusive/Set.h` |
| `Log.h` | `Base/include/rbx/Log.h` |
| `Memory.h` | `Base/include/rbx/Memory.h` |
| `ProcessPerfCounter.h` | `Base/include/rbx/ProcessPerfCounter.h` |
| `Profiler.h` | `Base/include/rbx/Profiler.h` |
| `RbxDbgInfo.cpp` | `Base/include/rbx/RbxDbgInfo.cpp` |
| `RunningAverage.h` | `Base/include/rbx/RunningAverage.h` |
| `TaskScheduler.Job.h` | `Base/include/rbx/TaskScheduler.Job.h` |
| `TaskScheduler.h` | `Base/include/rbx/TaskScheduler.h` |
| `Coordinator.h` | `Base/include/rbx/Tasks/Coordinator.h` |
| `atomic.h` | `Base/include/rbx/atomic.h` |
| `callable.h` | `Base/include/rbx/callable.h` |
| `intrusive_ptr_target.h` | `Base/include/rbx/intrusive_ptr_target.h` |
| `intrusive_weak_ptr.h` | `Base/include/rbx/intrusive_weak_ptr.h` |
| `make_shared.h` | `Base/include/rbx/make_shared.h` |
| `object_pool.h` | `Base/include/rbx/object_pool.h` |
| `rbxTime.h` | `Base/include/rbx/rbxTime.h` |
| `signal.h` | `Base/include/rbx/signal.h` |
| `threadsafe.h` | `Base/include/rbx/threadsafe.h` |
| `trie.h` | `Base/include/rbx/trie.h` |
| `simd_types.h` | `Base/include/simd/simd_types.h` |
| `SafeToLower.h` | `Base/include/util/SafeToLower.h` |
| `ScopedSingleton.h` | `Base/include/util/ScopedSingleton.h` |
| `stringbuffer.h` | `Base/include/util/stringbuffer.h` |
| `ublas_ext.h` | `Base/include/util/ublas_ext.h` |
| `SystemUtil.cpp` | `Base/rbx/Android/SystemUtil.cpp` |
| `ifaddrs.c` | `Base/rbx/Android/ifaddrs.c` |
| `CEvent.cpp` | `Base/rbx/CEvent.cpp` |
| `Crypt.cpp` | `Base/rbx/Crypt.cpp` |
| `SystemUtil.cpp` | `Base/rbx/Darwin/SystemUtil.cpp` |
| `SystemUtil.cpp` | `Base/rbx/Durango/SystemUtil.cpp` |
| `MathUtil.cpp` | `Base/rbx/MathUtil.cpp` |
| `Memory.cpp` | `Base/rbx/Memory.cpp` |
| `ProcessPerfCounter.cpp` | `Base/rbx/ProcessPerfCounter.cpp` |
| `Profiler.cpp` | `Base/rbx/Profiler.cpp` |
| `Signal.cpp` | `Base/rbx/Signal.cpp` |
| `TaskScheduler.Job.cpp` | `Base/rbx/TaskScheduler.Job.cpp` |
| `TaskScheduler.Thread.cpp` | `Base/rbx/TaskScheduler.Thread.cpp` |
| `TaskScheduler.cpp` | `Base/rbx/TaskScheduler.cpp` |
| `Coordinator.cpp` | `Base/rbx/Tasks/Coordinator.cpp` |
| `Time.cpp` | `Base/rbx/Time.cpp` |
| `Crypt.cpp` | `Base/rbx/Unix/Crypt.cpp` |
| `SystemUtil.cpp` | `Base/rbx/Win/SystemUtil.cpp` |
| `boost.cpp` | `Base/rbx/boost.cpp` |
| `Debug.cpp` | `Base/util/Debug.cpp` |
| `Log.cpp` | `Base/util/Log.cpp` |
| `RbxCrash.cpp` | `Base/util/RbxCrash.cpp` |
| `RegistryUtil.cpp` | `Base/util/RegistryUtil.cpp` |
| `StreamHelpers.cpp` | `Base/util/StreamHelpers.cpp` |

</details>

---

## Function Reference

### 1. `CPUCount`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
char CPUCount(unsigned int *TotAvailLogical,
					   unsigned int *TotAvailCore,
					   unsigned int *PhysicalNum);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `char` |
| **Modifiers** | `unsigned` |
| **Source Location** | `Base/HardwareInfo.cpp:4` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes CPUCount within Base Foundations. Coordinates interactions with `StatusFlag, systemMetric, c_str`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Exception handling block (try/catch recovery).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `StatusFlag`, `systemMetric`, `c_str`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `CPUCount`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 2. `main`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
int main();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | None |
| **Source Location** | `Base/HardwareInfo.cpp:38` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

to test this, use this line in the console (with gcc). g++ -IGeekInfo/src/geekinfo-2.1.4/include -I../boost_1_38_0/include HardwareInfo.cpp -o runHardareInfo -Wl,-syslibroot,/Developer/SDKs/MacOSX10.5.sdk -mmacosx-version-min=10.5 -arch i386 GeekInfo/src/geekinfo-2.1.4/build.x86_32/libgeekinfo.a -LGeekInfo/src/geekinfo-2.1.4/build.x86_32/lib -framework Carbon -framework IOKit -framework Cocoa -framework WebKit -framework AGL -framework OpenGL

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `systemMetricName`, `systemMetric`, `NewCPUCount`, `fprintf`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `main`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/fetchfflags.py`, `WindowsClient/RobloxGoldenHashPatcher/main.cpp`, `XboxClient/main.cpp`.

- **Alternative Implementation Files:** `XboxClient/fetchfflags.py`, `WindowsClient/RobloxGoldenHashPatcher/main.cpp`, `XboxClient/main.cpp`

---

### 3. `setAssertionHook`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void setAssertionHook(AssertionHook hook);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Base/RbxAssert.cpp:25` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes setAssertionHook within Base Foundations.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setAssertionHook`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 4. `assertionHook`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
AssertionHook assertionHook();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `AssertionHook` |
| **Modifiers** | None |
| **Source Location** | `Base/RbxAssert.cpp:29` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes assertionHook within Base Foundations.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `assertionHook`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 5. `setFailureHook`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void setFailureHook(AssertionHook hook);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Base/RbxAssert.cpp:33` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes setFailureHook within Base Foundations.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setFailureHook`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 6. `failureHook`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
AssertionHook failureHook();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `AssertionHook` |
| **Modifiers** | None |
| **Source Location** | `Base/RbxAssert.cpp:37` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes failureHook within Base Foundations.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `failureHook`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 7. `runtime_error`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::runtime_error runtime_error(const char* fmt,...);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::runtime_error` |
| **Modifiers** | None |
| **Source Location** | `Base/RbxFormat.cpp:19` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes runtime_error within Base Foundations. Coordinates interactions with `va_start, vformat, va_end`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Standard runtime error exception formulation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `va_start`, `vformat`, `va_end`.

#### How it is Used in Tests

This function is exercised in **10 test case(s)**:

- **`ClusterDeprecatedProperty::ParentCannotBeSet`** (`App.UnitTest/ClusterDeprecatedPropertyTest.cpp:69`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(dataModel-&gt;getWorkspace(), resultTuple-&gt;at(0).get&lt;shared_ptr&lt;Instance&gt; &gt;().get())`, `BOOST_CHECK_EQUAL("Cannot change Parent of type Terrain", e.what())`
  - **Callsite Snippet:** `\} catch (std::runtime_error& e) \{`
- **`ClusterDeprecatedProperty::SizeCannotBeSet`** (`App.UnitTest/ClusterDeprecatedPropertyTest.cpp:92`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(sizeVector, resultTuple-&gt;at(0).get&lt;Vector3&gt;())`, `BOOST_REQUIRE_EQUAL(sizeVector, resultTuple-&gt;at(0).get&lt;Vector3&gt;())`
  - **Callsite Snippet:** `\} catch (std::runtime_error& e) \{`
- **`LuaVector3Test::IsCloseNumArgs`** (`App.UnitTest/LuaVector3Test.cpp:9`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_THROW(dataModel.execute("return Vector3.new(0,0,0):isClose()"), std::runtime_error)`, `BOOST_CHECK_THROW(dataModel.execute("return Vector3.new(.00002,0,0):isClose()"), std::runtime_error)`
  - **Callsite Snippet:** `BOOST_CHECK_THROW(dataModel.execute("return Vector3.new(0,0,0):isClose()"), std::runtime_error);`
- **`SettingsTest::DifficultToCreateAServiceDirectlyUnderSettings`** (`App.UnitTest/SettingsTest.cpp:77`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE(settings.get())`, `BOOST_CHECK(errored)`
  - **Callsite Snippet:** `\} catch (std::runtime_error& ) \{`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 8. `format`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string format(const char* fmt,...);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `Base/RbxFormat.cpp:28` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes format within Base Foundations. Coordinates interactions with `va_start, vformat, va_end`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `va_start`, `vformat`, `va_end`.

#### How it is Used in Tests

This function is exercised in **4 test case(s)**:

- **`ClusterChangeHistoryTest::FillChunkStressTest`** (`App.UnitTest/ClusterChangeHistoryTest.cpp:99`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(0, chf.cluster-&gt;getNonEmptyCellCount())`
  - **Callsite Snippet:** `chf.changeHistory-&gt;requestWaypoint2(format("Pass %d", pass));`
- **`ModuleScriptTest::RequireManyModules`** (`App.UnitTest/ModuleScriptTest.cpp:631`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE(m)`, `BOOST_CHECK_EQUAL(ModuleScript::CompletedSuccess, m-&gt;vmState(
		dm-&gt;find&lt;ScriptContext&gt;()-&gt;getGlobalState(Security::GameScript_)).getCurrentState())`
  - **Callsite Snippet:** `dm-&gt;getWorkspace()-&gt;findFirstChildByName(format("Module%d", i)));`
- **`Format::SmallString`** (`Base.UnitTest/Time.cpp:10`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(RBX::format("%s", s.c_str()) == s)`
  - **Callsite Snippet:** `BOOST_CHECK( RBX::format("%s", s.c_str()) == s);`
- **`Format::BigString`** (`Base.UnitTest/Time.cpp:18`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(RBX::format("%s", s.c_str()) == s)`
  - **Callsite Snippet:** `BOOST_CHECK( RBX::format("%s", s.c_str()) == s);`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 9. `vformat`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
std::string vformat(const char *fmt, va_list argPtr);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `Base/RbxFormat.cpp:37` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes vformat within Base Foundations. Coordinates interactions with `_vscprintf, vsnprintf_s, string, reset`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new; C runtime dynamic heap allocation (malloc/calloc); C runtime memory release (free); RAII scoped heap buffer allocation (boost::scoped_array).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Defensive null-pointer validation guard.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `_vscprintf`, `vsnprintf_s`, `string`, `reset`, `get`, `result`, `vsnprintf`, `heapBuffer`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `vformat`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Behavior branches internally via conditional compilation for: Windows (Win32/x64 API). Windows builds utilize `_vscprintf` and `vsnprintf_s`; non-Windows targets utilize POSIX `vsnprintf`.

- **Platform Preprocessor Guards:** `Windows (Win32/x64 API)`
- **Caller Context Variations:** Windows builds utilize `_vscprintf` and `vsnprintf_s`; non-Windows targets utilize POSIX `vsnprintf`.

---

### 10. `RbxTotalUsableCoreCount`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
int RbxTotalUsableCoreCount(unsigned int defaultValue);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `unsigned` |
| **Source Location** | `Base/cpucount.cpp:7` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes RbxTotalUsableCoreCount within Base Foundations. Coordinates interactions with `hardware_concurrency, getCPUCoreCount`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `hardware_concurrency`, `getCPUCoreCount`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `RbxTotalUsableCoreCount`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Behavior branches internally via conditional compilation for: Windows (Win32/x64 API).

- **Platform Preprocessor Guards:** `Windows (Win32/x64 API)`

---

### 11. `what`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
char* what() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `char*` |
| **Modifiers** | `const const` |
| **Source Location** | `Base/include/RbxFormat.h:68` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes what within Base Foundations. Coordinates interactions with `c_str`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `c_str`.

#### How it is Used in Tests

This function is exercised in **5 test case(s)**:

- **`ClusterDeprecatedProperty::ParentCannotBeSet`** (`App.UnitTest/ClusterDeprecatedPropertyTest.cpp:69`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL("Cannot change Parent of type Terrain", e.what())`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL("Cannot change Parent of type Terrain", e.what());`
- **`ClusterDeprecatedProperty::SizeCannotBeSet`** (`App.UnitTest/ClusterDeprecatedPropertyTest.cpp:92`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL("Cannot Resize() Terrain", e.what())`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL("Cannot Resize() Terrain", e.what());`
- **`LuaReflection::CyclicTable1`** (`App.UnitTest/LuaReflection.cpp:857`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL("tables cannot be cyclic", e.what())`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL("tables cannot be cyclic", e.what());`
- **`LuaReflection::CyclicTable2`** (`App.UnitTest/LuaReflection.cpp:875`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL("tables cannot be cyclic", e.what())`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL("tables cannot be cyclic", e.what());`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 12. `what`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
char* what() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `char*` |
| **Modifiers** | `const const` |
| **Source Location** | `Base/include/RbxFormat.h:80` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes what within Base Foundations. Coordinates interactions with `c_str`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `c_str`.

#### How it is Used in Tests

This function is exercised in **5 test case(s)**:

- **`ClusterDeprecatedProperty::ParentCannotBeSet`** (`App.UnitTest/ClusterDeprecatedPropertyTest.cpp:69`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL("Cannot change Parent of type Terrain", e.what())`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL("Cannot change Parent of type Terrain", e.what());`
- **`ClusterDeprecatedProperty::SizeCannotBeSet`** (`App.UnitTest/ClusterDeprecatedPropertyTest.cpp:92`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL("Cannot Resize() Terrain", e.what())`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL("Cannot Resize() Terrain", e.what());`
- **`LuaReflection::CyclicTable1`** (`App.UnitTest/LuaReflection.cpp:857`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL("tables cannot be cyclic", e.what())`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL("tables cannot be cyclic", e.what());`
- **`LuaReflection::CyclicTable2`** (`App.UnitTest/LuaReflection.cpp:875`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL("tables cannot be cyclic", e.what())`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL("tables cannot be cyclic", e.what());`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 13. `MicroProfileTicksPerSecondCpu`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int64_t MicroProfileTicksPerSecondCpu();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int64_t` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:184` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileTicksPerSecondCpu within Base Foundations. Coordinates interactions with `mach_timebase_info`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `mach_timebase_info`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileTicksPerSecondCpu`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 14. `MicroProfileGetCurrentThreadId`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
uint64_t MicroProfileGetCurrentThreadId();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `uint64_t` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:195` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileGetCurrentThreadId within Base Foundations. Coordinates interactions with `pthread_threadid_np, pthread_self`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pthread_threadid_np`, `pthread_self`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileGetCurrentThreadId`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 15. `MicroProfileTicksPerSecondCpu`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int64_t MicroProfileTicksPerSecondCpu();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int64_t` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:221` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileTicksPerSecondCpu within Base Foundations.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileTicksPerSecondCpu`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 16. `MicroProfileGetTick`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int64_t MicroProfileGetTick();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int64_t` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:225` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileGetTick within Base Foundations. Coordinates interactions with `clock_gettime`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `clock_gettime`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileGetTick`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 17. `MicroProfileGetTimerIndex`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
uint16_t MicroProfileGetTimerIndex(MicroProfileToken t);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `uint16_t` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:388` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileGetTimerIndex within Base Foundations. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileGetTimerIndex`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 18. `MicroProfileGetGroupMask`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
uint64_t MicroProfileGetGroupMask(MicroProfileToken t);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `uint64_t` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:389` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileGetGroupMask within Base Foundations. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileGetGroupMask`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 19. `MicroProfileMakeToken`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
MicroProfileToken MicroProfileMakeToken(uint64_t nGroupMask, uint16_t nTimer);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `MicroProfileToken` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:390` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileMakeToken within Base Foundations. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileMakeToken`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 20. `MicroProfileLogType`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
uint64_t MicroProfileLogType(MicroProfileLogEntry Index);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `uint64_t` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:858` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileLogType within Base Foundations. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileLogType`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 21. `MicroProfileLogTimerIndex`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
uint64_t MicroProfileLogTimerIndex(MicroProfileLogEntry Index);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `uint64_t` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:864` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileLogTimerIndex within Base Foundations. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileLogTimerIndex`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 22. `MicroProfileMakeLogIndex`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
MicroProfileLogEntry MicroProfileMakeLogIndex(uint64_t nBegin, MicroProfileToken nToken, int64_t nTick);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `MicroProfileLogEntry` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:869` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileMakeLogIndex within Base Foundations. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileMakeLogIndex`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 23. `MicroProfileLogTickDifference`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int64_t MicroProfileLogTickDifference(MicroProfileLogEntry Start, MicroProfileLogEntry End);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int64_t` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:874` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileLogTickDifference within Base Foundations.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileLogTickDifference`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 24. `MicroProfileLogGetTick`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int64_t MicroProfileLogGetTick(MicroProfileLogEntry e);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int64_t` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:882` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileLogGetTick within Base Foundations.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileLogGetTick`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 25. `MicroProfileLogSetTick`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int64_t MicroProfileLogSetTick(MicroProfileLogEntry e, int64_t nTick);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int64_t` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:887` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileLogSetTick within Base Foundations. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileLogSetTick`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 26. `MicroProfileMin`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
T MicroProfileMin(T a, T b);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `T` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:892` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileMin within Base Foundations.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileMin`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 27. `MicroProfileMax`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
T MicroProfileMax(T a, T b);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `T` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:896` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileMax within Base Foundations.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileMax`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 28. `MicroProfileMsToTick`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int64_t MicroProfileMsToTick(float fMs, int64_t nTicksPerSecond);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int64_t` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:900` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileMsToTick within Base Foundations. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileMsToTick`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 29. `MicroProfileTickToMsMultiplier`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
float MicroProfileTickToMsMultiplier(int64_t nTicksPerSecond);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `float` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:905` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileTickToMsMultiplier within Base Foundations.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileTickToMsMultiplier`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 30. `MicroProfileGetGroupIndex`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
uint16_t MicroProfileGetGroupIndex(MicroProfileToken t);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `uint16_t` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:910` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileGetGroupIndex within Base Foundations. Coordinates interactions with `return, MicroProfileGet, MicroProfileGetTimerIndex`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`, `MicroProfileGet`, `MicroProfileGetTimerIndex`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileGetGroupIndex`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 31. `MicroProfileTicksPerSecondCpu`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int64_t MicroProfileTicksPerSecondCpu();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int64_t` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:927` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileTicksPerSecondCpu within Base Foundations. Coordinates interactions with `QueryPerformanceFrequency`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `QueryPerformanceFrequency`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileTicksPerSecondCpu`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 32. `MicroProfileGetTick`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int64_t MicroProfileGetTick();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int64_t` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:936` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileGetTick within Base Foundations. Coordinates interactions with `QueryPerformanceCounter`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `QueryPerformanceCounter`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileGetTick`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 33. `MicroProfileThreadStart`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void MicroProfileThreadStart(MicroProfileThread* pThread, MicroProfileThreadFunc Func);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:947` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileThreadStart within Base Foundations. Coordinates interactions with `thread`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `thread`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileThreadStart`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 34. `MicroProfileThreadJoin`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void MicroProfileThreadJoin(MicroProfileThread* pThread);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:952` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileThreadJoin within Base Foundations. Coordinates interactions with `join`. Employs heap memory deallocation via operator delete.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Heap memory deallocation via operator delete.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `join`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileThreadJoin`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 35. `MicroProfileCreateThreadLogKey`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void MicroProfileCreateThreadLogKey();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `Base/include/microprofile/microprofile.h:1007` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileCreateThreadLogKey within Base Foundations. Coordinates interactions with `pthread_key_create`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pthread_key_create`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileCreateThreadLogKey`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 36. `MicroProfileMutex`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::recursive_mutex& MicroProfileMutex();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::recursive_mutex&` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:1024` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileMutex within Base Foundations.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileMutex`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 37. `MicroProfileGetMutex`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::recursive_mutex& MicroProfileGetMutex();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::recursive_mutex&` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:1030` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileGetMutex within Base Foundations. Coordinates interactions with `MicroProfileMutex`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `MicroProfileMutex`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileGetMutex`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 38. `MicroProfileGet`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
MICROPROFILE_API MicroProfile* MicroProfileGet();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `MICROPROFILE_API MicroProfile*` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:1034` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileGet within Base Foundations.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileGet`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 39. `MicroProfileInit`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void MicroProfileInit();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:1042` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileInit within Base Foundations. Coordinates interactions with `MicroProfileMutex, lock, memset, strcpy`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `MicroProfileMutex`, `lock`, `memset`, `strcpy`, `MP_TICK`, `MicroProfileCreateThreadLog`, `MP_ASSERT`, `unlock`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileInit`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 40. `MicroProfileShutdown`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void MicroProfileShutdown();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:1109` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileShutdown within Base Foundations. Coordinates interactions with `Lock, MicroProfileMutex, MicroProfileWebServerStop, MicroProfileStopContextSwitchTrace`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `Lock`, `MicroProfileMutex`, `MicroProfileWebServerStop`, `MicroProfileStopContextSwitchTrace`, `MicroProfileGpuShutdown`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileShutdown`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 41. `MicroProfileGetThreadLog`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
MicroProfileThreadLog* MicroProfileGetThreadLog();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `MicroProfileThreadLog*` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:1119` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileGetThreadLog within Base Foundations. Coordinates interactions with `pthread_once, return, pthread_getspecific`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pthread_once`, `return`, `pthread_getspecific`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileGetThreadLog`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 42. `MicroProfileSetThreadLog`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void MicroProfileSetThreadLog(MicroProfileThreadLog* pLog);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:1124` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileSetThreadLog within Base Foundations. Coordinates interactions with `pthread_once, pthread_setspecific`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pthread_once`, `pthread_setspecific`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileSetThreadLog`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 43. `MicroProfileGetThreadLog`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
MicroProfileThreadLog* MicroProfileGetThreadLog();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `MicroProfileThreadLog*` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:1131` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileGetThreadLog within Base Foundations.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileGetThreadLog`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 44. `MicroProfileSetThreadLog`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void MicroProfileSetThreadLog(MicroProfileThreadLog* pLog);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:1135` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileSetThreadLog within Base Foundations.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileSetThreadLog`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 45. `MicroProfileCreateThreadLog`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
MicroProfileThreadLog* MicroProfileCreateThreadLog(const char* pName);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `MicroProfileThreadLog*` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:1140` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileCreateThreadLog within Base Foundations. Coordinates interactions with `MP_ASSERT, load, memset, strlen`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `MP_ASSERT`, `load`, `memset`, `strlen`, `memcpy`, `MP_GETCURRENTTHREADID`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileCreateThreadLog`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 46. `MicroProfileOnThreadCreate`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void MicroProfileOnThreadCreate(const char* pThreadName);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:1173` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileOnThreadCreate within Base Foundations. Coordinates interactions with `MicroProfileInit, Lock, MicroProfileMutex, MicroProfileGetThreadLog`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `MicroProfileInit`, `Lock`, `MicroProfileMutex`, `MicroProfileGetThreadLog`, `MicroProfileCreateThreadLog`, `MicroProfileGetThreadName`, `MP_ASSERT`, `MicroProfileSetThreadLog`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileOnThreadCreate`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 47. `MicroProfileOnThreadExit`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void MicroProfileOnThreadExit();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:1186` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileOnThreadExit within Base Foundations. Coordinates interactions with `Lock, MicroProfileMutex, MicroProfileGetThreadLog, MP_ASSERT`. Employs heap memory deallocation via operator delete.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Heap memory deallocation via operator delete.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `Lock`, `MicroProfileMutex`, `MicroProfileGetThreadLog`, `MP_ASSERT`, `store`, `memset`, `MicroProfileSetThreadLog`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileOnThreadExit`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 48. `MicroProfileGetOrCreateThreadLog`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
MicroProfileThreadLog* MicroProfileGetOrCreateThreadLog();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `MicroProfileThreadLog*` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:1225` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileGetOrCreateThreadLog within Base Foundations. Coordinates interactions with `MicroProfileGetThreadLog, MicroProfileOnThreadCreate`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `MicroProfileGetThreadLog`, `MicroProfileOnThreadCreate`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileGetOrCreateThreadLog`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 49. `MicroProfileFindToken`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
MicroProfileToken MicroProfileFindToken(const char* pGroup, const char* pName);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `MicroProfileToken` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:1254` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileFindToken within Base Foundations. Coordinates interactions with `MicroProfileInit, MicroProfileMutex, MP_STRCASECMP`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `MicroProfileInit`, `MicroProfileMutex`, `MP_STRCASECMP`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileFindToken`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 50. `MicroProfileGetGroup`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
uint16_t MicroProfileGetGroup(const char* pGroup, MicroProfileTokenType Type);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `uint16_t` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:1268` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileGetGroup within Base Foundations. Coordinates interactions with `MP_STRCASECMP, MP_ASSERT, strlen, memcpy`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `MP_STRCASECMP`, `MP_ASSERT`, `strlen`, `memcpy`, `uint64_t`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileGetGroup`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 51. `MicroProfileGetToken`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
MicroProfileToken MicroProfileGetToken(const char* pGroup, const char* pName, uint32_t nColor, MicroProfileTokenType Type);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `MicroProfileToken` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:1305` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileGetToken within Base Foundations. Coordinates interactions with `MicroProfileInit, MicroProfileMutex, MicroProfileFindToken, MicroProfileGetGroup`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `MicroProfileInit`, `MicroProfileMutex`, `MicroProfileFindToken`, `MicroProfileGetGroup`, `MicroProfileMakeToken`, `MicroProfileMax`, `strlen`, `MP_ASSERT`, `memcpy`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileGetToken`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 52. `MicroProfileGetLabelToken`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
MicroProfileToken MicroProfileGetLabelToken(const char* pGroup, MicroProfileTokenType Type);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `MicroProfileToken` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:1360` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileGetLabelToken within Base Foundations. Coordinates interactions with `MicroProfileInit, MicroProfileMutex, MicroProfileGetGroup, MicroProfileMakeToken`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `MicroProfileInit`, `MicroProfileMutex`, `MicroProfileGetGroup`, `MicroProfileMakeToken`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileGetLabelToken`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 53. `MicroProfileGetMetaToken`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
MicroProfileToken MicroProfileGetMetaToken(const char* pName);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `MicroProfileToken` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:1372` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileGetMetaToken within Base Foundations. Coordinates interactions with `MicroProfileInit, MicroProfileMutex, MP_STRCASECMP, MP_ASSERT`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `MicroProfileInit`, `MicroProfileMutex`, `MP_STRCASECMP`, `MP_ASSERT`, `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileGetMetaToken`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 54. `MicroProfileNextName`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
char* MicroProfileNextName(const char* pName, char* pNameOut, uint32_t* nSubNameLen) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `char*` |
| **Modifiers** | `const` |
| **Source Location** | `Base/include/microprofile/microprofile.h:1392` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileNextName within Base Foundations.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Multi-case state dispatch, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileNextName`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 55. `MicroProfileCounterFullName`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
char* MicroProfileCounterFullName(int nCounter) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `char*` |
| **Modifiers** | `const` |
| **Source Location** | `Base/include/microprofile/microprofile.h:1424` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileCounterFullName within Base Foundations. Coordinates interactions with `MicroProfileMin, memcpy`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `MicroProfileMin`, `memcpy`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileCounterFullName`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 56. `MicroProfileGetCounterTokenByParent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int MicroProfileGetCounterTokenByParent(int nParent, const char* pName);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:1452` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileGetCounterTokenByParent within Base Foundations. Coordinates interactions with `MP_STRCASECMP, strlen, MP_ASSERT, memcpy`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `MP_STRCASECMP`, `strlen`, `MP_ASSERT`, `memcpy`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileGetCounterTokenByParent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 57. `MicroProfileGetCounterToken`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
MicroProfileToken MicroProfileGetCounterToken(const char* pName);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `MicroProfileToken` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:1491` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileGetCounterToken within Base Foundations. Coordinates interactions with `MicroProfileInit, MicroProfileMutex, MicroProfileNextName, MicroProfileGetCounterTokenByParent`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `MicroProfileInit`, `MicroProfileMutex`, `MicroProfileNextName`, `MicroProfileGetCounterTokenByParent`, `MP_ASSERT`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileGetCounterToken`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 58. `MicroProfileLogPut`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void MicroProfileLogPut(MicroProfileToken nToken_, uint64_t nTick, uint64_t nBegin, MicroProfileThreadLog* pLog);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `inline` |
| **Source Location** | `Base/include/microprofile/microprofile.h:1513` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileLogPut within Base Foundations. Coordinates interactions with `MP_ASSERT, load, memset, MicroProfileMakeLogIndex`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `MP_ASSERT`, `load`, `memset`, `MicroProfileMakeLogIndex`, `store`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileLogPut`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 59. `MicroProfileEnter`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
uint64_t MicroProfileEnter(MicroProfileToken nToken_);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `uint64_t` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:1536` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileEnter within Base Foundations. Coordinates interactions with `MicroProfileGetGroupMask, MicroProfileGpuInsertTimer, MicroProfileLogPut, MP_TICK`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `MicroProfileGetGroupMask`, `MicroProfileGpuInsertTimer`, `MicroProfileLogPut`, `MP_TICK`, `MicroProfileGetOrCreateThreadLog`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileEnter`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 60. `MicroProfileAllocateLabel`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
uint64_t MicroProfileAllocateLabel(const char* pName);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `uint64_t` |
| **Modifiers** | None |
| **Source Location** | `Base/include/microprofile/microprofile.h:1561` |
| **Subsystem** | `Base Foundations` |

#### How it Works Internally

Executes MicroProfileAllocateLabel within Base Foundations. Coordinates interactions with `load, MicroProfileMutex, memset, store`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `load`, `MicroProfileMutex`, `memset`, `store`, `strlen`, `fetch_add`, `memcpy`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MicroProfileAllocateLabel`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---


:::tip Additional Functions
There are **846 additional internal and inline functions** in this subsystem. All functions are indexed and cross-referenced in the **[Complete Function Catalog](./function-catalog.md)**.
:::

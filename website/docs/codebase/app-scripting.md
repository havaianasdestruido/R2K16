---
sidebar_position: 7
title: App - Scripting & Lua VM
description: ScriptContext, Lua-5.1 runtime integration, Luau bridge, and debugger.
---

# App - Scripting & Lua VM

ScriptContext, Lua-5.1 runtime integration, Luau bridge, and debugger.

## Subsystem Metrics

- **Total Documented Functions:** `837`
- **Functions Exercised in Tests:** `69`
- **Platform-Divergent Implementations:** `48`
- **Component Source Files:** `37`

## Source Files

<details>
<summary>View all 37 source files in this subsystem</summary>

| Source File | Path |
| :--- | :--- |
| `DebuggerManager.h` | `App/include/script/DebuggerManager.h` |
| `ExitHandlers.h` | `App/include/script/ExitHandlers.h` |
| `IScriptFilter.h` | `App/include/script/IScriptFilter.h` |
| `LuaArguments.h` | `App/include/script/LuaArguments.h` |
| `LuaAtomicClasses.h` | `App/include/script/LuaAtomicClasses.h` |
| `LuaEnum.h` | `App/include/script/LuaEnum.h` |
| `LuaInstanceBridge.h` | `App/include/script/LuaInstanceBridge.h` |
| `LuaLibrary.h` | `App/include/script/LuaLibrary.h` |
| `LuaSourceContainer.h` | `App/include/script/LuaSourceContainer.h` |
| `LuaVM.h` | `App/include/script/LuaVM.h` |
| `ModuleScript.h` | `App/include/script/ModuleScript.h` |
| `ScriptContext.h` | `App/include/script/ScriptContext.h` |
| `ScriptStats.h` | `App/include/script/ScriptStats.h` |
| `ThreadRef.h` | `App/include/script/ThreadRef.h` |
| `script.h` | `App/include/script/script.h` |
| `CoreScript.cpp` | `App/script/CoreScript.cpp` |
| `DebuggerManager.cpp` | `App/script/DebuggerManager.cpp` |
| `LuaArguments.cpp` | `App/script/LuaArguments.cpp` |
| `LuaAtomicClasses.cpp` | `App/script/LuaAtomicClasses.cpp` |
| `LuaCoreFunctions.cpp` | `App/script/LuaCoreFunctions.cpp` |
| `LuaEnum.cpp` | `App/script/LuaEnum.cpp` |
| `LuaInstanceBridge.cpp` | `App/script/LuaInstanceBridge.cpp` |
| `LuaLibrary.cpp` | `App/script/LuaLibrary.cpp` |
| `LuaMemory.cpp` | `App/script/LuaMemory.cpp` |
| `LuaSignalBridge.cpp` | `App/script/LuaSignalBridge.cpp` |
| `LuaSourceContainer.cpp` | `App/script/LuaSourceContainer.cpp` |
| `LuaVM.cpp` | `App/script/LuaVM.cpp` |
| `LuaVMClient.cpp` | `App/script/LuaVMClient.cpp` |
| `LuaVMDummy.cpp` | `App/script/LuaVMDummy.cpp` |
| `LuaVMServer.cpp` | `App/script/LuaVMServer.cpp` |
| `ModuleScript.cpp` | `App/script/ModuleScript.cpp` |
| `Script.cpp` | `App/script/Script.cpp` |
| `ScriptAnalyzer.cpp` | `App/script/ScriptAnalyzer.cpp` |
| `ScriptContext.cpp` | `App/script/ScriptContext.cpp` |
| `ScriptEvent.cpp` | `App/script/ScriptEvent.cpp` |
| `ScriptStats.cpp` | `App/script/ScriptStats.cpp` |
| `ThreadRef.cpp` | `App/script/ThreadRef.cpp` |

</details>

---

## Function Reference

### 1. `~ISpecialBreakpoint`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
virtual ~ISpecialBreakpoint();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `virtual` |
| **Modifiers** | None |
| **Source Location** | `App/include/script/DebuggerManager.h:36` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Declaration or inline method for ~ISpecialBreakpoint.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `~ISpecialBreakpoint`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 2. `getEnabled`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool getEnabled() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/script/DebuggerManager.h:81` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes getEnabled within App - Scripting & Lua VM.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

This function is exercised in **2 test case(s)**:

- **`PostEffectTest::BlurEffectDefaults`** (`App.UnitTest/PostEffectTest.cpp:13`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(effect-&gt;getEnabled())`
  - **Callsite Snippet:** `BOOST_CHECK(effect-&gt;getEnabled());`
- **`SoundEffectTests::DistortionPropertiesAndParenting`** (`App.UnitTest/SoundEffectTest.cpp:15`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(effect-&gt;getEnabled())`
  - **Callsite Snippet:** `BOOST_CHECK(effect-&gt;getEnabled());`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 3. `getBreakOnErrorMode`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
BreakOnErrorMode getBreakOnErrorMode() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `BreakOnErrorMode` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/script/DebuggerManager.h:82` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes getBreakOnErrorMode within App - Scripting & Lua VM.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getBreakOnErrorMode`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 4. `getDebuggers`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Debuggers& getDebuggers() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Debuggers&` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/script/DebuggerManager.h:87` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes getDebuggers within App - Scripting & Lua VM.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getDebuggers`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 5. `setScriptAutoResume`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void setScriptAutoResume(bool state);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/script/DebuggerManager.h:110` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes setScriptAutoResume within App - Scripting & Lua VM.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setScriptAutoResume`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 6. `getScript`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Instance* getScript() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Instance*` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/script/DebuggerManager.h:187` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes getScript within App - Scripting & Lua VM. Coordinates interactions with `get`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `get`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getScript`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 7. `setIgnoreDebuggerBreak`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void setIgnoreDebuggerBreak(bool state);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/script/DebuggerManager.h:195` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes setIgnoreDebuggerBreak within App - Scripting & Lua VM.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setIgnoreDebuggerBreak`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 8. `getBreakpoints`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Breakpoints& getBreakpoints() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Breakpoints&` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/script/DebuggerManager.h:201` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes getBreakpoints within App - Scripting & Lua VM.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getBreakpoints`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 9. `getWatches`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Watches& getWatches() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Watches&` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/script/DebuggerManager.h:209` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes getWatches within App - Scripting & Lua VM.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getWatches`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 10. `isDebugging`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool isDebugging() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/script/DebuggerManager.h:218` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes isDebugging within App - Scripting & Lua VM. Coordinates interactions with `empty`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `empty`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isDebugging`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 11. `hasError`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool hasError() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/script/DebuggerManager.h:225` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes hasError within App - Scripting & Lua VM. Coordinates interactions with `empty`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `empty`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `hasError`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 12. `getCurrentLine`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int getCurrentLine() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/script/DebuggerManager.h:230` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes getCurrentLine within App - Scripting & Lua VM.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getCurrentLine`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 13. `getPausedThreads`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
PausedThreads& getPausedThreads() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `PausedThreads&` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/script/DebuggerManager.h:287` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes getPausedThreads within App - Scripting & Lua VM.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getPausedThreads`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 14. `isRootThreadResumed`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool isRootThreadResumed();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `App/include/script/DebuggerManager.h:293` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes isRootThreadResumed within App - Scripting & Lua VM.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isRootThreadResumed`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 15. `getCurrentThread`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
long getCurrentThread();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `long` |
| **Modifiers** | None |
| **Source Location** | `App/include/script/DebuggerManager.h:296` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes getCurrentThread within App - Scripting & Lua VM.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getCurrentThread`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 16. `getLine`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int getLine() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/script/DebuggerManager.h:351` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes getLine within App - Scripting & Lua VM.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getLine`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 17. `isEnabled`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
bool isEnabled() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/script/DebuggerManager.h:353` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes isEnabled within App - Scripting & Lua VM.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isEnabled`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.h`, `WindowsClient/GameVerbs.cpp`.

- **Alternative Implementation Files:** `WindowsClient/GameVerbs.h`, `WindowsClient/GameVerbs.cpp`

---

### 18. `getCondition`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string& getCondition() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string&` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/script/DebuggerManager.h:355` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes getCondition within App - Scripting & Lua VM.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getCondition`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 19. `DebuggerWatch`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
public: DebuggerWatch();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `public:` |
| **Modifiers** | None |
| **Source Location** | `App/include/script/DebuggerManager.h:379` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Declaration or inline method for DebuggerWatch.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `DebuggerWatch`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 20. `getCondition`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string& getCondition() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string&` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/script/DebuggerManager.h:382` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes getCondition within App - Scripting & Lua VM.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getCondition`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 21. `getExpression`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string& getExpression() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string&` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/script/DebuggerManager.h:384` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes getExpression within App - Scripting & Lua VM.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getExpression`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 22. `empty`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool empty() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/script/ExitHandlers.h:19` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes empty within App - Scripting & Lua VM.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

This function is exercised in **6 test case(s)**:

- **`LuaDebugger::FlatDataSerialization`** (`App.UnitTest/LuaDebugger.cpp:139`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(binaryDataStreamOriginal.str().empty() != true)`
  - **Callsite Snippet:** `BOOST_CHECK(binaryDataStreamOriginal.str().empty() != true);`
- **`LuaDebugger::NestedDataSerialization`** (`App.UnitTest/LuaDebugger.cpp:211`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(binaryDataStreamOriginal.str().empty() != true)`
  - **Callsite Snippet:** `BOOST_CHECK(binaryDataStreamOriginal.str().empty() != true);`
- **`URLParser::Split`** (`App.UnitTest/URLParserTest.cpp:7`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(url.query().empty())`
  - **Callsite Snippet:** `BOOST_CHECK(url.query().empty());`
- **`URLParser::Invalid`** (`App.UnitTest/URLParserTest.cpp:128`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK(!url.isValid())`, `BOOST_CHECK_EQUAL(url.asString(), "")`
  - **Callsite Snippet:** `BOOST_CHECK(url.scheme().empty());`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 23. `onRunTransition`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void onRunTransition(RunTransition event);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/script/IScriptFilter.h:44` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes onRunTransition within App - Scripting & Lua VM. Coordinates interactions with `onRunState`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `onRunState`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onRunTransition`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 24. `withVariantValue`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
R withVariantValue(const Reflection::Variant& value, F f);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `R` |
| **Modifiers** | None |
| **Source Location** | `App/include/script/LuaArguments.h:15` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Utility function that expands a variant to a strongly-typed value

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT); C++ exception throw on invalid state or failure; Standard runtime error exception formulation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lookupDescriptor`, `type`, `lookup`, `runtime_error`, `c_str`, `RBXASSERT`.
- **External Library Dependencies:** `G3D Graphics and Math Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `withVariantValue`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 25. `size`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
size_t size() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `size_t` |
| **Modifiers** | `virtual const` |
| **Source Location** | `App/include/script/LuaArguments.h:150` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes size within App - Scripting & Lua VM. Coordinates interactions with `lua_gettop`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `lua_gettop`.

#### How it is Used in Tests

This function is exercised in **59 test case(s)**:

- **`ClusterDeltaBuffer::LengthBitSetOrdering`** (`App.UnitTest/ClusterReplicationTest.cpp:286`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(i, updateBuffer.size())`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL(i, updateBuffer.size());`
- **`ClusterDeltaBuffer::BitSetDoesNotStoreDuplicates`** (`App.UnitTest/ClusterReplicationTest.cpp:309`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(0, s.size())`, `BOOST_CHECK_EQUAL(1, s.size())`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL(0, s.size());`
- **`ClusterDeltaBuffer::UpdatesGroupedByChunk`** (`App.UnitTest/ClusterReplicationTest.cpp:337`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL((i + 1) * 2, updateBuffer.size())`, `BOOST_CHECK_EQUAL(64 - (i + 1), updateBuffer.size())`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL((i + 1) * 2, updateBuffer.size());`
- **`ClusterDeltaBuffer::GrowRetainsOrder`** (`App.UnitTest/ClusterReplicationTest.cpp:402`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(i + 1, updateBuffer.size())`, `BOOST_CHECK_EQUAL(i + 1 - 32, updateBuffer.size())`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL(i + 1, updateBuffer.size());`

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/p2p.h`.

- **Alternative Implementation Files:** `XboxClient/p2p.h`

---

### 26. `getValues`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
shared_ptr<Reflection::Tuple> getValues(lua_State* L);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `shared_ptr&lt;Reflection::Tuple&gt;` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaArguments.h:156` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Gets all arguments from the stack and puts them into the ValueArray

- **Control Flow & Execution:** Iterative loop processing, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lua_gettop`, `args`, `get`, `RBXASSERT`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getValues`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 27. `pushTuple`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int pushTuple(const Reflection::Tuple& arguments, lua_State* L);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaArguments.h:171` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes pushTuple within App - Scripting & Lua VM. Coordinates interactions with `pushValues`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pushValues`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushTuple`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 28. `pushValues`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int pushValues(const Reflection::ValueArray& arguments, lua_State* L);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaArguments.h:178` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

pushes all the values from the ValueArray onto the stack

- **Control Flow & Execution:** Iterative loop processing, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `end`, `begin`, `push`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushValues`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 29. `pushArray`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int pushArray(_InIt _First, _InIt _Last, lua_State * const L);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaArguments.h:228` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes pushArray within App - Scripting & Lua VM. Coordinates interactions with `lua_createtable, push, RBXASSERT, lua_rawseti`.

- **Control Flow & Execution:** Iterative loop processing, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lua_createtable`, `push`, `RBXASSERT`, `lua_rawseti`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushArray`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 30. `pushCoordinateFrame`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void pushCoordinateFrame(lua_State *L, const G3D::CoordinateFrame& CF);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaAtomicClasses.h:29` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes pushCoordinateFrame within App - Scripting & Lua VM. Coordinates interactions with `pushNewObject`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pushNewObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushCoordinateFrame`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 31. `pushPhysicalProperties`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void pushPhysicalProperties(lua_State *L, const PhysicalProperties& v);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaAtomicClasses.h:62` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes pushPhysicalProperties within App - Scripting & Lua VM. Coordinates interactions with `getCustomEnabled, pushNewObject, lua_pushnil`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getCustomEnabled`, `pushNewObject`, `lua_pushnil`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushPhysicalProperties`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 32. `pushRect2D`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void pushRect2D(lua_State *L, const G3D::Rect2D& v);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaAtomicClasses.h:84` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes pushRect2D within App - Scripting & Lua VM. Coordinates interactions with `pushNewObject`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pushNewObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushRect2D`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 33. `pushRegion3`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void pushRegion3(lua_State *L, const RBX::Region3& v);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaAtomicClasses.h:99` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes pushRegion3 within App - Scripting & Lua VM. Coordinates interactions with `pushNewObject`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pushNewObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushRegion3`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 34. `pushRegion3int16`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void pushRegion3int16(lua_State *L, const RBX::Region3int16& v);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaAtomicClasses.h:115` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes pushRegion3int16 within App - Scripting & Lua VM. Coordinates interactions with `pushNewObject`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pushNewObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushRegion3int16`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 35. `pushVector3`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void pushVector3(lua_State *L, const G3D::Vector3& v);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaAtomicClasses.h:130` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes pushVector3 within App - Scripting & Lua VM. Coordinates interactions with `pushNewObject`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pushNewObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushVector3`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 36. `pushVector3int16`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void pushVector3int16(lua_State *L, const G3D::Vector3int16& v);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaAtomicClasses.h:152` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes pushVector3int16 within App - Scripting & Lua VM. Coordinates interactions with `pushNewObject`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pushNewObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushVector3int16`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 37. `pushRay`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void pushRay(lua_State *L, const RBX::RbxRay& v);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaAtomicClasses.h:172` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes pushRay within App - Scripting & Lua VM. Coordinates interactions with `pushNewObject`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pushNewObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushRay`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 38. `pushVector2`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void pushVector2(lua_State *L, const RBX::Vector2& v);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaAtomicClasses.h:193` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes pushVector2 within App - Scripting & Lua VM. Coordinates interactions with `pushNewObject`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pushNewObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushVector2`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 39. `pushVector2int16`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void pushVector2int16(lua_State *L, const RBX::Vector2int16& v);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaAtomicClasses.h:213` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes pushVector2int16 within App - Scripting & Lua VM. Coordinates interactions with `pushNewObject`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pushNewObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushVector2int16`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 40. `pushUDim`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void pushUDim(lua_State *L, const RBX::UDim& v);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaAtomicClasses.h:258` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes pushUDim within App - Scripting & Lua VM. Coordinates interactions with `pushNewObject`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pushNewObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushUDim`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 41. `pushCellID`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void pushCellID(lua_State *L, const CellID& v);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaAtomicClasses.h:327` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes pushCellID within App - Scripting & Lua VM. Coordinates interactions with `pushNewObject`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pushNewObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushCellID`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 42. `pushNumberSequence`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void pushNumberSequence(lua_State* L, const NumberSequence& v);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaAtomicClasses.h:343` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes pushNumberSequence within App - Scripting & Lua VM. Coordinates interactions with `pushNewObject`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pushNewObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushNumberSequence`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 43. `pushColorSequence`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void pushColorSequence(lua_State* L, const ColorSequence& v);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaAtomicClasses.h:355` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes pushColorSequence within App - Scripting & Lua VM. Coordinates interactions with `pushNewObject`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pushNewObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushColorSequence`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 44. `pushNumberSequenceKeypoint`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void pushNumberSequenceKeypoint(lua_State* L, const NumberSequenceKeypoint& v);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaAtomicClasses.h:366` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes pushNumberSequenceKeypoint within App - Scripting & Lua VM. Coordinates interactions with `pushNewObject`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pushNewObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushNumberSequenceKeypoint`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 45. `pushColorSequenceKeypoint`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void pushColorSequenceKeypoint(lua_State* L, const ColorSequenceKeypoint& v);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaAtomicClasses.h:377` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes pushColorSequenceKeypoint within App - Scripting & Lua VM. Coordinates interactions with `pushNewObject`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pushNewObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushColorSequenceKeypoint`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 46. `pushNumberRange`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void pushNumberRange(lua_State* L, const NumberRange& v);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaAtomicClasses.h:388` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes pushNumberRange within App - Scripting & Lua VM. Coordinates interactions with `pushNewObject`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pushNewObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushNumberRange`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 47. `getItem`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
EnumDescriptorItemPtr getItem(lua_State *L, unsigned int index);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `EnumDescriptorItemPtr` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaEnum.h:35` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes getItem within App - Scripting & Lua VM. Coordinates interactions with `getObject`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getItem`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 48. `getItem`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool getItem(lua_State *L, unsigned int index, EnumDescriptorItemPtr& value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaEnum.h:38` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes getItem within App - Scripting & Lua VM. Coordinates interactions with `getValue`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getValue`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getItem`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 49. `registerInstanceClassLibrary`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void registerInstanceClassLibrary(lua_State *L);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaInstanceBridge.h:18` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes registerInstanceClassLibrary within App - Scripting & Lua VM. Coordinates interactions with `luaL_register, lua_setreadonly, lua_pop`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `luaL_register`, `lua_setreadonly`, `lua_pop`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `registerInstanceClassLibrary`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 50. `getInstance`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
boost::shared_ptr<Instance> getInstance(lua_State *L, unsigned int index);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `boost::shared_ptr&lt;Instance&gt;` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/script/LuaInstanceBridge.h:30` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes getInstance within App - Scripting & Lua VM. Coordinates interactions with `getPtr`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getPtr`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getInstance`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 51. `getLibraryName`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string& getLibraryName() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string&` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/script/LuaLibrary.h:13` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes getLibraryName within App - Scripting & Lua VM.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getLibraryName`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 52. `fireSourceChanged`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void fireSourceChanged();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `virtual` |
| **Source Location** | `App/include/script/LuaSourceContainer.h:40` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Declaration or inline method for fireSourceChanged.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `fireSourceChanged`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 53. `onScriptIdChanged`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void onScriptIdChanged();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `virtual` |
| **Source Location** | `App/include/script/LuaSourceContainer.h:46` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Declaration or inline method for onScriptIdChanged.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onScriptIdChanged`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 54. `T`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
operator const T() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `operator const` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/script/LuaVM.h:50` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes T within App - Scripting & Lua VM. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `T`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 55. `double`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
operator const double() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `operator const` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/script/LuaVM.h:164` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes double within App - Scripting & Lua VM. Coordinates interactions with `_mm_load_pd, _mm_load_sd, _mm_xor_pd, _mm_cvtsd_f64`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `_mm_load_pd`, `_mm_load_sd`, `_mm_xor_pd`, `_mm_cvtsd_f64`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `double`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 56. `setReloadRequested`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void setReloadRequested(bool reload);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/script/ModuleScript.h:79` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes setReloadRequested within App - Scripting & Lua VM.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setReloadRequested`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 57. `getReloadRequested`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool getReloadRequested() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/script/ModuleScript.h:81` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes getReloadRequested within App - Scripting & Lua VM.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getReloadRequested`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 58. `update`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
FORCEINLINE void update(const void* ptr);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `FORCEINLINE void` |
| **Modifiers** | None |
| **Source Location** | `App/include/script/ScriptContext.h:128` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes update within App - Scripting & Lua VM.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

This function is exercised in **1 test case(s)**:

- **`HttpCacheEntryTest::CACHE_UPDATE_TEST`** (`App.UnitTest/HttpCacheEntryTest.cpp:81`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(200, result.getCacheHeader().responseCode)`, `BOOST_CHECK_EQUAL(httpHeaders, result.getResponseHeader().toString())`
  - **Callsite Snippet:** `HttpPlatformImpl::Cache::CacheResult result = HttpPlatformImpl::Cache::CacheResult::update(NULL, url.c_str(), 200, headers, body);`

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Behavior branches internally via conditional compilation for: Windows (Win32/x64 API). Alternative platform-specific implementations exist in: `RobloxStudio/filewatcher/FileWatcherWin32.cpp`.

- **Platform Preprocessor Guards:** `Windows (Win32/x64 API)`
- **Alternative Implementation Files:** `RobloxStudio/filewatcher/FileWatcherWin32.cpp`

---

### 59. `checkAnchor`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
FORCEINLINE bool checkAnchor(const void* ptr) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `FORCEINLINE bool` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/script/ScriptContext.h:138` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Executes checkAnchor within App - Scripting & Lua VM.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `checkAnchor`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Behavior branches internally via conditional compilation for: Windows (Win32/x64 API).

- **Platform Preprocessor Guards:** `Windows (Win32/x64 API)`

---

### 60. `state`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
: state(NotFetchedYet);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `:` |
| **Modifiers** | None |
| **Source Location** | `App/include/script/ScriptContext.h:199` |
| **Subsystem** | `App - Scripting & Lua VM` |

#### How it Works Internally

Declaration or inline method for state.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `state`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---


:::tip Additional Functions
There are **777 additional internal and inline functions** in this subsystem. All functions are indexed and cross-referenced in the **[Complete Function Catalog](./function-catalog.md)**.
:::

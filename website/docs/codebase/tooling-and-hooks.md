---
sidebar_position: 24
title: Tooling & Test Hooks
description: RbxTestHooks DLL, CoreScriptConverter2, and developer diagnostic tools.
---

# Tooling & Test Hooks

RbxTestHooks DLL, CoreScriptConverter2, and developer diagnostic tools.


## FAQ

### How should I use a test hook or converter safely?

Inspect the tool entry point and arguments first, and use a disposable copy for conversion experiments. The catalog does not guarantee tools are currently buildable.

### How can I investigate this in the repository?

From the repository root, search the relevant tracked files for a starting point (results are leads, not proof of behavior):

```bash
git grep -n -i -F -- 'hook' -- RbxTestHooks
```

Read the surrounding implementation and callers, and check relevant tests before making changes. A search may return no matches when terminology or tracked files change.

## Subsystem Metrics

- **Total Documented Functions:** `9`
- **Functions Exercised in Tests:** `0`
- **Platform-Divergent Implementations:** `2`
- **Component Source Files:** `3`

## Source Files

<details>
<summary>View all 3 source files in this subsystem</summary>

| Source File | Path |
| :--- | :--- |
| `cscmain.cpp` | `CoreScriptConverter2/cscmain.cpp` |
| `RbxTestHooks.cpp` | `RbxTestHooks/RbxTestHooks.cpp` |
| `dllmain.cpp` | `RbxTestHooks/dllmain.cpp` |

</details>

---

## Function Reference

### 1. `fatal`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int fatal(const char* fmt, ...);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `static` |
| **Source Location** | `CoreScriptConverter2/cscmain.cpp:69` |
| **Subsystem** | `Tooling & Test Hooks` |

#### How it Works Internally

Executes fatal within Tooling & Test Hooks. Coordinates interactions with `va_start, fprintf, vfprintf, va_end`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `va_start`, `fprintf`, `vfprintf`, `va_end`, `exit`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `fatal`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 2. `mapget`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
typename Map::mapped_type* mapget(const Map& m, const typename Map::key_type& k);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `typename Map::mapped_type*` |
| **Modifiers** | `static inline` |
| **Source Location** | `CoreScriptConverter2/cscmain.cpp:79` |
| **Subsystem** | `Tooling & Test Hooks` |

#### How it Works Internally

Executes mapget within Tooling & Test Hooks. Coordinates interactions with `find, end`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `find`, `end`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `mapget`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/XboxUtils.h`.

- **Alternative Implementation Files:** `XboxClient/XboxUtils.h`

---

### 3. `rdconfig`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void rdconfig(const char* cfgfile, char** argv);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `CoreScriptConverter2/cscmain.cpp:87` |
| **Subsystem** | `Tooling & Test Hooks` |

#### How it Works Internally

Executes rdconfig within Tooling & Test Hooks. Coordinates interactions with `clear, fopen, fatal, fgets`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `clear`, `fopen`, `fatal`, `fgets`, `strchr`, `isalnum`, `strlen`, `insert`, `value_type`, `fclose`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `rdconfig`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 4. `rdfile`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void rdfile(string* result, const path& filepath);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CoreScriptConverter2/cscmain.cpp:132` |
| **Subsystem** | `Tooling & Test Hooks` |

#### How it Works Internally

Executes rdfile within Tooling & Test Hooks. Coordinates interactions with `ASSERT, _wfopen, native, c_str`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `ASSERT`, `_wfopen`, `native`, `c_str`, `fopen`, `fatal`, `fseek`, `ftell`, `resize`, `fread`, `data`, `fclose`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `rdfile`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 5. `hexa`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
char* hexa(unsigned char ch);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `char*` |
| **Modifiers** | None |
| **Source Location** | `CoreScriptConverter2/cscmain.cpp:192` |
| **Subsystem** | `Tooling & Test Hooks` |

#### How it Works Internally

Executes hexa within Tooling & Test Hooks.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `hexa`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 6. `printBuffer`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void printBuffer(ostream& os, const string& name, const string& data);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `CoreScriptConverter2/cscmain.cpp:204` |
| **Subsystem** | `Tooling & Test Hooks` |

#### How it Works Internally

Executes printBuffer within Tooling & Test Hooks. Coordinates interactions with `size, hexa`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `size`, `hexa`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `printBuffer`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 7. `main`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
int main(int argc, char** argv);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | None |
| **Source Location** | `CoreScriptConverter2/cscmain.cpp:216` |
| **Subsystem** | `Tooling & Test Hooks` |

#### How it Works Internally

Executes main within Tooling & Test Hooks. Coordinates interactions with `strcmp, fprintf, fatal, rdconfig`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `strcmp`, `fprintf`, `fatal`, `rdconfig`, `c_str`, `begin`, `end`, `printf`, `mapget`, `rsclocPath`, `parent_path`, `buildFileList`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `main`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `WindowsClient/RobloxGoldenHashPatcher/main.cpp`, `XboxClient/fetchfflags.py`, `XboxClient/main.cpp`.

- **Alternative Implementation Files:** `WindowsClient/RobloxGoldenHashPatcher/main.cpp`, `XboxClient/fetchfflags.py`, `XboxClient/main.cpp`

---

### 8. `IWorkspaceTestHooks_ExecScript`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
HRESULT IWorkspaceTestHooks_ExecScript(IWorkspaceTestHooks *p, BSTR script, VARIANT arg1, VARIANT arg2, VARIANT arg3, VARIANT arg4, SAFEARRAY** result);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `HRESULT` |
| **Modifiers** | None |
| **Source Location** | `RbxTestHooks/RbxTestHooks.cpp:8` |
| **Subsystem** | `Tooling & Test Hooks` |

#### How it Works Internally

Executes IWorkspaceTestHooks_ExecScript within Tooling & Test Hooks. Coordinates interactions with `ExecScriptImpl`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `ExecScriptImpl`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `IWorkspaceTestHooks_ExecScript`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 9. `DllMain`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
BOOL APIENTRY DllMain(HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `BOOL APIENTRY` |
| **Modifiers** | None |
| **Source Location** | `RbxTestHooks/dllmain.cpp:2` |
| **Subsystem** | `Tooling & Test Hooks` |

#### How it Works Internally

Executes DllMain within Tooling & Test Hooks.

- **Control Flow & Execution:** Multi-case state dispatch, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `DllMain`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

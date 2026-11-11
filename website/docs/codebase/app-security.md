---
sidebar_position: 13
title: App - Security & Validation
description: Security contexts, permission checks, script signing, and hash verification.
---

# App - Security & Validation

Security contexts, permission checks, script signing, and hash verification.


## FAQ

### How do I verify a permission check?

Trace the protected operation and its caller to the actual identity or permission check. Do not infer authorization guarantees from a generated function label.

### How can I investigate this in the repository?

From the repository root, search the relevant tracked files for a starting point (results are leads, not proof of behavior):

```bash
git grep -n -i -F -- 'Security::' -- App
```

Read the surrounding implementation and callers, and check relevant tests before making changes. A search may return no matches when terminology or tracked files change.

## Subsystem Metrics

- **Total Documented Functions:** `29`
- **Functions Exercised in Tests:** `0`
- **Platform-Divergent Implementations:** `0`
- **Component Source Files:** `6`

## Source Files

<details>
<summary>View all 6 source files in this subsystem</summary>

| Source File | Path |
| :--- | :--- |
| `ApiSecurity.h` | `App/include/security/ApiSecurity.h` |
| `FuzzyTokens.h` | `App/include/security/FuzzyTokens.h` |
| `JunkCode.h` | `App/include/security/JunkCode.h` |
| `SecurityContext.h` | `App/include/security/SecurityContext.h` |
| `FuzzyTokens.cpp` | `App/security/FuzzyTokens.cpp` |
| `SecurityContext.cpp` | `App/security/SecurityContext.cpp` |

</details>

---

## Function Reference

### 1. `callCheckSetBasicFlag`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
FORCEINLINE void callCheckSetBasicFlag(unsigned int flags);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `FORCEINLINE void` |
| **Modifiers** | None |
| **Source Location** | `App/include/security/ApiSecurity.h:65` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Executes callCheckSetBasicFlag within App - Security & Validation. Coordinates interactions with `addFlagFast`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `addFlagFast`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `callCheckSetBasicFlag`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 2. `callCheckSetApiFlag`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
FORCEINLINE void callCheckSetApiFlag(unsigned int flags);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `FORCEINLINE void` |
| **Modifiers** | None |
| **Source Location** | `App/include/security/ApiSecurity.h:92` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Executes callCheckSetApiFlag within App - Security & Validation. Coordinates interactions with `addFlagSafe`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `addFlagSafe`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `callCheckSetApiFlag`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 3. `callCheckNop`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
FORCEINLINE void callCheckNop(unsigned int flags);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `FORCEINLINE void` |
| **Modifiers** | None |
| **Source Location** | `App/include/security/ApiSecurity.h:98` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Declaration or inline method for callCheckNop.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `callCheckNop`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 4. `getUnicodeDllName`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
WCHAR* getUnicodeDllName(const UNICODE_STRING& str) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `WCHAR*` |
| **Modifiers** | `inline const` |
| **Source Location** | `App/include/security/ApiSecurity.h:172` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Executes getUnicodeDllName within App - Security & Validation.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getUnicodeDllName`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 5. `rbxGetNtdll`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
HMODULE rbxGetNtdll();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `HMODULE` |
| **Modifiers** | `inline` |
| **Source Location** | `App/include/security/ApiSecurity.h:189` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

This gets the location of ntdll using the documented parts of the PE format. The intent is to make it harder for anyone who wants to hook GetModuleHandle. This is not foolproof as the PEB or PEB pointer could be modified.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `__readfsdword`, `getUnicodeDllName`, `_wcsnicmp`, `min`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `rbxGetNtdll`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 6. `detectDllByExceptionChain`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
FORCEINLINE uint32_t detectDllByExceptionChain(void* addrOfChain, unsigned int kFlags);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `FORCEINLINE uint32_t` |
| **Modifiers** | None |
| **Source Location** | `App/include/security/ApiSecurity.h:278` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

+ C *nextHandler     | + C *handler() + 8 *handler()       | + 8  scopeTable + 4  state           | + 4  tryLevel +00  saved ebp       | +00  saved ebp - 4  return address  | - 4  return address - 8  first arg       | - 8  first arg -xx  last arg        | -xx  last arg This will get generated in some functions that don't have try-catch blocks.  Basically if something could throw, objects might need to be destroyed. fs:[0] also contains a pointer to nextHandler, but is out of place in the middle of a function. The list will always have a size of at least 2 -- the entry in ntdll and the entry we started with. There is a case with boost::threads, as these get created with msvcr's threadstartex (after ntdll rtlInitThread).  However, boost::threads will have three exception handlers in the boost code before getting into msvcr.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `detectDllByExceptionChain`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 7. `generateCallInfo`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
FORCEINLINE void generateCallInfo(void* addrOfFirstArg, std::vector<CallChainInfo>& info);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `FORCEINLINE void` |
| **Modifiers** | None |
| **Source Location** | `App/include/security/ApiSecurity.h:324` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Executes generateCallInfo within App - Security & Validation. Coordinates interactions with `push_back, CallChainInfo`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `push_back`, `CallChainInfo`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `generateCallInfo`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 8. `detectDllByExceptionChainStack`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
FORCEINLINE uint32_t detectDllByExceptionChainStack(void* addrOfFirstArg, unsigned int kFlags);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `FORCEINLINE uint32_t` |
| **Modifiers** | None |
| **Source Location** | `App/include/security/ApiSecurity.h:345` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Executes detectDllByExceptionChainStack within App - Security & Validation.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `detectDllByExceptionChainStack`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 9. `detectDllByExceptionChainTeb`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
FORCEINLINE uint32_t detectDllByExceptionChainTeb(unsigned int kFlags);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `FORCEINLINE uint32_t` |
| **Modifiers** | None |
| **Source Location** | `App/include/security/ApiSecurity.h:355` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

not all functions add an exception handler to the chain, so the stack based method doesn't always work.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `__readfsdword`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `detectDllByExceptionChainTeb`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 10. `detectDllByExceptionChainTeb`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
FORCEINLINE uint32_t detectDllByExceptionChainTeb(unsigned int kFlags);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `FORCEINLINE uint32_t` |
| **Modifiers** | None |
| **Source Location** | `App/include/security/ApiSecurity.h:360` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Executes detectDllByExceptionChainTeb within App - Security & Validation.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `detectDllByExceptionChainTeb`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 11. `detectDllByExceptionChainStack`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
FORCEINLINE uint32_t detectDllByExceptionChainStack(void* addrOfFirstArg, unsigned int kFlags);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `FORCEINLINE uint32_t` |
| **Modifiers** | None |
| **Source Location** | `App/include/security/ApiSecurity.h:364` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Executes detectDllByExceptionChainStack within App - Security & Validation.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `detectDllByExceptionChainStack`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 12. `generateCallInfo`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
FORCEINLINE void generateCallInfo(void* addrOfFirstArg, std::vector<CallChainInfo>& info);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `FORCEINLINE void` |
| **Modifiers** | None |
| **Source Location** | `App/include/security/ApiSecurity.h:368` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Executes generateCallInfo within App - Security & Validation.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `generateCallInfo`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 13. `addFlagFast`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void addFlagFast(unsigned long long flags);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/security/FuzzyTokens.h:42` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Executes addFlagFast within App - Security & Validation.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `addFlagFast`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 14. `addFlagSafe`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void addFlagSafe(unsigned long long flags);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/security/FuzzyTokens.h:52` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Executes addFlagSafe within App - Security & Validation. Coordinates interactions with `lock`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** RAII mutex lock acquisition (scoped_lock); Thread mutual exclusion locking (boost::mutex).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lock`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `addFlagSafe`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 15. `getPrev`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
long long getPrev();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `long long` |
| **Modifiers** | `unsigned` |
| **Source Location** | `App/include/security/FuzzyTokens.h:58` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Executes getPrev within App - Security & Validation.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getPrev`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 16. `setLastTag`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void setLastTag(unsigned long long tag);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/security/FuzzyTokens.h:73` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Executes setLastTag within App - Security & Validation.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setLastTag`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 17. `junk`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void junk();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `inline` |
| **Source Location** | `App/include/security/JunkCode.h:11` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Declaration or inline method for junk.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `junk`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 18. `requirePermission`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void requirePermission(Permissions permission, const char* operation = 0) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/security/SecurityContext.h:69` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Throws an exception if the current thread's Context doesn't have the requested Role

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** C++ exception throw on invalid state or failure; Standard runtime error exception formulation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `isInRole`, `runtime_error`, `identity`, `operation`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `requirePermission`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 19. `hasPermission`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool hasPermission(Permissions permission);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `App/include/security/SecurityContext.h:90` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Executes hasPermission within App - Security & Validation. Coordinates interactions with `isInRole`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `isInRole`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `hasPermission`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 20. `Security::teaDecrypt`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
long long Security::teaDecrypt(unsigned long long inTag);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `long long` |
| **Modifiers** | `unsigned` |
| **Source Location** | `App/security/FuzzyTokens.cpp:6` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Executes teaDecrypt within App - Security & Validation. Coordinates interactions with `Algorithm`.

- **Control Flow & Execution:** Iterative loop processing, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `Algorithm`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `teaDecrypt`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 21. `Security::teaEncrypt`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
long long Security::teaEncrypt(unsigned long long inTag);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `long long` |
| **Modifiers** | `unsigned` |
| **Source Location** | `App/security/FuzzyTokens.cpp:29` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Executes teaEncrypt within App - Security & Validation.

- **Control Flow & Execution:** Iterative loop processing, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `teaEncrypt`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 22. `ClientFuzzySecurityToken::crypt`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
long long ClientFuzzySecurityToken::crypt();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `long long` |
| **Modifiers** | `unsigned` |
| **Source Location** | `App/security/FuzzyTokens.cpp:61` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Executes crypt within App - Security & Validation. Coordinates interactions with `lock, teaEncrypt`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** RAII mutex lock acquisition (scoped_lock); Thread mutual exclusion locking (boost::mutex).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lock`, `teaEncrypt`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `crypt`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 23. `ignoreFlags`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
: ignoreFlags(ignoreFlags);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `:` |
| **Modifiers** | None |
| **Source Location** | `App/security/FuzzyTokens.cpp:72` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Executes ignoreFlags within App - Security & Validation.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `ignoreFlags`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 24. `ServerFuzzySecurityToken::decrypt`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
long long ServerFuzzySecurityToken::decrypt(unsigned long long inTag);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `long long` |
| **Modifiers** | `unsigned` |
| **Source Location** | `App/security/FuzzyTokens.cpp:80` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

There is current some difficult to find bug that allows one security packet to be dropped or not sent.  This scheme was not designed to make this case easy.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `teaDecrypt`, `teaEncrypt`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `decrypt`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 25. `Context::isInRole`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool Context::isInRole(Identities identity, Permissions p);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `App/security/SecurityContext.cpp:10` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Executes isInRole within App - Security & Validation. Coordinates interactions with `defined, RBXASSERT`.

- **Control Flow & Execution:** Conditional branching, Multi-case state dispatch, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `defined`, `RBXASSERT`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isInRole`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 26. `Context::current`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Context& Context::current();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Context&` |
| **Modifiers** | None |
| **Source Location** | `App/security/SecurityContext.cpp:41` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Executes current within App - Security & Validation. Coordinates interactions with `ptr, get, anonymous, reset`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `ptr`, `get`, `anonymous`, `reset`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `current`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 27. `Context::tssCleanup`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Context::tssCleanup(Context*);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/security/SecurityContext.cpp:53` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Declaration or inline method for tssCleanup.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `tssCleanup`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 28. `Context::ptr`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
boost::thread_specific_ptr<Context>& Context::ptr();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `boost::thread_specific_ptr&lt;Context&gt;&` |
| **Modifiers** | None |
| **Source Location** | `App/security/SecurityContext.cpp:59` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Executes ptr within App - Security & Validation. Coordinates interactions with `value`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `value`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `ptr`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 29. `current`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
: current(identity);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `:` |
| **Modifiers** | None |
| **Source Location** | `App/security/SecurityContext.cpp:67` |
| **Subsystem** | `App - Security & Validation` |

#### How it Works Internally

Executes current within App - Security & Validation. Coordinates interactions with `ptr, get, reset`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `ptr`, `get`, `reset`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `current`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

---
sidebar_position: 20
title: Windows Client & Win Launcher
description: Windows player application, Document/View, launcher utilities, and hooks.
---

# Windows Client & Win Launcher

Windows player application, Document/View, launcher utilities, and hooks.

## Subsystem Metrics

- **Total Documented Functions:** `499`
- **Functions Exercised in Tests:** `14`
- **Platform-Divergent Implementations:** `117`
- **Component Source Files:** `45`

## Source Files

<details>
<summary>View all 45 source files in this subsystem</summary>

| Source File | Path |
| :--- | :--- |
| `AuthenticationMarshallar.cpp` | `Win/AuthenticationMarshallar.cpp` |
| `CheckDbg.cpp` | `Win/CheckDbg.cpp` |
| `DSVideoCaptureEngine.cpp` | `Win/DSVideoCaptureEngine.cpp` |
| `DSVideoCaptureEngine.h` | `Win/DSVideoCaptureEngine.h` |
| `DumpErrorUploader.cpp` | `Win/DumpErrorUploader.cpp` |
| `ErrorUploader.cpp` | `Win/ErrorUploader.cpp` |
| `ErrorUploader.h` | `Win/ErrorUploader.h` |
| `LogManager.cpp` | `Win/LogManager.cpp` |
| `LogManager.h` | `Win/LogManager.h` |
| `ProcessInformation.h` | `Win/ProcessInformation.h` |
| `ScriptErrorUploader.cpp` | `Win/ScriptErrorUploader.cpp` |
| `ScriptErrorUploader.h` | `Win/ScriptErrorUploader.h` |
| `SharedLauncher.cpp` | `Win/SharedLauncher.cpp` |
| `UserInputUtil.cpp` | `Win/UserInputUtil.cpp` |
| `VersionInfo.cpp` | `Win/VersionInfo.cpp` |
| `VideoControl.cpp` | `Win/VideoControl.cpp` |
| `VideoControl.h` | `Win/VideoControl.h` |
| `VistaTools.cpp` | `Win/VistaTools.cpp` |
| `VistaTools.h` | `Win/VistaTools.h` |
| `sitelock.h` | `Win/sitelock.h` |
| `Application.cpp` | `WindowsClient/Application.cpp` |
| `Application.h` | `WindowsClient/Application.h` |
| `Crypt.cpp` | `WindowsClient/Crypt.cpp` |
| `Document.cpp` | `WindowsClient/Document.cpp` |
| `Document.h` | `WindowsClient/Document.h` |
| `FunctionMarshaller.cpp` | `WindowsClient/FunctionMarshaller.cpp` |
| `GameVerbs.cpp` | `WindowsClient/GameVerbs.cpp` |
| `GameVerbs.h` | `WindowsClient/GameVerbs.h` |
| `RandomPadding.cpp` | `WindowsClient/RandomPadding.cpp` |
| `RbxWebView.cpp` | `WindowsClient/RbxWebView.cpp` |
| `RbxWebView.h` | `WindowsClient/RbxWebView.h` |
| `ReleasePatcher.cpp` | `WindowsClient/ReleasePatcher.cpp` |
| `RenderJob.cpp` | `WindowsClient/RenderJob.cpp` |
| `main.cpp` | `WindowsClient/RobloxGoldenHashPatcher/main.cpp` |
| `Teleporter.cpp` | `WindowsClient/Teleporter.cpp` |
| `Teleporter.h` | `WindowsClient/Teleporter.h` |
| `UserInput.cpp` | `WindowsClient/UserInput.cpp` |
| `UserInput.h` | `WindowsClient/UserInput.h` |
| `View.cpp` | `WindowsClient/View.cpp` |
| `View.h` | `WindowsClient/View.h` |
| `WebBrowserAxDialog.cpp` | `WindowsClient/WebBrowserAxDialog.cpp` |
| `WebBrowserAxDialog.h` | `WindowsClient/WebBrowserAxDialog.h` |
| `functionHooks.cpp` | `WindowsClient/functionHooks.cpp` |
| `main.cpp` | `WindowsClient/main.cpp` |
| `robloxHooks.cpp` | `WindowsClient/robloxHooks.cpp` |

</details>

---

## Function Reference

### 1. `buildUrl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string buildUrl(const char* url, const char* ticket);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `Win/AuthenticationMarshallar.cpp:20` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes buildUrl within Windows Client & Win Launcher.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `buildUrl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 2. `AuthenticationMarshallar::Authenticate`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string AuthenticationMarshallar::Authenticate(const char* url, const char* ticket);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `Win/AuthenticationMarshallar.cpp:32` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes Authenticate within Windows Client & Win Launcher. Coordinates interactions with `http, buildUrl, c_str, setAuthDomain`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Exception handling block (try/catch recovery).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `http`, `buildUrl`, `c_str`, `setAuthDomain`, `get`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `Authenticate`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 3. `AuthenticationMarshallar::AuthenticateAsync`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
RBX::HttpFuture AuthenticationMarshallar::AuthenticateAsync(const char* url, const char* ticket);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `RBX::HttpFuture` |
| **Modifiers** | None |
| **Source Location** | `Win/AuthenticationMarshallar.cpp:54` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes AuthenticateAsync within Windows Client & Win Launcher. Coordinates interactions with `addHeader, get, buildUrl`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `addHeader`, `get`, `buildUrl`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `AuthenticateAsync`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 4. `GetFS`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
DWORD GetFS();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `DWORD` |
| **Modifiers** | `static __forceinline` |
| **Source Location** | `Win/CheckDbg.cpp:6` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes GetFS within Windows Client & Win Launcher. Coordinates interactions with `GetFlag, __declspec, isDbg1, hash_value`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `GetFlag`, `__declspec`, `isDbg1`, `hash_value`, `return`, `isDbg2`, `rand`, `isDbg3`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetFS`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 5. `GetFlag`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
DWORD GetFlag(DWORD f);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `DWORD` |
| **Modifiers** | `static __forceinline` |
| **Source Location** | `Win/CheckDbg.cpp:19` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes GetFlag within Windows Client & Win Launcher.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetFlag`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 6. `GetTargetFrameRate`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int GetTargetFrameRate() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `const` |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:108` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes GetTargetFrameRate within Windows Client & Win Launcher.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetTargetFrameRate`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 7. `GetActualFrameRate`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int GetActualFrameRate() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `const` |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:109` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes GetActualFrameRate within Windows Client & Win Launcher.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetActualFrameRate`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 8. `GetTime`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
LONG GetTime();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `LONG` |
| **Modifiers** | `virtual` |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:166` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes GetTime within Windows Client & Win Launcher. Coordinates interactions with `Millisecs`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `Millisecs`.

#### How it is Used in Tests

This function is exercised in **1 test case(s)**:

- **`PathfindingTest::PathfindingStress`** (`App.UnitTest/PathfindingTest.cpp:48`)
  - **Usage Pattern:** `Direct Call`
  - **Callsite Snippet:** `RakNet::Time start_time = RakNet::GetTime();`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 9. `CVideoStreamFilter::pushNextFrame`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CVideoStreamFilter::pushNextFrame(BYTE *data, int size, int cx, int cy, int bpp);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:211` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes pushNextFrame within Windows Client & Win Launcher.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushNextFrame`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 10. `CVideoStreamFilter::GetTargetFrameRate`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int CVideoStreamFilter::GetTargetFrameRate() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `const` |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:216` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes GetTargetFrameRate within Windows Client & Win Launcher. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetTargetFrameRate`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 11. `CVideoStreamFilter::GetActualFrameRate`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int CVideoStreamFilter::GetActualFrameRate() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `const` |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:221` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes GetActualFrameRate within Windows Client & Win Launcher. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetActualFrameRate`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 12. `CVideoStreamFilter::SetAudioClock`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CVideoStreamFilter::SetAudioClock(IAudioTime *clock);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:226` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes SetAudioClock within Windows Client & Win Launcher. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `SetAudioClock`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 13. `CVideoStreamFilter::GetCaptureSize`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CVideoStreamFilter::GetCaptureSize(int &width, int &height);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:231` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes GetCaptureSize within Windows Client & Win Launcher.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetCaptureSize`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 14. `CVideoStreamFilter::GetQueueSize`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int CVideoStreamFilter::GetQueueSize();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:236` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes GetQueueSize within Windows Client & Win Launcher. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetQueueSize`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 15. `CVideoStream::SetAudioClock`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CVideoStream::SetAudioClock(IAudioTime *clock);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:267` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes SetAudioClock within Windows Client & Win Launcher.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `SetAudioClock`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 16. `CVideoStream::pushNextFrame`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CVideoStream::pushNextFrame(BYTE *data, int size, int cx, int cy, int bpp);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:272` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes pushNextFrame within Windows Client & Win Launcher. Coordinates interactions with `lock, push, Set`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lock`, `push`, `Set`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushNextFrame`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 17. `CVideoStream::GetQueueSize`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int CVideoStream::GetQueueSize();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:280` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes GetQueueSize within Windows Client & Win Launcher. Coordinates interactions with `lock, size`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lock`, `size`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetQueueSize`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 18. `CVideoStream::GetCaptureSize`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CVideoStream::GetCaptureSize(int &width, int &height);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:287` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes GetCaptureSize within Windows Client & Win Launcher.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetCaptureSize`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 19. `CVideoStream::FillBuffer`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
HRESULT CVideoStream::FillBuffer(IMediaSample *pms);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `HRESULT` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:293` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes FillBuffer within Windows Client & Win Launcher. Coordinates interactions with `CheckPointer, GetPointer, GetSize, cAutoLockShared`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Multi-case state dispatch, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new; Heap memory deallocation via operator delete.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `CheckPointer`, `GetPointer`, `GetSize`, `cAutoLockShared`, `Lock`, `size`, `Unlock`, `Wait`, `Reset`, `empty`, `front`, `GetAbsoluteTime`.
- **External Library Dependencies:** `Boost C++ Libraries`, `OpenGL / GLES Graphics API`, `FMOD Audio Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `FillBuffer`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 20. `CVideoStream::Notify`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
STDMETHODIMP CVideoStream::Notify(IBaseFilter * pSender, Quality q);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `STDMETHODIMP` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:355` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Notify Alter the repeat rate according to quality management messages sent from the downstream filter (often the renderer).  Wind it up or down according to the flooding level - also skip forward if we are notified of Late-ness

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `Notify`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 21. `CVideoStream::GetMediaType`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
HRESULT CVideoStream::GetMediaType(int iPosition, CMediaType *pmt);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `HRESULT` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:359` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes GetMediaType within Windows Client & Win Launcher. Coordinates interactions with `CheckPointer, cAutoLock, pStateLock, AllocFormatBuffer`.

- **Control Flow & Execution:** Conditional branching, Multi-case state dispatch, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `CheckPointer`, `cAutoLock`, `pStateLock`, `AllocFormatBuffer`, `return`, `ZeroMemory`, `GetBitmapSize`, `SetRectEmpty`, `SetType`, `SetFormatType`, `SetTemporalCompression`, `GetBitmapSubtype`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetMediaType`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 22. `CVideoStream::CheckMediaType`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
HRESULT CVideoStream::CheckMediaType(const CMediaType *pMediaType);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `HRESULT` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:411` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes CheckMediaType within Windows Client & Win Launcher. Coordinates interactions with `CheckPointer, Type, IsFixedSize, Subtype`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `CheckPointer`, `Type`, `IsFixedSize`, `Subtype`, `Format`, `abs`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `CheckMediaType`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 23. `CVideoStream::DecideBufferSize`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
HRESULT CVideoStream::DecideBufferSize(IMemAllocator *pAlloc, ALLOCATOR_PROPERTIES *pProperties);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `HRESULT` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:453` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes DecideBufferSize within Windows Client & Win Launcher. Coordinates interactions with `CheckPointer, cAutoLock, pStateLock, Format`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `CheckPointer`, `cAutoLock`, `pStateLock`, `Format`, `ASSERT`, `succeed`, `SetProperties`, `FAILED`, `buffer`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `DecideBufferSize`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 24. `CVideoStream::SetMediaType`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
HRESULT CVideoStream::SetMediaType(const CMediaType *pMediaType);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `HRESULT` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:492` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes SetMediaType within Windows Client & Win Launcher. Coordinates interactions with `cAutoLock, pStateLock, SUCCEEDED, Format`.

- **Control Flow & Execution:** Conditional branching, Multi-case state dispatch, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `cAutoLock`, `pStateLock`, `SUCCEEDED`, `Format`, `RBXASSERT`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `SetMediaType`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 25. `CVideoStream::OnThreadCreate`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
HRESULT CVideoStream::OnThreadCreate();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `HRESULT` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:525` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

OnThreadCreate As we go active reset the stream time to zero

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `cAutoLockShared`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `OnThreadCreate`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 26. `CAudioStreamFilter::GetExpectedFramesCount`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int CAudioStreamFilter::GetExpectedFramesCount(int frameDelay) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `const` |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:557` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes GetExpectedFramesCount within Windows Client & Win Launcher. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetExpectedFramesCount`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 27. `CAudioStreamFilter::StopSoundCapture`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CAudioStreamFilter::StopSoundCapture();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:567` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes StopSoundCapture within Windows Client & Win Launcher. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `StopSoundCapture`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 28. `CAudioStream::GetAbsoluteTime`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
LONG CAudioStream::GetAbsoluteTime();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `LONG` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:614` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes GetAbsoluteTime within Windows Client & Win Launcher.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetAbsoluteTime`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 29. `CAudioStream::GetExpectedFramesCount`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int CAudioStream::GetExpectedFramesCount(int frameDelay) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `const` |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:619` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes GetExpectedFramesCount within Windows Client & Win Launcher. Coordinates interactions with `return, Millisecs`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `return`, `Millisecs`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetExpectedFramesCount`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 30. `CAudioStream::StopSoundCapture`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CAudioStream::StopSoundCapture();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:624` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes StopSoundCapture within Windows Client & Win Launcher. Coordinates interactions with `setBypass, release, Set`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `setBypass`, `release`, `Set`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `StopSoundCapture`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 31. `CAudioStream::audioGrabber`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
FMOD_RESULT F_CALLBACK CAudioStream::audioGrabber(FMOD_DSP_STATE *dsp_state, float *inbuffer, float *outbuffer, unsigned int length, int inchannels, int *outchannels);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `FMOD_RESULT F_CALLBACK` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:635` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes audioGrabber within Windows Client & Win Launcher. Coordinates interactions with `getUserData, RBXASSERT, lock, push`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getUserData`, `RBXASSERT`, `lock`, `push`, `Set`.
- **External Library Dependencies:** `FMOD Audio Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `audioGrabber`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 32. `CAudioStream::FillBuffer`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
HRESULT CAudioStream::FillBuffer(IMediaSample *pms);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `HRESULT` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:671` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes FillBuffer within Windows Client & Win Launcher. Coordinates interactions with `CheckPointer, GetPointer, FAILED, lShared`. Employs heap memory deallocation via operator delete.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Heap memory deallocation via operator delete.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `CheckPointer`, `GetPointer`, `FAILED`, `lShared`, `Format`, `RBXASSERT`, `Lock`, `size`, `Unlock`, `Wait`, `Reset`, `empty`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `FillBuffer`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 33. `CAudioStream::DecideBufferSize`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
HRESULT CAudioStream::DecideBufferSize(IMemAllocator *pIMemAlloc, ALLOCATOR_PROPERTIES *pProperties);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `HRESULT` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:773` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes DecideBufferSize within Windows Client & Win Launcher. Coordinates interactions with `CheckPointer, Format, RBXASSERT, SetProperties`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `CheckPointer`, `Format`, `RBXASSERT`, `SetProperties`, `FAILED`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `DecideBufferSize`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 34. `CAudioStream::SetMediaType`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
HRESULT CAudioStream::SetMediaType(const CMediaType *pMediaType);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `HRESULT` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:814` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes SetMediaType within Windows Client & Win Launcher. Coordinates interactions with `cAutoLock, pStateLock, CheckMediaType`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `cAutoLock`, `pStateLock`, `CheckMediaType`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `SetMediaType`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 35. `CAudioStream::CheckMediaType`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
HRESULT CAudioStream::CheckMediaType(const CMediaType *pMediaType);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `HRESULT` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:823` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes CheckMediaType within Windows Client & Win Launcher. Coordinates interactions with `CheckPointer, lock, pStateLock, GetMediaType`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `CheckPointer`, `lock`, `pStateLock`, `GetMediaType`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `CheckMediaType`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 36. `CAudioStream::GetMediaType`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
HRESULT CAudioStream::GetMediaType(int iPosition, CMediaType *pmt);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `HRESULT` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:839` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes GetMediaType within Windows Client & Win Launcher. Coordinates interactions with `CheckPointer, cAutoLock, pStateLock, AllocFormatBuffer`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `CheckPointer`, `cAutoLock`, `pStateLock`, `AllocFormatBuffer`, `return`, `ZeroMemory`, `CreateAudioMediaType`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetMediaType`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 37. `CAudioStream::OnThreadCreate`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
HRESULT CAudioStream::OnThreadCreate(void);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `HRESULT` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:869` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes OnThreadCreate within Windows Client & Win Launcher. Coordinates interactions with `cAutoLockShared`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `cAutoLockShared`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `OnThreadCreate`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 38. `CAudioStream::Notify`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
STDMETHODIMP CAudioStream::Notify(IBaseFilter * pSender, Quality q);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `STDMETHODIMP` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:876` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes Notify within Windows Client & Win Launcher.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `Notify`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 39. `DSVideoCaptureEngine::BuildCaptureGraphNoThrow`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
HRESULT DSVideoCaptureEngine::BuildCaptureGraphNoThrow(int cx, int cy, bool forceNoAudio);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `HRESULT` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:915` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes BuildCaptureGraphNoThrow within Windows Client & Win Launcher. Coordinates interactions with `BuildCaptureGraph, __except`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `BuildCaptureGraph`, `__except`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `BuildCaptureGraphNoThrow`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 40. `DSVideoCaptureEngine::start`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool DSVideoCaptureEngine::start(int cx, int cy, SoundState  *s);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:927` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes start within Windows Client & Win Launcher. Coordinates interactions with `isRunning, GetSquareSizes, enabledFunction, getSampleRateFunction`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `isRunning`, `GetSquareSizes`, `enabledFunction`, `getSampleRateFunction`, `BuildCaptureGraphNoThrow`, `FAILED`, `ReportStatisticWithMessage`, `GetBaseURL`, `format`, `DestroyCaptureGgaph`, `BuildCaptureGraph`, `RBXASSERT`.

#### How it is Used in Tests

This function is exercised in **2 test case(s)**:

- **`RaycastTest::RayInvovlesThreeChunks`** (`App.UnitTest/RaycastTest.cpp:461`)
  - **Usage Pattern:** `Direct Call`
  - **Callsite Snippet:** `Vector3 start(0, 15, 15);`
- **`RaycastTest::TerrainLoopRepro`** (`App.UnitTest/RaycastTest.cpp:486`)
  - **Usage Pattern:** `Direct Call`
  - **Callsite Snippet:** `Vector3 start(-5.8e-22f, 253.4f, -.5f);`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 41. `DSVideoCaptureEngine::stop`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
bool DSVideoCaptureEngine::stop();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:971` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes stop within Windows Client & Win Launcher. Coordinates interactions with `isRunning, FASTLOG1, RBXASSERT, StopSoundCapture`. Employs heap memory deallocation via operator delete.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Heap memory deallocation via operator delete.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `isRunning`, `FASTLOG1`, `RBXASSERT`, `StopSoundCapture`, `Stop`, `FAILED`, `Sleep`, `SUCCEEDED`, `singleton`, `printf`, `DestroyCaptureGgaph`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

This function is exercised in **1 test case(s)**:

- **`SoundEffectTests::DistortionDSPUpdatesAndDetach`** (`App.UnitTest/SoundEffectTest.cpp:53`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(FMOD::System_Create(&system), FMOD_OK)`, `BOOST_REQUIRE_EQUAL(system-&gt;setOutput(FMOD_OUTPUTTYPE_NOSOUND), FMOD_OK)`
  - **Callsite Snippet:** `channel-&gt;stop();`

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `WindowsClient/RenderJob.cpp`, `XboxClient/renderJob.cpp`.

- **Alternative Implementation Files:** `WindowsClient/RenderJob.cpp`, `XboxClient/renderJob.cpp`

---

### 42. `DSVideoCaptureEngine::setVideoQuality`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void DSVideoCaptureEngine::setVideoQuality(int vq);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:1007` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Declaration or inline method for setVideoQuality.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setVideoQuality`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `Win/VideoControl.cpp`.

- **Alternative Implementation Files:** `Win/VideoControl.cpp`

---

### 43. `DSVideoCaptureEngine::isRunning`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool DSVideoCaptureEngine::isRunning();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:1010` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes isRunning within Windows Client & Win Launcher. Coordinates interactions with `GetState, RBXASSERT, SUCCEEDED, FAILED`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `GetState`, `RBXASSERT`, `SUCCEEDED`, `FAILED`, `FASTLOG`, `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isRunning`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 44. `DSVideoCaptureEngine::GetSquareSizes`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DSVideoCaptureEngine::GetSquareSizes(int cx, int cy, int &ncx, int &ncy);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:1029` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes GetSquareSizes within Windows Client & Win Launcher.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetSquareSizes`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 45. `doNothingCallbackContinuation`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void doNothingCallbackContinuation();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:1049` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Declaration or inline method for doNothingCallbackContinuation.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `doNothingCallbackContinuation`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 46. `cancelRecording`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void cancelRecording(DataModel* dm, Verb* cancelAction);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:1051` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes cancelRecording within Windows Client & Win Launcher. Coordinates interactions with `empty, notificationCallback, bind, doIt`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `empty`, `notificationCallback`, `bind`, `doIt`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `cancelRecording`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 47. `DSVideoCaptureEngine::pushNextFrame`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DSVideoCaptureEngine::pushNextFrame(void* device, Verb *cancelAction);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:1064` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes pushNextFrame within Windows Client & Win Launcher. Coordinates interactions with `FASTLOG, RBXASSERT, isRunning, GetAbsoluteTime`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new; Heap memory deallocation via operator delete.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `FASTLOG`, `RBXASSERT`, `isRunning`, `GetAbsoluteTime`, `doIt`, `getMainFramebuffer`, `getWidth`, `getHeight`, `GetSquareSizes`, `GetCaptureSize`, `getContainer`, `submitTask`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushNextFrame`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 48. `DSVideoCaptureEngine::GetTime`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
LONG DSVideoCaptureEngine::GetTime();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `LONG` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:1155` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes GetTime within Windows Client & Win Launcher. Coordinates interactions with `GetAudioTime`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `GetAudioTime`.

#### How it is Used in Tests

This function is exercised in **1 test case(s)**:

- **`PathfindingTest::PathfindingStress`** (`App.UnitTest/PathfindingTest.cpp:48`)
  - **Usage Pattern:** `Direct Call`
  - **Callsite Snippet:** `RakNet::Time start_time = RakNet::GetTime();`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 49. `DSVideoCaptureEngine::GetAbsoluteTime`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
LONG DSVideoCaptureEngine::GetAbsoluteTime();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `LONG` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:1160` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes GetAbsoluteTime within Windows Client & Win Launcher. Coordinates interactions with `timeGetTime`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `timeGetTime`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetAbsoluteTime`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 50. `DSVideoCaptureEngine::BuildCaptureGraph`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
HRESULT DSVideoCaptureEngine::BuildCaptureGraph(int cx, int cy, bool forceNoAudio);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `HRESULT` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:1175` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes BuildCaptureGraph within Windows Client & Win Launcher. Coordinates interactions with `GetVersionEx, ERROR_ON_FAIL, CoCreateInstance, QueryInterface`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `GetVersionEx`, `ERROR_ON_FAIL`, `CoCreateInstance`, `QueryInterface`, `CVideoStreamFilter`, `FAILED`, `AddFilter`, `GenerateFileName`, `SetFileName`, `WMCreateProfileManager`, `enabledFunction`, `LoadProfileByData`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `BuildCaptureGraph`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 51. `DSVideoCaptureEngine::DestroyCaptureGgaph`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DSVideoCaptureEngine::DestroyCaptureGgaph();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:1266` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes DestroyCaptureGgaph within Windows Client & Win Launcher. Coordinates interactions with `SAFE_RELEASE`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `SAFE_RELEASE`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `DestroyCaptureGgaph`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 52. `DSVideoCaptureEngine::GenerateFileName`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int DSVideoCaptureEngine::GenerateFileName(LPWSTR fileName);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | None |
| **Source Location** | `Win/DSVideoCaptureEngine.cpp:1276` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes GenerateFileName within Windows Client & Win Launcher. Coordinates interactions with `GetLocalTime, getUserDirectory, _snwprintf_s, wcsncpy_s`.

- **Control Flow & Execution:** Iterative loop processing, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `GetLocalTime`, `getUserDirectory`, `_snwprintf_s`, `wcsncpy_s`, `native`, `c_str`, `clear`, `push_back`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GenerateFileName`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 53. `getFileName`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
std::string & getFileName();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string &` |
| **Modifiers** | `virtual` |
| **Source Location** | `Win/DSVideoCaptureEngine.h:41` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes getFileName within Windows Client & Win Launcher.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getFileName`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `WindowsClient/RobloxGoldenHashPatcher/main.cpp`.

- **Alternative Implementation Files:** `WindowsClient/RobloxGoldenHashPatcher/main.cpp`

---

### 54. `DumpErrorUploader::InitCrashEvent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DumpErrorUploader::InitCrashEvent(const std::string& url, const std::string& crashEventFileName);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Win/DumpErrorUploader.cpp:35` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes InitCrashEvent within Windows Client & Win Launcher. Coordinates interactions with `urlEncode, current, writeEntry, format`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `urlEncode`, `current`, `writeEntry`, `format`, `c_str`, `reset`, `Http`, `reserve`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `InitCrashEvent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 55. `DumpErrorUploader::Upload`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void DumpErrorUploader::Upload(const std::string& url);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Win/DumpErrorUploader.cpp:47` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes Upload within Windows Client & Win Launcher. Coordinates interactions with `CreateMutex, TEXT, singleton, printf`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** RAII mutex lock acquisition (scoped_lock); Thread mutual exclusion locking (boost::mutex).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `CreateMutex`, `TEXT`, `singleton`, `printf`, `GetLastError`, `getMainLogManager`, `gatherCrashLogs`, `lock`, `size`, `push`, `wake`, `run`.
- **External Library Dependencies:** `Boost C++ Libraries`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `Upload`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `Win/ScriptErrorUploader.cpp`.

- **Alternative Implementation Files:** `Win/ScriptErrorUploader.cpp`

---

### 56. `LogFilter`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int LogFilter(unsigned int code, struct _EXCEPTION_POINTERS *ep);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | None |
| **Source Location** | `Win/DumpErrorUploader.cpp:91` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes LogFilter within Windows Client & Win Launcher. Coordinates interactions with `singleton, printf`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `singleton`, `printf`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `LogFilter`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 57. `DumpErrorUploader::UploadCrashEventFile`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DumpErrorUploader::UploadCrashEventFile(struct _EXCEPTION_POINTERS *excInfo);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Win/DumpErrorUploader.cpp:97` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes UploadCrashEventFile within Windows Client & Win Launcher. Coordinates interactions with `singleton, printf, post, c_str`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Exception handling block (try/catch recovery).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `singleton`, `printf`, `post`, `c_str`, `reportCounter`, `addPoint`, `nowFastSec`, `usedMemoryBytes`, `getMainLogManager`, `getGameState`, `str`, `getSessionId`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`, `InfluxDB Metrics Ingestion Client`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `UploadCrashEventFile`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 58. `DumpErrorUploader::run`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
RBX::worker_thread::work_result DumpErrorUploader::run(shared_ptr<data> _data);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `RBX::worker_thread::work_result` |
| **Modifiers** | None |
| **Source Location** | `Win/DumpErrorUploader.cpp:151` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes run within Windows Client & Win Launcher. Coordinates interactions with `lock, empty, CloseHandle, reportCounter`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** RAII mutex lock acquisition (scoped_lock); Thread mutual exclusion locking (boost::mutex).
- **Error Handling & Invariants:** Exception handling block (try/catch recovery).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lock`, `empty`, `CloseHandle`, `reportCounter`, `front`, `printf`, `c_str`, `substr`, `size`, `find`, `urlEncode`, `data`.
- **External Library Dependencies:** `Boost C++ Libraries`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

This function is exercised in **30 test case(s)**:

- **`Instance::WaitForChildReturnsImmediatelyIfChildPresent`** (`App.UnitTest/Instance.cpp:264`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(part-&gt;getName(), "Renamed")`
  - **Callsite Snippet:** `ServiceProvider::create&lt;RunService&gt;(&dm)-&gt;run();`
- **`Instance::WaitForSameChildAfterInitialWaitForChild`** (`App.UnitTest/Instance.cpp:289`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(part-&gt;getName(), "Renamed")`
  - **Callsite Snippet:** `ServiceProvider::create&lt;RunService&gt;(&dm)-&gt;run();`
- **`Instance::TwoScriptsWaitingForSameChild`** (`App.UnitTest/Instance.cpp:314`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK(dm-&gt;getWorkspace()-&gt;findFirstChildByName("Alice") != NULL)`, `BOOST_CHECK(dm-&gt;getWorkspace()-&gt;findFirstChildByName("Bob") != NULL)`
  - **Callsite Snippet:** `ServiceProvider::create&lt;RunService&gt;(&dm)-&gt;run();`
- **`Instance::TwoScriptsWaitingForSameChildRenameOnResume`** (`App.UnitTest/Instance.cpp:356`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL("PartBx", part-&gt;getName())`, `BOOST_CHECK_EQUAL("PartA", part2-&gt;getName())`
  - **Callsite Snippet:** `ServiceProvider::create&lt;RunService&gt;(&dm)-&gt;run();`

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `Win/ScriptErrorUploader.cpp`.

- **Alternative Implementation Files:** `Win/ScriptErrorUploader.cpp`

---

### 59. `ErrorUploader::MoveRelative`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string ErrorUploader::MoveRelative(LPCTSTR fileName, std::string path);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `Win/ErrorUploader.cpp:28` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes MoveRelative within Windows Client & Win Launcher. Coordinates interactions with `RemoveFileSpec, Append, c_str, FileExists`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `RemoveFileSpec`, `Append`, `c_str`, `FileExists`, `_mkdir`, `StripPath`, `MoveFile`, `DeleteFile`, `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `MoveRelative`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 60. `Cancel`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Cancel();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Win/ErrorUploader.h:43` |
| **Subsystem** | `Windows Client & Win Launcher` |

#### How it Works Internally

Executes Cancel within Windows Client & Win Launcher. Coordinates interactions with `lock, empty, pop`.

- **Control Flow & Execution:** Iterative loop processing.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** RAII mutex lock acquisition (scoped_lock); Thread mutual exclusion locking (boost::mutex).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lock`, `empty`, `pop`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `Cancel`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---


:::tip Additional Functions
There are **439 additional internal and inline functions** in this subsystem. All functions are indexed and cross-referenced in the **[Complete Function Catalog](./function-catalog.md)**.
:::

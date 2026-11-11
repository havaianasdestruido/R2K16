---
sidebar_position: 17
title: Client Shared Subsystems
description: Cross-platform CookiesEngine, DataModel serialization, and SDL controllers.
---

# Client Shared Subsystems

Cross-platform CookiesEngine, DataModel serialization, and SDL controllers.


## FAQ

### Does shared client code behave identically on every platform?

Not necessarily. Check platform conditionals and the platform-specific callers before drawing conclusions from a shared source file.

### How can I investigate this in the repository?

From the repository root, search the relevant tracked files for a starting point (results are leads, not proof of behavior):

```bash
git grep -n -i -F -- 'DataModel' -- ClientShared
```

Read the surrounding implementation and callers, and check relevant tests before making changes. A search may return no matches when terminology or tracked files change.

## Subsystem Metrics

- **Total Documented Functions:** `114`
- **Functions Exercised in Tests:** `5`
- **Platform-Divergent Implementations:** `35`
- **Component Source Files:** `15`

## Source Files

<details>
<summary>View all 15 source files in this subsystem</summary>

| Source File | Path |
| :--- | :--- |
| `CountersClient.cpp` | `ClientShared/CountersClient.cpp` |
| `DataModelEmptySerialize.cpp` | `ClientShared/DataModelEmptySerialize.cpp` |
| `DataModelSerialize.cpp` | `ClientShared/DataModelSerialize.cpp` |
| `InfluxDbHelper.cpp` | `ClientShared/InfluxDbHelper.cpp` |
| `InfluxDbHelper.h` | `ClientShared/InfluxDbHelper.h` |
| `CookiesEngine.cpp` | `ClientShared/Mac/CookiesEngine.cpp` |
| `CookiesEngine.cpp` | `ClientShared/Mobile/CookiesEngine.cpp` |
| `RobloxServicesTools.cpp` | `ClientShared/RobloxServicesTools.cpp` |
| `SDLGameController.cpp` | `ClientShared/SDLGameController.cpp` |
| `SimpleJSON.cpp` | `ClientShared/SimpleJSON.cpp` |
| `SimpleJSON.h` | `ClientShared/SimpleJSON.h` |
| `StringConv.cpp` | `ClientShared/StringConv.cpp` |
| `CookiesEngine.cpp` | `ClientShared/Win/CookiesEngine.cpp` |
| `format_string.cpp` | `ClientShared/format_string.cpp` |
| `format_string.h` | `ClientShared/format_string.h` |

</details>

---

## Function Reference

### 1. `CountersClient::registerEvent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CountersClient::registerEvent(std::wstring eventName, bool fireImmediately);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/CountersClient.cpp:18` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes registerEvent within Client Shared Subsystems. Coordinates interactions with `insert, reportEvents, find, end`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `insert`, `reportEvents`, `find`, `end`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `registerEvent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 2. `CountersClient::reportEvents`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CountersClient::reportEvents();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/CountersClient.cpp:35` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes reportEvents within Client Shared Subsystems.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `reportEvents`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 3. `CountersClient::reportEvents`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CountersClient::reportEvents(std::set<std::wstring> &events);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/CountersClient.cpp:40` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes reportEvents within Client Shared Subsystems. Coordinates interactions with `empty, begin, end, convert_w2s`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `empty`, `begin`, `end`, `convert_w2s`, `clear`, `CrackUrl`, `convert_s2w`, `c_str`, `GetScheme`, `InternetOpen`, `InternetConnect`, `GetHostName`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `reportEvents`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 4. `DataModel::serializeDataModel`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
shared_ptr<std::stringstream> DataModel::serializeDataModel(const Instance::SaveFilter saveFilter);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `shared_ptr&lt;std::stringstream&gt;` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/DataModelEmptySerialize.cpp:13` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

The purpose of this file is to enable DataModel to compile but to NOT include any XML serializing code.  this makes "place stealing hacks" more difficult to implement.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `serializeDataModel`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 5. `DataModel::serverSave`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DataModel::serverSave();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/DataModelEmptySerialize.cpp:17` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Declaration or inline method for serverSave.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `serverSave`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 6. `DataModel::internalSave`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DataModel::internalSave(ContentId contentId);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/DataModelEmptySerialize.cpp:29` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Declaration or inline method for internalSave.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `internalSave`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 7. `DataModel::serializeDataModel`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
shared_ptr<std::stringstream> DataModel::serializeDataModel(const Instance::SaveFilter saveFilter);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `shared_ptr&lt;std::stringstream&gt;` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/DataModelSerialize.cpp:22` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes serializeDataModel within Client Shared Subsystems. Coordinates interactions with `stream, stringstream, serialize`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new; Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `stream`, `stringstream`, `serialize`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `serializeDataModel`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 8. `DataModel::serverSave`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DataModel::serverSave();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/DataModelSerialize.cpp:31` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes serverSave within Client Shared Subsystems. Coordinates interactions with `serializeDataModel, Http, post, isCloudEdit`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `serializeDataModel`, `Http`, `post`, `isCloudEdit`, `gamechat`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `serverSave`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 9. `DataModel::internalSave`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DataModel::internalSave(ContentId contentId);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/DataModelSerialize.cpp:77` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes internalSave within Client Shared Subsystems. Coordinates interactions with `RBXASSERT, toString, substr, find`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT); C++ exception throw on invalid state or failure; Exception handling block (try/catch recovery).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `RBXASSERT`, `toString`, `substr`, `find`, `string`, `length`, `time`, `ReportStatisticWithMessage`, `GetBaseURL`, `c_str`, `serializeDataModel`, `saveRequest`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `internalSave`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 10. `InfluxDb::init`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void InfluxDb::init(const std::string& _reporter, const std::string& _url, const std::string& _database, const std::string& _user, const std::string& _pw);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/InfluxDbHelper.cpp:20` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes init within Client Shared Subsystems. Coordinates interactions with `empty`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `empty`.

#### How it is Used in Tests

This function is exercised in **5 test case(s)**:

- **`SoundEffectTests::DistortionDSPUpdatesAndDetach`** (`App.UnitTest/SoundEffectTest.cpp:53`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(system-&gt;init(16, FMOD_INIT_NORMAL, NULL), FMOD_OK)`
  - **Callsite Snippet:** `BOOST_REQUIRE_EQUAL(system-&gt;init(16, FMOD_INIT_NORMAL, NULL), FMOD_OK);`
- **`Trie::SimpleTest`** (`Base.UnitTest/trie.cpp:86`)
  - **Usage Pattern:** `Direct Call`
  - **Callsite Snippet:** `std::string key = init(trie, map, hashmap);`
- **`Trie::PerfTrie`** (`Base.UnitTest/trie.cpp:95`)
  - **Usage Pattern:** `Performance Benchmark`
  - **Callsite Snippet:** `std::string key = init(trie, map, hashmap);`
- **`Trie::PerfMap`** (`Base.UnitTest/trie.cpp:106`)
  - **Usage Pattern:** `Performance Benchmark`
  - **Callsite Snippet:** `std::string key = init(trie, map, hashmap);`

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChat.cpp`, `Win/LogManager.cpp`, `App/util/XboxHttp2.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChat.cpp`, `Win/LogManager.cpp`, `App/util/XboxHttp2.cpp`, `XboxClient/VoiceChatMaxNet.cpp`

---

### 11. `InfluxDb::setLocation`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void InfluxDb::setLocation(const std::string& loc);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/InfluxDbHelper.cpp:36` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes setLocation within Client Shared Subsystems.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setLocation`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 12. `InfluxDb::setAppVersion`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void InfluxDb::setAppVersion(const std::string& ver);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/InfluxDbHelper.cpp:41` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes setAppVersion within Client Shared Subsystems.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setAppVersion`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 13. `InfluxDb::getReportingUrl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string& InfluxDb::getReportingUrl() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string&` |
| **Modifiers** | `const` |
| **Source Location** | `ClientShared/InfluxDbHelper.cpp:46` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes getReportingUrl within Client Shared Subsystems.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getReportingUrl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 14. `InfluxDb::getUrlHost`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string& InfluxDb::getUrlHost() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string&` |
| **Modifiers** | `const` |
| **Source Location** | `ClientShared/InfluxDbHelper.cpp:51` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes getUrlHost within Client Shared Subsystems.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getUrlHost`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 15. `InfluxDb::getUrlPath`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string& InfluxDb::getUrlPath() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string&` |
| **Modifiers** | `const` |
| **Source Location** | `ClientShared/InfluxDbHelper.cpp:56` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes getUrlPath within Client Shared Subsystems.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getUrlPath`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 16. `InfluxDb::addPoint`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void InfluxDb::addPoint(const std::string& name, const rapidjson::Value& value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/InfluxDbHelper.cpp:61` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes addPoint within Client Shared Subsystems. Coordinates interactions with `GetType, runtime_error, string, GetString`.

- **Control Flow & Execution:** Conditional branching, Multi-case state dispatch.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** C++ exception throw on invalid state or failure; Standard runtime error exception formulation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `GetType`, `runtime_error`, `string`, `GetString`, `IsDouble`, `GetDouble`, `IsInt`, `GetInt`, `IsInt64`, `GetInt64`, `IsUint`, `GetUint`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `addPoint`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 17. `InfluxDb::getJsonStringForPosting`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string InfluxDb::getJsonStringForPosting(const std::string& seriesName);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/InfluxDbHelper.cpp:125` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes getJsonStringForPosting within Client Shared Subsystems. Coordinates interactions with `begin, end`.

- **Control Flow & Execution:** Iterative loop processing, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `begin`, `end`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getJsonStringForPosting`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 18. `InfluxDb`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
public: InfluxDb();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `public:` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/InfluxDbHelper.h:12` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Declaration or inline method for InfluxDb.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `InfluxDb`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 19. `createDirectoryRecursive`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void createDirectoryRecursive(const std::string& path);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `ClientShared/Mac/CookiesEngine.cpp:17` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Creates a directory tree without invoking a shell. The old implementation interpolated a preference-controlled path into "mkdir -p %s" and passed it to system(), so a crafted CFPreferences value could execute arbitrary commands. EEXIST is ignored; any other failure is simply left to the caller's existing error handling.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `empty`, `size`, `find`, `substr`, `mkdir`, `c_str`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `createDirectoryRecursive`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 20. `CookiesEngine::reportValue`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
bool CookiesEngine::reportValue(CookiesEngine &engine, std::string key, std::string value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/Mac/CookiesEngine.cpp:36` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes reportValue within Client Shared Subsystems. Coordinates interactions with `SetValue, usleep`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `SetValue`, `usleep`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `reportValue`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `ClientShared/Mobile/CookiesEngine.cpp`, `ClientShared/Win/CookiesEngine.cpp`. Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

- **Alternative Implementation Files:** `ClientShared/Mobile/CookiesEngine.cpp`, `ClientShared/Win/CookiesEngine.cpp`
- **Caller Context Variations:** Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

---

### 21. `CookiesEngine::getCookiesFilePath`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
std::wstring CookiesEngine::getCookiesFilePath();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::wstring` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/Mac/CookiesEngine.cpp:54` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes getCookiesFilePath within Client Shared Subsystems. Coordinates interactions with `path, CFSTR, CFPreferencesCopyAppValue, CFStringGetMaximumSizeForEncoding`. Employs c runtime dynamic heap allocation (malloc/calloc).

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** C runtime dynamic heap allocation (malloc/calloc); C runtime memory release (free).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `path`, `CFSTR`, `CFPreferencesCopyAppValue`, `CFStringGetMaximumSizeForEncoding`, `CFStringGetLength`, `malloc`, `CFStringGetCString`, `rfind`, `createDirectoryRecursive`, `substr`, `free`, `CFRelease`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getCookiesFilePath`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `ClientShared/Mobile/CookiesEngine.cpp`, `ClientShared/Win/CookiesEngine.cpp`. Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

- **Alternative Implementation Files:** `ClientShared/Mobile/CookiesEngine.cpp`, `ClientShared/Win/CookiesEngine.cpp`
- **Caller Context Variations:** Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

---

### 22. `CookiesEngine::setCookiesFilePath`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void CookiesEngine::setCookiesFilePath(std::wstring &path);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/Mac/CookiesEngine.cpp:90` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes setCookiesFilePath within Client Shared Subsystems. Coordinates interactions with `warning, CookiesEngine, fopen, convert_w2s`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `warning`, `CookiesEngine`, `fopen`, `convert_w2s`, `c_str`, `fclose`, `ParseFileContent`, `seekg`, `tellg`, `buf`, `read`, `data`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setCookiesFilePath`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `ClientShared/Mobile/CookiesEngine.cpp`, `ClientShared/Win/CookiesEngine.cpp`. Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

- **Alternative Implementation Files:** `ClientShared/Mobile/CookiesEngine.cpp`, `ClientShared/Win/CookiesEngine.cpp`
- **Caller Context Variations:** Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

---

### 23. `CookiesEngine::ParseFileContent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void CookiesEngine::ParseFileContent(std::fstream &f);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/Mac/CookiesEngine.cpp:114` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes ParseFileContent within Client Shared Subsystems. Coordinates interactions with `seekg, tellg, buf, read`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `seekg`, `tellg`, `buf`, `read`, `data`, `find`, `substr`, `empty`, `length`, `insert`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `ParseFileContent`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `ClientShared/Mobile/CookiesEngine.cpp`, `ClientShared/Win/CookiesEngine.cpp`. Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

- **Alternative Implementation Files:** `ClientShared/Mobile/CookiesEngine.cpp`, `ClientShared/Win/CookiesEngine.cpp`
- **Caller Context Variations:** Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

---

### 24. `CookiesEngine::FlushContent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void CookiesEngine::FlushContent(std::fstream &f);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/Mac/CookiesEngine.cpp:148` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes FlushContent within Client Shared Subsystems. Coordinates interactions with `seekg, tellg, flush, begin`.

- **Control Flow & Execution:** Iterative loop processing.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `seekg`, `tellg`, `flush`, `begin`, `end`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `FlushContent`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `ClientShared/Mobile/CookiesEngine.cpp`, `ClientShared/Win/CookiesEngine.cpp`. Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

- **Alternative Implementation Files:** `ClientShared/Mobile/CookiesEngine.cpp`, `ClientShared/Win/CookiesEngine.cpp`
- **Caller Context Variations:** Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

---

### 25. `CookiesEngine::SetValue`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
int CookiesEngine::SetValue(std::string key, std::string value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/Mac/CookiesEngine.cpp:169` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes SetValue within Client Shared Subsystems. Coordinates interactions with `empty, convert_w2s, c_str, is_open`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `empty`, `convert_w2s`, `c_str`, `is_open`, `clear`, `ParseFileContent`, `FlushContent`, `close`.

#### How it is Used in Tests

This function is exercised in **6 test case(s)**:

- **`FastLog::FastFlags`** (`Base.UnitTest/Log.cpp:102`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(FFlag::TestFastFlag, false)`, `BOOST_CHECK_EQUAL(FFlag::TestFastFlag, true)`
  - **Callsite Snippet:** `FLog::SetValue("TestFastFlag", "True", FASTVARTYPE_STATIC);`
- **`FastLog::SettingUnknownGroups`** (`Base.UnitTest/Log.cpp:112`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(UnknownGroup, 1)`, `BOOST_CHECK_EQUAL(UnknownFlag, true)`
  - **Callsite Snippet:** `FLog::SetValue("UnknownGroup", "1", FASTVARTYPE_STATIC);`
- **`FastLog::DynamicVariables`** (`Base.UnitTest/Log.cpp:128`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(DFFlag::DebugUnitDynamicFlag, true)`, `BOOST_CHECK_EQUAL(DFFlag::DebugUnitDynamicFlag, false)`
  - **Callsite Snippet:** `FLog::SetValue("DebugUnitDynamicFlag", "false", FASTVARTYPE_STATIC);`
- **`FastLog::FastInts`** (`Base.UnitTest/Log.cpp:137`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(FInt::TestFastInt, 2)`
  - **Callsite Snippet:** `FLog::SetValue("TestFastInt", "2", FASTVARTYPE_STATIC);`

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `ClientShared/Mobile/CookiesEngine.cpp`, `ClientShared/Win/CookiesEngine.cpp`. Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

- **Alternative Implementation Files:** `ClientShared/Mobile/CookiesEngine.cpp`, `ClientShared/Win/CookiesEngine.cpp`
- **Caller Context Variations:** Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

---

### 26. `CookiesEngine::GetValue`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
std::string CookiesEngine::GetValue(std::string key, int *errorCode, bool *exists);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/Mac/CookiesEngine.cpp:194` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes GetValue within Client Shared Subsystems. Coordinates interactions with `empty, string, convert_w2s, c_str`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `empty`, `string`, `convert_w2s`, `c_str`, `is_open`, `clear`, `ParseFileContent`, `begin`, `end`, `close`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetValue`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `Win/VersionInfo.cpp`, `ClientShared/Win/CookiesEngine.cpp`, `ClientShared/Mobile/CookiesEngine.cpp`. Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

- **Alternative Implementation Files:** `Win/VersionInfo.cpp`, `ClientShared/Win/CookiesEngine.cpp`, `ClientShared/Mobile/CookiesEngine.cpp`
- **Caller Context Variations:** Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

---

### 27. `CookiesEngine::DeleteValue`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
int CookiesEngine::DeleteValue(std::string key);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/Mac/CookiesEngine.cpp:236` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes DeleteValue within Client Shared Subsystems. Coordinates interactions with `empty, convert_w2s, c_str, is_open`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `empty`, `convert_w2s`, `c_str`, `is_open`, `clear`, `ParseFileContent`, `begin`, `end`, `erase`, `FlushContent`, `close`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `DeleteValue`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `ClientShared/Mobile/CookiesEngine.cpp`, `ClientShared/Win/CookiesEngine.cpp`. Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

- **Alternative Implementation Files:** `ClientShared/Mobile/CookiesEngine.cpp`, `ClientShared/Win/CookiesEngine.cpp`
- **Caller Context Variations:** Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

---

### 28. `CookiesEngine::reportValue`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
bool CookiesEngine::reportValue(CookiesEngine &engine, std::string key, std::string value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/Mobile/CookiesEngine.cpp:2` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes reportValue within Client Shared Subsystems.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `reportValue`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `ClientShared/Win/CookiesEngine.cpp`, `ClientShared/Mac/CookiesEngine.cpp`. Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

- **Alternative Implementation Files:** `ClientShared/Win/CookiesEngine.cpp`, `ClientShared/Mac/CookiesEngine.cpp`
- **Caller Context Variations:** Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

---

### 29. `CookiesEngine::getCookiesFilePath`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
std::wstring CookiesEngine::getCookiesFilePath();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::wstring` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/Mobile/CookiesEngine.cpp:7` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes getCookiesFilePath within Client Shared Subsystems. Coordinates interactions with `path, convert_s2w`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `path`, `convert_s2w`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getCookiesFilePath`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `ClientShared/Win/CookiesEngine.cpp`, `ClientShared/Mac/CookiesEngine.cpp`. Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

- **Alternative Implementation Files:** `ClientShared/Win/CookiesEngine.cpp`, `ClientShared/Mac/CookiesEngine.cpp`
- **Caller Context Variations:** Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

---

### 30. `CookiesEngine::setCookiesFilePath`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void CookiesEngine::setCookiesFilePath(std::wstring &path);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/Mobile/CookiesEngine.cpp:14` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Declaration or inline method for setCookiesFilePath.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setCookiesFilePath`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `ClientShared/Win/CookiesEngine.cpp`, `ClientShared/Mac/CookiesEngine.cpp`. Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

- **Alternative Implementation Files:** `ClientShared/Win/CookiesEngine.cpp`, `ClientShared/Mac/CookiesEngine.cpp`
- **Caller Context Variations:** Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

---

### 31. `CookiesEngine::ParseFileContent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void CookiesEngine::ParseFileContent(std::fstream &f);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/Mobile/CookiesEngine.cpp:23` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Declaration or inline method for ParseFileContent.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `ParseFileContent`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `ClientShared/Win/CookiesEngine.cpp`, `ClientShared/Mac/CookiesEngine.cpp`. Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

- **Alternative Implementation Files:** `ClientShared/Win/CookiesEngine.cpp`, `ClientShared/Mac/CookiesEngine.cpp`
- **Caller Context Variations:** Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

---

### 32. `CookiesEngine::FlushContent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void CookiesEngine::FlushContent(std::fstream &f);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/Mobile/CookiesEngine.cpp:27` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Declaration or inline method for FlushContent.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `FlushContent`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `ClientShared/Win/CookiesEngine.cpp`, `ClientShared/Mac/CookiesEngine.cpp`. Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

- **Alternative Implementation Files:** `ClientShared/Win/CookiesEngine.cpp`, `ClientShared/Mac/CookiesEngine.cpp`
- **Caller Context Variations:** Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

---

### 33. `CookiesEngine::SetValue`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
int CookiesEngine::SetValue(std::string key, std::string value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/Mobile/CookiesEngine.cpp:31` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes SetValue within Client Shared Subsystems.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

This function is exercised in **6 test case(s)**:

- **`FastLog::FastFlags`** (`Base.UnitTest/Log.cpp:102`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(FFlag::TestFastFlag, false)`, `BOOST_CHECK_EQUAL(FFlag::TestFastFlag, true)`
  - **Callsite Snippet:** `FLog::SetValue("TestFastFlag", "True", FASTVARTYPE_STATIC);`
- **`FastLog::SettingUnknownGroups`** (`Base.UnitTest/Log.cpp:112`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(UnknownGroup, 1)`, `BOOST_CHECK_EQUAL(UnknownFlag, true)`
  - **Callsite Snippet:** `FLog::SetValue("UnknownGroup", "1", FASTVARTYPE_STATIC);`
- **`FastLog::DynamicVariables`** (`Base.UnitTest/Log.cpp:128`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(DFFlag::DebugUnitDynamicFlag, true)`, `BOOST_CHECK_EQUAL(DFFlag::DebugUnitDynamicFlag, false)`
  - **Callsite Snippet:** `FLog::SetValue("DebugUnitDynamicFlag", "false", FASTVARTYPE_STATIC);`
- **`FastLog::FastInts`** (`Base.UnitTest/Log.cpp:137`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(FInt::TestFastInt, 2)`
  - **Callsite Snippet:** `FLog::SetValue("TestFastInt", "2", FASTVARTYPE_STATIC);`

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `ClientShared/Win/CookiesEngine.cpp`, `ClientShared/Mac/CookiesEngine.cpp`. Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

- **Alternative Implementation Files:** `ClientShared/Win/CookiesEngine.cpp`, `ClientShared/Mac/CookiesEngine.cpp`
- **Caller Context Variations:** Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

---

### 34. `CookiesEngine::GetValue`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
std::string CookiesEngine::GetValue(std::string key, int *errorCode, bool *exists);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/Mobile/CookiesEngine.cpp:36` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes GetValue within Client Shared Subsystems.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetValue`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `Win/VersionInfo.cpp`, `ClientShared/Mac/CookiesEngine.cpp`, `ClientShared/Win/CookiesEngine.cpp`. Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

- **Alternative Implementation Files:** `Win/VersionInfo.cpp`, `ClientShared/Mac/CookiesEngine.cpp`, `ClientShared/Win/CookiesEngine.cpp`
- **Caller Context Variations:** Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

---

### 35. `CookiesEngine::DeleteValue`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
int CookiesEngine::DeleteValue(std::string key);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/Mobile/CookiesEngine.cpp:41` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes DeleteValue within Client Shared Subsystems.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `DeleteValue`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `ClientShared/Win/CookiesEngine.cpp`, `ClientShared/Mac/CookiesEngine.cpp`. Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

- **Alternative Implementation Files:** `ClientShared/Win/CookiesEngine.cpp`, `ClientShared/Mac/CookiesEngine.cpp`
- **Caller Context Variations:** Windows client uses WinINet cookie cache; Mac uses NSHTTPCookieStorage; Mobile uses sandbox file store.

---

### 36. `trim_trailing_slashes`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string trim_trailing_slashes(const std::string& path);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/RobloxServicesTools.cpp:13` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes trim_trailing_slashes within Client Shared Subsystems. Coordinates interactions with `find_last_not_of, substr`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `find_last_not_of`, `substr`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `trim_trailing_slashes`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 37. `BuildGenericApiUrl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string BuildGenericApiUrl(const std::string& baseUrl, const std::string& serviceNameIn, const std::string& path, const std::string& key, const char* scheme = "https");
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | `static` |
| **Source Location** | `ClientShared/RobloxServicesTools.cpp:19` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes BuildGenericApiUrl within Client Shared Subsystems. Coordinates interactions with `serviceName, substr, size, format_string`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `serviceName`, `substr`, `size`, `format_string`, `c_str`, `find`, `length`, `empty`, `replace`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `BuildGenericApiUrl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 38. `GetCountersUrl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string GetCountersUrl(const std::string& baseUrl, const std::string& key);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/RobloxServicesTools.cpp:82` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes GetCountersUrl within Client Shared Subsystems. Coordinates interactions with `BuildGenericApiUrl`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `BuildGenericApiUrl`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetCountersUrl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 39. `GetCountersMultiIncrementUrl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string GetCountersMultiIncrementUrl(const std::string& baseUrl, const std::string& key);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/RobloxServicesTools.cpp:87` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes GetCountersMultiIncrementUrl within Client Shared Subsystems. Coordinates interactions with `BuildGenericApiUrl`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `BuildGenericApiUrl`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetCountersMultiIncrementUrl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 40. `GetSettingsUrl`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string GetSettingsUrl(const std::string& baseUrl, const std::string& group, const std::string& key);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/RobloxServicesTools.cpp:92` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes GetSettingsUrl within Client Shared Subsystems. Coordinates interactions with `BuildGenericApiUrl, format_string, c_str`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `BuildGenericApiUrl`, `format_string`, `c_str`.

#### How it is Used in Tests

This function is exercised in **3 test case(s)**:

- **`SettingsUrl::SettingsUrlProd`** (`App.UnitTest/SettingsURL.cpp:7`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(url, testUrl)`, `BOOST_CHECK_EQUAL(url, testUrl)`
  - **Callsite Snippet:** `std::string url = GetSettingsUrl("www.roblox.com", "Test", "TestKey");`
- **`SettingsUrl::SettingsUrlNewGametest`** (`App.UnitTest/SettingsURL.cpp:17`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(url, testUrl)`, `BOOST_CHECK_EQUAL(url, testUrl)`
  - **Callsite Snippet:** `std::string url = GetSettingsUrl("www.gametest1.robloxlabs.com", "Test", "TestKey");`
- **`SettingsUrl::SettingsUrlGametest`** (`App.UnitTest/SettingsURL.cpp:27`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(url, testUrl)`, `BOOST_CHECK_EQUAL(url, testUrl)`
  - **Callsite Snippet:** `std::string url = GetSettingsUrl("www.gametest1.roblox.com", "Test", "TestKey");`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 41. `GetSecurityKeyUrl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string GetSecurityKeyUrl(const std::string& baseUrl, const std::string& key);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/RobloxServicesTools.cpp:97` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes GetSecurityKeyUrl within Client Shared Subsystems. Coordinates interactions with `BuildGenericApiUrl`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `BuildGenericApiUrl`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetSecurityKeyUrl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 42. `GetSecurityKeyUrl2`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string GetSecurityKeyUrl2(const std::string& baseUrl, const std::string& key);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/RobloxServicesTools.cpp:102` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes GetSecurityKeyUrl2 within Client Shared Subsystems. Coordinates interactions with `BuildGenericApiUrl`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `BuildGenericApiUrl`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetSecurityKeyUrl2`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 43. `GetClientVersionUploadUrl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string GetClientVersionUploadUrl(const std::string& baseUrl, const std::string& key);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/RobloxServicesTools.cpp:109` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

used by bootstrapper

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `BuildGenericApiUrl`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetClientVersionUploadUrl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 44. `GetPlayerGameDataUrl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string GetPlayerGameDataUrl(const std::string& baseurl, int userId, const std::string& key);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/RobloxServicesTools.cpp:113` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes GetPlayerGameDataUrl within Client Shared Subsystems. Coordinates interactions with `BuildGenericApiUrl, format_string`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `BuildGenericApiUrl`, `format_string`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetPlayerGameDataUrl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 45. `GetWebChatFilterURL`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string GetWebChatFilterURL(const std::string& baseUrl, const std::string& key);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/RobloxServicesTools.cpp:118` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes GetWebChatFilterURL within Client Shared Subsystems. Coordinates interactions with `BuildGenericApiUrl`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `BuildGenericApiUrl`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetWebChatFilterURL`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 46. `GetMD5HashUrl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string GetMD5HashUrl(const std::string& baseUrl, const std::string& key);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/RobloxServicesTools.cpp:123` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes GetMD5HashUrl within Client Shared Subsystems. Coordinates interactions with `BuildGenericApiUrl`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `BuildGenericApiUrl`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetMD5HashUrl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 47. `GetMemHashUrl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string GetMemHashUrl(const std::string& baseUrl, const std::string& key);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/RobloxServicesTools.cpp:128` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes GetMemHashUrl within Client Shared Subsystems. Coordinates interactions with `BuildGenericApiUrl`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `BuildGenericApiUrl`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetMemHashUrl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 48. `GetGridUrl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string GetGridUrl(const std::string& anyUrl, bool changeToDataDomain);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/RobloxServicesTools.cpp:133` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes GetGridUrl within Client Shared Subsystems. Coordinates interactions with `trim_trailing_slashes, ReplaceTopSubdomain`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `trim_trailing_slashes`, `ReplaceTopSubdomain`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetGridUrl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 49. `GetDmpUrl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string GetDmpUrl(const std::string& anyUrl, bool changeToDataDomain);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/RobloxServicesTools.cpp:143` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes GetDmpUrl within Client Shared Subsystems. Coordinates interactions with `trim_trailing_slashes, ReplaceTopSubdomain`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `trim_trailing_slashes`, `ReplaceTopSubdomain`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetDmpUrl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 50. `GetBreakpadUrl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string GetBreakpadUrl(const std::string& anyUrl, bool changeToDataDomain);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/RobloxServicesTools.cpp:153` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes GetBreakpadUrl within Client Shared Subsystems. Coordinates interactions with `trim_trailing_slashes, ReplaceTopSubdomain`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `trim_trailing_slashes`, `ReplaceTopSubdomain`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetBreakpadUrl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 51. `ReplaceTopSubdomain`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string ReplaceTopSubdomain(const std::string& anyUrl, const char* newTopSubDoman);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/RobloxServicesTools.cpp:163` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes ReplaceTopSubdomain within Client Shared Subsystems. Coordinates interactions with `result, find, replace`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `result`, `find`, `replace`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `ReplaceTopSubdomain`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 52. `BuildGenericPersistenceUrl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string BuildGenericPersistenceUrl(const std::string& baseUrl, const std::string& servicePath);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/RobloxServicesTools.cpp:178` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes BuildGenericPersistenceUrl within Client Shared Subsystems. Coordinates interactions with `constructedURLDomain, constructedServicePath, ReplaceTopSubdomain, ends_with`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `constructedURLDomain`, `constructedServicePath`, `ReplaceTopSubdomain`, `ends_with`, `append`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `BuildGenericPersistenceUrl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 53. `BuildGenericGameUrl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string BuildGenericGameUrl(const std::string& baseUrl, const std::string& servicePath);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/RobloxServicesTools.cpp:191` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes BuildGenericGameUrl within Client Shared Subsystems. Coordinates interactions with `constructedURLDomain, constructedServicePath, ReplaceTopSubdomain, ends_with`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `constructedURLDomain`, `constructedServicePath`, `ReplaceTopSubdomain`, `ends_with`, `append`, `starts_with`, `erase`, `begin`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `BuildGenericGameUrl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 54. `SDLGameController::initSDL`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void SDLGameController::initSDL();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/SDLGameController.cpp:15` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes initSDL within Client Shared Subsystems. Coordinates interactions with `SDL_Init, SDL_GetError, fprintf, c_str`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `SDL_Init`, `SDL_GetError`, `fprintf`, `c_str`, `fromAssets`, `findAsset`, `SDL_GameControllerAddMappingsFromFile`, `singleton`, `printf`, `lock`, `submitTask`, `bind`.
- **External Library Dependencies:** `Boost C++ Libraries`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `initSDL`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 55. `SDLGameController::bindToDataModel`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void SDLGameController::bindToDataModel();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/SDLGameController.cpp:42` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes bindToDataModel within Client Shared Subsystems. Coordinates interactions with `getUserInputService, connect, bind, getHapticService`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getUserInputService`, `connect`, `bind`, `getHapticService`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `bindToDataModel`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 56. `SDLGameController::getUserInputService`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
RBX::UserInputService* SDLGameController::getUserInputService();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `RBX::UserInputService*` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/SDLGameController.cpp:78` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes getUserInputService within Client Shared Subsystems. Coordinates interactions with `lock, get`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lock`, `get`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getUserInputService`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 57. `SDLGameController::getHapticService`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
RBX::HapticService* SDLGameController::getHapticService();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `RBX::HapticService*` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/SDLGameController.cpp:91` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes getHapticService within Client Shared Subsystems. Coordinates interactions with `lock, get`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lock`, `get`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getHapticService`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 58. `SDLGameController::getGamepadService`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
RBX::GamepadService* SDLGameController::getGamepadService();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `RBX::GamepadService*` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/SDLGameController.cpp:104` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes getGamepadService within Client Shared Subsystems. Coordinates interactions with `lock, get`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lock`, `get`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getGamepadService`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 59. `SDLGameController::removeControllerMapping`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
SDL_GameController* SDLGameController::removeControllerMapping(int joystickId);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `SDL_GameController*` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/SDLGameController.cpp:117` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes removeControllerMapping within Client Shared Subsystems. Coordinates interactions with `getUserInputService, find, end, erase`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getUserInputService`, `find`, `end`, `erase`, `safeFireGamepadDisconnected`, `getGamepadEnumForInt`, `SDL_HapticDestroyEffect`, `SDL_HapticClose`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `removeControllerMapping`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 60. `SDLGameController::setupControllerId`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void SDLGameController::setupControllerId(int joystickId, int gamepadId, SDL_GameController *pad);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientShared/SDLGameController.cpp:151` |
| **Subsystem** | `Client Shared Subsystems` |

#### How it Works Internally

Executes setupControllerId within Client Shared Subsystems. Coordinates interactions with `getUserInputService, safeFireGamepadConnected, getGamepadEnumForInt`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getUserInputService`, `safeFireGamepadConnected`, `getGamepadEnumForInt`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setupControllerId`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---


:::tip Additional Functions
There are **54 additional internal and inline functions** in this subsystem. All functions are indexed and cross-referenced in the **[Complete Function Catalog](./function-catalog.md)**.
:::

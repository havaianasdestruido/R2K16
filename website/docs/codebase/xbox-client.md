---
sidebar_position: 23
title: Xbox Client Subsystems
description: Xbox Durango client, controller buffer, voice chat, and async services.
---

# Xbox Client Subsystems

Xbox Durango client, controller buffer, voice chat, and async services.

## Subsystem Metrics

- **Total Documented Functions:** `299`
- **Functions Exercised in Tests:** `14`
- **Platform-Divergent Implementations:** `65`
- **Component Source Files:** `27`

## Source Files

<details>
<summary>View all 27 source files in this subsystem</summary>

| Source File | Path |
| :--- | :--- |
| `ControllerBuffer.cpp` | `XboxClient/ControllerBuffer.cpp` |
| `ControllerBuffer.h` | `XboxClient/ControllerBuffer.h` |
| `KeyboardProvider.cpp` | `XboxClient/KeyboardProvider.cpp` |
| `UserTranslator.cpp` | `XboxClient/UserTranslator.cpp` |
| `UserTranslator.h` | `XboxClient/UserTranslator.h` |
| `VoiceChat.cpp` | `XboxClient/VoiceChat.cpp` |
| `VoiceChat.h` | `XboxClient/VoiceChat.h` |
| `VoiceChatBase.h` | `XboxClient/VoiceChatBase.h` |
| `VoiceChatMaxNet.cpp` | `XboxClient/VoiceChatMaxNet.cpp` |
| `VoiceChatMaxNet.h` | `XboxClient/VoiceChatMaxNet.h` |
| `XbLiveUtils.cpp` | `XboxClient/XbLiveUtils.cpp` |
| `XboxGameController.cpp` | `XboxClient/XboxGameController.cpp` |
| `XboxGameController.h` | `XboxClient/XboxGameController.h` |
| `XboxMultiplayerManager.cpp` | `XboxClient/XboxMultiplayerManager.cpp` |
| `XboxMultiplayerManager.h` | `XboxClient/XboxMultiplayerManager.h` |
| `XboxService.cpp` | `XboxClient/XboxService.cpp` |
| `XboxUtils.cpp` | `XboxClient/XboxUtils.cpp` |
| `XboxUtils.h` | `XboxClient/XboxUtils.h` |
| `async.h` | `XboxClient/async.h` |
| `fetchfflags.py` | `XboxClient/fetchfflags.py` |
| `main.cpp` | `XboxClient/main.cpp` |
| `marshaller.cpp` | `XboxClient/marshaller.cpp` |
| `marshaller.h` | `XboxClient/marshaller.h` |
| `p2p.cpp` | `XboxClient/p2p.cpp` |
| `p2p.h` | `XboxClient/p2p.h` |
| `renderJob.cpp` | `XboxClient/renderJob.cpp` |
| `xdpevents.h` | `XboxClient/xdpevents.h` |

</details>

---

## Function Reference

### 1. `ControllerBuffer::updateBuffer`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void ControllerBuffer::updateBuffer();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/ControllerBuffer.cpp:14` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes updateBuffer within Xbox Client Subsystems. Coordinates interactions with `lock, getRbxGamepadIntFromGamepad, GetAt, GetCurrentReading`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** RAII mutex lock acquisition (scoped_lock); Thread mutual exclusion locking (boost::mutex).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lock`, `getRbxGamepadIntFromGamepad`, `GetAt`, `GetCurrentReading`, `bufferGamepadButtons`, `bufferGamepadAxis`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `updateBuffer`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 2. `ControllerBuffer::processButton`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void ControllerBuffer::processButton(InputObject::UserInputType userInputType, const RBX::KeyCode buttonCode, const int buttonState);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/ControllerBuffer.cpp:39` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes processButton within Xbox Client Subsystems. Coordinates interactions with `gamepadButtonCombo, newGamepadButtonState, Vector3, find`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `gamepadButtonCombo`, `newGamepadButtonState`, `Vector3`, `find`, `end`, `back`, `push_back`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `processButton`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 3. `ControllerBuffer::bufferGamepadButtons`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void ControllerBuffer::bufferGamepadButtons(const int controllerIndex, IGamepadReading^& gamepadReading);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/ControllerBuffer.cpp:57` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes bufferGamepadButtons within Xbox Client Subsystems. Coordinates interactions with `getGamepadEnumForInt, processButton`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getGamepadEnumForInt`, `processButton`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `bufferGamepadButtons`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 4. `ControllerBuffer::processAxis`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void ControllerBuffer::processAxis(RBX::InputObject::UserInputType userInputType, const RBX::KeyCode axisCode, const Vector3 axisValue);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/ControllerBuffer.cpp:80` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes processAxis within Xbox Client Subsystems. Coordinates interactions with `zero, gamepadAxisCombo, newGamepadAxisState, find`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `zero`, `gamepadAxisCombo`, `newGamepadAxisState`, `find`, `end`, `back`, `push_back`.
- **External Library Dependencies:** `G3D Graphics and Math Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `processAxis`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 5. `ControllerBuffer::bufferGamepadAxis`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void ControllerBuffer::bufferGamepadAxis(const int controllerIndex, IGamepadReading^& gamepadReading);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/ControllerBuffer.cpp:108` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes bufferGamepadAxis within Xbox Client Subsystems. Coordinates interactions with `getGamepadEnumForInt, processAxis, Vector3`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getGamepadEnumForInt`, `processAxis`, `Vector3`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `bufferGamepadAxis`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 6. `ControllerBuffer::getBufferedInput`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
ControllerBuffer::GamepadValueBufferMap ControllerBuffer::getBufferedInput();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `ControllerBuffer::GamepadValueBufferMap` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/ControllerBuffer.cpp:118` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes getBufferedInput within Xbox Client Subsystems. Coordinates interactions with `lock, swap`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** RAII mutex lock acquisition (scoped_lock); Thread mutual exclusion locking (boost::mutex).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lock`, `swap`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getBufferedInput`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 7. `ControllerBuffer::getPollingMsec`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
float ControllerBuffer::getPollingMsec();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `float` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/ControllerBuffer.cpp:130` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes getPollingMsec within Xbox Client Subsystems. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getPollingMsec`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 8. `setXboxGameController`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void setXboxGameController(XboxGameController* newController);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/ControllerBuffer.h:31` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes setXboxGameController within Xbox Client Subsystems.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setXboxGameController`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 9. `KeyboardProvider::registerTextBoxListener`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void KeyboardProvider::registerTextBoxListener(RBX::DataModel* dm);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/KeyboardProvider.cpp:14` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes registerTextBoxListener within Xbox Client Subsystems. Coordinates interactions with `connect, bind`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `connect`, `bind`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `registerTextBoxListener`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 10. `KeyboardProvider::showKeyBoardLua`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void KeyboardProvider::showKeyBoardLua(std::string& title, std::string& description, std::string& defaultText, RBX::XboxKeyBoardType keyboardType, RBX::DataModel* dm);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/KeyboardProvider.cpp:73` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes showKeyBoardLua within Xbox Client Subsystems. Coordinates interactions with `void, submitTask, keyboardClosedSignal, data`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `void`, `submitTask`, `keyboardClosedSignal`, `data`, `InterlockedExchange`, `ws2s`, `Data`, `showKeyBoard`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `showKeyBoardLua`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 11. `KeyboardProvider::showKeyBoard`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void KeyboardProvider::showKeyBoard(shared_ptr<RBX::Instance> instance);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/KeyboardProvider.cpp:103` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes showKeyBoard within Xbox Client Subsystems. Coordinates interactions with `get, getText, wstr, begin`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Dynamic heap allocation via C++ operator new; Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `get`, `getText`, `wstr`, `begin`, `end`, `String`, `c_str`, `void`, `submitTask`, `textboxDidFinishEditing`, `InterlockedExchange`, `ws2s`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `showKeyBoard`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/XboxService.cpp`.

- **Alternative Implementation Files:** `XboxClient/XboxService.cpp`

---

### 12. `constructJsonRequest`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string constructJsonRequest(const UserIDTranslator::GametagSet& tags);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | `static` |
| **Source Location** | `XboxClient/UserTranslator.cpp:6` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes constructJsonRequest within Xbox Client Subsystems. Coordinates interactions with `empty, begin, end`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `empty`, `begin`, `end`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `constructJsonRequest`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 13. `UserIDTranslator::get`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void UserIDTranslator::get(OutputVector& result, const InputVector& inputs);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/UserTranslator.cpp:36` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes get within Xbox Client Subsystems. Coordinates interactions with `lock, clear, begin, end`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Multi-case state dispatch.
- **Memory Management:** Dynamic heap allocation via C++ operator new; Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** RAII mutex lock acquisition (scoped_lock).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lock`, `clear`, `begin`, `end`, `string`, `Entry`, `insert`, `getState`, `store`, `push_back`, `empty`, `constructJsonRequest`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

This function is exercised in **73 test case(s)**:

- **`AutowedgeTest::ExplosionBelowTerrainWorks`** (`App.UnitTest/AutowedgeTest.cpp:247`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(fixture.cluster-&gt;getVoxelGrid()-&gt;getCellMaterial(Vector3int16(kOffset, 0, kOffset)), CELL_MATERIAL_Grass)`, `BOOST_REQUIRE_EQUAL(fixture.cluster-&gt;getVoxelGrid()-&gt;getCellMaterial(Vector3int16(kOffset, 0, kOffset)), CELL_MATERIAL_Water)`
  - **Callsite Snippet:** `Explosion::propPosition.setValue(exp.get(), Vector3(0,2,0));`
- **`AutowedgeTest::ExplosionAboveTerrainWorks`** (`App.UnitTest/AutowedgeTest.cpp:270`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(fixture.cluster-&gt;getVoxelGrid()-&gt;getCellMaterial(Vector3int16(kOffset, 62, kOffset)), CELL_MATERIAL_Grass)`, `BOOST_REQUIRE_EQUAL(fixture.cluster-&gt;getVoxelGrid()-&gt;getCellMaterial(Vector3int16(kOffset, 62, kOffset)), CELL_MATERIAL_Water)`
  - **Callsite Snippet:** `Explosion::propPosition.setValue(exp.get(), Vector3(0,240,0));`
- **`ClusterDeprecatedProperty::ParentCannotBeSet`** (`App.UnitTest/ClusterDeprecatedPropertyTest.cpp:69`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(dataModel-&gt;getWorkspace(), resultTuple-&gt;at(0).get&lt;shared_ptr&lt;Instance&gt; &gt;().get())`, `BOOST_REQUIRE_EQUAL(dataModel-&gt;getWorkspace(), resultTuple-&gt;at(0).get&lt;shared_ptr&lt;Instance&gt; &gt;().get())`
  - **Callsite Snippet:** `BOOST_REQUIRE_EQUAL(dataModel-&gt;getWorkspace(), resultTuple-&gt;at(0).get&lt;shared_ptr&lt;Instance&gt; &gt;().get());`
- **`ClusterDeltaBuffer::SendRandomTerrain`** (`App.UnitTest/ClusterReplicationTest.cpp:1225`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_LE(packets,DesiredSendHertz*TargetSeconds)`
  - **Callsite Snippet:** `float TargetSeconds = 20;`

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `RobloxStudio/RobloxMainWindow.cpp`.

- **Alternative Implementation Files:** `RobloxStudio/RobloxMainWindow.cpp`

---

### 14. `UserIDTranslator::waitForUIDs`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void UserIDTranslator::waitForUIDs(const std::vector< const UserIDTranslator::Entry* >& uids);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/UserTranslator.cpp:146` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes waitForUIDs within Xbox Client Subsystems. Coordinates interactions with `size, getState, Sleep`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `size`, `getState`, `Sleep`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `waitForUIDs`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 15. `getState`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
ResultState getState() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `ResultState` |
| **Modifiers** | `const` |
| **Source Location** | `XboxClient/UserTranslator.h:26` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes getState within Xbox Client Subsystems. Coordinates interactions with `return, load`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `return`, `load`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getState`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 16. `currentUser`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
: currentUser(nullptr);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `:` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChat.cpp:18` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes currentUser within Xbox Client Subsystems. Coordinates interactions with `ChatManager, MeshManager, String, s2ws`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Exception handling block (try/catch recovery).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `ChatManager`, `MeshManager`, `String`, `s2ws`, `data`, `Data`, `ws2s`, `dprintf`, `c_str`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `currentUser`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 17. `VoiceChat::init`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChat::init();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChat.cpp:65` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes init within Xbox Client Subsystems. Coordinates interactions with `shared_from_this, GetMeshPacketManager, sharedPtrToThis, lock`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new; Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `shared_from_this`, `GetMeshPacketManager`, `sharedPtrToThis`, `lock`, `onIncomingChatMessage`, `GetAssociation`, `onMeshConnectionAdded`, `onMeshConnectionRemoved`, `onOutgoingChatPacketReady`, `onDebugMessageReceived`, `CompareUniqueConsoleIdentifiersHandler`, `Compare`.
- **External Library Dependencies:** `Boost C++ Libraries`.

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

**Divergence Analysis:** Alternative platform-specific implementations exist in: `Win/LogManager.cpp`, `XboxClient/VoiceChatMaxNet.cpp`, `App/util/XboxHttp2.cpp`.

- **Alternative Implementation Files:** `Win/LogManager.cpp`, `XboxClient/VoiceChatMaxNet.cpp`, `App/util/XboxHttp2.cpp`

---

### 18. `VoiceChat::onMeshConnectionAdded`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void VoiceChat::onMeshConnectionAdded(Microsoft::Xbox::Samples::NetworkMesh::MeshConnection^ meshConnection);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChat.cpp:177` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes onMeshConnectionAdded within Xbox Client Subsystems. Coordinates interactions with `HandleNewRemoteConsole, GetAssociation`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `HandleNewRemoteConsole`, `GetAssociation`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onMeshConnectionAdded`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 19. `VoiceChat::onMeshConnectionRemoved`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void VoiceChat::onMeshConnectionRemoved(Microsoft::Xbox::Samples::NetworkMesh::MeshConnection^ meshConnection);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChat.cpp:183` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes onMeshConnectionRemoved within Xbox Client Subsystems. Coordinates interactions with `async, RemoveRemoteConsoleAsync, GetAssociation, detach`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `async`, `RemoveRemoteConsoleAsync`, `GetAssociation`, `detach`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onMeshConnectionRemoved`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 20. `VoiceChat::multiplayerUserAdded`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChat::multiplayerUserAdded(Microsoft::Xbox::Services::Multiplayer::MultiplayerSessionMember^ member);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChat.cpp:191` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes multiplayerUserAdded within Xbox Client Subsystems.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `multiplayerUserAdded`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChatMaxNet.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChatMaxNet.cpp`

---

### 21. `VoiceChat::multiplayerUserRemoved`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChat::multiplayerUserRemoved(Microsoft::Xbox::Services::Multiplayer::MultiplayerSessionMember^ member);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChat.cpp:196` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes multiplayerUserRemoved within Xbox Client Subsystems.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `multiplayerUserRemoved`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChatMaxNet.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChatMaxNet.cpp`

---

### 22. `VoiceChat::onOutgoingChatPacketReady`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChat::onOutgoingChatPacketReady(Microsoft::Xbox::GameChat::ChatPacketEventArgs^ args);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChat.cpp:201` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes onOutgoingChatPacketReady within Xbox Client Subsystems. Coordinates interactions with `GetConnectionsByType, GetAt, GetMeshPacketManager, SendChatMessage`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `GetConnectionsByType`, `GetAt`, `GetMeshPacketManager`, `SendChatMessage`, `GetAssociation`, `onIncomingChatMessage`, `ProcessIncomingChatMessage`, `setMuteState`, `UnmuteUserFromAllChannels`, `MuteUserFromAllChannels`, `muteAll`, `MuteAllUsersFromAllChannels`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onOutgoingChatPacketReady`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChatMaxNet.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChatMaxNet.cpp`

---

### 23. `VoiceChat::onIncomingChatMessage`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void VoiceChat::onIncomingChatMessage(Windows::Storage::Streams::IBuffer^ chatMessage, Platform::Object^ uniqueRemoteConsoleIdentifier);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChat.cpp:227` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes onIncomingChatMessage within Xbox Client Subsystems. Coordinates interactions with `ProcessIncomingChatMessage`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `ProcessIncomingChatMessage`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onIncomingChatMessage`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 24. `VoiceChat::setMuteState`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChat::setMuteState(bool muted, Microsoft::Xbox::GameChat::ChatUser^ chatUser);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChat.cpp:235` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes setMuteState within Xbox Client Subsystems. Coordinates interactions with `UnmuteUserFromAllChannels, MuteUserFromAllChannels`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `UnmuteUserFromAllChannels`, `MuteUserFromAllChannels`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setMuteState`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChatMaxNet.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChatMaxNet.cpp`

---

### 25. `VoiceChat::muteAll`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChat::muteAll();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChat.cpp:244` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes muteAll within Xbox Client Subsystems. Coordinates interactions with `MuteAllUsersFromAllChannels`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `MuteAllUsersFromAllChannels`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `muteAll`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChatMaxNet.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChatMaxNet.cpp`

---

### 26. `VoiceChat::unmuteAll`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChat::unmuteAll();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChat.cpp:250` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes unmuteAll within Xbox Client Subsystems. Coordinates interactions with `UnmuteAllUsersFromAllChannels`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `UnmuteAllUsersFromAllChannels`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `unmuteAll`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChatMaxNet.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChatMaxNet.cpp`

---

### 27. `VoiceChat::onDebugMessageReceived`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChat::onDebugMessageReceived(Microsoft::Xbox::GameChat::DebugMessageEventArgs^ args);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChat.cpp:256` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes onDebugMessageReceived within Xbox Client Subsystems. Coordinates interactions with `dprintf, ws2s, Data, c_str`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `dprintf`, `ws2s`, `Data`, `c_str`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onDebugMessageReceived`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChatMaxNet.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChatMaxNet.cpp`

---

### 28. `VoiceChat::headsetConnected`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChat::headsetConnected(Windows::Xbox::System::User^ user);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChat.cpp:261` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes headsetConnected within Xbox Client Subsystems. Coordinates interactions with `addLocalUserToChannel, GetConnectionsByType, HandleNewRemoteConsole, GetAssociation`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `addLocalUserToChannel`, `GetConnectionsByType`, `HandleNewRemoteConsole`, `GetAssociation`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `headsetConnected`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChatMaxNet.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChatMaxNet.cpp`

---

### 29. `VoiceChat::headsetDisconnected`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void VoiceChat::headsetDisconnected();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChat.cpp:276` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes headsetDisconnected within Xbox Client Subsystems. Coordinates interactions with `removeLocalUserFromChannel`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `removeLocalUserFromChannel`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `headsetDisconnected`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 30. `VoiceChat::addLocalUserToChannel`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChat::addLocalUserToChannel(uint8 channelIndex, Windows::Xbox::System::User^ user);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChat.cpp:282` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes addLocalUserToChannel within Xbox Client Subsystems. Coordinates interactions with `async, AddLocalUserToChatChannelAsync, detach`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `async`, `AddLocalUserToChatChannelAsync`, `detach`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `addLocalUserToChannel`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChatMaxNet.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChatMaxNet.cpp`

---

### 31. `VoiceChat::removeLocalUserFromChannel`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChat::removeLocalUserFromChannel();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChat.cpp:305` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes removeLocalUserFromChannel within Xbox Client Subsystems. Coordinates interactions with `async, RemoveLocalUserFromChatChannelAsync, detach`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `async`, `RemoveLocalUserFromChatChannelAsync`, `detach`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `removeLocalUserFromChannel`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChatMaxNet.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChatMaxNet.cpp`

---

### 32. `VoiceChat::addConnections`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChat::addConnections(Windows::Foundation::Collections::IVectorView<MultiplayerSessionMember^>^ members);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChat.cpp:314` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes addConnections within Xbox Client Subsystems. Coordinates interactions with `IsEmpty, find, end, FromBase64String`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `IsEmpty`, `find`, `end`, `FromBase64String`, `ConnectToAddress`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `addConnections`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChatMaxNet.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChatMaxNet.cpp`

---

### 33. `VoiceChat::removeConnections`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChat::removeConnections(Windows::Foundation::Collections::IVectorView<MultiplayerSessionMember^>^ members);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChat.cpp:337` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes removeConnections within Xbox Client Subsystems. Coordinates interactions with `IsEmpty, find, end, FromBase64String`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `IsEmpty`, `find`, `end`, `FromBase64String`, `DisconectFromAddress`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `removeConnections`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChatMaxNet.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChatMaxNet.cpp`

---

### 34. `create`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
boost::shared_ptr<VoiceChatBase> create(unsigned char sessionConsoleId);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `boost::shared_ptr&lt;VoiceChatBase&gt;` |
| **Modifiers** | `static` |
| **Source Location** | `XboxClient/VoiceChat.h:14` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes create within Xbox Client Subsystems. Coordinates interactions with `VoiceChat, init`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new; Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `VoiceChat`, `init`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

This function is exercised in **39 test case(s)**:

- **`AutowedgeTest::ExplosionBelowTerrainWorks`** (`App.UnitTest/AutowedgeTest.cpp:247`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(fixture.cluster-&gt;getVoxelGrid()-&gt;getCellMaterial(Vector3int16(kOffset, 0, kOffset)), CELL_MATERIAL_Grass)`, `BOOST_REQUIRE(check)`
  - **Callsite Snippet:** `shared_ptr&lt;Explosion&gt; exp = Creatable&lt;Instance&gt;::create&lt;Explosion&gt;();`
- **`AutowedgeTest::ExplosionAboveTerrainWorks`** (`App.UnitTest/AutowedgeTest.cpp:270`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(fixture.cluster-&gt;getVoxelGrid()-&gt;getCellMaterial(Vector3int16(kOffset, 62, kOffset)), CELL_MATERIAL_Grass)`, `BOOST_REQUIRE(check)`
  - **Callsite Snippet:** `shared_ptr&lt;Explosion&gt; exp = Creatable&lt;Instance&gt;::create&lt;Explosion&gt;();`
- **`Instance::WaitForChildReturnsImmediatelyIfChildPresent`** (`App.UnitTest/Instance.cpp:264`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(part-&gt;getName(), "Renamed")`
  - **Callsite Snippet:** `shared_ptr&lt;Script&gt; script = Creatable&lt;RBX::Instance&gt;::create&lt;Script&gt;();`
- **`Instance::WaitForSameChildAfterInitialWaitForChild`** (`App.UnitTest/Instance.cpp:289`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(part-&gt;getName(), "Renamed")`
  - **Callsite Snippet:** `shared_ptr&lt;Script&gt; script = Creatable&lt;RBX::Instance&gt;::create&lt;Script&gt;();`

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `Rendering/GfxCore/GL/ContextGLAndroid.cpp`, `Rendering/GfxCore/GL/ContextGLMac.mm`, `XboxClient/async.h`.

- **Alternative Implementation Files:** `Rendering/GfxCore/GL/ContextGLAndroid.cpp`, `Rendering/GfxCore/GL/ContextGLMac.mm`, `XboxClient/async.h`, `XboxClient/VoiceChatMaxNet.h`, `Rendering/GfxCore/GL/ContextGLWin32.cpp`

---

### 35. `~VoiceChatBase`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
public:
        virtual ~VoiceChatBase();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `public:
        virtual` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatBase.h:11` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Declaration or inline method for ~VoiceChatBase.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `~VoiceChatBase`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 36. `getMuteState`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
unsigned getMuteState(unsigned memberId);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `unsigned` |
| **Modifiers** | `virtual` |
| **Source Location** | `XboxClient/VoiceChatBase.h:36` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes getMuteState within Xbox Client Subsystems. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getMuteState`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChatMaxNet.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChatMaxNet.cpp`

---

### 37. `muteUser`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void muteUser(unsigned memberId);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `virtual` |
| **Source Location** | `XboxClient/VoiceChatBase.h:39` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Declaration or inline method for muteUser.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `muteUser`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChatMaxNet.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChatMaxNet.cpp`

---

### 38. `unmuteUser`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void unmuteUser(unsigned memberId);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `virtual` |
| **Source Location** | `XboxClient/VoiceChatBase.h:41` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Declaration or inline method for unmuteUser.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `unmuteUser`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChatMaxNet.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChatMaxNet.cpp`

---

### 39. `updateMember`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void updateMember(unsigned memberId, float distance, TalkingDelta* talkingDeltaOut);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `virtual` |
| **Source Location** | `XboxClient/VoiceChatBase.h:42` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Declaration or inline method for updateMember.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `updateMember`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChatMaxNet.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChatMaxNet.cpp`

---

### 40. `xbLiveContext`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
: xbLiveContext(xboxLiveContext);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `:` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatMaxNet.cpp:22` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes xbLiveContext within Xbox Client Subsystems. Coordinates interactions with `ChatManager, reset, Network`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `ChatManager`, `reset`, `Network`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `xbLiveContext`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 41. `VoiceChatMaxNet::init`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChatMaxNet::init();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatMaxNet.cpp:45` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes init within Xbox Client Subsystems. Coordinates interactions with `shared_from_this, sharedPtrToThis, lock, onOutgoingChatPacketReady`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new; Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** RAII mutex lock acquisition (scoped_lock).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `shared_from_this`, `sharedPtrToThis`, `lock`, `onOutgoingChatPacketReady`, `onDebugMessageReceived`, `CompareUniqueConsoleIdentifiersHandler`, `RBXASSERT`, `return`, `Equals`, `muteAll`, `unmuteAll`, `subscribeToChatMessages_NoLock`.
- **External Library Dependencies:** `Boost C++ Libraries`.

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

- **Alternative Implementation Files:** `XboxClient/VoiceChat.cpp`, `Win/LogManager.cpp`, `App/util/XboxHttp2.cpp`

---

### 42. `VoiceChatMaxNet::updateMember`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChatMaxNet::updateMember(unsigned memberId, float distance, TalkingDelta* talkingDeltaOut);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatMaxNet.cpp:133` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes updateMember within Xbox Client Subsystems. Coordinates interactions with `GetChatUsers, get, RBXASSERT, TalkingState`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `GetChatUsers`, `get`, `RBXASSERT`, `TalkingState`, `GetAllChannels`, `GetAt`, `clamp`.
- **External Library Dependencies:** `G3D Graphics and Math Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `updateMember`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChatBase.h`.

- **Alternative Implementation Files:** `XboxClient/VoiceChatBase.h`

---

### 43. `VoiceChatMaxNet::handleNewRemoteConnection`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void VoiceChatMaxNet::handleNewRemoteConnection(ConsoleId^ consoleId);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatMaxNet.cpp:177` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes handleNewRemoteConnection within Xbox Client Subsystems. Coordinates interactions with `HandleNewRemoteConsole`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `HandleNewRemoteConsole`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `handleNewRemoteConnection`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 44. `VoiceChatMaxNet::multiplayerUserAdded`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChatMaxNet::multiplayerUserAdded(Microsoft::Xbox::Services::Multiplayer::MultiplayerSessionMember^ member);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatMaxNet.cpp:182` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes multiplayerUserAdded within Xbox Client Subsystems. Coordinates interactions with `lock, RBXASSERT, find, end`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new; Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** RAII mutex lock acquisition (scoped_lock).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT); Defensive null-pointer validation guard.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lock`, `RBXASSERT`, `find`, `end`, `shared_from_this`, `IsEmpty`, `GetChatUsers`, `createPeer`, `TalkingState`, `handleNewRemoteConnection`, `ConsoleId`, `getPeerId`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `multiplayerUserAdded`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChat.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChat.cpp`

---

### 45. `VoiceChatMaxNet::multiplayerUserRemoved`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChatMaxNet::multiplayerUserRemoved(Microsoft::Xbox::Services::Multiplayer::MultiplayerSessionMember^ member);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatMaxNet.cpp:228` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes multiplayerUserRemoved within Xbox Client Subsystems. Coordinates interactions with `lock, RBXASSERT, find, end`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** RAII mutex lock acquisition (scoped_lock).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lock`, `RBXASSERT`, `find`, `end`, `destroyPeer`, `erase`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `multiplayerUserRemoved`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChat.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChat.cpp`

---

### 46. `VoiceChatMaxNet::sendData`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void VoiceChatMaxNet::sendData(Xp2p::PeerPtr peer, Windows::Storage::Streams::IBuffer^ buffer, unsigned int flags);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatMaxNet.cpp:240` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes sendData within Xbox Client Subsystems. Coordinates interactions with `QueryInterface, IID_PPV_ARGS, Buffer, memcpy`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Defensive null-pointer validation guard.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `QueryInterface`, `IID_PPV_ARGS`, `Buffer`, `memcpy`, `sendPacket`, `Sleep`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `sendData`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 47. `VoiceChatMaxNet::onOutgoingChatPacketReady`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChatMaxNet::onOutgoingChatPacketReady(Microsoft::Xbox::GameChat::ChatPacketEventArgs^ args);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatMaxNet.cpp:265` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes onOutgoingChatPacketReady within Xbox Client Subsystems. Coordinates interactions with `get, lock, subscriptionLock, find`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** RAII mutex lock acquisition (scoped_lock).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `get`, `lock`, `subscriptionLock`, `find`, `end`, `sendData`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onOutgoingChatPacketReady`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChat.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChat.cpp`

---

### 48. `VoiceChatMaxNet::receive`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void VoiceChatMaxNet::receive();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatMaxNet.cpp:293` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes receive within Xbox Client Subsystems. Coordinates interactions with `recvPacket, processPacket, ConsoleId, getPeerId`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Multi-case state dispatch.
- **Memory Management:** Dynamic heap allocation via C++ operator new; Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** RAII mutex lock acquisition (scoped_lock).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `recvPacket`, `processPacket`, `ConsoleId`, `getPeerId`, `DataWriter`, `WriteBytes`, `getDataSize`, `DetachBuffer`, `ProcessIncomingChatMessage`, `getUserByMemberId`, `shared_from_this`, `async`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `receive`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 49. `VoiceChatMaxNet::setMuteState`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChatMaxNet::setMuteState(bool muted, Microsoft::Xbox::GameChat::ChatUser^ chatUser);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatMaxNet.cpp:364` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes setMuteState within Xbox Client Subsystems. Coordinates interactions with `UnmuteUserFromAllChannels, MuteUserFromAllChannels`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `UnmuteUserFromAllChannels`, `MuteUserFromAllChannels`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setMuteState`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChat.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChat.cpp`

---

### 50. `VoiceChatMaxNet::getMuteState`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
unsigned VoiceChatMaxNet::getMuteState(unsigned memberId);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `unsigned` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatMaxNet.cpp:373` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes getMuteState within Xbox Client Subsystems. Coordinates interactions with `getUserByMemberId, find, end`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getUserByMemberId`, `find`, `end`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getMuteState`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChatBase.h`.

- **Alternative Implementation Files:** `XboxClient/VoiceChatBase.h`

---

### 51. `VoiceChatMaxNet::muteAll`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChatMaxNet::muteAll();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatMaxNet.cpp:385` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes muteAll within Xbox Client Subsystems. Coordinates interactions with `MuteAllUsersFromAllChannels`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `MuteAllUsersFromAllChannels`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `muteAll`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChat.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChat.cpp`

---

### 52. `VoiceChatMaxNet::unmuteAll`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChatMaxNet::unmuteAll();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatMaxNet.cpp:391` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes unmuteAll within Xbox Client Subsystems. Coordinates interactions with `UnmuteAllUsersFromAllChannels`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `UnmuteAllUsersFromAllChannels`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `unmuteAll`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChat.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChat.cpp`

---

### 53. `VoiceChatMaxNet::muteUser`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChatMaxNet::muteUser(unsigned memberId);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatMaxNet.cpp:412` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes muteUser within Xbox Client Subsystems. Coordinates interactions with `getUserByMemberId, MuteUserFromAllChannels`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getUserByMemberId`, `MuteUserFromAllChannels`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `muteUser`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChatBase.h`.

- **Alternative Implementation Files:** `XboxClient/VoiceChatBase.h`

---

### 54. `VoiceChatMaxNet::unmuteUser`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChatMaxNet::unmuteUser(unsigned memberId);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatMaxNet.cpp:418` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes unmuteUser within Xbox Client Subsystems. Coordinates interactions with `getUserByMemberId, UnmuteUserFromAllChannels`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getUserByMemberId`, `UnmuteUserFromAllChannels`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `unmuteUser`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChatBase.h`.

- **Alternative Implementation Files:** `XboxClient/VoiceChatBase.h`

---

### 55. `VoiceChatMaxNet::onDebugMessageReceived`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChatMaxNet::onDebugMessageReceived(Microsoft::Xbox::GameChat::DebugMessageEventArgs^ args);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatMaxNet.cpp:424` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes onDebugMessageReceived within Xbox Client Subsystems. Coordinates interactions with `dprintf, ws2s, Data, c_str`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `dprintf`, `ws2s`, `Data`, `c_str`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onDebugMessageReceived`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChat.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChat.cpp`

---

### 56. `VoiceChatMaxNet::headsetConnected`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChatMaxNet::headsetConnected(Windows::Xbox::System::User^ user);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatMaxNet.cpp:429` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes headsetConnected within Xbox Client Subsystems. Coordinates interactions with `addLocalUserToChannel, lock, HandleNewRemoteConsole, ConsoleId`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** RAII mutex lock acquisition (scoped_lock).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `addLocalUserToChannel`, `lock`, `HandleNewRemoteConsole`, `ConsoleId`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `headsetConnected`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChat.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChat.cpp`

---

### 57. `VoiceChatMaxNet::addLocalUserToChannel`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChatMaxNet::addLocalUserToChannel(uint8 channelIndex, Windows::Xbox::System::User^ user);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatMaxNet.cpp:444` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes addLocalUserToChannel within Xbox Client Subsystems. Coordinates interactions with `lock, async, AddLocalUserToChatChannelAsync, except`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** RAII mutex lock acquisition (scoped_lock).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lock`, `async`, `AddLocalUserToChatChannelAsync`, `except`, `dprintf`, `Data`, `join`, `removeLocalUserFromChannel_NoLock`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `addLocalUserToChannel`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChat.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChat.cpp`

---

### 58. `VoiceChatMaxNet::removeLocalUserFromChannel`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChatMaxNet::removeLocalUserFromChannel();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatMaxNet.cpp:464` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes removeLocalUserFromChannel within Xbox Client Subsystems. Coordinates interactions with `lock, removeLocalUserFromChannel_NoLock`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** RAII mutex lock acquisition (scoped_lock).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lock`, `removeLocalUserFromChannel_NoLock`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `removeLocalUserFromChannel`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChat.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChat.cpp`

---

### 59. `VoiceChatMaxNet::removeLocalUserFromChannel_NoLock`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void VoiceChatMaxNet::removeLocalUserFromChannel_NoLock();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatMaxNet.cpp:470` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes removeLocalUserFromChannel_NoLock within Xbox Client Subsystems. Coordinates interactions with `async, RemoveLocalUserFromChatChannelAsync, except, dprintf`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `async`, `RemoveLocalUserFromChatChannelAsync`, `except`, `dprintf`, `Data`, `join`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `removeLocalUserFromChannel_NoLock`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 60. `VoiceChatMaxNet::addConnections`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void VoiceChatMaxNet::addConnections(Windows::Foundation::Collections::IVectorView<MultiplayerSessionMember^>^ members);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `XboxClient/VoiceChatMaxNet.cpp:485` |
| **Subsystem** | `Xbox Client Subsystems` |

#### How it Works Internally

Executes addConnections within Xbox Client Subsystems.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `addConnections`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChat.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChat.cpp`

---


:::tip Additional Functions
There are **239 additional internal and inline functions** in this subsystem. All functions are indexed and cross-referenced in the **[Complete Function Catalog](./function-catalog.md)**.
:::

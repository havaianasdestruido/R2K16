---
sidebar_position: 11
title: App - Tools & User Input
description: Studio draggers, Selection system, UserInputService, and GUI components.
---

# App - Tools & User Input

Studio draggers, Selection system, UserInputService, and GUI components.

## Subsystem Metrics

- **Total Documented Functions:** `498`
- **Functions Exercised in Tests:** `13`
- **Platform-Divergent Implementations:** `17`
- **Component Source Files:** `48`

## Source Files

<details>
<summary>View all 48 source files in this subsystem</summary>

| Source File | Path |
| :--- | :--- |
| `ChatOutput.cpp` | `App/gui/ChatOutput.cpp` |
| `ChatWidget.cpp` | `App/gui/ChatWidget.cpp` |
| `EquationDisplay.cpp` | `App/gui/EquationDisplay.cpp` |
| `GUI.cpp` | `App/gui/GUI.cpp` |
| `GuiDraw.cpp` | `App/gui/GuiDraw.cpp` |
| `ProfanityFilter.cpp` | `App/gui/ProfanityFilter.cpp` |
| `Widget.cpp` | `App/gui/Widget.cpp` |
| `ChatOutput.h` | `App/include/gui/ChatOutput.h` |
| `ChatWidget.h` | `App/include/gui/ChatWidget.h` |
| `GUI.h` | `App/include/gui/GUI.h` |
| `GuiEvent.h` | `App/include/gui/GuiEvent.h` |
| `Widget.h` | `App/include/gui/Widget.h` |
| `AdvLuaDragger.h` | `App/include/tool/AdvLuaDragger.h` |
| `AdvMoveTool.h` | `App/include/tool/AdvMoveTool.h` |
| `AdvRotateTool.h` | `App/include/tool/AdvRotateTool.h` |
| `AdvRunDragger.h` | `App/include/tool/AdvRunDragger.h` |
| `DragUtilities.h` | `App/include/tool/DragUtilities.h` |
| `Dragger.h` | `App/include/tool/Dragger.h` |
| `LuaDragger.h` | `App/include/tool/LuaDragger.h` |
| `MegaDragger.h` | `App/include/tool/MegaDragger.h` |
| `ToolsArrow.h` | `App/include/tool/ToolsArrow.h` |
| `AdvDragTool.cpp` | `App/tool/AdvDragTool.cpp` |
| `AdvLuaDragTool.cpp` | `App/tool/AdvLuaDragTool.cpp` |
| `AdvLuaDragger.cpp` | `App/tool/AdvLuaDragger.cpp` |
| `AdvMoveTool.cpp` | `App/tool/AdvMoveTool.cpp` |
| `AdvRotateTool.cpp` | `App/tool/AdvRotateTool.cpp` |
| `AdvRunDragger.cpp` | `App/tool/AdvRunDragger.cpp` |
| `AxisMoveTool.cpp` | `App/tool/AxisMoveTool.cpp` |
| `CloneTool.cpp` | `App/tool/CloneTool.cpp` |
| `DragTool.cpp` | `App/tool/DragTool.cpp` |
| `DragUtilities.cpp` | `App/tool/DragUtilities.cpp` |
| `Dragger.cpp` | `App/tool/Dragger.cpp` |
| `DropTool.cpp` | `App/tool/DropTool.cpp` |
| `GameTool.cpp` | `App/tool/GameTool.cpp` |
| `GrabTool.cpp` | `App/tool/GrabTool.cpp` |
| `GroupDragTool.cpp` | `App/tool/GroupDragTool.cpp` |
| `GroupDropTool.cpp` | `App/tool/GroupDropTool.cpp` |
| `HammerTool.cpp` | `App/tool/HammerTool.cpp` |
| `LuaDragTool.cpp` | `App/tool/LuaDragTool.cpp` |
| `LuaDragger.cpp` | `App/tool/LuaDragger.cpp` |
| `MegaDragger.cpp` | `App/tool/MegaDragger.cpp` |
| `MoveResizeJoinTool.cpp` | `App/tool/MoveResizeJoinTool.cpp` |
| `NullTool.cpp` | `App/tool/NullTool.cpp` |
| `PartDragTool.cpp` | `App/tool/PartDragTool.cpp` |
| `PartDropTool.cpp` | `App/tool/PartDropTool.cpp` |
| `ResizeTool.cpp` | `App/tool/ResizeTool.cpp` |
| `RunDragger.cpp` | `App/tool/RunDragger.cpp` |
| `ToolsArrow.cpp` | `App/tool/ToolsArrow.cpp` |

</details>

---

## Function Reference

### 1. `lerpLength`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
float lerpLength(const std::string& msg, float min, float max);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `float` |
| **Modifiers** | `static` |
| **Source Location** | `App/gui/ChatOutput.cpp:33` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes lerpLength within App - Tools & User Input. Coordinates interactions with `min, length`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `min`, `length`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `lerpLength`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 2. `ChatLine::ComputeBubbleLifetime`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
float ChatLine::ComputeBubbleLifetime(const std::string& msg, bool isSelf);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `float` |
| **Modifiers** | None |
| **Source Location** | `App/gui/ChatOutput.cpp:38` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes ComputeBubbleLifetime within App - Tools & User Input. Coordinates interactions with `lerpLength`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lerpLength`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `ComputeBubbleLifetime`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 3. `createChatBubbleMain`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
shared_ptr<Scale9Frame> createChatBubbleMain(const std::string& filePrefix);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `shared_ptr&lt;Scale9Frame&gt;` |
| **Modifiers** | `static` |
| **Source Location** | `App/gui/ChatOutput.cpp:99` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes createChatBubbleMain within App - Tools & User Input. Coordinates interactions with `setName, setScaleEdgeSize, Vector2int16, setSlicePrefix`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `setName`, `setScaleEdgeSize`, `Vector2int16`, `setSlicePrefix`, `setBackgroundTransparency`, `setBorderSizePixel`, `setSize`, `UDim2`, `setPosition`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `createChatBubbleMain`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 4. `createChatBubbleWithTail`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
shared_ptr<Scale9Frame> createChatBubbleWithTail(const std::string& filePrefix, const UDim2& position, const UDim2& size);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `shared_ptr&lt;Scale9Frame&gt;` |
| **Modifiers** | `static` |
| **Source Location** | `App/gui/ChatOutput.cpp:115` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes createChatBubbleWithTail within App - Tools & User Input. Coordinates interactions with `createChatBubbleMain, setName, setImage, setBackgroundTransparency`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `createChatBubbleMain`, `setName`, `setImage`, `setBackgroundTransparency`, `setBorderSizePixel`, `setPosition`, `setSize`, `setParent`, `get`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `createChatBubbleWithTail`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 5. `createScaledChatBubbleWithTail`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
shared_ptr<Scale9Frame> createScaledChatBubbleWithTail(const std::string& filePrefix, float frameScaleSize, const UDim2& position);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `shared_ptr&lt;Scale9Frame&gt;` |
| **Modifiers** | `static` |
| **Source Location** | `App/gui/ChatOutput.cpp:131` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes createScaledChatBubbleWithTail within App - Tools & User Input. Coordinates interactions with `createChatBubbleMain, setName, setBackgroundTransparency, setSizeConstraint`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `createChatBubbleMain`, `setName`, `setBackgroundTransparency`, `setSizeConstraint`, `setPosition`, `UDim2`, `setSize`, `setParent`, `get`, `setImage`, `setBorderSizePixel`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `createScaledChatBubbleWithTail`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 6. `createChatImposter`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
shared_ptr<GuiObject> createChatImposter(const std::string& filePrefix, const std::string& dotDotDot, float yOffset);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `shared_ptr&lt;GuiObject&gt;` |
| **Modifiers** | `static` |
| **Source Location** | `App/gui/ChatOutput.cpp:156` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes createChatImposter within App - Tools & User Input. Coordinates interactions with `setName, setImage, setBackgroundTransparency, setBorderSizePixel`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `setName`, `setImage`, `setBackgroundTransparency`, `setBorderSizePixel`, `setPosition`, `UDim2`, `setSize`, `setParent`, `get`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `createChatImposter`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 7. `PlayerChatLine::getCharacter`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
ModelInstance* PlayerChatLine::getCharacter() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `ModelInstance*` |
| **Modifiers** | `const const` |
| **Source Location** | `App/gui/ChatOutput.cpp:221` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes getCharacter within App - Tools & User Input. Coordinates interactions with `getOrigin`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getOrigin`.

#### How it is Used in Tests

This function is exercised in **7 test case(s)**:

- **`Network::ReplicationDoesNotAllowRedundantExistingJointsWithCharacterToBeSeen`** (`App.UnitTest/Network.cpp:822`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE(lighting)`, `BOOST_REQUIRE(lighting)`
  - **Callsite Snippet:** `clientCharacterModel = player-&gt;getCharacter();`
- **`Network::ServerStressTestClient`** (`App.UnitTest/Network.cpp:1143`)
  - **Usage Pattern:** `Direct Call`
  - **Callsite Snippet:** `ModelInstance* character = player-&gt;getCharacter();`
- **`ReplicatorGcJobTest::MovingPartOutsideOfStreamedAreaCausesItToBeGced`** (`App.UnitTest/ReplicatorGcJobTest.cpp:98`)
  - **Usage Pattern:** `Performance Benchmark`
  - **Assertions Checked:** `BOOST_REQUIRE(clientDm-&gt;getWorkspace()-&gt;findFirstChildByName("BasePlate"))`, `BOOST_REQUIRE(clientDm-&gt;getWorkspace()-&gt;findFirstChildByName("ToStreamOut"))`
  - **Callsite Snippet:** `ModelInstance* character = player-&gt;getCharacter();`
- **`ReplicatorGcJobTest::MovingPartAndItsParentOutsideOfStreamedAreaShouldNotRemoveThePartTwice`** (`App.UnitTest/ReplicatorGcJobTest.cpp:195`)
  - **Usage Pattern:** `Performance Benchmark`
  - **Assertions Checked:** `BOOST_REQUIRE(clientDm-&gt;getWorkspace()-&gt;findFirstChildByName("BasePlate"))`, `BOOST_REQUIRE(parent)`
  - **Callsite Snippet:** `ModelInstance* character = player-&gt;getCharacter();`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 8. `ChatOutput::acceleratedBubbleDecay`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void ChatOutput::acceleratedBubbleDecay(ChatLine* line, float wallStep, bool isMoving, bool isVisible);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/ChatOutput.cpp:226` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes acceleratedBubbleDecay within App - Tools & User Input.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `acceleratedBubbleDecay`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 9. `ChatOutput::SanitizeChatLine`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string ChatOutput::SanitizeChatLine(const std::string& msg);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `App/gui/ChatOutput.cpp:238` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes SanitizeChatLine within App - Tools & User Input. Coordinates interactions with `size, substr`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `size`, `substr`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `SanitizeChatLine`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 10. `ChatOutput::onServiceProvider`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void ChatOutput::onServiceProvider(ServiceProvider* oldProvider, ServiceProvider* newProvider);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/ChatOutput.cpp:250` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes onServiceProvider within App - Tools & User Input. Coordinates interactions with `disconnect, connect, bind`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `disconnect`, `connect`, `bind`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onServiceProvider`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 11. `ChatOutput::removeOldest`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void ChatOutput::removeOldest();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/ChatOutput.cpp:272` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes removeOldest within App - Tools & User Input. Coordinates interactions with `pop_front`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `pop_front`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `removeOldest`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 12. `ChatOutput::removeExpired`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool ChatOutput::removeExpired();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `App/gui/ChatOutput.cpp:278` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes removeExpired within App - Tools & User Input. Coordinates interactions with `min, singleton, empty, front`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `min`, `singleton`, `empty`, `front`, `get`, `pop_front`, `begin`, `end`, `playerfifo`, `size`, `lock`, `setParent`.
- **External Library Dependencies:** `Boost C++ Libraries`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `removeExpired`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 13. `ChatOutput::onHeartbeat`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void ChatOutput::onHeartbeat(const Heartbeat& heartbeat);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/ChatOutput.cpp:322` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes onHeartbeat within App - Tools & User Input. Coordinates interactions with `begin, end, playerfifo, size`. Employs heap memory deallocation via operator delete.

- **Control Flow & Execution:** Iterative loop processing.
- **Memory Management:** Heap memory deallocation via operator delete; Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `begin`, `end`, `playerfifo`, `size`, `acceleratedBubbleDecay`, `get`, `removeExpired`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onHeartbeat`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 14. `ChatOutput::createBillboardGuiHelper`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void ChatOutput::createBillboardGuiHelper(Instance* instance, bool onlyCharacter);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/ChatOutput.cpp:342` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes createBillboardGuiHelper within App - Tools & User Input. Coordinates interactions with `lock, setAdornee, setRobloxLocked, setParent`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new; Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lock`, `setAdornee`, `setRobloxLocked`, `setParent`, `findFirstChildByName`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `createBillboardGuiHelper`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 15. `ChatOutput::onGameChatMessage`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void ChatOutput::onGameChatMessage(boost::shared_ptr<Instance> origin, const std::string& message, ChatService::ChatColor color);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/ChatOutput.cpp:380` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes onGameChatMessage within App - Tools & User Input. Coordinates interactions with `ContainsProfanity, getLocalPlayer, getCharacter, get`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Conditional branching, Multi-case state dispatch, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new; Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `ContainsProfanity`, `getLocalPlayer`, `getCharacter`, `get`, `SanitizeChatLine`, `line`, `GameChatLine`, `getOrigin`, `push_back`, `createBillboardGuiHelper`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onGameChatMessage`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 16. `ChatOutput::onPlayerChatMessage`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void ChatOutput::onPlayerChatMessage(const Network::ChatMessage& event);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/ChatOutput.cpp:401` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes onPlayerChatMessage within App - Tools & User Input. Coordinates interactions with `starts_with, size, singleton, removeOldest`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Multi-case state dispatch, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new; Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT); Defensive null-pointer validation guard.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `starts_with`, `size`, `singleton`, `removeOldest`, `getLocalPlayer`, `get`, `SanitizeChatLine`, `line`, `PlayerChatLine`, `push_back`, `getOrigin`, `chat`.
- **External Library Dependencies:** `Boost C++ Libraries`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onPlayerChatMessage`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 17. `ChatOutput::bubbleChatEnabled`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool ChatOutput::bubbleChatEnabled();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `App/gui/ChatOutput.cpp:447` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes bubbleChatEnabled within App - Tools & User Input. Coordinates interactions with `getBubbleChat`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getBubbleChat`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `bubbleChatEnabled`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 18. `ChatOutput::render2d`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void ChatOutput::render2d(Adorn* adorn);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/ChatOutput.cpp:456` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes render2d within App - Tools & User Input. Coordinates interactions with `render2d_bubbleStyle, bubbleChatEnabled`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `render2d_bubbleStyle`, `bubbleChatEnabled`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `render2d`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 19. `ChatOutput::renderBubbleImposters`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void ChatOutput::renderBubbleImposters(Adorn* adorn, weak_ptr<const Instance> weakOwner, weak_ptr<PartInstance> weakHead);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/ChatOutput.cpp:461` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes renderBubbleImposters within App - Tools & User Input. Coordinates interactions with `lock, get, viewportBillboarder, Vector3`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Defensive null-pointer validation guard.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lock`, `get`, `viewportBillboarder`, `Vector3`, `Vector2`, `UDim2`, `update`, `getViewport`, `getConstCamera`, `getPartSizeXml`, `calcRenderingCoordinateFrame`, `isVisibleAndValid`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `renderBubbleImposters`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 20. `ChatOutput::renderBubbles`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void ChatOutput::renderBubbles(Adorn* adorn, weak_ptr<const Instance> weakOwner, weak_ptr<PartInstance> weakHead, bool playerBubbleChat,
							   Vector3 extentsOffset, Vector3 studsOffset);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/ChatOutput.cpp:495` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes renderBubbles within App - Tools & User Input. Coordinates interactions with `lock, get, size, UDim`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Defensive null-pointer validation guard.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lock`, `get`, `size`, `UDim`, `contribution`, `viewportBillboarder`, `zero`, `update`, `getViewport`, `getConstCamera`, `getPartSizeXml`, `calcRenderingCoordinateFrame`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `renderBubbles`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 21. `ChatOutput::render2d_bubbleStyle`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void ChatOutput::render2d_bubbleStyle(Adorn* adorn, bool playerBubbleChat);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/ChatOutput.cpp:641` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes render2d_bubbleStyle within App - Tools & User Input. Coordinates interactions with `begin, end, playerfifo, lock`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Multi-case state dispatch.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `begin`, `end`, `playerfifo`, `lock`, `setRenderFunction`, `empty`, `Vector3`, `camera`, `findFirstChildByName`, `RBXASSERT`, `getName`, `getParent`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `render2d_bubbleStyle`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 22. `UnifiedImageWidget::getWidgetState`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Gui::WidgetState UnifiedImageWidget::getWidgetState() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Gui::WidgetState` |
| **Modifiers** | `const` |
| **Source Location** | `App/gui/ChatWidget.cpp:8` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes getWidgetState within App - Tools & User Input. Coordinates interactions with `getMenuState`.

- **Control Flow & Execution:** Multi-case state dispatch, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getMenuState`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getWidgetState`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 23. `UnifiedImageWidget::render2dMe`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void UnifiedImageWidget::render2dMe(Adorn* adorn);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/ChatWidget.cpp:22` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes render2dMe within App - Tools & User Input. Coordinates interactions with `isVisible, setImageFromName, render2d, getMyRect`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `isVisible`, `setImageFromName`, `render2d`, `getMyRect`, `getCanvas`, `getWidgetState`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `render2dMe`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 24. `ChatButton::isVisible`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool ChatButton::isVisible() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `App/gui/ChatWidget.cpp:33` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes isVisible within App - Tools & User Input. Coordinates interactions with `return, getLocalPlayer, clientIsPresent`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `return`, `getLocalPlayer`, `clientIsPresent`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isVisible`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 25. `ChatWidget::findMenuString`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string ChatWidget::findMenuString(GuiItem* item);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `App/gui/ChatWidget.cpp:48` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes findMenuString within App - Tools & User Input. Coordinates interactions with `RBXASSERT, getParent, findChildIndex, getGuiParent`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `RBXASSERT`, `getParent`, `findChildIndex`, `getGuiParent`, `convertToString`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `findMenuString`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 26. `ChatWidget::onMenuStateChanged`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void ChatWidget::onMenuStateChanged();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/ChatWidget.cpp:64` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes onMenuStateChanged within App - Tools & User Input. Coordinates interactions with `getMenuState, setMenuState`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getMenuState`, `setMenuState`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onMenuStateChanged`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 27. `ChatWidget::process`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
GuiResponse ChatWidget::process(const shared_ptr<InputObject>& event);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `GuiResponse` |
| **Modifiers** | None |
| **Source Location** | `App/gui/ChatWidget.cpp:73` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes process within App - Tools & User Input. Coordinates interactions with `isVisible, isMouseEvent, isLeftMouseUpEvent, getMyRect`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `isVisible`, `isMouseEvent`, `isLeftMouseUpEvent`, `getMyRect`, `Canvas`, `getWindowSize`, `pointInRect`, `get2DPosition`, `playSound`, `ClickSound`, `findMenuString`, `chat`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `process`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.cpp`.

- **Alternative Implementation Files:** `Network/Replicator.NewInstanceItem.cpp`

---

### 28. `EquationDisplay::getLabel`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string EquationDisplay::getLabel() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | `const` |
| **Source Location** | `App/gui/EquationDisplay.cpp:27` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes getLabel within App - Tools & User Input. Coordinates interactions with `getRootAncestor, RBXASSERT, getMetric`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getRootAncestor`, `RBXASSERT`, `getMetric`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getLabel`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 29. `EquationDisplay::render2d`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void EquationDisplay::render2d(Adorn* adorn);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/EquationDisplay.cpp:42` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes render2d within App - Tools & User Input. Coordinates interactions with `isVisible, label2d, getLabel`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `isVisible`, `label2d`, `getLabel`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `render2d`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 30. `GuiItem::disabledFill`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Color4& GuiItem::disabledFill() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Color4&` |
| **Modifiers** | `const` |
| **Source Location** | `App/gui/GUI.cpp:11` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes disabledFill within App - Tools & User Input.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `disabledFill`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 31. `GuiItem::translucentBackdrop`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Color4& GuiItem::translucentBackdrop() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Color4&` |
| **Modifiers** | `const` |
| **Source Location** | `App/gui/GUI.cpp:13` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes translucentBackdrop within App - Tools & User Input.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `translucentBackdrop`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 32. `GuiItem::translucentDebugBackdrop`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Color4& GuiItem::translucentDebugBackdrop() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Color4&` |
| **Modifiers** | `const` |
| **Source Location** | `App/gui/GUI.cpp:14` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes translucentDebugBackdrop within App - Tools & User Input.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `translucentDebugBackdrop`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 33. `GuiItem::menuSelect`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Color4& GuiItem::menuSelect() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Color4&` |
| **Modifiers** | `const` |
| **Source Location** | `App/gui/GUI.cpp:15` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes menuSelect within App - Tools & User Input.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `menuSelect`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 34. `GuiItem::getGuiParent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
GuiItem* GuiItem::getGuiParent();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `GuiItem*` |
| **Modifiers** | None |
| **Source Location** | `App/gui/GUI.cpp:29` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes getGuiParent within App - Tools & User Input. Coordinates interactions with `getParent`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getParent`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getGuiParent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 35. `GuiItem::getGuiParent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
GuiItem* GuiItem::getGuiParent() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `GuiItem*` |
| **Modifiers** | `const const` |
| **Source Location** | `App/gui/GUI.cpp:35` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes getGuiParent within App - Tools & User Input. Coordinates interactions with `getParent`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getParent`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getGuiParent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 36. `GuiItem::getGuiItem`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
GuiItem* GuiItem::getGuiItem(int index);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `GuiItem*` |
| **Modifiers** | None |
| **Source Location** | `App/gui/GUI.cpp:40` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes getGuiItem within App - Tools & User Input. Coordinates interactions with `getChild`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getChild`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getGuiItem`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 37. `GuiItem::getGuiItem`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
GuiItem* GuiItem::getGuiItem(int index) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `GuiItem*` |
| **Modifiers** | `const const` |
| **Source Location** | `App/gui/GUI.cpp:45` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes getGuiItem within App - Tools & User Input. Coordinates interactions with `getChild`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getChild`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getGuiItem`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 38. `GuiItem::onDescendantRemoving`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void GuiItem::onDescendantRemoving(const shared_ptr<Instance>& instance);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/GUI.cpp:50` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes onDescendantRemoving within App - Tools & User Input. Coordinates interactions with `loseFocus`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `loseFocus`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onDescendantRemoving`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 39. `GuiItem::getMyRect`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Rect GuiItem::getMyRect(Canvas canvas) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Rect` |
| **Modifiers** | `const` |
| **Source Location** | `App/gui/GUI.cpp:58` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes getMyRect within App - Tools & User Input. Coordinates interactions with `getPosition, Rect, getSize`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getPosition`, `Rect`, `getSize`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getMyRect`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 40. `GuiItem::processNonFocus`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
GuiResponse GuiItem::processNonFocus(const shared_ptr<InputObject>& event);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `GuiResponse` |
| **Modifiers** | None |
| **Source Location** | `App/gui/GUI.cpp:66` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes processNonFocus within App - Tools & User Input. Coordinates interactions with `numChildren, getGuiItem, get, process`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `numChildren`, `getGuiItem`, `get`, `process`, `wasSunk`, `loseFocus`, `shared_from`, `notSunk`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `processNonFocus`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 41. `GuiItem::process`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
GuiResponse GuiItem::process(const shared_ptr<InputObject>& event);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `GuiResponse` |
| **Modifiers** | None |
| **Source Location** | `App/gui/GUI.cpp:90` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Throw away idle events

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `isMouseEvent`, `getUserInputType`, `notSunk`, `canLoseFocus`, `processNonFocus`, `wasSunk`, `loseFocus`, `RBXASSERT`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `process`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.cpp`.

- **Alternative Implementation Files:** `Network/Replicator.NewInstanceItem.cpp`

---

### 42. `GuiItem::label2d`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void GuiItem::label2d(Adorn* adorn,
	const std::string& label,
	const Color4& fill,
	const Color4& border,
	Text::XAlign align) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `const` |
| **Source Location** | `App/gui/GUI.cpp:122` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes label2d within App - Tools & User Input. Coordinates interactions with `length, getMyRect, getCanvas, size`.

- **Control Flow & Execution:** Conditional branching, Multi-case state dispatch.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `length`, `getMyRect`, `getCanvas`, `size`, `center`, `drawFont2D`, `getFontSize`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `label2d`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 43. `Canvas::normalizedFontSize`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int Canvas::normalizedFontSize(int fontSize) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `const` |
| **Source Location** | `App/gui/GUI.cpp:187` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes normalizedFontSize within App - Tools & User Input. Coordinates interactions with `percentSize, iFloor, toPixelSize`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `percentSize`, `iFloor`, `toPixelSize`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `normalizedFontSize`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 44. `GuiRoot::render2d`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void GuiRoot::render2d(Adorn* adorn);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/GUI.cpp:194` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes render2d within App - Tools & User Input. Coordinates interactions with `numChildren, getGuiItem`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `numChildren`, `getGuiItem`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `render2d`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 45. `GuiRoot::render2dItem`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void GuiRoot::render2dItem(Adorn* adorn, GuiItem* guiItem);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/GUI.cpp:202` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes render2dItem within App - Tools & User Input. Coordinates interactions with `render2d`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `render2d`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `render2dItem`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 46. `RelativePanel::init`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void RelativePanel::init(const Layout& layout);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/GUI.cpp:212` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

ScreenPanel

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `setName`.

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

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChat.cpp`, `Win/LogManager.cpp`, `XboxClient/VoiceChatMaxNet.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChat.cpp`, `Win/LogManager.cpp`, `XboxClient/VoiceChatMaxNet.cpp`, `App/util/XboxHttp2.cpp`

---

### 47. `RelativePanel::getPosition`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector2 RelativePanel::getPosition(Canvas canvas) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector2` |
| **Modifiers** | `const` |
| **Source Location** | `App/gui/GUI.cpp:222` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes getPosition within App - Tools & User Input. Coordinates interactions with `canvasRect, zero, getSize, inset`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `canvasRect`, `zero`, `getSize`, `inset`, `positionChild`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getPosition`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 48. `TopMenuBar::init`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void TopMenuBar::init();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/GUI.cpp:237` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

TopMenuBar

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `clear`.

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

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChat.cpp`, `Win/LogManager.cpp`, `XboxClient/VoiceChatMaxNet.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChat.cpp`, `Win/LogManager.cpp`, `XboxClient/VoiceChatMaxNet.cpp`, `App/util/XboxHttp2.cpp`

---

### 49. `TopMenuBar::process`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
GuiResponse TopMenuBar::process(const shared_ptr<InputObject>& event);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `GuiResponse` |
| **Modifiers** | None |
| **Source Location** | `App/gui/GUI.cpp:267` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes process within App - Tools & User Input. Coordinates interactions with `isVisible, wasSunk, isMouseEvent, getMyRect`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `isVisible`, `wasSunk`, `isMouseEvent`, `getMyRect`, `Canvas`, `getWindowSize`, `pointInRect`, `get2DPosition`, `sunk`, `notSunk`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `process`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.cpp`.

- **Alternative Implementation Files:** `Network/Replicator.NewInstanceItem.cpp`

---

### 50. `TopMenuBar::getSize`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
Vector2 TopMenuBar::getSize(Canvas canvas) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector2` |
| **Modifiers** | `const` |
| **Source Location** | `App/gui/GUI.cpp:287` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes getSize within App - Tools & User Input. Coordinates interactions with `numChildren, getGuiItem, max, RBXASSERT`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Multi-case state dispatch, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `numChildren`, `getGuiItem`, `max`, `RBXASSERT`.

#### How it is Used in Tests

This function is exercised in **2 test case(s)**:

- **`PostEffectTest::BlurEffectDefaults`** (`App.UnitTest/PostEffectTest.cpp:13`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(effect-&gt;getSize(), 24.f)`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL(effect-&gt;getSize(), 24.f);`
- **`PostEffectTest::BlurEffectSizeClamped`** (`App.UnitTest/PostEffectTest.cpp:35`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(effect-&gt;getSize(), 10.f)`, `BOOST_CHECK_EQUAL(effect-&gt;getSize(), 0.f)`, `BOOST_CHECK_EQUAL(effect-&gt;getSize(), 56.f)`, `BOOST_CHECK_EQUAL(effect-&gt;getSize(), BlurEffect::maxSize())`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL(effect-&gt;getSize(), 10.f);`

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `RobloxStudio/RobloxRibbonMainWindow.cpp`.

- **Alternative Implementation Files:** `RobloxStudio/RobloxRibbonMainWindow.cpp`

---

### 51. `TopMenuBar::getChildPosition`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector2 TopMenuBar::getChildPosition(const GuiItem* child, Canvas canvas) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector2` |
| **Modifiers** | `const` |
| **Source Location** | `App/gui/GUI.cpp:315` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes getChildPosition within App - Tools & User Input. Coordinates interactions with `getPosition, getSize, numChildren, getGuiItem`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Multi-case state dispatch, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getPosition`, `getSize`, `numChildren`, `getGuiItem`, `RBXASSERT`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getChildPosition`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 52. `TopMenuBar::render2d`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void TopMenuBar::render2d(Adorn* adorn);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/GUI.cpp:351` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes render2d within App - Tools & User Input. Coordinates interactions with `isVisible, clear, rect2d, getMyRect2D`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `isVisible`, `clear`, `rect2d`, `getMyRect2D`, `getCanvas`, `numChildren`, `getGuiItem`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `render2d`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 53. `UnifiedWidget::init`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void UnifiedWidget::init();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/GUI.cpp:370` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

UnifiedWidget

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `setGuiSize`, `Vector2`.

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

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/VoiceChat.cpp`, `Win/LogManager.cpp`, `XboxClient/VoiceChatMaxNet.cpp`.

- **Alternative Implementation Files:** `XboxClient/VoiceChat.cpp`, `Win/LogManager.cpp`, `XboxClient/VoiceChatMaxNet.cpp`, `App/util/XboxHttp2.cpp`

---

### 54. `UnifiedWidget::render2dMe`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void UnifiedWidget::render2dMe(Adorn* adorn);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/GUI.cpp:381` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes render2dMe within App - Tools & User Input. Coordinates interactions with `rect2d, getMyRect2D, getCanvas, menuSelect`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `rect2d`, `getMyRect2D`, `getCanvas`, `menuSelect`, `white`, `outlineRect2d`, `black`, `label2d`, `getName`, `clear`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `render2dMe`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 55. `UnifiedWidget::render2dChildren`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void UnifiedWidget::render2dChildren(Adorn* adorn);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/GUI.cpp:396` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes render2dChildren within App - Tools & User Input. Coordinates interactions with `showChildren, numChildren, getGuiItem, render2d`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `showChildren`, `numChildren`, `getGuiItem`, `render2d`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `render2dChildren`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 56. `UnifiedWidget::render2d`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void UnifiedWidget::render2d(Adorn* adorn);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/GUI.cpp:408` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes render2d within App - Tools & User Input. Coordinates interactions with `isVisible, render2dMe, render2dChildren`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `isVisible`, `render2dMe`, `render2dChildren`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `render2d`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 57. `UnifiedWidget::firstChildPosition`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector2 UnifiedWidget::firstChildPosition(Canvas canvas) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector2` |
| **Modifiers** | `const` |
| **Source Location** | `App/gui/GUI.cpp:419` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

each item is 24 units high

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getPosition`, `getSize`, `numChildren`, `max`, `min`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `firstChildPosition`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 58. `UnifiedWidget::childOffset`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector2 UnifiedWidget::childOffset() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector2` |
| **Modifiers** | `const` |
| **Source Location** | `App/gui/GUI.cpp:445` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes childOffset within App - Tools & User Input. Coordinates interactions with `Vector2`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `Vector2`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `childOffset`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 59. `UnifiedWidget::getChildPosition`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector2 UnifiedWidget::getChildPosition(const GuiItem* child, Canvas canvas) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector2` |
| **Modifiers** | `const` |
| **Source Location** | `App/gui/GUI.cpp:451` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes getChildPosition within App - Tools & User Input. Coordinates interactions with `firstChildPosition, numChildren, getGuiItem, childOffset`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `firstChildPosition`, `numChildren`, `getGuiItem`, `childOffset`, `RBXASSERT`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getChildPosition`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 60. `UnifiedWidget::onLoseFocus`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void UnifiedWidget::onLoseFocus();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/gui/GUI.cpp:468` |
| **Subsystem** | `App - Tools & User Input` |

#### How it Works Internally

Executes onLoseFocus within App - Tools & User Input.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onLoseFocus`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---


:::tip Additional Functions
There are **438 additional internal and inline functions** in this subsystem. All functions are indexed and cross-referenced in the **[Complete Function Catalog](./function-catalog.md)**.
:::

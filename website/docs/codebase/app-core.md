---
sidebar_position: 14
title: App - Engine Core
description: Core engine runtime headers, shared data structures, and foundational classes.
---

# App - Engine Core

Core engine runtime headers, shared data structures, and foundational classes.


## FAQ

### What does this page cover under engine core?

Its current source list focuses on Lua bridge headers. Inspect the template and its call sites before using a generated signature; template context and ownership matter.

### How can I investigate this in the repository?

From the repository root, search the relevant tracked files for a starting point (results are leads, not proof of behavior):

```bash
git grep -n -i -F -- 'memberFunctionProxy' -- App/include/lua
```

Read the surrounding implementation and callers, and check relevant tests before making changes. A search may return no matches when terminology or tracked files change.

## Subsystem Metrics

- **Total Documented Functions:** `21`
- **Functions Exercised in Tests:** `3`
- **Platform-Divergent Implementations:** `1`
- **Component Source Files:** `2`

## Source Files

<details>
<summary>View all 2 source files in this subsystem</summary>

| Source File | Path |
| :--- | :--- |
| `LuaBridge.h` | `App/include/lua/LuaBridge.h` |
| `lua.hpp` | `App/include/lua/lua.hpp` |

</details>

---

## Function Reference

### 1. `memberFunctionProxy`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int memberFunctionProxy(lua_State* thread);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | None |
| **Source Location** | `App/include/lua/LuaBridge.h:12` |
| **Subsystem** | `App - Engine Core` |

#### How it Works Internally

Executes memberFunctionProxy within App - Engine Core. Coordinates interactions with `lua_touserdata, lua_upvalueindex, return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lua_touserdata`, `lua_upvalueindex`, `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `memberFunctionProxy`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 2. `pushMemberFunction`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void pushMemberFunction(lua_State* L, C* c);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/lua/LuaBridge.h:19` |
| **Subsystem** | `App - Engine Core` |

#### How it Works Internally

Executes pushMemberFunction within App - Engine Core. Coordinates interactions with `lua_pushlightuserdata, lua_pushcclosure`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lua_pushlightuserdata`, `lua_pushcclosure`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushMemberFunction`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 3. `pushNewObject`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Class* pushNewObject(lua_State *L);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Class*` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/lua/LuaBridge.h:33` |
| **Subsystem** | `App - Engine Core` |

#### How it Works Internally

0 arg constructor

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lua_newuserdata`, `new`, `luaL_getmetatable`, `lua_setmetatable`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushNewObject`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 4. `pushNewObject`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Class* pushNewObject(lua_State *L, Param1 param1);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Class*` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/lua/LuaBridge.h:42` |
| **Subsystem** | `App - Engine Core` |

#### How it Works Internally

1 arg constructor

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lua_newuserdata`, `new`, `Class`, `luaL_getmetatable`, `lua_setmetatable`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushNewObject`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 5. `pushNewObject`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Class* pushNewObject(lua_State *L, Param1 param1, Param2 param2);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Class*` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/lua/LuaBridge.h:52` |
| **Subsystem** | `App - Engine Core` |

#### How it Works Internally

2 arg constructor

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lua_newuserdata`, `new`, `Class`, `luaL_getmetatable`, `lua_setmetatable`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pushNewObject`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 6. `getObject`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Class& getObject(lua_State *L, unsigned int index);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Class&` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/lua/LuaBridge.h:63` |
| **Subsystem** | `App - Engine Core` |

#### How it Works Internally

Throws an exception if index doesn't hold the right type

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `luaL_checkudata`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getObject`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 7. `getValue`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
bool getValue(lua_State *L, unsigned int index, V& value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/lua/LuaBridge.h:69` |
| **Subsystem** | `App - Engine Core` |

#### How it Works Internally

Returns false if index doesn't hold the right type (leaving value unchanged)

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT); C++ exception throw on invalid state or failure.
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `lua_touserdata`, `lua_getmetatable`, `lua_getfield`, `lua_rawequal`, `lua_pop`, `registerClass`, `on_index`, `on_newindex`, `on_tostring`, `on_gc`, `getObject`, `Class`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

This function is exercised in **5 test case(s)**:

- **`ModuleScriptTest::ReturnStatefulClosure`** (`App.UnitTest/ModuleScriptTest.cpp:63`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(16, Instance::fastDynamicCast&lt;IntValue&gt;(inst16)-&gt;getValue())`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL(16, Instance::fastDynamicCast&lt;IntValue&gt;(inst16)-&gt;getValue());`
- **`ModuleScriptTest::SharedLoadResult`** (`App.UnitTest/ModuleScriptTest.cpp:108`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(14, Instance::fastDynamicCast&lt;IntValue&gt;(inst14)-&gt;getValue())`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL(14, Instance::fastDynamicCast&lt;IntValue&gt;(inst14)-&gt;getValue());`
- **`PropertyChangedSignal::WaitResumesOnRequestedProperty`** (`App.UnitTest/PropertyChangedSignal.cpp:190`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(marker-&gt;getValue(), "")`, `BOOST_CHECK_EQUAL(marker-&gt;getValue(), "woke up")`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL(marker-&gt;getValue(), "");`
- **`Xml::Parse`** (`App.UnitTest/XmlElement.cpp:12`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_REQUIRE(node-&gt;getValue(value))`, `BOOST_REQUIRE(attribute-&gt;getValue(value))`
  - **Callsite Snippet:** `BOOST_REQUIRE(node-&gt;getValue(value));`

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Behavior branches internally via conditional compilation for: Windows (Win32/x64 API).

- **Platform Preprocessor Guards:** `Windows (Win32/x64 API)`

---

### 8. `on_gc`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int on_gc(lua_State *L);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/lua/LuaBridge.h:105` |
| **Subsystem** | `App - Engine Core` |

#### How it Works Internally

Executes on_gc within App - Engine Core. Coordinates interactions with `getObject, Class`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getObject`, `Class`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `on_gc`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 9. `on_tostring`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int on_tostring(lua_State *L);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/lua/LuaBridge.h:110` |
| **Subsystem** | `App - Engine Core` |

#### How it Works Internally

Executes on_tostring within App - Engine Core. Coordinates interactions with `getObject`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `on_tostring`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 10. `on_newindex`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int on_newindex(lua_State *L);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/lua/LuaBridge.h:114` |
| **Subsystem** | `App - Engine Core` |

#### How it Works Internally

Executes on_newindex within App - Engine Core. Coordinates interactions with `lua_checkstring_secure, getObject`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lua_checkstring_secure`, `getObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `on_newindex`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 11. `on_index`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int on_index(lua_State *L);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/lua/LuaBridge.h:120` |
| **Subsystem** | `App - Engine Core` |

#### How it Works Internally

Executes on_index within App - Engine Core. Coordinates interactions with `lua_checkstring_secure, getObject`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lua_checkstring_secure`, `getObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `on_index`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 12. `on_eq`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int on_eq(lua_State *L);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/lua/LuaBridge.h:125` |
| **Subsystem** | `App - Engine Core` |

#### How it Works Internally

Executes on_eq within App - Engine Core. Coordinates interactions with `lua_pushboolean, getObject`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lua_pushboolean`, `getObject`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `on_eq`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 13. `registerClass`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void registerClass(lua_State *L);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/lua/LuaBridge.h:137` |
| **Subsystem** | `App - Engine Core` |

#### How it Works Internally

Executes registerClass within App - Engine Core. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `registerClass`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 14. `registerClassLibrary`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void registerClassLibrary(lua_State *L);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/lua/LuaBridge.h:141` |
| **Subsystem** | `App - Engine Core` |

#### How it Works Internally

Executes registerClassLibrary within App - Engine Core. Coordinates interactions with `lua_pushlightuserdata, newweaktable, lua_rawset`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lua_pushlightuserdata`, `newweaktable`, `lua_rawset`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `registerClassLibrary`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 15. `push`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void push(lua_State *L, boost::shared_ptr<Class> instance);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/lua/LuaBridge.h:148` |
| **Subsystem** | `App - Engine Core` |

#### How it Works Internally

Executes push within App - Engine Core. Coordinates interactions with `lua_pushnil, lua_gettop, lua_pushlightuserdata, lua_rawget`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lua_pushnil`, `lua_gettop`, `lua_pushlightuserdata`, `lua_rawget`, `RBXASSERT`, `lua_isnil`, `get`, `lua_pop`, `pushNewObject`, `lua_pushvalue`, `lua_rawset`, `lua_remove`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

This function is exercised in **5 test case(s)**:

- **`ClusterDeltaBuffer::LengthBitSetOrdering`** (`App.UnitTest/ClusterReplicationTest.cpp:286`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(i, updateBuffer.size())`, `BOOST_CHECK_EQUAL(i, out.x)`
  - **Callsite Snippet:** `updateBuffer.push(Vector3int16(i, 0, 0));`
- **`ClusterDeltaBuffer::BitSetDoesNotStoreDuplicates`** (`App.UnitTest/ClusterReplicationTest.cpp:309`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK(!s.contains(info))`, `BOOST_CHECK_EQUAL(0, s.size())`
  - **Callsite Snippet:** `updateBuffer.push(testLocation);`
- **`ClusterDeltaBuffer::UpdatesGroupedByChunk`** (`App.UnitTest/ClusterReplicationTest.cpp:337`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL((i + 1) * 2, updateBuffer.size())`, `BOOST_REQUIRE(first == Vector3int16(0, 0, 0) || first == Vector3int16(0, 20, 0))`
  - **Callsite Snippet:** `updateBuffer.push(Vector3int16(i, 0, 0));`
- **`ClusterDeltaBuffer::UpdatesContinueByChunk`** (`App.UnitTest/ClusterReplicationTest.cpp:370`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(Vector3int16(40,0,0), read)`, `BOOST_CHECK_EQUAL(Vector3int16(41,0,0), read1)`
  - **Callsite Snippet:** `updateBuffer.push(Vector3int16(40,0,0));`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 16. `getPtr`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
boost::shared_ptr<Class> getPtr(lua_State *L, unsigned int index);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `boost::shared_ptr&lt;Class&gt;` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/lua/LuaBridge.h:186` |
| **Subsystem** | `App - Engine Core` |

#### How it Works Internally

Executes getPtr within App - Engine Core. Coordinates interactions with `lua_isnil, getObject`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lua_isnil`, `getObject`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getPtr`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 17. `getPtr`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool getPtr(lua_State *L, unsigned int index, V& value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/lua/LuaBridge.h:194` |
| **Subsystem** | `App - Engine Core` |

#### How it Works Internally

Executes getPtr within App - Engine Core. Coordinates interactions with `lua_isnil, getValue`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lua_isnil`, `getValue`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getPtr`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 18. `registerClass`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void registerClass(lua_State *L);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/lua/LuaBridge.h:213` |
| **Subsystem** | `App - Engine Core` |

#### How it Works Internally

Executes registerClass within App - Engine Core.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `registerClass`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 19. `registerClassLibrary`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void registerClassLibrary(lua_State *L);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/lua/LuaBridge.h:216` |
| **Subsystem** | `App - Engine Core` |

#### How it Works Internally

Executes registerClassLibrary within App - Engine Core. Coordinates interactions with `lua_pushlightuserdata, lua_newtable, lua_rawset`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lua_pushlightuserdata`, `lua_newtable`, `lua_rawset`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `registerClassLibrary`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 20. `push`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void push(lua_State *L, T item);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/lua/LuaBridge.h:223` |
| **Subsystem** | `App - Engine Core` |

#### How it Works Internally

Executes push within App - Engine Core. Coordinates interactions with `lua_gettop, lua_pushlightuserdata, lua_rawget, RBXASSERT`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lua_gettop`, `lua_pushlightuserdata`, `lua_rawget`, `RBXASSERT`, `lua_isnil`, `lua_pop`, `pushNewObject`, `lua_pushvalue`, `lua_rawset`, `lua_remove`.

#### How it is Used in Tests

This function is exercised in **5 test case(s)**:

- **`ClusterDeltaBuffer::LengthBitSetOrdering`** (`App.UnitTest/ClusterReplicationTest.cpp:286`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(i, updateBuffer.size())`, `BOOST_CHECK_EQUAL(i, out.x)`
  - **Callsite Snippet:** `updateBuffer.push(Vector3int16(i, 0, 0));`
- **`ClusterDeltaBuffer::BitSetDoesNotStoreDuplicates`** (`App.UnitTest/ClusterReplicationTest.cpp:309`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK(!s.contains(info))`, `BOOST_CHECK_EQUAL(0, s.size())`
  - **Callsite Snippet:** `updateBuffer.push(testLocation);`
- **`ClusterDeltaBuffer::UpdatesGroupedByChunk`** (`App.UnitTest/ClusterReplicationTest.cpp:337`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL((i + 1) * 2, updateBuffer.size())`, `BOOST_REQUIRE(first == Vector3int16(0, 0, 0) || first == Vector3int16(0, 20, 0))`
  - **Callsite Snippet:** `updateBuffer.push(Vector3int16(i, 0, 0));`
- **`ClusterDeltaBuffer::UpdatesContinueByChunk`** (`App.UnitTest/ClusterReplicationTest.cpp:370`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(Vector3int16(40,0,0), read)`, `BOOST_CHECK_EQUAL(Vector3int16(41,0,0), read1)`
  - **Callsite Snippet:** `updateBuffer.push(Vector3int16(40,0,0));`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 21. `lua_pushstring`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void lua_pushstring(lua_State* thread, const std::string& s);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `inline` |
| **Source Location** | `App/include/lua/lua.hpp:14` |
| **Subsystem** | `App - Engine Core` |

#### How it Works Internally

Executes lua_pushstring within App - Engine Core. Coordinates interactions with `lua_pushlstring, c_str, size`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lua_pushlstring`, `c_str`, `size`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `lua_pushstring`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

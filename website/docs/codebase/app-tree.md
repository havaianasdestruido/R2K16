---
sidebar_position: 4
title: App - Instance Tree
description: Instance tree, RootInstance, ServiceProvider, and reflection bindings.
---

# App - Instance Tree

Instance tree, RootInstance, ServiceProvider, and reflection bindings.


## FAQ

### How can I trace a hierarchy change?

Inspect Instance parenting, callers and notifications together. A function signature alone cannot establish all lifecycle effects.

### How can I investigate this in the repository?

From the repository root, search the relevant tracked files for a starting point (results are leads, not proof of behavior):

```bash
git grep -n -i -F -- 'setParent' -- App/v8tree
```

Read the surrounding implementation and callers, and check relevant tests before making changes. A search may return no matches when terminology or tracked files change.

## Subsystem Metrics

- **Total Documented Functions:** `208`
- **Functions Exercised in Tests:** `41`
- **Platform-Divergent Implementations:** `21`
- **Component Source Files:** `9`

## Source Files

<details>
<summary>View all 9 source files in this subsystem</summary>

| Source File | Path |
| :--- | :--- |
| `Instance.h` | `App/include/v8tree/Instance.h` |
| `Property.h` | `App/include/v8tree/Property.h` |
| `Service.h` | `App/include/v8tree/Service.h` |
| `Verb.h` | `App/include/v8tree/Verb.h` |
| `EnumProperty.cpp` | `App/v8tree/EnumProperty.cpp` |
| `Instance.cpp` | `App/v8tree/Instance.cpp` |
| `Property.cpp` | `App/v8tree/Property.cpp` |
| `Service.cpp` | `App/v8tree/Service.cpp` |
| `Verb.cpp` | `App/v8tree/Verb.cpp` |

</details>

---

## Function Reference

### 1. `DescribedCreatable`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
protected:
	inline DescribedCreatable();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `protected:
	inline` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:37` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Declaration or inline method for DescribedCreatable.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `DescribedCreatable`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 2. `DescribedNonCreatable`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
protected:
	inline DescribedNonCreatable();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `protected:
	inline` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:55` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Declaration or inline method for DescribedNonCreatable.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `DescribedNonCreatable`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 3. `~OnDemandInstance`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
virtual ~OnDemandInstance();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `virtual` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:145` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Declaration or inline method for ~OnDemandInstance.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `~OnDemandInstance`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 4. `lockParent`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void lockParent();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:187` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes lockParent within App - Instance Tree.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

This function is exercised in **1 test case(s)**:

- **`Instance::ReparentingLock`** (`App.UnitTest/Instance.cpp:213`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK(!parent-&gt;getIsParentLocked())`, `BOOST_CHECK(parent-&gt;getIsParentLocked())`
  - **Callsite Snippet:** `child-&gt;unlockParent();`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 5. `unlockParent`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void unlockParent();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:189` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes unlockParent within App - Instance Tree.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

This function is exercised in **2 test case(s)**:

- **`Instance::ReparentingLock`** (`App.UnitTest/Instance.cpp:213`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK(!parent-&gt;getIsParentLocked())`, `BOOST_CHECK(parent-&gt;getIsParentLocked())`
  - **Callsite Snippet:** `child-&gt;unlockParent();`
- **`SettingsTest::AddingSelectionWithPartChildDoesNukeSettings`** (`App.UnitTest/SettingsTest.cpp:234`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK(errored)`
  - **Callsite Snippet:** `sel-&gt;unlockParent();`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 6. `getIsParentLocked`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool getIsParentLocked() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8tree/Instance.h:190` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getIsParentLocked within App - Instance Tree.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

This function is exercised in **1 test case(s)**:

- **`Instance::ReparentingLock`** (`App.UnitTest/Instance.cpp:213`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(!parent-&gt;getIsParentLocked())`, `BOOST_CHECK(parent-&gt;getIsParentLocked())`, `BOOST_CHECK(child-&gt;getIsParentLocked())`, `BOOST_CHECK(!child-&gt;getIsParentLocked())`
  - **Callsite Snippet:** `BOOST_CHECK(!parent-&gt;getIsParentLocked());`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 7. `getIsArchivable`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool getIsArchivable() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8tree/Instance.h:195` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getIsArchivable within App - Instance Tree.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getIsArchivable`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 8. `~ICombinedSignalData`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
public:
		virtual ~ICombinedSignalData();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `public:
		virtual` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:228` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Declaration or inline method for ~ICombinedSignalData.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `~ICombinedSignalData`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 9. `child`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
: child(child);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `:` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:236` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Declaration or inline method for child.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `child`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 10. `child`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
: child(child);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `:` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:245` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Declaration or inline method for child.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `child`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 11. `OutfitChangedSignalData`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
public: OutfitChangedSignalData();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `public:` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:263` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Declaration or inline method for OutfitChangedSignalData.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `OutfitChangedSignalData`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 12. `HumanoidChangedSignalData`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
public: HumanoidChangedSignalData();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `public:` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:292` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Declaration or inline method for HumanoidChangedSignalData.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `HumanoidChangedSignalData`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 13. `childAddedSignal`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void childAddedSignal(shared_ptr<Instance>& inst);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:298` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes childAddedSignal within App - Instance Tree. Coordinates interactions with `onDemandRead, onDemandWrite`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `onDemandRead`, `onDemandWrite`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `childAddedSignal`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 14. `childRemovedSignal`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void childRemovedSignal(shared_ptr<Instance>& inst);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:302` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes childRemovedSignal within App - Instance Tree. Coordinates interactions with `onDemandRead, onDemandWrite`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `onDemandRead`, `onDemandWrite`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `childRemovedSignal`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 15. `descendantAddedSignal`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void descendantAddedSignal(shared_ptr<Instance>& inst);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:305` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes descendantAddedSignal within App - Instance Tree. Coordinates interactions with `onDemandRead, onDemandWrite`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `onDemandRead`, `onDemandWrite`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `descendantAddedSignal`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 16. `descendantRemovingSignal`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void descendantRemovingSignal(const shared_ptr<Instance>& inst);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:308` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes descendantRemovingSignal within App - Instance Tree. Coordinates interactions with `onDemandRead, onDemandWrite`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `onDemandRead`, `onDemandWrite`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `descendantRemovingSignal`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 17. `getClassNameStr`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string& getClassNameStr() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string&` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8tree/Instance.h:327` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getClassNameStr within App - Instance Tree. Coordinates interactions with `getClassName, toString`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getClassName`, `toString`.

#### How it is Used in Tests

This function is exercised in **1 test case(s)**:

- **`PostEffectTest::BlurEffectDefaults`** (`App.UnitTest/PostEffectTest.cpp:13`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(effect-&gt;getClassNameStr(), "BlurEffect")`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL(effect-&gt;getClassNameStr(), "BlurEffect");`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 18. `getReadableDebugId`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string getReadableDebugId(int scopeLength) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8tree/Instance.h:329` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getReadableDebugId within App - Instance Tree. Coordinates interactions with `getGuid, readableString`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getGuid`, `readableString`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getReadableDebugId`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 19. `getReadableDebugId`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string getReadableDebugId() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8tree/Instance.h:331` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getReadableDebugId within App - Instance Tree. Coordinates interactions with `getGuid, readableString`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getGuid`, `readableString`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getReadableDebugId`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 20. `getReadableDebugId`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string getReadableDebugId(int scopeLength);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:332` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getReadableDebugId within App - Instance Tree. Coordinates interactions with `getGuid, readableString`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getGuid`, `readableString`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getReadableDebugId`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 21. `getParent`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Instance* getParent();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Instance*` |
| **Modifiers** | `inline` |
| **Source Location** | `App/include/v8tree/Instance.h:339` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getParent within App - Instance Tree.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

This function is exercised in **8 test case(s)**:

- **`CustomEvents::CreatingStateSanityCheck`** (`App.UnitTest/CustomEvents.cpp:78`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL((Instance *)NULL, evt-&gt;getParent())`, `BOOST_REQUIRE_EQUAL((Instance *)NULL, evt-&gt;getParent())`
  - **Callsite Snippet:** `BOOST_REQUIRE_EQUAL((Instance *)NULL, evt-&gt;getParent());`
- **`Instance::Parenting`** (`App.UnitTest/Instance.cpp:193`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(checkAncestor-&gt;getParent() != NULL)`
  - **Callsite Snippet:** `BOOST_CHECK(checkAncestor-&gt;getParent() != NULL);`
- **`Instance::ReparentingLock`** (`App.UnitTest/Instance.cpp:213`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(child-&gt;getParent() == parent.get())`
  - **Callsite Snippet:** `BOOST_CHECK(child-&gt;getParent() == parent.get());`
- **`Instance::WaitForChildOutsideOfDataModel`** (`App.UnitTest/Instance.cpp:525`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_REQUIRE(part-&gt;getParent() == NULL)`
  - **Callsite Snippet:** `BOOST_REQUIRE(part-&gt;getParent() == NULL);`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 22. `getParent`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Instance* getParent() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Instance*` |
| **Modifiers** | `inline const const` |
| **Source Location** | `App/include/v8tree/Instance.h:341` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getParent within App - Instance Tree.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

This function is exercised in **8 test case(s)**:

- **`CustomEvents::CreatingStateSanityCheck`** (`App.UnitTest/CustomEvents.cpp:78`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL((Instance *)NULL, evt-&gt;getParent())`, `BOOST_REQUIRE_EQUAL((Instance *)NULL, evt-&gt;getParent())`
  - **Callsite Snippet:** `BOOST_REQUIRE_EQUAL((Instance *)NULL, evt-&gt;getParent());`
- **`Instance::Parenting`** (`App.UnitTest/Instance.cpp:193`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(checkAncestor-&gt;getParent() != NULL)`
  - **Callsite Snippet:** `BOOST_CHECK(checkAncestor-&gt;getParent() != NULL);`
- **`Instance::ReparentingLock`** (`App.UnitTest/Instance.cpp:213`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(child-&gt;getParent() == parent.get())`
  - **Callsite Snippet:** `BOOST_CHECK(child-&gt;getParent() == parent.get());`
- **`Instance::WaitForChildOutsideOfDataModel`** (`App.UnitTest/Instance.cpp:525`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_REQUIRE(part-&gt;getParent() == NULL)`
  - **Callsite Snippet:** `BOOST_REQUIRE(part-&gt;getParent() == NULL);`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 23. `getParentDangerous`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Instance* getParentDangerous() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Instance*` |
| **Modifiers** | `inline const` |
| **Source Location** | `App/include/v8tree/Instance.h:343` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getParentDangerous within App - Instance Tree.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getParentDangerous`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 24. `getRootAncestor`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Instance* getRootAncestor();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Instance*` |
| **Modifiers** | `inline` |
| **Source Location** | `App/include/v8tree/Instance.h:346` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getRootAncestor within App - Instance Tree.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getRootAncestor`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 25. `getRootAncestor`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Instance* getRootAncestor() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Instance*` |
| **Modifiers** | `inline const const` |
| **Source Location** | `App/include/v8tree/Instance.h:347` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getRootAncestor within App - Instance Tree.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getRootAncestor`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 26. `getRootAncestor`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Instance* getRootAncestor(Instance* instance);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Instance*` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/v8tree/Instance.h:348` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getRootAncestor within App - Instance Tree.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getRootAncestor`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 27. `getRootAncestor`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Instance* getRootAncestor(const Instance* instance) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Instance*` |
| **Modifiers** | `static const` |
| **Source Location** | `App/include/v8tree/Instance.h:350` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getRootAncestor within App - Instance Tree.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getRootAncestor`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 28. `getRobloxLocked`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool getRobloxLocked() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8tree/Instance.h:351` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getRobloxLocked within App - Instance Tree.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getRobloxLocked`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 29. `setParent`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void setParent(Instance* instance);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:356` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes setParent within App - Instance Tree. Coordinates interactions with `setParentInternal`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `setParentInternal`.

#### How it is Used in Tests

This function is exercised in **88 test case(s)**:

- **`AutowedgeTest::ExplosionBelowTerrainWorks`** (`App.UnitTest/AutowedgeTest.cpp:247`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(fixture.cluster-&gt;getVoxelGrid()-&gt;getCellMaterial(Vector3int16(kOffset, 0, kOffset)), CELL_MATERIAL_Grass)`, `BOOST_REQUIRE(check)`
  - **Callsite Snippet:** `exp-&gt;setParent(fixture.workspace);`
- **`AutowedgeTest::ExplosionAboveTerrainWorks`** (`App.UnitTest/AutowedgeTest.cpp:270`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(fixture.cluster-&gt;getVoxelGrid()-&gt;getCellMaterial(Vector3int16(kOffset, 62, kOffset)), CELL_MATERIAL_Grass)`, `BOOST_REQUIRE(check)`
  - **Callsite Snippet:** `exp-&gt;setParent(fixture.workspace);`
- **`CustomEvents::SettingParentToNullDoesBreakConnection`** (`App.UnitTest/CustomEvents.cpp:239`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(1, callCounter-&gt;calls)`, `BOOST_REQUIRE_EQUAL(.1f, callCounter-&gt;lastValue)`
  - **Callsite Snippet:** `partParent-&gt;setParent(fixture-&gt;getWorkspace());`
- **`CustomEvents::BreakingConnectionSetsReceiverToZero`** (`App.UnitTest/CustomEvents.cpp:301`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(1, callCounter-&gt;calls)`, `BOOST_REQUIRE_EQUAL(.1f, callCounter-&gt;lastValue)`
  - **Callsite Snippet:** `partParent-&gt;setParent(fixture-&gt;getWorkspace());`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 30. `setLockedParent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool setLockedParent(Instance* instance);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:358` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes setLockedParent within App - Instance Tree. Coordinates interactions with `setParentInternal`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `setParentInternal`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setLockedParent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 31. `setParent2`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void setParent2(shared_ptr<Instance> instance);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:359` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes setParent2 within App - Instance Tree. Coordinates interactions with `setParent, get`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `setParent`, `get`.

#### How it is Used in Tests

This function is exercised in **1 test case(s)**:

- **`Instance::Parenting`** (`App.UnitTest/Instance.cpp:193`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_THROW(instance-&gt;setParent2(dm.dataModel), std::exception)`, `BOOST_CHECK_THROW(checkAncestor-&gt;setParent2(dm.dataModel), std::exception)`, `BOOST_CHECK_THROW(checkAncestor-&gt;setParent2(instance), std::exception)`
  - **Callsite Snippet:** `checkAncestor-&gt;setParent2(instance);`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 32. `getName`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
std::string& getName() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string&` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8tree/Instance.h:369` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getName within App - Instance Tree. Coordinates interactions with `get`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `get`.

#### How it is Used in Tests

This function is exercised in **19 test case(s)**:

- **`Instance::WaitForChildReturnsImmediatelyIfChildPresent`** (`App.UnitTest/Instance.cpp:264`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(part-&gt;getName(), "Renamed")`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL(part-&gt;getName(), "Renamed");`
- **`Instance::WaitForSameChildAfterInitialWaitForChild`** (`App.UnitTest/Instance.cpp:289`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(part-&gt;getName(), "Renamed")`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL(part-&gt;getName(), "Renamed");`
- **`Instance::TwoScriptsWaitingForSameChildRenameOnResume`** (`App.UnitTest/Instance.cpp:356`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL("PartBx", part-&gt;getName())`, `BOOST_CHECK_EQUAL("PartA", part2-&gt;getName())`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL("PartBx", part-&gt;getName());`
- **`Instance::WaitForDifferentChildAfterInitialWaitForChild`** (`App.UnitTest/Instance.cpp:478`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(part-&gt;getName(), "Phase1")`, `BOOST_CHECK_EQUAL(part-&gt;getName(), "Phase2")`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL(part-&gt;getName(), "Phase1");`

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `RobloxStudio/RobloxRibbonMainWindow.cpp`.

- **Alternative Implementation Files:** `RobloxStudio/RobloxRibbonMainWindow.cpp`

---

### 33. `getFullNameForReflection`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string getFullNameForReflection();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:374` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getFullNameForReflection within App - Instance Tree. Coordinates interactions with `getFullName`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getFullName`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getFullNameForReflection`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 34. `isAncestorOf`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool isAncestorOf(const Instance* descendant) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8tree/Instance.h:375` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes isAncestorOf within App - Instance Tree. Coordinates interactions with `getParent`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getParent`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isAncestorOf`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 35. `isAncestorOf2`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool isAncestorOf2(shared_ptr<Instance> descendant);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:385` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes isAncestorOf2 within App - Instance Tree. Coordinates interactions with `isAncestorOf, get`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `isAncestorOf`, `get`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isAncestorOf2`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 36. `isDescendantOf2`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool isDescendantOf2(shared_ptr<Instance> ancestor);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:387` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes isDescendantOf2 within App - Instance Tree. Coordinates interactions with `isDescendantOf, get`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `isDescendantOf`, `get`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isDescendantOf2`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 37. `isDescendantOf`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool isDescendantOf(const Instance* ancestor) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8tree/Instance.h:390` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

isDescendantOf will return true if parent==NULL (consistent with the fact that a top-level Instance has parent==NULL)

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getParent`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isDescendantOf`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 38. `findFirstAncestorOfType`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Type* findFirstAncestorOfType();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Type*` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:400` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes findFirstAncestorOfType within App - Instance Tree. Coordinates interactions with `getParent`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getParent`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `findFirstAncestorOfType`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 39. `numChildren`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
size_t numChildren() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `size_t` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8tree/Instance.h:412` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes numChildren within App - Instance Tree. Coordinates interactions with `size`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `size`.

#### How it is Used in Tests

This function is exercised in **2 test case(s)**:

- **`ChatTests::ReportAbuse`** (`App.UnitTest/ChatTests.cpp:353`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK(event-&gt;Wait(RBX::Time::Interval::from_seconds(10)))`
  - **Callsite Snippet:** `if (players-&gt;numChildren() == 1)`
- **`SelectionTest::LayerCollectorResetOnSpawn`** (`App.UnitTest/SelectionTest.cpp:64`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE(gui)`, `BOOST_CHECK(persistent-&gt;getResetOnSpawn())`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL(gui-&gt;numChildren(), 2u);`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 40. `computeStringCost`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int computeStringCost(const std::string& value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/v8tree/Instance.h:417` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes computeStringCost within App - Instance Tree. Coordinates interactions with `length`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `length`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `computeStringCost`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 41. `getChild`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Instance* getChild(size_t index);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Instance*` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:421` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getChild within App - Instance Tree. Coordinates interactions with `return, get`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`, `get`.

#### How it is Used in Tests

This function is exercised in **3 test case(s)**:

- **`ChatTests::ReportAbuse`** (`App.UnitTest/ChatTests.cpp:353`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK(event-&gt;Wait(RBX::Time::Interval::from_seconds(10)))`
  - **Callsite Snippet:** `Player* player = boost::polymorphic_downcast&lt;Player*&gt;(players-&gt;getChild(0));`
- **`Instance::SetParentNull`** (`App.UnitTest/Instance.cpp:251`)
  - **Usage Pattern:** `Direct Call`
  - **Callsite Snippet:** `RBX::Instance* child = parent-&gt;getChild(0);`
- **`NetworkSecurity::SecurePlayerReplication`** (`App.UnitTest/NetworkSecurity.cpp:186`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE(player)`, `BOOST_REQUIRE(players)`
  - **Callsite Snippet:** `RBX::Network::Player* player = Instance::fastDynamicCast&lt;RBX::Network::Player&gt;(players-&gt;getChild(0));`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 42. `getChild`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Instance* getChild(size_t index) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Instance*` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8tree/Instance.h:424` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getChild within App - Instance Tree. Coordinates interactions with `return, get`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `return`, `get`.

#### How it is Used in Tests

This function is exercised in **3 test case(s)**:

- **`ChatTests::ReportAbuse`** (`App.UnitTest/ChatTests.cpp:353`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK(event-&gt;Wait(RBX::Time::Interval::from_seconds(10)))`
  - **Callsite Snippet:** `Player* player = boost::polymorphic_downcast&lt;Player*&gt;(players-&gt;getChild(0));`
- **`Instance::SetParentNull`** (`App.UnitTest/Instance.cpp:251`)
  - **Usage Pattern:** `Direct Call`
  - **Callsite Snippet:** `RBX::Instance* child = parent-&gt;getChild(0);`
- **`NetworkSecurity::SecurePlayerReplication`** (`App.UnitTest/NetworkSecurity.cpp:186`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE(player)`, `BOOST_REQUIRE(players)`
  - **Callsite Snippet:** `RBX::Network::Player* player = Instance::fastDynamicCast&lt;RBX::Network::Player&gt;(players-&gt;getChild(0));`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 43. `findFirstChildByName`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Instance* findFirstChildByName(const std::string& findName);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Instance*` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:435` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes findFirstChildByName within App - Instance Tree. Coordinates interactions with `findConstFirstChildByName`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `findConstFirstChildByName`.

#### How it is Used in Tests

This function is exercised in **45 test case(s)**:

- **`Instance::TwoScriptsWaitingForSameChild`** (`App.UnitTest/Instance.cpp:314`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(dm-&gt;getWorkspace()-&gt;findFirstChildByName("Alice") != NULL)`, `BOOST_CHECK(dm-&gt;getWorkspace()-&gt;findFirstChildByName("Bob") != NULL)`
  - **Callsite Snippet:** `BOOST_CHECK(dm-&gt;getWorkspace()-&gt;findFirstChildByName("Alice") != NULL);`
- **`Instance::TwoScriptsWaitingForDifferentChildren`** (`App.UnitTest/Instance.cpp:414`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(dm-&gt;getWorkspace()-&gt;findFirstChildByName("Alice") == NULL)`, `BOOST_CHECK(dm-&gt;getWorkspace()-&gt;findFirstChildByName("AliceX") != NULL)`, `BOOST_CHECK(dm-&gt;getWorkspace()-&gt;findFirstChildByName("Bob") == NULL)`, `BOOST_CHECK(dm-&gt;getWorkspace()-&gt;findFirstChildByName("BobX") == NULL)`, `BOOST_CHECK(dm-&gt;getWorkspace()-&gt;findFirstChildByName("Alice") == NULL)`
  - **Callsite Snippet:** `BOOST_CHECK(dm-&gt;getWorkspace()-&gt;findFirstChildByName("Alice") == NULL);`
- **`ModuleScriptTest::ModuleScriptsDoNotRunOnTheirOwn`** (`App.UnitTest/ModuleScriptTest.cpp:13`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(dm-&gt;getWorkspace()-&gt;findFirstChildByName("BUG") == NULL)`
  - **Callsite Snippet:** `BOOST_CHECK(dm-&gt;getWorkspace()-&gt;findFirstChildByName("BUG") == NULL);`
- **`ModuleScriptTest::ScopeOfScriptInReturnedFunctions`** (`App.UnitTest/ModuleScriptTest.cpp:35`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(dm-&gt;getWorkspace()-&gt;findFirstChildByName("Module2") != NULL)`, `BOOST_CHECK(dm-&gt;getWorkspace()-&gt;findFirstChildByName("Caller2") == NULL)`
  - **Callsite Snippet:** `BOOST_CHECK(dm-&gt;getWorkspace()-&gt;findFirstChildByName("Module2") != NULL);`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 44. `findFirstChildByNameDangerous`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Instance* findFirstChildByNameDangerous(const std::string& findName) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Instance*` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8tree/Instance.h:438` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes findFirstChildByNameDangerous within App - Instance Tree. Coordinates interactions with `findConstFirstChildByName`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `findConstFirstChildByName`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `findFirstChildByNameDangerous`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 45. `findFirstChildByName2`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
shared_ptr<Instance> findFirstChildByName2(std::string findName, bool recursive);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `shared_ptr&lt;Instance&gt;` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:446` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Used for Reflection:

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `shared_from`, `findFirstChildByNameRecursive`, `findFirstChildByName`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `findFirstChildByName2`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 46. `queryTypedChild`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Type* queryTypedChild(int index);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Type*` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:451` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

queryTypedChild

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `get`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `queryTypedChild`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 47. `queryTypedChild`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Type* queryTypedChild(int index) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Type*` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8tree/Instance.h:455` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes queryTypedChild within App - Instance Tree. Coordinates interactions with `get`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `get`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `queryTypedChild`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 48. `getTypedChild`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Type* getTypedChild(int index);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Type*` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:461` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

getTypedChild

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `get`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getTypedChild`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 49. `getTypedChild`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Type* getTypedChild(int index) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Type*` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8tree/Instance.h:465` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getTypedChild within App - Instance Tree. Coordinates interactions with `get`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `get`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getTypedChild`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 50. `queryTypedParent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Type* queryTypedParent();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Type*` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:472` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

queryTypedParent

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `queryTypedParent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 51. `queryTypedParent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Type* queryTypedParent() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Type*` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8tree/Instance.h:476` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes queryTypedParent within App - Instance Tree.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `queryTypedParent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 52. `getTypedParent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Type* getTypedParent();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Type*` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:483` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

getTypedParent

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getTypedParent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 53. `getTypedParent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Type* getTypedParent() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Type*` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8tree/Instance.h:487` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getTypedParent within App - Instance Tree.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getTypedParent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 54. `getTypedRoot`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Type* getTypedRoot();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Type*` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:494` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

getTypedRoot

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `RBXASSERT`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getTypedRoot`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 55. `getTypedRoot`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Type* getTypedRoot() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Type*` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8tree/Instance.h:504` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getTypedRoot within App - Instance Tree. Coordinates interactions with `RBXASSERT`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `RBXASSERT`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getTypedRoot`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 56. `getChildren`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
copy_on_write_ptr<Instances>& getChildren() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `copy_on_write_ptr&lt;Instances&gt;&` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8tree/Instance.h:514` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes getChildren within App - Instance Tree.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

This function is exercised in **2 test case(s)**:

- **`SettingsTest::AddingPartUnderSelectionDoesNukeSettings`** (`App.UnitTest/SettingsTest.cpp:211`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL((RBX::Instances*)NULL, sel-&gt;getChildren().read().get())`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL((RBX::Instances*)NULL, sel-&gt;getChildren().read().get());`
- **`WebSerializer::TestWebSerializerInstance`** (`App.UnitTest/WebSerializerTest.cpp:115`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(newValue.get&lt;shared_ptr&lt;Instance&gt; &gt;()-&gt;getChildren()-&gt;size() == 3)`
  - **Callsite Snippet:** `BOOST_CHECK(newValue.get&lt;shared_ptr&lt;Instance&gt; &gt;()-&gt;getChildren()-&gt;size() == 3);`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 57. `getChildren2`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
shared_ptr<const Instances> getChildren2();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `shared_ptr&lt;const Instances&gt;` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8tree/Instance.h:519` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Used for reflection. Note that it might return NULL (or an empty container) TODO - this is dangerous?  getting const children?

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `read`.

#### How it is Used in Tests

This function is exercised in **1 test case(s)**:

- **`CustomEvents::CloneEventAndReceiver`** (`App.UnitTest/CustomEvents.cpp:491`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(2, children-&gt;size())`, `BOOST_REQUIRE(clonedEvent)`
  - **Callsite Snippet:** `shared_ptr&lt;const Instances&gt; children(clonedParent-&gt;getChildren2());`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 58. `visitChildren`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void visitChildren(const Func& func) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `inline const` |
| **Source Location** | `App/include/v8tree/Instance.h:520` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes visitChildren within App - Instance Tree. Coordinates interactions with `read, end, begin`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `read`, `end`, `begin`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

This function is exercised in **1 test case(s)**:

- **`LuaDebugger::FlatDataSerialization`** (`App.UnitTest/LuaDebugger.cpp:139`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK(workspace != NULL)`, `BOOST_CHECK(debuggerManager.getDataModel() != NULL)`
  - **Callsite Snippet:** `workspace-&gt;visitChildren(boost::bind(&addDebuggerData, _1, shared_from(&debuggerManager), debuggerData));`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 59. `countDescendantsOfType`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int countDescendantsOfType() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `inline const` |
| **Source Location** | `App/include/v8tree/Instance.h:533` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes countDescendantsOfType within App - Instance Tree. Coordinates interactions with `read, end, begin`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `read`, `end`, `begin`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `countDescendantsOfType`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 60. `visitDescendants`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void visitDescendants(const Func& func) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `inline const` |
| **Source Location** | `App/include/v8tree/Instance.h:548` |
| **Subsystem** | `App - Instance Tree` |

#### How it Works Internally

Executes visitDescendants within App - Instance Tree. Coordinates interactions with `read, end, begin`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `read`, `end`, `begin`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

This function is exercised in **1 test case(s)**:

- **`LuaDebugger::NestedDataSerialization`** (`App.UnitTest/LuaDebugger.cpp:211`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK(workspace != NULL)`, `BOOST_CHECK(debuggerManager.getDataModel() != NULL)`
  - **Callsite Snippet:** `workspace-&gt;visitDescendants(boost::bind(&addDebuggerData, _1, shared_from(&debuggerManager), debuggerData));`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---


:::tip Additional Functions
There are **148 additional internal and inline functions** in this subsystem. All functions are indexed and cross-referenced in the **[Complete Function Catalog](./function-catalog.md)**.
:::

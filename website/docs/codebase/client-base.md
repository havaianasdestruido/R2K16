---
sidebar_position: 18
title: Client Base Configuration
description: MachineConfiguration, ReflectionMetadata, and RenderSettingsItem.
---

# Client Base Configuration

MachineConfiguration, ReflectionMetadata, and RenderSettingsItem.


## FAQ

### What is the role of ClientBase?

It contains client-facing configuration and settings components; trace the application that consumes them before assuming a setting applies to every client.

### How can I investigate this in the repository?

From the repository root, search the relevant tracked files for a starting point (results are leads, not proof of behavior):

```bash
git grep -n -i -F -- 'Settings' -- ClientBase
```

Read the surrounding implementation and callers, and check relevant tests before making changes. A search may return no matches when terminology or tracked files change.

## Subsystem Metrics

- **Total Documented Functions:** `77`
- **Functions Exercised in Tests:** `11`
- **Platform-Divergent Implementations:** `11`
- **Component Source Files:** `4`

## Source Files

<details>
<summary>View all 4 source files in this subsystem</summary>

| Source File | Path |
| :--- | :--- |
| `MachineConfiguration.cpp` | `ClientBase/MachineConfiguration.cpp` |
| `ReflectionMetadata.cpp` | `ClientBase/ReflectionMetadata.cpp` |
| `ReflectionMetadata.h` | `ClientBase/ReflectionMetadata.h` |
| `RenderSettingsItem.cpp` | `ClientBase/RenderSettingsItem.cpp` |

</details>

---

## Function Reference

### 1. `appendProperty`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void appendProperty(const char* category, std::stringstream& data, const RBX::Reflection::Property& prop);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `ClientBase/MachineConfiguration.cpp:16` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes appendProperty within Client Base Configuration. Coordinates interactions with `getDescriptor, getName, c_str, getStringValue`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getDescriptor`, `getName`, `c_str`, `getStringValue`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `appendProperty`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 2. `HandleAsyncHttp`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void HandleAsyncHttp(std::string *response, std::exception *exception);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `ClientBase/MachineConfiguration.cpp:27` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes HandleAsyncHttp within Client Base Configuration.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `HandleAsyncHttp`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 3. `postMachineConfiguration`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void postMachineConfiguration(const char* baseURL, int lastGfxMode);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/MachineConfiguration.cpp:35` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes postMachineConfiguration within Client Base Configuration. Coordinates interactions with `BuildGenericGameUrl, trim_trailing_slashes, string, displayResolution`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Exception handling block (try/catch recovery).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `BuildGenericGameUrl`, `trim_trailing_slashes`, `string`, `displayResolution`, `fullscreenResolution`, `singleton`, `setVertexShaderModel`, `setPixelShaderModel`, `sscanf_s`, `resolution`, `c_str`, `getFullscreenSize`.
- **External Library Dependencies:** `Boost C++ Libraries`, `G3D Graphics and Math Engine`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `postMachineConfiguration`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Behavior branches internally via conditional compilation for: Windows (Win32/x64 API).

- **Platform Preprocessor Guards:** `Windows (Win32/x64 API)`

---

### 4. `Metadata::Reflection::registerClasses`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Metadata::Reflection::registerClasses();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:58` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes registerClasses within Client Base Configuration. Coordinates interactions with `classDescriptor, safe_static_do_get_singleton, getResourcesFolder, toUtf8`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Multi-case state dispatch, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr); Unique RAII pointer lifetime control (boost::scoped_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT); Defensive null-pointer validation guard.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `classDescriptor`, `safe_static_do_get_singleton`, `getResourcesFolder`, `toUtf8`, `utf8_decode`, `string`, `constData`, `size`, `load`, `GetModuleFileNameW`, `exePath`, `remove_filename`.
- **External Library Dependencies:** `Boost C++ Libraries`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `registerClasses`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 5. `Metadata::Reflection::safe_static_do_get_singleton`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
shared_ptr<Metadata::Reflection> Metadata::Reflection::safe_static_do_get_singleton();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `shared_ptr&lt;Metadata::Reflection&gt;` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:64` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes safe_static_do_get_singleton within Client Base Configuration. Coordinates interactions with `getResourcesFolder, toUtf8, utf8_decode, string`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getResourcesFolder`, `toUtf8`, `utf8_decode`, `string`, `constData`, `size`, `load`, `GetModuleFileNameW`, `exePath`, `remove_filename`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `safe_static_do_get_singleton`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 6. `Metadata::Reflection::save`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Metadata::Reflection::save(const boost::filesystem::path& filePath);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:95` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

TODO: Merge with GlobalSettings and make part of Serializer class????

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Unique RAII pointer lifetime control (boost::scoped_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `root`, `newRootElement`, `writeChildren`, `get`, `stream`, `native`, `c_str`, `machine`, `serialize`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `save`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 7. `Metadata::Reflection::load`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Metadata::Reflection::load(const boost::filesystem::path& filePath);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:105` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

TODO: Merge with GlobalSettings and make part of Serializer class????

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `empty`, `FASTLOGS`, `string`, `c_str`, `stream`, `native`, `machine`, `rdbuf`, `root`, `parse`, `readChildren`, `get`.

#### How it is Used in Tests

This function is exercised in **1 test case(s)**:

- **`PathfindingTest::PathfindingStress`** (`App.UnitTest/PathfindingTest.cpp:48`)
  - **Usage Pattern:** `Direct Call`
  - **Callsite Snippet:** `serializer.load(stream,dataModel.get());`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 8. `Metadata::Reflection::get`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
Metadata::Class* Metadata::Reflection::get(const ClassDescriptor& descriptor, bool findBestMatch) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Metadata::Class*` |
| **Modifiers** | `const` |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:128` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes get within Client Base Configuration.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

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

**Divergence Analysis:** Alternative platform-specific implementations exist in: `RobloxStudio/RobloxMainWindow.cpp`, `XboxClient/UserTranslator.cpp`.

- **Alternative Implementation Files:** `RobloxStudio/RobloxMainWindow.cpp`, `XboxClient/UserTranslator.cpp`

---

### 9. `Metadata::Classes::get`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
Metadata::Class* Metadata::Classes::get(const ClassDescriptor& descriptor, bool findBestMatch);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Metadata::Class*` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:133` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes get within Client Base Configuration. Coordinates interactions with `findFirstChildByName, toString, getBase`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Defensive null-pointer validation guard.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `findFirstChildByName`, `toString`, `getBase`.
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

**Divergence Analysis:** Alternative platform-specific implementations exist in: `RobloxStudio/RobloxMainWindow.cpp`, `XboxClient/UserTranslator.cpp`.

- **Alternative Implementation Files:** `RobloxStudio/RobloxMainWindow.cpp`, `XboxClient/UserTranslator.cpp`

---

### 10. `Metadata::Reflection::get`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
Metadata::Member* Metadata::Reflection::get(const PropertyDescriptor& descriptor) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Metadata::Member*` |
| **Modifiers** | `const` |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:145` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes get within Client Base Configuration. Coordinates interactions with `findFirstChildByNameDangerous, toString`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `findFirstChildByNameDangerous`, `toString`.
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

**Divergence Analysis:** Alternative platform-specific implementations exist in: `RobloxStudio/RobloxMainWindow.cpp`, `XboxClient/UserTranslator.cpp`.

- **Alternative Implementation Files:** `RobloxStudio/RobloxMainWindow.cpp`, `XboxClient/UserTranslator.cpp`

---

### 11. `Metadata::Reflection::get`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
Metadata::Member* Metadata::Reflection::get(const FunctionDescriptor& descriptor) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Metadata::Member*` |
| **Modifiers** | `const` |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:152` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes get within Client Base Configuration. Coordinates interactions with `findFirstChildByNameDangerous, toString`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `findFirstChildByNameDangerous`, `toString`.
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

**Divergence Analysis:** Alternative platform-specific implementations exist in: `RobloxStudio/RobloxMainWindow.cpp`, `XboxClient/UserTranslator.cpp`.

- **Alternative Implementation Files:** `RobloxStudio/RobloxMainWindow.cpp`, `XboxClient/UserTranslator.cpp`

---

### 12. `Metadata::Reflection::get`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
Metadata::Member* Metadata::Reflection::get(const YieldFunctionDescriptor& descriptor) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Metadata::Member*` |
| **Modifiers** | `const` |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:159` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes get within Client Base Configuration. Coordinates interactions with `findFirstChildByNameDangerous, toString`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `findFirstChildByNameDangerous`, `toString`.
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

**Divergence Analysis:** Alternative platform-specific implementations exist in: `RobloxStudio/RobloxMainWindow.cpp`, `XboxClient/UserTranslator.cpp`.

- **Alternative Implementation Files:** `RobloxStudio/RobloxMainWindow.cpp`, `XboxClient/UserTranslator.cpp`

---

### 13. `Metadata::Reflection::get`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
Metadata::Member* Metadata::Reflection::get(const EventDescriptor& descriptor) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Metadata::Member*` |
| **Modifiers** | `const` |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:166` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes get within Client Base Configuration. Coordinates interactions with `findFirstChildByNameDangerous, toString`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `findFirstChildByNameDangerous`, `toString`.
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

**Divergence Analysis:** Alternative platform-specific implementations exist in: `RobloxStudio/RobloxMainWindow.cpp`, `XboxClient/UserTranslator.cpp`.

- **Alternative Implementation Files:** `RobloxStudio/RobloxMainWindow.cpp`, `XboxClient/UserTranslator.cpp`

---

### 14. `Metadata::Reflection::get`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
Metadata::Member* Metadata::Reflection::get(const CallbackDescriptor& descriptor) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Metadata::Member*` |
| **Modifiers** | `const` |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:173` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes get within Client Base Configuration. Coordinates interactions with `findFirstChildByNameDangerous, toString`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `findFirstChildByNameDangerous`, `toString`.
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

**Divergence Analysis:** Alternative platform-specific implementations exist in: `RobloxStudio/RobloxMainWindow.cpp`, `XboxClient/UserTranslator.cpp`.

- **Alternative Implementation Files:** `RobloxStudio/RobloxMainWindow.cpp`, `XboxClient/UserTranslator.cpp`

---

### 15. `Metadata::Reflection::get`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
Metadata::Enum* Metadata::Reflection::get(const EnumDescriptor& descriptor) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Metadata::Enum*` |
| **Modifiers** | `const` |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:180` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes get within Client Base Configuration. Coordinates interactions with `findFirstChildByName, toString`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `findFirstChildByName`, `toString`.
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

**Divergence Analysis:** Alternative platform-specific implementations exist in: `RobloxStudio/RobloxMainWindow.cpp`, `XboxClient/UserTranslator.cpp`.

- **Alternative Implementation Files:** `RobloxStudio/RobloxMainWindow.cpp`, `XboxClient/UserTranslator.cpp`

---

### 16. `Metadata::Reflection::get`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
Metadata::EnumItem* Metadata::Reflection::get(const EnumDescriptor::Item& item) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Metadata::EnumItem*` |
| **Modifiers** | `const` |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:185` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes get within Client Base Configuration. Coordinates interactions with `findFirstChildByNameDangerous, toString`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `findFirstChildByNameDangerous`, `toString`.
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

**Divergence Analysis:** Alternative platform-specific implementations exist in: `RobloxStudio/RobloxMainWindow.cpp`, `XboxClient/UserTranslator.cpp`.

- **Alternative Implementation Files:** `RobloxStudio/RobloxMainWindow.cpp`, `XboxClient/UserTranslator.cpp`

---

### 17. `writeMetadata`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void writeMetadata(const Metadata::Item* metadata, const Descriptor& descriptor);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:198` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes writeMetadata within Client Base Configuration. Coordinates interactions with `isBrowsable, isDeprecated, isBackend`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `isBrowsable`, `isDeprecated`, `isBackend`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `writeMetadata`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 18. `writeMemberInfo`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void writeMemberInfo(const Reflection::MemberDescriptor* d);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:208` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes writeMemberInfo within Client Base Configuration.

- **Control Flow & Execution:** Multi-case state dispatch.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `writeMemberInfo`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 19. `writeProperty`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void writeProperty(const Reflection::PropertyDescriptor* d, const Reflection::ClassDescriptor* c);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:238` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes writeProperty within Client Base Configuration. Coordinates interactions with `isScriptable, c_str, writeMetadata, singleton`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `isScriptable`, `c_str`, `writeMetadata`, `singleton`, `get`, `isPublic`, `isReadOnly`, `isWriteOnly`, `writeMemberInfo`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `writeProperty`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 20. `writeArg`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void writeArg(const Reflection::SignatureDescriptor::Item& arg, bool* first);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:256` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes writeArg within Client Base Configuration. Coordinates interactions with `c_str, hasDefaultValue`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `c_str`, `hasDefaultValue`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `writeArg`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 21. `writeArgs`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void writeArgs(const Reflection::SignatureDescriptor& d);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:271` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes writeArgs within Client Base Configuration. Coordinates interactions with `for_each, begin, end, bind`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `for_each`, `begin`, `end`, `bind`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `writeArgs`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 22. `writeFunction`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void writeFunction(const Reflection::FunctionDescriptor* d, const Reflection::ClassDescriptor* c);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:277` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes writeFunction within Client Base Configuration. Coordinates interactions with `getSignature, c_str, writeArgs, writeMetadata`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getSignature`, `c_str`, `writeArgs`, `writeMetadata`, `singleton`, `get`, `writeMemberInfo`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `writeFunction`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 23. `writeYieldFunction`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void writeYieldFunction(const Reflection::YieldFunctionDescriptor* d, const Reflection::ClassDescriptor* c);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:289` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes writeYieldFunction within Client Base Configuration. Coordinates interactions with `getSignature, c_str, writeArgs, writeMetadata`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getSignature`, `c_str`, `writeArgs`, `writeMetadata`, `singleton`, `get`, `writeMemberInfo`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `writeYieldFunction`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 24. `writeEvent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void writeEvent(const Reflection::EventDescriptor* d, const Reflection::ClassDescriptor* c);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:301` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes writeEvent within Client Base Configuration. Coordinates interactions with `isScriptable, c_str, writeArgs, getSignature`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `isScriptable`, `c_str`, `writeArgs`, `getSignature`, `writeMetadata`, `singleton`, `get`, `writeMemberInfo`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `writeEvent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 25. `writeCallback`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void writeCallback(const Reflection::CallbackDescriptor* d, const Reflection::ClassDescriptor* c);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:315` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes writeCallback within Client Base Configuration. Coordinates interactions with `getSignature, c_str, writeArgs, isAsync`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getSignature`, `c_str`, `writeArgs`, `isAsync`, `writeMetadata`, `singleton`, `get`, `writeMemberInfo`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `writeCallback`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 26. `writeClassHeader`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void writeClassHeader(const Reflection::ClassDescriptor* d);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:329` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes writeClassHeader within Client Base Configuration. Coordinates interactions with `c_str, getBase, rootDescriptor, writeMetadata`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `c_str`, `getBase`, `rootDescriptor`, `writeMetadata`, `singleton`, `get`, `isScriptCreatable`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `writeClassHeader`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 27. `writeClass`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void writeClass(const Reflection::ClassDescriptor* d);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:341` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes writeClass within Client Base Configuration. Coordinates interactions with `rootDescriptor, writeClassHeader, for_each, bind`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `rootDescriptor`, `writeClassHeader`, `for_each`, `bind`, `derivedClasses_begin`, `derivedClasses_end`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `writeClass`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 28. `writeEnum`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void writeEnum(const EnumDescriptor* d);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:387` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes writeEnum within Client Base Configuration. Coordinates interactions with `c_str, for_each, begin, end`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `c_str`, `for_each`, `begin`, `end`, `bind`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `writeEnum`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 29. `writeEnumItem`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void writeEnumItem(const EnumDescriptor::Item* d);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:396` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes writeEnumItem within Client Base Configuration. Coordinates interactions with `writeMetadata, singleton, get`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `writeMetadata`, `singleton`, `get`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `writeEnumItem`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 30. `writeAPI`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void writeAPI();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:403` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes writeAPI within Client Base Configuration. Coordinates interactions with `writeClass, rootDescriptor, for_each, enumsBegin`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `writeClass`, `rootDescriptor`, `for_each`, `enumsBegin`, `enumsEnd`, `bind`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `writeAPI`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 31. `checkConflict`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
T* checkConflict(const T* desc, std::map<std::string, const T*>& map) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `T*` |
| **Modifiers** | `const` |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:414` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes checkConflict within Client Base Configuration. Coordinates interactions with `toString`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `toString`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `checkConflict`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 32. `writeConflictingMember`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void writeConflictingMember(const ClassDescriptor* desc, const MemberDescriptor* member);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:425` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes writeConflictingMember within Client Base Configuration. Coordinates interactions with `writeProperty, writeFunction, writeYieldFunction, writeEvent`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `writeProperty`, `writeFunction`, `writeYieldFunction`, `writeEvent`, `writeCallback`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `writeConflictingMember`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 33. `writeConflictingMembers`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void writeConflictingMembers(const ClassDescriptor* desc, std::map<std::string, const MemberDescriptor*>& members);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:439` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes writeConflictingMembers within Client Base Configuration. Coordinates interactions with `descriptors_begin, descriptors_end, checkConflict, toString`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `descriptors_begin`, `descriptors_end`, `checkConflict`, `toString`, `writeConflictingMember`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `writeConflictingMembers`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 34. `writeConflicts`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void writeConflicts();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:456` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes writeConflicts within Client Base Configuration. Coordinates interactions with `all_begin, all_end, checkConflict, toString`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `all_begin`, `all_end`, `checkConflict`, `toString`, `writeClassHeader`, `enumsBegin`, `enumsEnd`, `begin`, `end`, `writeEnumItem`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `writeConflicts`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 35. `Metadata::writeEverything`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Metadata::writeEverything(std::ostream& stream);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.cpp:515` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes writeEverything within Client Base Configuration. Coordinates interactions with `writeConflicts, writeAPI`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `writeConflicts`, `writeAPI`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `writeEverything`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 36. `safe_static_init_singleton`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void safe_static_init_singleton();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `ClientBase/ReflectionMetadata.h:30` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes safe_static_init_singleton within Client Base Configuration. Coordinates interactions with `safe_static_do_get_singleton`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `safe_static_do_get_singleton`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `safe_static_init_singleton`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 37. `singleton`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
shared_ptr<Reflection> singleton();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `shared_ptr&lt;Reflection&gt;` |
| **Modifiers** | `static` |
| **Source Location** | `ClientBase/ReflectionMetadata.h:34` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes singleton within Client Base Configuration. Coordinates interactions with `call_once, safe_static_do_get_singleton`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `call_once`, `safe_static_do_get_singleton`.
- **External Library Dependencies:** `Boost C++ Libraries`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

This function is exercised in **9 test case(s)**:

- **`LuaDebugger::FlatDataSerialization`** (`App.UnitTest/LuaDebugger.cpp:139`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK(workspace != NULL)`, `BOOST_CHECK(debuggerManager.getDataModel() != NULL)`
  - **Callsite Snippet:** `RBX::Scripting::DebuggerManager& debuggerManager = RBX::Scripting::DebuggerManager::singleton();`
- **`LuaDebugger::NestedDataSerialization`** (`App.UnitTest/LuaDebugger.cpp:211`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK(workspace != NULL)`, `BOOST_CHECK(debuggerManager.getDataModel() != NULL)`
  - **Callsite Snippet:** `RBX::Scripting::DebuggerManager& debuggerManager = RBX::Scripting::DebuggerManager::singleton();`
- **`ReplicatorGcJobTest::MovingPartOutsideOfStreamedAreaCausesItToBeGced`** (`App.UnitTest/ReplicatorGcJobTest.cpp:98`)
  - **Usage Pattern:** `Performance Benchmark`
  - **Assertions Checked:** `BOOST_REQUIRE(clientDm-&gt;getWorkspace()-&gt;findFirstChildByName("BasePlate"))`, `BOOST_REQUIRE(clientDm-&gt;getWorkspace()-&gt;findFirstChildByName("ToStreamOut"))`
  - **Callsite Snippet:** `NetworkSettings::singleton().setExtraMemoryUsedInMB(MemoryStats::totalMemoryBytes()/1024/1024);`
- **`ReplicatorGcJobTest::MovingPartAndItsParentOutsideOfStreamedAreaShouldNotRemoveThePartTwice`** (`App.UnitTest/ReplicatorGcJobTest.cpp:195`)
  - **Usage Pattern:** `Performance Benchmark`
  - **Assertions Checked:** `BOOST_REQUIRE(clientDm-&gt;getWorkspace()-&gt;findFirstChildByName("BasePlate"))`, `BOOST_REQUIRE(parent)`
  - **Callsite Snippet:** `NetworkSettings::singleton().setExtraMemoryUsedInMB(MemoryStats::totalMemoryBytes()/1024/1024);`

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `RobloxStudio/MobileDevelopmentDeployer.cpp`.

- **Alternative Implementation Files:** `RobloxStudio/MobileDevelopmentDeployer.cpp`

---

### 38. `Classes`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
public: Classes();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `public:` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.h:59` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes Classes within Client Base Configuration.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `Classes`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 39. `isBrowsable`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool isBrowsable() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `ClientBase/ReflectionMetadata.h:79` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Browsable means it is visible in docs for end-users

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isBrowsable`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 40. `getBase`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Class* getBase() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Class*` |
| **Modifiers** | `const const` |
| **Source Location** | `ClientBase/ReflectionMetadata.h:125` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes getBase within Client Base Configuration. Coordinates interactions with `getParent`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getParent`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getBase`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 41. `getExplorerOrder`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int getExplorerOrder() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `const` |
| **Source Location** | `ClientBase/ReflectionMetadata.h:127` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes getExplorerOrder within Client Base Configuration. Coordinates interactions with `getBase`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getBase`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getExplorerOrder`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 42. `isExplorerItem`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool isExplorerItem() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `ClientBase/ReflectionMetadata.h:133` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes isExplorerItem within Client Base Configuration. Coordinates interactions with `getExplorerOrder`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getExplorerOrder`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isExplorerItem`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 43. `getExplorerImageIndex`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int getExplorerImageIndex() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `const` |
| **Source Location** | `ClientBase/ReflectionMetadata.h:136` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes getExplorerImageIndex within Client Base Configuration. Coordinates interactions with `getBase, max, getPreferredParent, getInsertable`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getBase`, `max`, `getPreferredParent`, `getInsertable`, `Class`, `explorerOrder`, `explorerImageIndex`, `preferredParent`, `insertable`, `Members`, `Properties`, `Functions`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getExplorerImageIndex`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 44. `getPreferredParent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string getPreferredParent() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | `const` |
| **Source Location** | `ClientBase/ReflectionMetadata.h:141` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes getPreferredParent within Client Base Configuration.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getPreferredParent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 45. `getInsertable`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool getInsertable() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `ClientBase/ReflectionMetadata.h:145` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes getInsertable within Client Base Configuration.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getInsertable`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 46. `Members`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
public: Members();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `public:` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.h:153` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Declaration or inline method for Members.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `Members`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 47. `Properties`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
public: Properties();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `public:` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.h:160` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Declaration or inline method for Properties.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `Properties`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 48. `Functions`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
public: Functions();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `public:` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.h:167` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Declaration or inline method for Functions.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `Functions`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 49. `YieldFunctions`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
public: YieldFunctions();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `public:` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.h:174` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Declaration or inline method for YieldFunctions.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `YieldFunctions`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 50. `Events`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
public: Events();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `public:` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.h:181` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Declaration or inline method for Events.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `Events`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 51. `Callbacks`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
public: Callbacks();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `public:` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.h:188` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Declaration or inline method for Callbacks.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `Callbacks`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 52. `Member`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
public: Member();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `public:` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.h:195` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Declaration or inline method for Member.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `Member`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 53. `Enums`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
public: Enums();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `public:` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.h:202` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Declaration or inline method for Enums.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `Enums`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 54. `Enum`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
public: Enum();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `public:` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.h:209` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Declaration or inline method for Enum.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `Enum`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 55. `EnumItem`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
public: EnumItem();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `public:` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/ReflectionMetadata.h:216` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Declaration or inline method for EnumItem.

- **Control Flow & Execution:** Linear execution flow.
- **Memory Management:** Standard stack allocation.
- **Concurrency & Thread Safety:** Unsynchronized / single-threaded context.
- **Error Handling & Invariants:** Standard return value verification.
- **State Mutation:** Stateless or local modification.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `EnumItem`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 56. `CRenderSettingsItem::setShowAggregation`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CRenderSettingsItem::setShowAggregation(bool value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/RenderSettingsItem.cpp:172` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes setShowAggregation within Client Base Configuration. Coordinates interactions with `settingsChangedSignal`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `settingsChangedSignal`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setShowAggregation`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 57. `CRenderSettingsItem::runProfiler`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CRenderSettingsItem::runProfiler(bool overwriteExistingValues);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/RenderSettingsItem.cpp:181` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes runProfiler within Client Base Configuration. Coordinates interactions with `setValue`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `setValue`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `runProfiler`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 58. `CRenderSettingsItem::setAASamples`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CRenderSettingsItem::setAASamples(AASamples value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/RenderSettingsItem.cpp:190` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes setAASamples within Client Base Configuration. Coordinates interactions with `settingsChangedSignal`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `settingsChangedSignal`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setAASamples`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 59. `CRenderSettingsItem::setResolutionPreference`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CRenderSettingsItem::setResolutionPreference(ResolutionPreset value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/RenderSettingsItem.cpp:200` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes setResolutionPreference within Client Base Configuration. Coordinates interactions with `settingsChangedSignal`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `settingsChangedSignal`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setResolutionPreference`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 60. `CRenderSettingsItem::setFullscreenSize`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void CRenderSettingsItem::setFullscreenSize(G3D::Vector2int16 value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `ClientBase/RenderSettingsItem.cpp:209` |
| **Subsystem** | `Client Base Configuration` |

#### How it Works Internally

Executes setFullscreenSize within Client Base Configuration.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setFullscreenSize`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---


:::tip Additional Functions
There are **17 additional internal and inline functions** in this subsystem. All functions are indexed and cross-referenced in the **[Complete Function Catalog](./function-catalog.md)**.
:::

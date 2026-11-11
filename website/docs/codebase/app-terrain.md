---
sidebar_position: 10
title: App - Voxel Terrain Engines
description: Voxel occupancy grid, smooth terrain v2, materials, and spatial partitioning.
---

# App - Voxel Terrain Engines

Voxel occupancy grid, smooth terrain v2, materials, and spatial partitioning.


## FAQ

### Which terrain generation should I inspect?

Identify whether the caller uses voxel or voxel2 before changing storage or material logic. The two representations should not be assumed interchangeable.

### How can I investigate this in the repository?

From the repository root, search the relevant tracked files for a starting point (results are leads, not proof of behavior):

```bash
git grep -n -i -F -- 'Material' -- App/voxel2
```

Read the surrounding implementation and callers, and check relevant tests before making changes. A search may return no matches when terminology or tracked files change.

## Subsystem Metrics

- **Total Documented Functions:** `206`
- **Functions Exercised in Tests:** `39`
- **Platform-Divergent Implementations:** `7`
- **Component Source Files:** `20`

## Source Files

<details>
<summary>View all 20 source files in this subsystem</summary>

| Source File | Path |
| :--- | :--- |
| `Cell.h` | `App/include/voxel/Cell.h` |
| `Grid.Chunk.h` | `App/include/voxel/Grid.Chunk.h` |
| `Grid.h` | `App/include/voxel/Grid.h` |
| `Serializer.h` | `App/include/voxel/Serializer.h` |
| `Util.h` | `App/include/voxel/Util.h` |
| `Voxelizer.h` | `App/include/voxel/Voxelizer.h` |
| `BitSerializer.h` | `App/include/voxel2/BitSerializer.h` |
| `Conversion.h` | `App/include/voxel2/Conversion.h` |
| `Grid.h` | `App/include/voxel2/Grid.h` |
| `GridListener.h` | `App/include/voxel2/GridListener.h` |
| `MaterialTable.h` | `App/include/voxel2/MaterialTable.h` |
| `Mesher.h` | `App/include/voxel2/Mesher.h` |
| `Cell.cpp` | `App/voxel/Cell.cpp` |
| `Grid.Chunk.cpp` | `App/voxel/Grid.Chunk.cpp` |
| `Grid.cpp` | `App/voxel/Grid.cpp` |
| `Util.cpp` | `App/voxel/Util.cpp` |
| `Voxelizer.cpp` | `App/voxel/Voxelizer.cpp` |
| `Grid.cpp` | `App/voxel2/Grid.cpp` |
| `MaterialTable.cpp` | `App/voxel2/MaterialTable.cpp` |
| `Mesher.cpp` | `App/voxel2/Mesher.cpp` |

</details>

---

## Function Reference

### 1. `getBlock`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
public:
	CellBlock getBlock() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `public:
	CellBlock` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/voxel/Cell.h:90` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes getBlock within App - Voxel Terrain Engines. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

This function is exercised in **2 test case(s)**:

- **`ClusterDeltaBuffer::AllCellPermutations`** (`App.UnitTest/ClusterReplicationTest.cpp:977`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(0, serverWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(0, clientWrapper-&gt;getReplicationData().updateBuffer.size())`
  - **Callsite Snippet:** `if (data.solid.getBlock() != CELL_BLOCK_Empty) \{`
- **`VoxelCellUtilTest::WriteOneFormatReadOther`** (`App.UnitTest/VoxelCellUtilTest.cpp:45`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_REQUIRE(v.solid.getBlock() == b)`
  - **Callsite Snippet:** `BOOST_REQUIRE(v.solid.getBlock() == b);`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 2. `getOrientation`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
CellOrientation getOrientation() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `CellOrientation` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/voxel/Cell.h:93` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes getOrientation within App - Voxel Terrain Engines. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

This function is exercised in **2 test case(s)**:

- **`ClusterDeltaBuffer::AllCellPermutations`** (`App.UnitTest/ClusterReplicationTest.cpp:977`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(0, serverWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(0, clientWrapper-&gt;getReplicationData().updateBuffer.size())`
  - **Callsite Snippet:** `substitute.solid.setOrientation(data.solid.getOrientation());`
- **`VoxelCellUtilTest::WriteOneFormatReadOther`** (`App.UnitTest/VoxelCellUtilTest.cpp:45`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_REQUIRE(v.solid.getOrientation() == o)`
  - **Callsite Snippet:** `BOOST_REQUIRE(v.solid.getOrientation() == o);`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 3. `setBlock`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void setBlock(CellBlock block);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/voxel/Cell.h:96` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes setBlock within App - Voxel Terrain Engines.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.

#### How it is Used in Tests

This function is exercised in **12 test case(s)**:

- **`ClusterDeltaBuffer::AllCellPermutations`** (`App.UnitTest/ClusterReplicationTest.cpp:977`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(0, serverWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(0, clientWrapper-&gt;getReplicationData().updateBuffer.size())`
  - **Callsite Snippet:** `substitute.solid.setBlock((CellBlock)(data.solid.getBlock() % 5));`
- **`ClusterDeltaBuffer::EmptyTerrainDoesNotGetReplicatedToNewPlayers`** (`App.UnitTest/ClusterReplicationTest.cpp:1177`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK(!clientCluster-&gt;isAllocated())`, `BOOST_CHECK(clientCluster-&gt;isAllocated())`
  - **Callsite Snippet:** `cell.solid.setBlock(CELL_BLOCK_Solid);`
- **`RaycastTest::StartInsideWaterHitsWaterBlockInterface`** (`App.UnitTest/RaycastTest.cpp:246`)
  - **Usage Pattern:** `Direct Call`
  - **Callsite Snippet:** `cell.solid.setBlock(CELL_BLOCK_Solid);`
- **`RaycastTest::HitsWedgeInWaterWedgeAsAppropriate`** (`App.UnitTest/RaycastTest.cpp:277`)
  - **Usage Pattern:** `Direct Call`
  - **Callsite Snippet:** `cell.solid.setBlock(CELL_BLOCK_VerticalWedge);`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 4. `setOrientation`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void setOrientation(CellOrientation orientation);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/voxel/Cell.h:98` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes setOrientation within App - Voxel Terrain Engines.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.

#### How it is Used in Tests

This function is exercised in **9 test case(s)**:

- **`ClusterDeltaBuffer::AllCellPermutations`** (`App.UnitTest/ClusterReplicationTest.cpp:977`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(0, serverWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(0, clientWrapper-&gt;getReplicationData().updateBuffer.size())`
  - **Callsite Snippet:** `substitute.solid.setOrientation(data.solid.getOrientation());`
- **`RaycastTest::StartInsideWaterHitsWaterBlockInterface`** (`App.UnitTest/RaycastTest.cpp:246`)
  - **Usage Pattern:** `Direct Call`
  - **Callsite Snippet:** `cell.solid.setOrientation(CELL_ORIENTATION_NegZ);`
- **`RaycastTest::HitsWedgeInWaterWedgeAsAppropriate`** (`App.UnitTest/RaycastTest.cpp:277`)
  - **Usage Pattern:** `Direct Call`
  - **Callsite Snippet:** `cell.solid.setOrientation(CELL_ORIENTATION_NegZ);`
- **`RaycastTest::GetSurfaceReturnsCellSurface`** (`App.UnitTest/RaycastTest.cpp:337`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(tmp, NORM_X_NEG)`, `BOOST_CHECK_EQUAL(surface.getPartInstance(), dm.cluster)`
  - **Callsite Snippet:** `cell.solid.setOrientation(CELL_ORIENTATION_NegZ);`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 5. `getWaterData`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int getWaterData() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `unsigned const` |
| **Source Location** | `App/include/voxel/Cell.h:109` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes getWaterData within App - Voxel Terrain Engines. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getWaterData`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 6. `getForce`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
public:
	WaterCellForce getForce() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `public:
	WaterCellForce` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/voxel/Cell.h:113` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes getForce within App - Voxel Terrain Engines. Coordinates interactions with `return, getWaterData`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `return`, `getWaterData`.

#### How it is Used in Tests

This function is exercised in **1 test case(s)**:

- **`VoxelCellUtilTest::WriteOneFormatReadOther`** (`App.UnitTest/VoxelCellUtilTest.cpp:45`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE(CELL_MATERIAL_Deprecated_Empty == (CellMaterial)0)`, `BOOST_REQUIRE(CELL_BLOCK_Solid == (CellBlock)0)`
  - **Callsite Snippet:** `BOOST_REQUIRE(v.water.getForce() == f);`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 7. `getDirection`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
WaterCellDirection getDirection() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `WaterCellDirection` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/voxel/Cell.h:117` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes getDirection within App - Voxel Terrain Engines. Coordinates interactions with `return, getWaterData`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `return`, `getWaterData`.

#### How it is Used in Tests

This function is exercised in **1 test case(s)**:

- **`VoxelCellUtilTest::WriteOneFormatReadOther`** (`App.UnitTest/VoxelCellUtilTest.cpp:45`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE(CELL_MATERIAL_Deprecated_Empty == (CellMaterial)0)`, `BOOST_REQUIRE(CELL_BLOCK_Solid == (CellBlock)0)`
  - **Callsite Snippet:** `BOOST_REQUIRE(v.water.getDirection() == d);`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 8. `setForceAndDirection`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void setForceAndDirection(WaterCellForce force, WaterCellDirection direction);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/voxel/Cell.h:120` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes setForceAndDirection within App - Voxel Terrain Engines.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

This function is exercised in **1 test case(s)**:

- **`VoxelCellUtilTest::WriteOneFormatReadOther`** (`App.UnitTest/VoxelCellUtilTest.cpp:45`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE(CELL_MATERIAL_Deprecated_Empty == (CellMaterial)0)`, `BOOST_REQUIRE(CELL_BLOCK_Solid == (CellBlock)0)`
  - **Callsite Snippet:** `v.water.setForceAndDirection((WaterCellForce)f, (WaterCellDirection)d);`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 9. `isExplicitWaterCell`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool isExplicitWaterCell() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `inline const` |
| **Source Location** | `App/include/voxel/Cell.h:150` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Indicates if this cell has been set to water explicitly by the user. Note that water can also exist in wedge cells. Use Region and/or Region::iterator methods for a way to detect all kinds of water simultaneously.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `isEmpty`, `getBlock`.

#### How it is Used in Tests

This function is exercised in **1 test case(s)**:

- **`VoxelCellUtilTest::WriteOneFormatReadOther`** (`App.UnitTest/VoxelCellUtilTest.cpp:45`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE(CELL_MATERIAL_Deprecated_Empty == (CellMaterial)0)`, `BOOST_REQUIRE(CELL_BLOCK_Solid == (CellBlock)0)`
  - **Callsite Snippet:** `BOOST_REQUIRE(v.isExplicitWaterCell());`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 10. `serializeAsUnsignedChar`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
char serializeAsUnsignedChar(const Cell v);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `char` |
| **Modifiers** | `static inline unsigned` |
| **Source Location** | `App/include/voxel/Cell.h:160` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Convert to/from unsigned char, for networking and saving to file

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `serializeAsUnsignedChar`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 11. `deserializeFromUnsignedChar`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Cell deserializeFromUnsignedChar(unsigned char cell);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Cell` |
| **Modifiers** | `static inline` |
| **Source Location** | `App/include/voxel/Cell.h:163` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes deserializeFromUnsignedChar within App - Voxel Terrain Engines. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `deserializeFromUnsignedChar`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 12. `convertToUnsignedCharForFile`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
char convertToUnsignedCharForFile(const Cell v);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `char` |
| **Modifiers** | `static inline unsigned` |
| **Source Location** | `App/include/voxel/Cell.h:166` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes convertToUnsignedCharForFile within App - Voxel Terrain Engines. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `convertToUnsignedCharForFile`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 13. `readUnsignedCharFromFile`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Cell readUnsignedCharFromFile(unsigned char cell);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Cell` |
| **Modifiers** | `static inline` |
| **Source Location** | `App/include/voxel/Cell.h:169` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes readUnsignedCharFromFile within App - Voxel Terrain Engines. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `readUnsignedCharFromFile`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 14. `asUnsignedCharForDeprecatedUses`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
char asUnsignedCharForDeprecatedUses(const Cell v);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `char` |
| **Modifiers** | `static inline unsigned` |
| **Source Location** | `App/include/voxel/Cell.h:173` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Old style voxel access. Avoid using these methods where possible.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

This function is exercised in **2 test case(s)**:

- **`VoxelCellUtilTest::WriteOneFormatReadOther`** (`App.UnitTest/VoxelCellUtilTest.cpp:45`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE(CELL_MATERIAL_Deprecated_Empty == (CellMaterial)0)`, `BOOST_REQUIRE(CELL_BLOCK_Solid == (CellBlock)0)`
  - **Callsite Snippet:** `unsigned char oldCell = Cell::asUnsignedCharForDeprecatedUses(v);`
- **`VoxelCellUtilTest::ConstantVoxelsMatchDeprecatedVersion`** (`App.UnitTest/VoxelCellUtilTest.cpp:111`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_REQUIRE(Cell::asUnsignedCharForDeprecatedUses(Constants::kUniqueEmptyCellRepresentation) == V1Deprecated::UNIQUE_EMPTY_CELL_REPRESENTATION)`, `BOOST_REQUIRE(Cell::asUnsignedCharForDeprecatedUses(Constants::kWaterOnWedgeCell) == V1Deprecated::WATER_ON_WEDGE_CELL)`
  - **Callsite Snippet:** `BOOST_REQUIRE(Cell::asUnsignedCharForDeprecatedUses(Constants::kUniqueEmptyCellRepresentation) == V1Deprecated::UNIQUE_EMPTY_CELL_REPRESENTATION);`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 15. `readUnsignedCharFromDeprecatedUse`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Cell readUnsignedCharFromDeprecatedUse(unsigned char cell);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Cell` |
| **Modifiers** | `static inline` |
| **Source Location** | `App/include/voxel/Cell.h:176` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes readUnsignedCharFromDeprecatedUse within App - Voxel Terrain Engines. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

This function is exercised in **3 test case(s)**:

- **`ClusterDeltaBuffer::AllCellPermutations`** (`App.UnitTest/ClusterReplicationTest.cpp:977`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(0, serverWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(0, clientWrapper-&gt;getReplicationData().updateBuffer.size())`
  - **Callsite Snippet:** `Cell data = Cell::readUnsignedCharFromDeprecatedUse(i);`
- **`VoxelCellUtilTest::WriteOneFormatReadOther`** (`App.UnitTest/VoxelCellUtilTest.cpp:45`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE(CELL_MATERIAL_Deprecated_Empty == (CellMaterial)0)`, `BOOST_REQUIRE(CELL_BLOCK_Solid == (CellBlock)0)`
  - **Callsite Snippet:** `Cell v = Cell::readUnsignedCharFromDeprecatedUse(oldCell);`
- **`VoxelCellUtilTest::ConstantVoxelsMatchDeprecatedVersion`** (`App.UnitTest/VoxelCellUtilTest.cpp:111`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_REQUIRE(Constants::kUniqueEmptyCellRepresentation == Cell::readUnsignedCharFromDeprecatedUse(V1Deprecated::UNIQUE_EMPTY_CELL_REPRESENTATION))`, `BOOST_REQUIRE(Constants::kWaterOnWedgeCell == Cell::readUnsignedCharFromDeprecatedUse(V1Deprecated::WATER_ON_WEDGE_CELL))`
  - **Callsite Snippet:** `BOOST_REQUIRE(Constants::kUniqueEmptyCellRepresentation == Cell::readUnsignedCharFromDeprecatedUse(V1Deprecated::UNIQUE_EMPTY_CELL_REPRESENTATION));`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 16. `Cell::isEmpty`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool Cell::isEmpty() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/voxel/Cell.h:190` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes isEmpty within App - Voxel Terrain Engines. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isEmpty`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 17. `voxelCoordOffsetToIndexOffset`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int voxelCoordOffsetToIndexOffset(const Vector3int16& offset);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `static inline` |
| **Source Location** | `App/include/voxel/Grid.Chunk.h:32` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes voxelCoordOffsetToIndexOffset within App - Voxel Terrain Engines. Coordinates interactions with `return, Vector3int16, sum`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`, `Vector3int16`, `sum`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `voxelCoordOffsetToIndexOffset`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 18. `voxelCoordToArrayIndex`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int voxelCoordToArrayIndex(const Vector3int16& coord);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `static inline unsigned` |
| **Source Location** | `App/include/voxel/Grid.Chunk.h:36` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes voxelCoordToArrayIndex within App - Voxel Terrain Engines. Coordinates interactions with `voxelCoordOffsetToIndexOffset, voxelCoordinateRelativeToEnclosingRegion`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `voxelCoordOffsetToIndexOffset`, `voxelCoordinateRelativeToEnclosingRegion`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `voxelCoordToArrayIndex`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 19. `getData`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::vector<Cell>& getData();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::vector&lt;Cell&gt;&` |
| **Modifiers** | None |
| **Source Location** | `App/include/voxel/Grid.Chunk.h:49` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes getData within App - Voxel Terrain Engines.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getData`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 20. `getConstData`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::vector<Cell>& getConstData() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::vector&lt;Cell&gt;&` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/voxel/Grid.Chunk.h:51` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes getConstData within App - Voxel Terrain Engines.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getConstData`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 21. `getMaterial`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::vector<unsigned char>& getMaterial();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::vector&lt;unsigned char&gt;&` |
| **Modifiers** | None |
| **Source Location** | `App/include/voxel/Grid.Chunk.h:52` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes getMaterial within App - Voxel Terrain Engines.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getMaterial`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 22. `getConstMaterial`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::vector<unsigned char>& getConstMaterial() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::vector&lt;unsigned char&gt;&` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/voxel/Grid.Chunk.h:53` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes getConstMaterial within App - Voxel Terrain Engines.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getConstMaterial`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 23. `updateCountOfNonEmptyCells`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void updateCountOfNonEmptyCells(int delta);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/voxel/Grid.Chunk.h:54` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes updateCountOfNonEmptyCells within App - Voxel Terrain Engines. Coordinates interactions with `RBXASSERT`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `RBXASSERT`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `updateCountOfNonEmptyCells`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 24. `hasNoUsefulData`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool hasNoUsefulData() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/voxel/Grid.Chunk.h:59` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes hasNoUsefulData within App - Voxel Terrain Engines.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `hasNoUsefulData`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 25. `fillLocalAreaInfo`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void fillLocalAreaInfo(const Vector3int16& centerCoord,
			const Water::RelevantNeighbors& relevantNeighbors,
			Water::LocalAreaInfo* out) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/voxel/Grid.Chunk.h:64` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

for water

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `fillLocalAreaInfo`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 26. `getNonEmptyCellCount`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int getNonEmptyCellCount() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `inline unsigned const` |
| **Source Location** | `App/include/voxel/Grid.h:45` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

returns the number of cells in the terrain that are not empty

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

This function is exercised in **2 test case(s)**:

- **`ClusterChangeHistoryTest::FillChunkStressTest`** (`App.UnitTest/ClusterChangeHistoryTest.cpp:99`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(0, chf.cluster-&gt;getNonEmptyCellCount())`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL(0, chf.cluster-&gt;getNonEmptyCellCount());`
- **`ClusterChangeHistoryTest::PartiallyOverlappingChunkTest`** (`App.UnitTest/ClusterChangeHistoryTest.cpp:126`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(0, chf.cluster-&gt;getNonEmptyCellCount())`
  - **Callsite Snippet:** `BOOST_CHECK_EQUAL(0, chf.cluster-&gt;getNonEmptyCellCount());`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 27. `encodeFromPosition`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void encodeFromPosition(const Grid* voxelStore, Vector3int16& cellpos,
			const SpatialRegion::Id& lastChunkPos, const Grid::Region& region,
			RecentlyEncodedBuffer& lastSeenNewCells,
			CellBuffer& cellBuffer, OutputStream* outputStream) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/voxel/Serializer.h:25` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes encodeFromPosition within App - Voxel Terrain Engines. Coordinates interactions with `serializeAsUnsignedChar, voxelAt, materialAt, find`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `serializeAsUnsignedChar`, `voxelAt`, `materialAt`, `find`, `WriteBits`, `push`, `nextCellInIterationOrder`, `regionContainingVoxel`, `chk`, `pop`, `RBXASSERT`, `encode`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `encodeFromPosition`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 28. `encodeCells`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void encodeCells(const Grid* voxelStore, CellBuffer& cellBuffer,
			OutputStream* outputStream, int sizeLimitInBytes) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/voxel/Serializer.h:81` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes encodeCells within App - Voxel Terrain Engines. Coordinates interactions with `kCellInChunkBits, getRegionDimensionInVoxelsAsBitShifts, lastChunkPos, size`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `kCellInChunkBits`, `getRegionDimensionInVoxelsAsBitShifts`, `lastChunkPos`, `size`, `GetNumberOfBytesUsed`, `pop`, `regionContainingVoxel`, `voxelCoordinateRelativeToEnclosingRegion`, `WriteBits`, `value`, `inclusiveVoxelExtentsOfRegion`, `getRegion`.
- **External Library Dependencies:** `Boost C++ Libraries`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `encodeCells`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 29. `decodeCells`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void decodeCells(Grid* voxelStore, InputStream& inputStream,
			CellUpdateFilter& filter);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/voxel/Serializer.h:154` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes decodeCells within App - Voxel Terrain Engines. Coordinates interactions with `kCellInChunkBits, getRegionDimensionInVoxelsAsBitShifts, chunkPos, ReadBits`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `kCellInChunkBits`, `getRegionDimensionInVoxelsAsBitShifts`, `chunkPos`, `ReadBits`, `cellPos`, `globalVoxelCoordinateFromRegionAndRelativeCoordinate`, `push`, `canSet`, `setCell`, `deserializeFromUnsignedChar`, `nextCellInIterationOrder`, `decode`.
- **External Library Dependencies:** `Boost C++ Libraries`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `decodeCells`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 30. `getCellMaterial_Deprecated`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
CellMaterial getCellMaterial_Deprecated(unsigned char cell);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `CellMaterial` |
| **Modifiers** | `inline` |
| **Source Location** | `App/include/voxel/Util.h:12` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes getCellMaterial_Deprecated within App - Voxel Terrain Engines. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

This function is exercised in **1 test case(s)**:

- **`VoxelCellUtilTest::WriteOneFormatReadOther`** (`App.UnitTest/VoxelCellUtilTest.cpp:45`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE(CELL_MATERIAL_Deprecated_Empty == (CellMaterial)0)`, `BOOST_REQUIRE(CELL_BLOCK_Solid == (CellBlock)0)`
  - **Callsite Snippet:** `BOOST_REQUIRE(V1Deprecated::getCellMaterial_Deprecated(oldCell) == CELL_MATERIAL_Deprecated_Empty);`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 31. `setCellMaterial_Deprecated`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void setCellMaterial_Deprecated(unsigned char& cell, CellMaterial material);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `inline` |
| **Source Location** | `App/include/voxel/Util.h:14` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes setCellMaterial_Deprecated within App - Voxel Terrain Engines.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

This function is exercised in **1 test case(s)**:

- **`VoxelCellUtilTest::WriteOneFormatReadOther`** (`App.UnitTest/VoxelCellUtilTest.cpp:45`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE(CELL_MATERIAL_Deprecated_Empty == (CellMaterial)0)`, `BOOST_REQUIRE(CELL_BLOCK_Solid == (CellBlock)0)`
  - **Callsite Snippet:** `V1Deprecated::setCellMaterial_Deprecated(oldCell, (CellMaterial)m);`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 32. `readMaterial`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
CellMaterial readMaterial(const unsigned char* materials, const unsigned int cellIndex, const Cell cell);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `CellMaterial` |
| **Modifiers** | `inline` |
| **Source Location** | `App/include/voxel/Util.h:15` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes readMaterial within App - Voxel Terrain Engines. Coordinates interactions with `return, getBlock`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`, `getBlock`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `readMaterial`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 33. `writeMaterial`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void writeMaterial(unsigned char* materials, unsigned int cellIndex, const CellMaterial newMaterial);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `inline` |
| **Source Location** | `App/include/voxel/Util.h:22` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes writeMaterial within App - Voxel Terrain Engines. Coordinates interactions with `RBXASSERT`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `RBXASSERT`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `writeMaterial`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 34. `rotate`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
SkippedCorner rotate(SkippedCorner corner, const CellOrientation orient);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `SkippedCorner` |
| **Modifiers** | `static inline` |
| **Source Location** | `App/include/voxel/Util.h:53` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes rotate within App - Voxel Terrain Engines. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `rotate`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 35. `divideTopLeftToBottomRight`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool divideTopLeftToBottomRight(SkippedCorner corner);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `static inline` |
| **Source Location** | `App/include/voxel/Util.h:57` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes divideTopLeftToBottomRight within App - Voxel Terrain Engines.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `divideTopLeftToBottomRight`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 36. `XZAxisMirror`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
SkippedCorner XZAxisMirror(SkippedCorner corner);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `SkippedCorner` |
| **Modifiers** | `static inline` |
| **Source Location** | `App/include/voxel/Util.h:61` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes XZAxisMirror within App - Voxel Terrain Engines.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `XZAxisMirror`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 37. `YAxisMirror`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
SkippedCorner YAxisMirror(SkippedCorner corner);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `SkippedCorner` |
| **Modifiers** | `static inline` |
| **Source Location** | `App/include/voxel/Util.h:67` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes YAxisMirror within App - Voxel Terrain Engines.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `YAxisMirror`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 38. `inverse`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
BlockAxisFace inverse(const BlockAxisFace other);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `BlockAxisFace` |
| **Modifiers** | `static` |
| **Source Location** | `App/include/voxel/Util.h:73` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes inverse within App - Voxel Terrain Engines.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `inverse`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 39. `GetOrientedFace`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
BlockAxisFace& GetOrientedFace(Cell cell, FaceDirection f) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `BlockAxisFace&` |
| **Modifiers** | `inline const` |
| **Source Location** | `App/include/voxel/Util.h:100` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes GetOrientedFace within App - Voxel Terrain Engines. Coordinates interactions with `asUnsignedCharForDeprecatedUses`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `asUnsignedCharForDeprecatedUses`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `GetOrientedFace`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 40. `isWedgeSideNotFull`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool isWedgeSideNotFull(Cell voxel, FaceDirection f);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `inline` |
| **Source Location** | `App/include/voxel/Util.h:105` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes isWedgeSideNotFull within App - Voxel Terrain Engines. Coordinates interactions with `GetOrientedFace`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `GetOrientedFace`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isWedgeSideNotFull`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 41. `worldToCell_floor`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector3int16 worldToCell_floor(const Vector3& worldPos);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector3int16` |
| **Modifiers** | `inline` |
| **Source Location** | `App/include/voxel/Util.h:109` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes worldToCell_floor within App - Voxel Terrain Engines. Coordinates interactions with `Vector3int16, floorf`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `Vector3int16`, `floorf`.

#### How it is Used in Tests

This function is exercised in **2 test case(s)**:

- **`RaycastTest::GetSurfaceDoesNotHitTerrainEdge`** (`App.UnitTest/RaycastTest.cpp:406`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(sanityCheck, Vector3int16(0, 19, -1))`, `BOOST_CHECK_EQUAL(tmp, NORM_Y_NEG)`
  - **Callsite Snippet:** `Vector3int16 sanityCheck = worldToCell_floor(rayStart);`
- **`VoxelCellUtilTest::WorldToCell`** (`App.UnitTest/VoxelCellUtilTest.cpp:11`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(Vector3int16(
						kOffset + (x - 1) / 2,
						(y - 1) / 2,
						kOffset + (z - 1) / 2),
					worldToCell_floor(kEpsilon * Vector3(x,y,z)))`
  - **Callsite Snippet:** `worldToCell_floor(kEpsilon * Vector3(x,y,z)));`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 42. `worldSpaceToCellSpace`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector3 worldSpaceToCellSpace(const Vector3& worldPos);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector3` |
| **Modifiers** | `inline` |
| **Source Location** | `App/include/voxel/Util.h:117` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes worldSpaceToCellSpace within App - Voxel Terrain Engines. Coordinates interactions with `Vector3`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `Vector3`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `worldSpaceToCellSpace`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 43. `cellSpaceToWorldSpace`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector3 cellSpaceToWorldSpace(const Vector3& cellPos);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector3` |
| **Modifiers** | `inline` |
| **Source Location** | `App/include/voxel/Util.h:124` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes cellSpaceToWorldSpace within App - Voxel Terrain Engines. Coordinates interactions with `Vector3`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `Vector3`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `cellSpaceToWorldSpace`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 44. `cellToWorld_smallestCorner`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector3 cellToWorld_smallestCorner(const Vector3int16& cellPos);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector3` |
| **Modifiers** | `inline` |
| **Source Location** | `App/include/voxel/Util.h:132` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes cellToWorld_smallestCorner within App - Voxel Terrain Engines. Coordinates interactions with `Vector3`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `Vector3`.

#### How it is Used in Tests

This function is exercised in **4 test case(s)**:

- **`RaycastTest::GetSurfaceReturnsCellSurface`** (`App.UnitTest/RaycastTest.cpp:337`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(tmp, NORM_X_NEG)`, `BOOST_CHECK_EQUAL(surface.getPartInstance(), dm.cluster)`
  - **Callsite Snippet:** `Vector3 worldCellCenter = cellToWorld_smallestCorner(filledCell) + (Vector3(kCELL_SIZE, kCELL_SIZE, kCELL_SIZE) / 2);`
- **`RaycastTest::GetSurfaceDoesNotHitTerrainEdge`** (`App.UnitTest/RaycastTest.cpp:406`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(sanityCheck, Vector3int16(0, 19, -1))`, `BOOST_CHECK_EQUAL(tmp, NORM_Y_NEG)`
  - **Callsite Snippet:** `Vector3 worldCellCorner = cellToWorld_smallestCorner(filledCell);`
- **`RaycastTest::BoundingBoxIncludesTerrainButRayMissesTerrain`** (`App.UnitTest/RaycastTest.cpp:439`)
  - **Usage Pattern:** `Direct Call`
  - **Callsite Snippet:** `Vector3 start = cellToWorld_smallestCorner(Vector3int16(-2,0,0)) + kHalfCell;`
- **`VoxelCellUtilTest::CellToWorld`** (`App.UnitTest/VoxelCellUtilTest.cpp:28`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(mcExtents.min(), newExtents.min())`, `BOOST_CHECK_EQUAL(mcExtents.max(), newExtents.max())`
  - **Callsite Snippet:** `Extents newExtents = Extents(cellToWorld_smallestCorner(cell),`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 45. `cellToWorld_center`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector3 cellToWorld_center(const Vector3int16& cellPos);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector3` |
| **Modifiers** | `inline` |
| **Source Location** | `App/include/voxel/Util.h:142` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes cellToWorld_center within App - Voxel Terrain Engines. Coordinates interactions with `cellToWorld_smallestCorner, Vector3`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `cellToWorld_smallestCorner`, `Vector3`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `cellToWorld_center`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 46. `cellToWorld_largestCorner`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector3 cellToWorld_largestCorner(const Vector3int16& cellPos);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector3` |
| **Modifiers** | `inline` |
| **Source Location** | `App/include/voxel/Util.h:147` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes cellToWorld_largestCorner within App - Voxel Terrain Engines. Coordinates interactions with `cellToWorld_smallestCorner, Vector3int16`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `cellToWorld_smallestCorner`, `Vector3int16`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `cellToWorld_largestCorner`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 47. `getTerrainExtentsInCells`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Region3int16 getTerrainExtentsInCells();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Region3int16` |
| **Modifiers** | `inline` |
| **Source Location** | `App/include/voxel/Util.h:151` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes getTerrainExtentsInCells within App - Voxel Terrain Engines. Coordinates interactions with `Region3int16, Vector3int16`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `Region3int16`, `Vector3int16`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getTerrainExtentsInCells`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 48. `getTerrainExtents`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Extents getTerrainExtents();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Extents` |
| **Modifiers** | `inline` |
| **Source Location** | `App/include/voxel/Util.h:158` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes getTerrainExtents within App - Voxel Terrain Engines. Coordinates interactions with `getTerrainExtentsInCells, Extents, cellToWorld_smallestCorner, getMinPos`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getTerrainExtentsInCells`, `Extents`, `cellToWorld_smallestCorner`, `getMinPos`, `cellToWorld_largestCorner`, `getMaxPos`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getTerrainExtents`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 49. `setNonFixedPartsEnabled`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void setNonFixedPartsEnabled(bool value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/voxel/Voxelizer.h:43` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes setNonFixedPartsEnabled within App - Voxel Terrain Engines.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setNonFixedPartsEnabled`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 50. `getNonFixedPartsEnabled`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool getNonFixedPartsEnabled() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/voxel/Voxelizer.h:45` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes getNonFixedPartsEnabled within App - Voxel Terrain Engines.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getNonFixedPartsEnabled`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 51. `encodeIndex`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
public:
	void encodeIndex(const Vector3int32& index, BitStream& stream);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `public:
	void` |
| **Modifiers** | None |
| **Source Location** | `App/include/voxel2/BitSerializer.h:8` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes encodeIndex within App - Voxel Terrain Engines. Coordinates interactions with `encodeChunkIndex`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `encodeChunkIndex`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `encodeIndex`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 52. `encodeContent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void encodeContent(const Box& box, BitStream& stream);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/voxel2/BitSerializer.h:15` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes encodeContent within App - Voxel Terrain Engines. Coordinates interactions with `encodeChunkData`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `encodeChunkData`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `encodeContent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 53. `decodeIndex`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void decodeIndex(Vector3int32& index, BitStream& stream);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/voxel2/BitSerializer.h:20` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes decodeIndex within App - Voxel Terrain Engines. Coordinates interactions with `decodeChunkIndex`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `decodeChunkIndex`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `decodeIndex`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 54. `decodeContent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void decodeContent(Box& box, BitStream& stream);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/voxel2/BitSerializer.h:29` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes decodeContent within App - Voxel Terrain Engines. Coordinates interactions with `decodeChunkData`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `decodeChunkData`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `decodeContent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 55. `encodeChunkIndex`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void encodeChunkIndex(const Vector3int32& diff, BitStream& stream);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/voxel2/BitSerializer.h:38` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes encodeChunkIndex within App - Voxel Terrain Engines. Coordinates interactions with `char, short`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `char`, `short`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `encodeChunkIndex`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 56. `decodeChunkIndex`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void decodeChunkIndex(Vector3int32& diff, BitStream& stream);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/voxel2/BitSerializer.h:68` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes decodeChunkIndex within App - Voxel Terrain Engines. Coordinates interactions with `Vector3int32`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `Vector3int32`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `decodeChunkIndex`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 57. `encodeChunkData`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void encodeChunkData(const Box& box, BitStream& stream);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/voxel2/BitSerializer.h:111` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes encodeChunkData within App - Voxel Terrain Engines. Coordinates interactions with `isEmpty, getSize, resize, memcpy`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT); C++ exception throw on invalid state or failure; Standard runtime error exception formulation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `isEmpty`, `getSize`, `resize`, `memcpy`, `readRow`, `size`, `values`, `WriteBits`, `full`, `custom`, `material`, `new`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `encodeChunkData`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 58. `decodeChunkData`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void decodeChunkData(Box& box, BitStream& stream);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/voxel2/BitSerializer.h:195` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes decodeChunkData within App - Voxel Terrain Engines. Coordinates interactions with `RBXASSERT, isEmpty, getSize, resize`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT); C++ exception throw on invalid state or failure; Standard runtime error exception formulation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `RBXASSERT`, `isEmpty`, `getSize`, `resize`, `size`, `ReadBits`, `runtime_error`, `cell`, `memcpy`, `writeRow`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `decodeChunkData`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 59. `getOccupancyFromSolidBlock`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
char getOccupancyFromSolidBlock(Voxel::CellBlock block);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `char` |
| **Modifiers** | `inline unsigned` |
| **Source Location** | `App/include/voxel2/Conversion.h:35` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes getOccupancyFromSolidBlock within App - Voxel Terrain Engines. Coordinates interactions with `RBXASSERT`.

- **Control Flow & Execution:** Multi-case state dispatch, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `RBXASSERT`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getOccupancyFromSolidBlock`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 60. `getCellBlockFromCell`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Voxel::CellBlock getCellBlockFromCell(const Cell& cell);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Voxel::CellBlock` |
| **Modifiers** | `inline` |
| **Source Location** | `App/include/voxel2/Conversion.h:58` |
| **Subsystem** | `App - Voxel Terrain Engines` |

#### How it Works Internally

Executes getCellBlockFromCell within App - Voxel Terrain Engines. Coordinates interactions with `getMaterial, getOccupancy`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getMaterial`, `getOccupancy`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getCellBlockFromCell`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---


:::tip Additional Functions
There are **146 additional internal and inline functions** in this subsystem. All functions are indexed and cross-referenced in the **[Complete Function Catalog](./function-catalog.md)**.
:::

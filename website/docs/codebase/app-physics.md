---
sidebar_position: 5
title: App - World Simulation & Physics
description: Physics world, contacts, mechanisms, assemblies, primitives, and joints.
---

# App - World Simulation & Physics

Physics world, contacts, mechanisms, assemblies, primitives, and joints.

## Subsystem Metrics

- **Total Documented Functions:** `2042`
- **Functions Exercised in Tests:** `67`
- **Platform-Divergent Implementations:** `33`
- **Component Source Files:** `158`

## Source Files

<details>
<summary>View all 158 source files in this subsystem</summary>

| Source File | Path |
| :--- | :--- |
| `Body.h` | `App/include/v8kernel/Body.h` |
| `BulletShapeConnectors.h` | `App/include/v8kernel/BulletShapeConnectors.h` |
| `BuoyancyConnector.h` | `App/include/v8kernel/BuoyancyConnector.h` |
| `Cofm.h` | `App/include/v8kernel/Cofm.h` |
| `Connector.h` | `App/include/v8kernel/Connector.h` |
| `Constants.h` | `App/include/v8kernel/Constants.h` |
| `ContactConnector.h` | `App/include/v8kernel/ContactConnector.h` |
| `IStage.h` | `App/include/v8kernel/IStage.h` |
| `Kernel.h` | `App/include/v8kernel/Kernel.h` |
| `KernelData.h` | `App/include/v8kernel/KernelData.h` |
| `KernelIndex.h` | `App/include/v8kernel/KernelIndex.h` |
| `Link.h` | `App/include/v8kernel/Link.h` |
| `Pair.h` | `App/include/v8kernel/Pair.h` |
| `Point.h` | `App/include/v8kernel/Point.h` |
| `PolyConnectors.h` | `App/include/v8kernel/PolyConnectors.h` |
| `SimBody.h` | `App/include/v8kernel/SimBody.h` |
| `Assembly.h` | `App/include/v8world/Assembly.h` |
| `AssemblyStage.h` | `App/include/v8world/AssemblyStage.h` |
| `Ball.h` | `App/include/v8world/Ball.h` |
| `BasicSpatialHashPrimitive.h` | `App/include/v8world/BasicSpatialHashPrimitive.h` |
| `Block.h` | `App/include/v8world/Block.h` |
| `BlockCorners.h` | `App/include/v8world/BlockCorners.h` |
| `BlockMesh.h` | `App/include/v8world/BlockMesh.h` |
| `BulletGeometryPoolObjects.h` | `App/include/v8world/BulletGeometryPoolObjects.h` |
| `Buoyancy.h` | `App/include/v8world/Buoyancy.h` |
| `CellContact.h` | `App/include/v8world/CellContact.h` |
| `Clump.h` | `App/include/v8world/Clump.h` |
| `Contact.h` | `App/include/v8world/Contact.h` |
| `ContactManager.h` | `App/include/v8world/ContactManager.h` |
| `CornerWedgeMesh.h` | `App/include/v8world/CornerWedgeMesh.h` |
| `DistributedPhysics.h` | `App/include/v8world/DistributedPhysics.h` |
| `Edge.h` | `App/include/v8world/Edge.h` |
| `EdgeBuffer.h` | `App/include/v8world/EdgeBuffer.h` |
| `Enum.h` | `App/include/v8world/Enum.h` |
| `Geometry.h` | `App/include/v8world/Geometry.h` |
| `GeometryPool.h` | `App/include/v8world/GeometryPool.h` |
| `GlueJoint.h` | `App/include/v8world/GlueJoint.h` |
| `HumanoidStage.h` | `App/include/v8world/HumanoidStage.h` |
| `IMoving.h` | `App/include/v8world/IMoving.h` |
| `IPipelined.h` | `App/include/v8world/IPipelined.h` |
| `IWorldStage.h` | `App/include/v8world/IWorldStage.h` |
| `Joint.h` | `App/include/v8world/Joint.h` |
| `KDTree.h` | `App/include/v8world/KDTree.h` |
| `KernelJoint.h` | `App/include/v8world/KernelJoint.h` |
| `Mechanism.h` | `App/include/v8world/Mechanism.h` |
| `MegaClusterMesh.h` | `App/include/v8world/MegaClusterMesh.h` |
| `Mesh.h` | `App/include/v8world/Mesh.h` |
| `Motor6DJoint.h` | `App/include/v8world/Motor6DJoint.h` |
| `MotorJoint.h` | `App/include/v8world/MotorJoint.h` |
| `MovingAssemblyStage.h` | `App/include/v8world/MovingAssemblyStage.h` |
| `ParallelRampMesh.h` | `App/include/v8world/ParallelRampMesh.h` |
| `Poly.h` | `App/include/v8world/Poly.h` |
| `PolyCellContact.h` | `App/include/v8world/PolyCellContact.h` |
| `PolyContact.h` | `App/include/v8world/PolyContact.h` |
| `PolyPolyContact.h` | `App/include/v8world/PolyPolyContact.h` |
| `Primitive.h` | `App/include/v8world/Primitive.h` |
| `PrismMesh.h` | `App/include/v8world/PrismMesh.h` |
| `PyramidMesh.h` | `App/include/v8world/PyramidMesh.h` |
| `RightAngleRampMesh.h` | `App/include/v8world/RightAngleRampMesh.h` |
| `RigidJoint.h` | `App/include/v8world/RigidJoint.h` |
| `RotateJoint.h` | `App/include/v8world/RotateJoint.h` |
| `SendPhysics.h` | `App/include/v8world/SendPhysics.h` |
| `SimJob.h` | `App/include/v8world/SimJob.h` |
| `SimulateStage.h` | `App/include/v8world/SimulateStage.h` |
| `SleepStage.h` | `App/include/v8world/SleepStage.h` |
| `SmoothClusterGeometry.h` | `App/include/v8world/SmoothClusterGeometry.h` |
| `SnapJoint.h` | `App/include/v8world/SnapJoint.h` |
| `SpatialFilter.h` | `App/include/v8world/SpatialFilter.h` |
| `SpatialHashMultiRes.h` | `App/include/v8world/SpatialHashMultiRes.h` |
| `SurfaceData.h` | `App/include/v8world/SurfaceData.h` |
| `Tolerance.h` | `App/include/v8world/Tolerance.h` |
| `TreeStage.h` | `App/include/v8world/TreeStage.h` |
| `TriangleMesh.h` | `App/include/v8world/TriangleMesh.h` |
| `WedgeMesh.h` | `App/include/v8world/WedgeMesh.h` |
| `WeldJoint.h` | `App/include/v8world/WeldJoint.h` |
| `World.h` | `App/include/v8world/World.h` |
| `Body.cpp` | `App/v8kernel/Body.cpp` |
| `BulletShapeConnectors.cpp` | `App/v8kernel/BulletShapeConnectors.cpp` |
| `BuoyancyConnector.cpp` | `App/v8kernel/BuoyancyConnector.cpp` |
| `Cofm.cpp` | `App/v8kernel/Cofm.cpp` |
| `Connector.cpp` | `App/v8kernel/Connector.cpp` |
| `Constants.cpp` | `App/v8kernel/Constants.cpp` |
| `ContactConnector.cpp` | `App/v8kernel/ContactConnector.cpp` |
| `Kernel.cpp` | `App/v8kernel/Kernel.cpp` |
| `Link.cpp` | `App/v8kernel/Link.cpp` |
| `Pair.cpp` | `App/v8kernel/Pair.cpp` |
| `Point.cpp` | `App/v8kernel/Point.cpp` |
| `PolyConnectors.cpp` | `App/v8kernel/PolyConnectors.cpp` |
| `SimBody.cpp` | `App/v8kernel/SimBody.cpp` |
| `Assembly.cpp` | `App/v8world/Assembly.cpp` |
| `AssemblyHistory.cpp` | `App/v8world/AssemblyHistory.cpp` |
| `AssemblyStage.cpp` | `App/v8world/AssemblyStage.cpp` |
| `Ball.cpp` | `App/v8world/Ball.cpp` |
| `BallCellContact.cpp` | `App/v8world/BallCellContact.cpp` |
| `BallPolyContact.cpp` | `App/v8world/BallPolyContact.cpp` |
| `Block.cpp` | `App/v8world/Block.cpp` |
| `BulletContact.cpp` | `App/v8world/BulletContact.cpp` |
| `BulletShapeCellContact.cpp` | `App/v8world/BulletShapeCellContact.cpp` |
| `BulletShapeContact.cpp` | `App/v8world/BulletShapeContact.cpp` |
| `Buoyancy.cpp` | `App/v8world/Buoyancy.cpp` |
| `CellContact.cpp` | `App/v8world/CellContact.cpp` |
| `CleanStage.cpp` | `App/v8world/CleanStage.cpp` |
| `Clump.cpp` | `App/v8world/Clump.cpp` |
| `Contact.cpp` | `App/v8world/Contact.cpp` |
| `ContactManager.cpp` | `App/v8world/ContactManager.cpp` |
| `ContactStage.cpp` | `App/v8world/ContactStage.cpp` |
| `CornerWedgePoly.cpp` | `App/v8world/CornerWedgePoly.cpp` |
| `Cylinder.cpp` | `App/v8world/Cylinder.cpp` |
| `Edge.cpp` | `App/v8world/Edge.cpp` |
| `EdgeBuffer.cpp` | `App/v8world/EdgeBuffer.cpp` |
| `EdgeStage.cpp` | `App/v8world/EdgeStage.cpp` |
| `GlueJoint.cpp` | `App/v8world/GlueJoint.cpp` |
| `GroundStage.cpp` | `App/v8world/GroundStage.cpp` |
| `HumanoidStage.cpp` | `App/v8world/HumanoidStage.cpp` |
| `IMoving.cpp` | `App/v8world/IMoving.cpp` |
| `IPipelined.cpp` | `App/v8world/IPipelined.cpp` |
| `IWorldStage.cpp` | `App/v8world/IWorldStage.cpp` |
| `Joint.cpp` | `App/v8world/Joint.cpp` |
| `JointBuilder.cpp` | `App/v8world/JointBuilder.cpp` |
| `JointStage.cpp` | `App/v8world/JointStage.cpp` |
| `KDTree.cpp` | `App/v8world/KDTree.cpp` |
| `KernelJoint.cpp` | `App/v8world/KernelJoint.cpp` |
| `MaterialProperties.cpp` | `App/v8world/MaterialProperties.cpp` |
| `MechToAssemblyStage.cpp` | `App/v8world/MechToAssemblyStage.cpp` |
| `Mechanism.cpp` | `App/v8world/Mechanism.cpp` |
| `MegaClusterPoly.cpp` | `App/v8world/MegaClusterPoly.cpp` |
| `Mesh.cpp` | `App/v8world/Mesh.cpp` |
| `Motor6DJoint.cpp` | `App/v8world/Motor6DJoint.cpp` |
| `MotorJoint.cpp` | `App/v8world/MotorJoint.cpp` |
| `MovingAssemblyStage.cpp` | `App/v8world/MovingAssemblyStage.cpp` |
| `MovingStage.cpp` | `App/v8world/MovingStage.cpp` |
| `MutilJoint.cpp` | `App/v8world/MutilJoint.cpp` |
| `ParallelRampPoly.cpp` | `App/v8world/ParallelRampPoly.cpp` |
| `Poly.cpp` | `App/v8world/Poly.cpp` |
| `PolyCellContact.cpp` | `App/v8world/PolyCellContact.cpp` |
| `PolyContact.cpp` | `App/v8world/PolyContact.cpp` |
| `PolyPolyContact.cpp` | `App/v8world/PolyPolyContact.cpp` |
| `Primitive.cpp` | `App/v8world/Primitive.cpp` |
| `PrismPoly.cpp` | `App/v8world/PrismPoly.cpp` |
| `PyramidPoly.cpp` | `App/v8world/PyramidPoly.cpp` |
| `RightAngleRampPoly.cpp` | `App/v8world/RightAngleRampPoly.cpp` |
| `RigidJoint.cpp` | `App/v8world/RigidJoint.cpp` |
| `RotateJoint.cpp` | `App/v8world/RotateJoint.cpp` |
| `SendPhysics.cpp` | `App/v8world/SendPhysics.cpp` |
| `SimJob.cpp` | `App/v8world/SimJob.cpp` |
| `SimulateStage.cpp` | `App/v8world/SimulateStage.cpp` |
| `SleepStage.cpp` | `App/v8world/SleepStage.cpp` |
| `SmoothClusterGeometry.cpp` | `App/v8world/SmoothClusterGeometry.cpp` |
| `SnapJoint.cpp` | `App/v8world/SnapJoint.cpp` |
| `SpatialFilter.cpp` | `App/v8world/SpatialFilter.cpp` |
| `SpatialHashMultiRes.cpp` | `App/v8world/SpatialHashMultiRes.cpp` |
| `StepJointsStage.cpp` | `App/v8world/StepJointsStage.cpp` |
| `TerrainPartition.cpp` | `App/v8world/TerrainPartition.cpp` |
| `TreeStage.cpp` | `App/v8world/TreeStage.cpp` |
| `TriangleMesh.cpp` | `App/v8world/TriangleMesh.cpp` |
| `WedgePoly.cpp` | `App/v8world/WedgePoly.cpp` |
| `WeldJoint.cpp` | `App/v8world/WeldJoint.cpp` |
| `World.cpp` | `App/v8world/World.cpp` |

</details>

---

## Function Reference

### 1. `getLeafBodyIndex`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int& getLeafBodyIndex();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int&` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:74` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getLeafBodyIndex within App - World Simulation & Physics.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getLeafBodyIndex`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 2. `getCofm`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Cofm* getCofm();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Cofm*` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:84` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getCofm within App - World Simulation & Physics.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getCofm`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 3. `getSimBody`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
SimBody* getSimBody();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `SimBody*` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:87` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getSimBody within App - World Simulation & Physics.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getSimBody`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 4. `getConstSimBody`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
SimBody* getConstSimBody() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `SimBody*` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8kernel/Body.h:88` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getConstSimBody within App - World Simulation & Physics.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getConstSimBody`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 5. `getMeInParent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
CoordinateFrame& getMeInParent() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `CoordinateFrame&` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8kernel/Body.h:108` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getMeInParent within App - World Simulation & Physics. Coordinates interactions with `RBXASSERT, getParent, getLink, getChildInParent`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `RBXASSERT`, `getParent`, `getLink`, `getChildInParent`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getMeInParent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 6. `getConstMeInParent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
CoordinateFrame& getConstMeInParent() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `CoordinateFrame&` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8kernel/Body.h:113` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getConstMeInParent within App - World Simulation & Physics. Coordinates interactions with `RBXASSERT, getConstParent, getConstLink, linked`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `RBXASSERT`, `getConstParent`, `getConstLink`, `linked`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getConstMeInParent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 7. `pvIsUpToDate`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool pvIsUpToDate() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8kernel/Body.h:120` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes pvIsUpToDate within App - World Simulation & Physics. Coordinates interactions with `getConstParent, getRoot, getStateIndexNoUpdate`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getConstParent`, `getRoot`, `getStateIndexNoUpdate`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `pvIsUpToDate`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 8. `calcRoot`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Body* calcRoot();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Body*` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:137` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes calcRoot within App - World Simulation & Physics. Coordinates interactions with `getParent`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getParent`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `calcRoot`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 9. `calcRootConst`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Body* calcRootConst() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Body*` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8kernel/Body.h:139` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes calcRootConst within App - World Simulation & Physics. Coordinates interactions with `getConstParent`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getConstParent`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `calcRootConst`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 10. `getRootSimBody`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
SimBody* getRootSimBody();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `SimBody*` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:158` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getRootSimBody within App - World Simulation & Physics. Coordinates interactions with `getRoot, getSimBody`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getRoot`, `getSimBody`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getRootSimBody`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 11. `getConstRootSimBody`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
SimBody* getConstRootSimBody() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `SimBody*` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8kernel/Body.h:160` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getConstRootSimBody within App - World Simulation & Physics. Coordinates interactions with `getRoot, getConstSimBody`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getRoot`, `getConstSimBody`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getConstRootSimBody`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 12. `getUID`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
boost::uint64_t getUID() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `boost::uint64_t` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8kernel/Body.h:163` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getUID within App - World Simulation & Physics.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getUID`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 13. `setGuidIndex`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void setGuidIndex(int _guidIndex);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:166` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Used only by the solver inspector to id the objects between different clients

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setGuidIndex`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 14. `getGuidIndex`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int getGuidIndex() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8kernel/Body.h:167` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getGuidIndex within App - World Simulation & Physics.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getGuidIndex`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 15. `cofmIsClean`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool cofmIsClean();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:171` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

From Cofm, SimBody

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getCofm`, `getIsDirty`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `cofmIsClean`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 16. `makeStateDirty`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void makeStateDirty();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:178` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes makeStateDirty within App - World Simulation & Physics. Coordinates interactions with `getRoot, advanceStateIndex`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getRoot`, `advanceStateIndex`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `makeStateDirty`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 17. `getStateIndex`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int getStateIndex();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `unsigned` |
| **Source Location** | `App/include/v8kernel/Body.h:182` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getStateIndex within App - World Simulation & Physics. Coordinates interactions with `updatePV`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `updatePV`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getStateIndex`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 18. `getStateIndexNoUpdate`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int getStateIndexNoUpdate() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `unsigned const` |
| **Source Location** | `App/include/v8kernel/Body.h:187` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getStateIndexNoUpdate within App - World Simulation & Physics.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getStateIndexNoUpdate`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 19. `getChild`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Body* getChild(int i);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Body*` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:194` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Base vs. Branch

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

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

### 20. `getConstChild`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Body* getConstChild(int i) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Body*` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8kernel/Body.h:196` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getConstChild within App - World Simulation & Physics.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getConstChild`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 21. `getParent`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Body* getParent();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Body*` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:197` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getParent within App - World Simulation & Physics.

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

### 22. `getConstParent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Body* getConstParent() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Body*` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8kernel/Body.h:199` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getConstParent within App - World Simulation & Physics.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getConstParent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 23. `getLink`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Link* getLink();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Link*` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:200` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getLink within App - World Simulation & Physics.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getLink`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 24. `getConstLink`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Link* getConstLink() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Link*` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8kernel/Body.h:202` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getConstLink within App - World Simulation & Physics.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getConstLink`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 25. `getRoot`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Body* getRoot() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Body*` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8kernel/Body.h:203` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getRoot within App - World Simulation & Physics. Coordinates interactions with `RBXASSERT_SLOW, calcRootConst`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `RBXASSERT_SLOW`, `calcRootConst`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getRoot`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 26. `getRoot`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Body* getRoot();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Body*` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:208` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getRoot within App - World Simulation & Physics. Coordinates interactions with `RBXASSERT_SLOW, calcRootConst`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `RBXASSERT_SLOW`, `calcRootConst`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getRoot`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 27. `getCofmOffset`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector3& getCofmOffset() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector3&` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8kernel/Body.h:213` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getCofmOffset within App - World Simulation & Physics.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getCofmOffset`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 28. `getMeInAncestor`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
CoordinateFrame getMeInAncestor(const Body* ancestor) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `CoordinateFrame` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8kernel/Body.h:221` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Only works on bodies in same clump - otherwise not const for the link and will assert

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `CoordinateFrame`, `getConstParent`, `getConstMeInParent`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getMeInAncestor`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 29. `getMass`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
float getMass() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `float` |
| **Modifiers** | `inline const` |
| **Source Location** | `App/include/v8kernel/Body.h:232` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getMass within App - World Simulation & Physics.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getMass`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 30. `getIBody`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Matrix3 getIBody() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Matrix3` |
| **Modifiers** | `inline const` |
| **Source Location** | `App/include/v8kernel/Body.h:234` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getIBody within App - World Simulation & Physics.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getIBody`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 31. `getIBodyV3`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector3 getIBodyV3() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector3` |
| **Modifiers** | `inline const` |
| **Source Location** | `App/include/v8kernel/Body.h:235` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getIBodyV3 within App - World Simulation & Physics. Coordinates interactions with `toDiagonal, getIBody`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `toDiagonal`, `getIBody`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getIBodyV3`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 32. `getMoment`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Matrix3 getMoment() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Matrix3` |
| **Modifiers** | `inline const` |
| **Source Location** | `App/include/v8kernel/Body.h:237` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getMoment within App - World Simulation & Physics. Coordinates interactions with `getIBody`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getIBody`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getMoment`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 33. `getPrincipalMoment`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector3 getPrincipalMoment() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector3` |
| **Modifiers** | `inline const` |
| **Source Location** | `App/include/v8kernel/Body.h:238` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getPrincipalMoment within App - World Simulation & Physics. Coordinates interactions with `getIBodyV3`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getIBodyV3`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getPrincipalMoment`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 34. `getIWorld`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Matrix3 getIWorld();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Matrix3` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:239` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getIWorld within App - World Simulation & Physics. Coordinates interactions with `momentToWorldSpace, getIBody, getCoordinateFrame`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `momentToWorldSpace`, `getIBody`, `getCoordinateFrame`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getIWorld`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 35. `getBranchMass`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
float getBranchMass();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `float` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:243` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Branch refers to everything below me....

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getCofm`, `getMass`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getBranchMass`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 36. `getBranchIBody`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Matrix3 getBranchIBody();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Matrix3` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:244` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getBranchIBody within App - World Simulation & Physics. Coordinates interactions with `getCofm, getMoment`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getCofm`, `getMoment`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getBranchIBody`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 37. `getBranchIBodyV3`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector3 getBranchIBodyV3();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector3` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:245` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getBranchIBodyV3 within App - World Simulation & Physics. Coordinates interactions with `toDiagonal, getBranchIBody`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `toDiagonal`, `getBranchIBody`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getBranchIBodyV3`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 38. `getBranchIWorld`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Matrix3 getBranchIWorld();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Matrix3` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:246` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getBranchIWorld within App - World Simulation & Physics. Coordinates interactions with `momentToWorldSpace, getBranchIBody, getCoordinateFrame`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `momentToWorldSpace`, `getBranchIBody`, `getCoordinateFrame`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getBranchIWorld`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 39. `getPvFast`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
PV& getPvFast() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `PV&` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8kernel/Body.h:252` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getPvFast within App - World Simulation & Physics. Coordinates interactions with `RBXASSERT_FISHING, pvIsUpToDate`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `RBXASSERT_FISHING`, `pvIsUpToDate`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getPvFast`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 40. `getPvUnsafe`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
PV& getPvUnsafe() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `PV&` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8kernel/Body.h:259` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Current Job should hold the Data Model write lock or somehow have locked the Body::mutex.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `updatePV`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getPvUnsafe`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 41. `getPV_Spin_Lock`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
PV& getPV_Spin_Lock() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `PV&` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8kernel/Body.h:263` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getPV_Spin_Lock within App - World Simulation & Physics. Coordinates interactions with `lock, updatePV`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Spinlock synchronization via RBX::spin_mutex; RAII mutex lock acquisition (scoped_lock).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `lock`, `updatePV`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getPV_Spin_Lock`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 42. `getPvSafe`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
PV& getPvSafe() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `PV&` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8kernel/Body.h:269` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getPvSafe within App - World Simulation & Physics. Coordinates interactions with `getPV_Spin_Lock`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getPV_Spin_Lock`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getPvSafe`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 43. `getPosFast`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector3& getPosFast() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector3&` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8kernel/Body.h:274` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getPosFast within App - World Simulation & Physics. Coordinates interactions with `RBXASSERT_FISHING, pvIsUpToDate`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `RBXASSERT_FISHING`, `pvIsUpToDate`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getPosFast`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 44. `getPos`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector3& getPos() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector3&` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8kernel/Body.h:279` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getPos within App - World Simulation & Physics. Coordinates interactions with `updatePV`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `updatePV`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getPos`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 45. `getCoordinateFrameFast`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
CoordinateFrame& getCoordinateFrameFast() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `CoordinateFrame&` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8kernel/Body.h:284` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getCoordinateFrameFast within App - World Simulation & Physics. Coordinates interactions with `RBXASSERT_FISHING, pvIsUpToDate`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `RBXASSERT_FISHING`, `pvIsUpToDate`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getCoordinateFrameFast`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 46. `getCoordinateFrame`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
CoordinateFrame& getCoordinateFrame() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `CoordinateFrame&` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8kernel/Body.h:289` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getCoordinateFrame within App - World Simulation & Physics. Coordinates interactions with `updatePV`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `updatePV`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getCoordinateFrame`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 47. `getVelocity`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Velocity& getVelocity() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Velocity&` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8kernel/Body.h:294` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getVelocity within App - World Simulation & Physics. Coordinates interactions with `updatePV`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `updatePV`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getVelocity`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 48. `getCanThrottle`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool getCanThrottle() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8kernel/Body.h:299` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getCanThrottle within App - World Simulation & Physics.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getCanThrottle`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 49. `accumulateImpulseAtBranchCofm`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void accumulateImpulseAtBranchCofm(const Vector3& impulse);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:303` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes accumulateImpulseAtBranchCofm within App - World Simulation & Physics. Coordinates interactions with `getRootSimBody`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getRootSimBody`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `accumulateImpulseAtBranchCofm`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 50. `accumulateLinearImpulse`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void accumulateLinearImpulse(const Vector3& impulse, const Vector3& worldPos);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:309` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes accumulateLinearImpulse within App - World Simulation & Physics. Coordinates interactions with `getRootSimBody, accumulateImpulse`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getRootSimBody`, `accumulateImpulse`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `accumulateLinearImpulse`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 51. `accumulateRotationalImpulse`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void accumulateRotationalImpulse(const Vector3& impulse);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:315` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes accumulateRotationalImpulse within App - World Simulation & Physics. Coordinates interactions with `getRootSimBody`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getRootSimBody`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `accumulateRotationalImpulse`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 52. `accumulateForceAtBranchCofm`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void accumulateForceAtBranchCofm(const Vector3& force);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:321` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes accumulateForceAtBranchCofm within App - World Simulation & Physics. Coordinates interactions with `RBXASSERT, getRoot, getRootSimBody, accumulateForceCofm`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `RBXASSERT`, `getRoot`, `getRootSimBody`, `accumulateForceCofm`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `accumulateForceAtBranchCofm`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 53. `accumulateForce`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void accumulateForce(const Vector3& force, const Vector3& worldPos);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:328` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes accumulateForce within App - World Simulation & Physics. Coordinates interactions with `getRootSimBody`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getRootSimBody`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `accumulateForce`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 54. `accumulateTorque`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void accumulateTorque(const Vector3& torque);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:334` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes accumulateTorque within App - World Simulation & Physics. Coordinates interactions with `getRootSimBody`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getRootSimBody`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `accumulateTorque`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 55. `resetForceAccumulators`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void resetForceAccumulators();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:340` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes resetForceAccumulators within App - World Simulation & Physics. Coordinates interactions with `getRootSimBody`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getRootSimBody`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `resetForceAccumulators`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 56. `resetImpulseAccumulators`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void resetImpulseAccumulators();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:346` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes resetImpulseAccumulators within App - World Simulation & Physics. Coordinates interactions with `getRootSimBody`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getRootSimBody`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `resetImpulseAccumulators`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 57. `getBranchForce`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector3& getBranchForce() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector3&` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8kernel/Body.h:352` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getBranchForce within App - World Simulation & Physics. Coordinates interactions with `RBXASSERT, getRoot, getConstRootSimBody, getForce`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `RBXASSERT`, `getRoot`, `getConstRootSimBody`, `getForce`, `zero`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getBranchForce`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 58. `getBranchTorque`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector3& getBranchTorque() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector3&` |
| **Modifiers** | `const const` |
| **Source Location** | `App/include/v8kernel/Body.h:358` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getBranchTorque within App - World Simulation & Physics. Coordinates interactions with `RBXASSERT, getRoot, getConstRootSimBody, getTorque`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `RBXASSERT`, `getRoot`, `getConstRootSimBody`, `getTorque`, `zero`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getBranchTorque`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 59. `getBranchVelocity`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Velocity& getBranchVelocity() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Velocity&` |
| **Modifiers** | `const` |
| **Source Location** | `App/include/v8kernel/Body.h:364` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

Executes getBranchVelocity within App - World Simulation & Physics. Coordinates interactions with `RBXASSERT, getRoot, getRootSimBody, getPV`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `RBXASSERT`, `getRoot`, `getRootSimBody`, `getPV`, `zero`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getBranchVelocity`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 60. `setParent`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void setParent(Body* parent);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/include/v8kernel/Body.h:374` |
| **Subsystem** | `App - World Simulation & Physics` |

#### How it Works Internally

setting properties

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `setIndexedTreeParent`.

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


:::tip Additional Functions
There are **1982 additional internal and inline functions** in this subsystem. All functions are indexed and cross-referenced in the **[Complete Function Catalog](./function-catalog.md)**.
:::

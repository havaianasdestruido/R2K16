---
sidebar_position: 6
title: App - Solvers & Humanoids
description: PGS constraint solver, Featherstone mechanics, and Humanoid state machine.
---

# App - Solvers & Humanoids

PGS constraint solver, Featherstone mechanics, and Humanoid state machine.


## FAQ

### How do I investigate a solver or humanoid change?

Trace the relevant solver constraint or humanoid state and its callers, then look for simulation tests. The generated catalog cannot prove numerical stability.

### How can I investigate this in the repository?

From the repository root, search the relevant tracked files for a starting point (results are leads, not proof of behavior):

```bash
git grep -n -i -F -- 'Constraint' -- App/solver
```

Read the surrounding implementation and callers, and check relevant tests before making changes. A search may return no matches when terminology or tracked files change.

## Subsystem Metrics

- **Total Documented Functions:** `660`
- **Functions Exercised in Tests:** `44`
- **Platform-Divergent Implementations:** `12`
- **Component Source Files:** `33`

## Source Files

<details>
<summary>View all 33 source files in this subsystem</summary>

| Source File | Path |
| :--- | :--- |
| `Balancing.cpp` | `App/humanoid/Balancing.cpp` |
| `FallingDown.cpp` | `App/humanoid/FallingDown.cpp` |
| `Flying.cpp` | `App/humanoid/Flying.cpp` |
| `Freefall.cpp` | `App/humanoid/Freefall.cpp` |
| `Humanoid.cpp` | `App/humanoid/Humanoid.cpp` |
| `HumanoidState.cpp` | `App/humanoid/HumanoidState.cpp` |
| `Jumping.cpp` | `App/humanoid/Jumping.cpp` |
| `MovingNoPhysicsBase.cpp` | `App/humanoid/MovingNoPhysicsBase.cpp` |
| `Ragdoll.cpp` | `App/humanoid/Ragdoll.cpp` |
| `Running.cpp` | `App/humanoid/Running.cpp` |
| `RunningBase.cpp` | `App/humanoid/RunningBase.cpp` |
| `StatusInstance.cpp` | `App/humanoid/StatusInstance.cpp` |
| `Swimming.cpp` | `App/humanoid/Swimming.cpp` |
| `Balancing.h` | `App/include/humanoid/Balancing.h` |
| `Freefall.h` | `App/include/humanoid/Freefall.h` |
| `Humanoid.h` | `App/include/humanoid/Humanoid.h` |
| `HumanoidState.h` | `App/include/humanoid/HumanoidState.h` |
| `Jumping.h` | `App/include/humanoid/Jumping.h` |
| `RunningBase.h` | `App/include/humanoid/RunningBase.h` |
| `Swimming.h` | `App/include/humanoid/Swimming.h` |
| `Constraint.h` | `App/include/solver/Constraint.h` |
| `ConstraintJacobian.h` | `App/include/solver/ConstraintJacobian.h` |
| `DebugSerializer.h` | `App/include/solver/DebugSerializer.h` |
| `Solver.h` | `App/include/solver/Solver.h` |
| `SolverBody.h` | `App/include/solver/SolverBody.h` |
| `SolverContainers.h` | `App/include/solver/SolverContainers.h` |
| `SolverProfiler.h` | `App/include/solver/SolverProfiler.h` |
| `SolverSerializer.h` | `App/include/solver/SolverSerializer.h` |
| `Constraint.cpp` | `App/solver/Constraint.cpp` |
| `ConstraintJacobian.cpp` | `App/solver/ConstraintJacobian.cpp` |
| `Solver.cpp` | `App/solver/Solver.cpp` |
| `SolverBody.cpp` | `App/solver/SolverBody.cpp` |
| `SolverKernel.cpp` | `App/solver/SolverKernel.cpp` |

</details>

---

## Function Reference

### 1. `Balancing::balanceRate`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int Balancing::balanceRate(double torqueMag);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Balancing.cpp:32` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes balanceRate within App - Solvers & Humanoids. Coordinates interactions with `return`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `balanceRate`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 2. `Balancing::balanceRateForPGS`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int Balancing::balanceRateForPGS();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Balancing.cpp:42` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes balanceRateForPGS within App - Solvers & Humanoids.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `balanceRateForPGS`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 3. `Balancing::onComputeForceImpl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Balancing::onComputeForceImpl();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Balancing.cpp:47` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes onComputeForceImpl within App - Solvers & Humanoids. Coordinates interactions with `RBXASSERT, getHumanoid, isInKernel, getRootBodyFast`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `RBXASSERT`, `getHumanoid`, `isInKernel`, `getRootBodyFast`, `accumulateTorque`, `getTorsoBodyFast`, `getCoordinateFrame`, `column`, `unitY`, `cross`, `getVelocity`, `getBranchTorque`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onComputeForceImpl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 4. `Dead::onStepImpl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Dead::onStepImpl();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/FallingDown.cpp:28` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes onStepImpl within App - Solvers & Humanoids. Coordinates interactions with `backendProcessing, getHumanoid, setHealth`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `backendProcessing`, `getHumanoid`, `setHealth`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onStepImpl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 5. `Dead::onSimulatorStepImpl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Dead::onSimulatorStepImpl(float stepDt);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/FallingDown.cpp:35` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes onSimulatorStepImpl within App - Solvers & Humanoids. Coordinates interactions with `getHumanoid, breakJointsOnDeath, getCharacterFromHumanoid, breakJoints`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getHumanoid`, `breakJointsOnDeath`, `getCharacterFromHumanoid`, `breakJoints`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onSimulatorStepImpl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 6. `Flying::onSimulatorStepImpl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Flying::onSimulatorStepImpl(float stepDt);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Flying.cpp:21` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes onSimulatorStepImpl within App - Solvers & Humanoids.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onSimulatorStepImpl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 7. `Flying::onComputeForceImpl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Flying::onComputeForceImpl();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Flying.cpp:27` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes onComputeForceImpl within App - Solvers & Humanoids.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onComputeForceImpl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 8. `Freefall::characterVelocityInfluence`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
float Freefall::characterVelocityInfluence();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `float` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Freefall.cpp:16` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes characterVelocityInfluence within App - Solvers & Humanoids.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `characterVelocityInfluence`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 9. `Freefall::floorVelocityInfluence`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
float Freefall::floorVelocityInfluence();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `float` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Freefall.cpp:18` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes floorVelocityInfluence within App - Solvers & Humanoids.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `floorVelocityInfluence`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 10. `Freefall::velocityDecay`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
float Freefall::velocityDecay();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `float` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Freefall.cpp:19` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes velocityDecay within App - Solvers & Humanoids.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `velocityDecay`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 11. `Freefall::kTurnSpeed`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
float Freefall::kTurnSpeed();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `float` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Freefall.cpp:58` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes kTurnSpeed within App - Solvers & Humanoids.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `kTurnSpeed`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 12. `Freefall::kTurnSpeedForPGS`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
float Freefall::kTurnSpeedForPGS();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `float` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Freefall.cpp:62` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes kTurnSpeedForPGS within App - Solvers & Humanoids.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `kTurnSpeedForPGS`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 13. `Freefall::onSimulatorStepImpl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Freefall::onSimulatorStepImpl(const float stepDt);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Freefall.cpp:66` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes onSimulatorStepImpl within App - Solvers & Humanoids. Coordinates interactions with `getHumanoid, getTorsoSlow, characterVelocityInfluence, getLinearVelocity`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getHumanoid`, `getTorsoSlow`, `characterVelocityInfluence`, `getLinearVelocity`, `floorVelocityInfluence`, `getFloorPointVelocity`, `calcDesiredWalkVelocity`, `magnitude`, `zero`, `radWrap`, `getHeading`, `getTorsoHeading`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onSimulatorStepImpl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 14. `Freefall::onComputeForceImpl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Freefall::onComputeForceImpl();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Freefall.cpp:114` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes onComputeForceImpl within App - Solvers & Humanoids. Coordinates interactions with `getHumanoid, getRootBodyFast, getWorld, getUsingPGSSolver`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getHumanoid`, `getRootBodyFast`, `getWorld`, `getUsingPGSSolver`, `kTurnP`, `getBranchIBodyV3`, `getVelocity`, `kTurnPForFreeFallPGS`, `kTurnAccelMax`, `getBranchTorque`, `clamp`, `accumulateTorque`.
- **External Library Dependencies:** `G3D Graphics and Math Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onComputeForceImpl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 15. `Humanoid::isStateInString`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool Humanoid::isStateInString(const std::string& text, const HUMAN::StateType &compare, HUMAN::StateType& value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:238` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes isStateInString within App - Solvers & Humanoids. Coordinates interactions with `getStateNameByType`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getStateNameByType`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isStateInString`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 16. `getAppendageString`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string& getAppendageString(size_t appendage, bool R15) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string&` |
| **Modifiers** | `static const` |
| **Source Location** | `App/humanoid/Humanoid.cpp:283` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes getAppendageString within App - Solvers & Humanoids. Coordinates interactions with `RBXASSERT`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `RBXASSERT`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getAppendageString`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 17. `collectStatus`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void collectStatus(shared_ptr<RBX::Instance> instance, Reflection::ValueArray* result);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:372` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes collectStatus within App - Solvers & Humanoids. Coordinates interactions with `singleton, lookup, getName, c_str`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `singleton`, `lookup`, `getName`, `c_str`, `convertToValue`, `push_back`, `getStatuses`, `result`, `getStatusFast`, `visitChildren`, `bind`, `get`.
- **External Library Dependencies:** `Boost C++ Libraries`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `collectStatus`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 18. `Humanoid::getStatuses`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
shared_ptr<const Reflection::ValueArray> Humanoid::getStatuses();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `shared_ptr&lt;const Reflection::ValueArray&gt;` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:387` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes getStatuses within App - Solvers & Humanoids. Coordinates interactions with `result, getStatusFast, visitChildren, bind`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `result`, `getStatusFast`, `visitChildren`, `bind`, `get`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getStatuses`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 19. `Humanoid::hasStatus`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool Humanoid::hasStatus(Status newStatus);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:396` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes hasStatus within App - Solvers & Humanoids. Coordinates interactions with `hasCustomStatus, singleton, convertToString`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `hasCustomStatus`, `singleton`, `convertToString`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `hasStatus`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 20. `Humanoid::hasCustomStatus`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool Humanoid::hasCustomStatus(std::string name);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:401` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes hasCustomStatus within App - Solvers & Humanoids. Coordinates interactions with `getStatusFast, findFirstChildByName`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getStatusFast`, `findFirstChildByName`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `hasCustomStatus`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 21. `Humanoid::addCustomStatus`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool Humanoid::addCustomStatus(std::string name);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:412` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes addCustomStatus within App - Solvers & Humanoids. Coordinates interactions with `getStatusFast, findFirstChildByName, setName, setValue`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT); C++ exception throw on invalid state or failure; Exception handling block (try/catch recovery).
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `getStatusFast`, `findFirstChildByName`, `setName`, `setValue`, `setParent`, `addStatus`, `singleton`, `convertToString`, `removeCustomStatus`, `removeStatus`, `setNameOcclusion`, `raisePropertyChanged`.
- **External Library Dependencies:** `Boost C++ Libraries`, `G3D Graphics and Math Engine`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `addCustomStatus`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 22. `Humanoid::addStatus`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool Humanoid::addStatus(Status newStatus);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:428` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes addStatus within App - Solvers & Humanoids. Coordinates interactions with `addCustomStatus, singleton, convertToString`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `addCustomStatus`, `singleton`, `convertToString`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `addStatus`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 23. `Humanoid::removeCustomStatus`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool Humanoid::removeCustomStatus(std::string name);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:433` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes removeCustomStatus within App - Solvers & Humanoids. Coordinates interactions with `getStatusFast, findFirstChildByName, setParent`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getStatusFast`, `findFirstChildByName`, `setParent`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `removeCustomStatus`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 24. `Humanoid::removeStatus`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool Humanoid::removeStatus(Status newStatus);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:447` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes removeStatus within App - Solvers & Humanoids. Coordinates interactions with `removeCustomStatus, singleton, convertToString`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `removeCustomStatus`, `singleton`, `convertToString`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `removeStatus`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 25. `Humanoid::setNameOcclusion`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Humanoid::setNameOcclusion(NameOcclusion value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:452` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes setNameOcclusion within App - Solvers & Humanoids. Coordinates interactions with `raisePropertyChanged`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `raisePropertyChanged`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setNameOcclusion`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 26. `Humanoid::setDisplayDistanceType`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Humanoid::setDisplayDistanceType(HumanoidDisplayDistanceType value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:461` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes setDisplayDistanceType within App - Solvers & Humanoids. Coordinates interactions with `raisePropertyChanged`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `raisePropertyChanged`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setDisplayDistanceType`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 27. `Humanoid::onDescendantAdded`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Humanoid::onDescendantAdded(Instance* instance);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:470` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes onDescendantAdded within App - Solvers & Humanoids. Coordinates interactions with `getParent, getStatusFast, singleton, convertToValue`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getParent`, `getStatusFast`, `singleton`, `convertToValue`, `getName`, `c_str`, `statusAddedSignal`, `customStatusAddedSignal`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onDescendantAdded`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 28. `Humanoid::onDescendantRemoving`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Humanoid::onDescendantRemoving(const shared_ptr<Instance>& instance);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:482` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes onDescendantRemoving within App - Solvers & Humanoids. Coordinates interactions with `getParent, getStatusFast, singleton, convertToValue`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getParent`, `getStatusFast`, `singleton`, `convertToValue`, `getName`, `c_str`, `statusRemovedSignal`, `customStatusRemovedSignal`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onDescendantRemoving`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 29. `Humanoid::onServiceProvider`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Humanoid::onServiceProvider(ServiceProvider* oldProvider, ServiceProvider* newProvider);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:493` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes onServiceProvider within App - Solvers & Humanoids. Coordinates interactions with `connect, bind, backendProcessing, impersonate`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `connect`, `bind`, `backendProcessing`, `impersonate`, `getForceR15`, `setRigType`, `disconnect`, `onServiceProviderIStepped`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onServiceProvider`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 30. `Humanoid::getDead`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool Humanoid::getDead() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `App/humanoid/Humanoid.cpp:527` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes getDead within App - Solvers & Humanoids. Coordinates interactions with `RBXASSERT, get, return, getStateType`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `RBXASSERT`, `get`, `return`, `getStateType`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getDead`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 31. `Humanoid::setWalkSpeed`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Humanoid::setWalkSpeed(float value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:539` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes setWalkSpeed within App - Solvers & Humanoids. Coordinates interactions with `raisePropertyChanged`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `raisePropertyChanged`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setWalkSpeed`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 32. `Humanoid::setPercentWalkSpeed`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Humanoid::setPercentWalkSpeed(float value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:552` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes setPercentWalkSpeed within App - Solvers & Humanoids. Coordinates interactions with `clamp`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `clamp`.
- **External Library Dependencies:** `G3D Graphics and Math Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setPercentWalkSpeed`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 33. `Humanoid::setJumpPower`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Humanoid::setJumpPower(float value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:562` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes setJumpPower within App - Solvers & Humanoids. Coordinates interactions with `clamp, raisePropertyChanged`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `clamp`, `raisePropertyChanged`.
- **External Library Dependencies:** `G3D Graphics and Math Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setJumpPower`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 34. `Humanoid::setMaxSlopeAngle`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Humanoid::setMaxSlopeAngle(float value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:573` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes setMaxSlopeAngle within App - Solvers & Humanoids. Coordinates interactions with `clamp, raisePropertyChanged`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `clamp`, `raisePropertyChanged`.
- **External Library Dependencies:** `G3D Graphics and Math Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setMaxSlopeAngle`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 35. `Humanoid::setHipHeight`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Humanoid::setHipHeight(float value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:585` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes setHipHeight within App - Solvers & Humanoids. Coordinates interactions with `raisePropertyChanged`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `raisePropertyChanged`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setHipHeight`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 36. `Humanoid::setHealth`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Humanoid::setHealth(float value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:594` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes setHealth within App - Solvers & Humanoids. Coordinates interactions with `updateHadHealth, raisePropertyChanged, healthChangedSignal`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `updateHadHealth`, `raisePropertyChanged`, `healthChangedSignal`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setHealth`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 37. `Humanoid::setHealthUi`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Humanoid::setHealthUi(float value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:605` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes setHealthUi within App - Solvers & Humanoids. Coordinates interactions with `clamp, raisePropertyChanged, setHealth`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `clamp`, `raisePropertyChanged`, `setHealth`.
- **External Library Dependencies:** `G3D Graphics and Math Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setHealthUi`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 38. `Humanoid::setMaxHealth`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Humanoid::setMaxHealth(float value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:620` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes setMaxHealth within App - Solvers & Humanoids. Coordinates interactions with `raisePropertyChanged, healthChangedSignal`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `raisePropertyChanged`, `healthChangedSignal`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setMaxHealth`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 39. `Humanoid::getConstLocalHumanoidFromContext`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Humanoid* Humanoid::getConstLocalHumanoidFromContext(const Instance* context) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Humanoid*` |
| **Modifiers** | `const` |
| **Source Location** | `App/humanoid/Humanoid.cpp:645` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes getConstLocalHumanoidFromContext within App - Solvers & Humanoids. Coordinates interactions with `findConstLocalCharacter, modelIsConstCharacter`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `findConstLocalCharacter`, `modelIsConstCharacter`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getConstLocalHumanoidFromContext`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 40. `Humanoid::getLocalHumanoidFromContext`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Humanoid* Humanoid::getLocalHumanoidFromContext(Instance* context);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Humanoid*` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:655` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes getLocalHumanoidFromContext within App - Solvers & Humanoids. Coordinates interactions with `findLocalCharacter, modelIsCharacter`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `findLocalCharacter`, `modelIsCharacter`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getLocalHumanoidFromContext`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 41. `Humanoid::getLocalHeadFromContext`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
PartInstance* Humanoid::getLocalHeadFromContext(Instance* context);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `PartInstance*` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:665` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes getLocalHeadFromContext within App - Solvers & Humanoids. Coordinates interactions with `findLocalCharacter, getHeadFromCharacter`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `findLocalCharacter`, `getHeadFromCharacter`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getLocalHeadFromContext`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 42. `Humanoid::getConstLocalHeadFromContext`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
PartInstance* Humanoid::getConstLocalHeadFromContext(const Instance* context) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `PartInstance*` |
| **Modifiers** | `const` |
| **Source Location** | `App/humanoid/Humanoid.cpp:671` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes getConstLocalHeadFromContext within App - Solvers & Humanoids. Coordinates interactions with `findConstLocalCharacter, getConstHeadFromCharacter`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `findConstLocalCharacter`, `getConstHeadFromCharacter`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getConstLocalHeadFromContext`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 43. `Humanoid::getConstHeadFromCharacter`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
PartInstance* Humanoid::getConstHeadFromCharacter(const ModelInstance* character) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `PartInstance*` |
| **Modifiers** | `const` |
| **Source Location** | `App/humanoid/Humanoid.cpp:677` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes getConstHeadFromCharacter within App - Solvers & Humanoids. Coordinates interactions with `return, findConstFirstChildByName`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `return`, `findConstFirstChildByName`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getConstHeadFromCharacter`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 44. `Humanoid::getHeadFromCharacter`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
PartInstance* Humanoid::getHeadFromCharacter(ModelInstance* character);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `PartInstance*` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:685` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes getHeadFromCharacter within App - Solvers & Humanoids. Coordinates interactions with `getConstHeadFromCharacter`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getConstHeadFromCharacter`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getHeadFromCharacter`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 45. `Humanoid::getGrip`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Weld* Humanoid::getGrip(Instance* character);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Weld*` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:690` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes getGrip within App - Solvers & Humanoids. Coordinates interactions with `modelIsCharacter, getRightArmSlow, findFirstChildByName`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `modelIsCharacter`, `getRightArmSlow`, `findFirstChildByName`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getGrip`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 46. `newJoint`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
shared_ptr<JointInstance> newJoint(bool animated);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `shared_ptr&lt;JointInstance&gt;` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:703` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes newJoint within App - Solvers & Humanoids. Coordinates interactions with `setMaxVelocity`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `setMaxVelocity`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `newJoint`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 47. `Humanoid::setRigType`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Humanoid::setRigType(HumanoidRigType type);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:716` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes setRigType within App - Solvers & Humanoids. Coordinates interactions with `current, requirePermission, raisePropertyChanged, singleton`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** C++ exception throw on invalid state or failure; Exception handling block (try/catch recovery).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `current`, `requirePermission`, `raisePropertyChanged`, `singleton`, `printf`, `getParent`, `shared_from`, `findFirstChildByName`, `getAppendageString`, `getUseR15`, `updateSiblingPropertyListener`, `updateBaseInstance`.
- **External Library Dependencies:** `Boost C++ Libraries`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setRigType`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 48. `createJoint`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void createJoint(const std::string& jointName, Attachment& parentAttachment, Attachment& partForJointAttachment);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `App/humanoid/Humanoid.cpp:751` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes createJoint within App - Solvers & Humanoids. Coordinates interactions with `getParent, setName, setPart0, setPart1`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getParent`, `setName`, `setPart0`, `setPart1`, `setC0`, `getFrameInPart`, `setC1`, `setParent`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `createJoint`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 49. `Humanoid::buildJointsFromAttachments`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Humanoid::buildJointsFromAttachments(PartInstance* part, std::vector<PartInstance*>& characterParts);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:767` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes buildJointsFromAttachments within App - Solvers & Humanoids. Coordinates interactions with `getChildren2, end, begin, get`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getChildren2`, `end`, `begin`, `get`, `getName`, `find`, `joints`, `substr`, `findConstFirstChildByName`, `findFirstChildByName`, `createJoint`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `buildJointsFromAttachments`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 50. `Humanoid::buildJoints`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Humanoid::buildJoints(RBX::DataModel* dm);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:821` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Server side

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new; Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** TaskScheduler global job queue dispatching.
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT); Defensive null-pointer validation guard.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `setValue`, `get`, `setParent`, `getCharacterFromHumanoid`, `RBXASSERT`, `getForceR15`, `getTorsoFast`, `getParts`, `buildJointsFromAttachments`, `getHeadSlow`, `getAppendageSlow`, `getRightArmSlow`.
- **External Library Dependencies:** `Boost C++ Libraries`, `G3D Graphics and Math Engine`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `buildJoints`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 51. `Humanoid::askSetParent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool Humanoid::askSetParent(const Instance* instance) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `App/humanoid/Humanoid.cpp:921` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes askSetParent within App - Solvers & Humanoids.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `askSetParent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 52. `Humanoid::constHumanoidFromBodyPart`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Humanoid* Humanoid::constHumanoidFromBodyPart(const Instance* bodyPart) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Humanoid*` |
| **Modifiers** | `const` |
| **Source Location** | `App/humanoid/Humanoid.cpp:930` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes constHumanoidFromBodyPart within App - Solvers & Humanoids. Coordinates interactions with `modelIsConstCharacter, getParent`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `modelIsConstCharacter`, `getParent`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `constHumanoidFromBodyPart`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 53. `Humanoid::constHumanoidFromDescendant`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Humanoid* Humanoid::constHumanoidFromDescendant(const Instance* bodyPart) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Humanoid*` |
| **Modifiers** | `const` |
| **Source Location** | `App/humanoid/Humanoid.cpp:935` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes constHumanoidFromDescendant within App - Solvers & Humanoids. Coordinates interactions with `getParent, modelIsConstCharacter`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getParent`, `modelIsConstCharacter`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `constHumanoidFromDescendant`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 54. `Humanoid::humanoidFromBodyPart`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Humanoid* Humanoid::humanoidFromBodyPart(Instance* bodyPart);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Humanoid*` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:952` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes humanoidFromBodyPart within App - Solvers & Humanoids. Coordinates interactions with `modelIsCharacter, getParent, constHumanoidFromBodyPart`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `modelIsCharacter`, `getParent`, `constHumanoidFromBodyPart`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `humanoidFromBodyPart`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 55. `Humanoid::modelIsConstCharacter`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Humanoid* Humanoid::modelIsConstCharacter(const Instance* testModel) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Humanoid*` |
| **Modifiers** | `const` |
| **Source Location** | `App/humanoid/Humanoid.cpp:963` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

abstract so as not to include Humanoid in general code for now - anything with a humanoid directly below it comes up yes

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `modelIsConstCharacter`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 56. `Humanoid::modelIsCharacter`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Humanoid* Humanoid::modelIsCharacter(Instance* testModel);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Humanoid*` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:967` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes modelIsCharacter within App - Solvers & Humanoids. Coordinates interactions with `modelIsConstCharacter`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `modelIsConstCharacter`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `modelIsCharacter`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 57. `Humanoid::getConstCharacterFromHumanoid`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
ModelInstance* Humanoid::getConstCharacterFromHumanoid(const Humanoid* humanoid) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `ModelInstance*` |
| **Modifiers** | `const` |
| **Source Location** | `App/humanoid/Humanoid.cpp:972` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes getConstCharacterFromHumanoid within App - Solvers & Humanoids. Coordinates interactions with `getParent`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getParent`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getConstCharacterFromHumanoid`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 58. `Humanoid::getCharacterFromHumanoid`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
ModelInstance* Humanoid::getCharacterFromHumanoid(Humanoid* humanoid);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `ModelInstance*` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:985` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes getCharacterFromHumanoid within App - Solvers & Humanoids. Coordinates interactions with `getConstCharacterFromHumanoid`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getConstCharacterFromHumanoid`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getCharacterFromHumanoid`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 59. `Humanoid::hasWalkToPoint`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool Humanoid::hasWalkToPoint(Vector3& worldPosition) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `App/humanoid/Humanoid.cpp:994` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Controller stuff

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getPlayerFromCharacter`, `getCharacterFromHumanoid`, `singleton`, `inHybridMode`, `inMousepanMode`, `get`, `findConstWorkspace`, `contextInWorkspace`, `getCoordinateFrame`, `pointToWorldSpace`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `hasWalkToPoint`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 60. `Humanoid::getCurrentStateType`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
HUMAN::StateType Humanoid::getCurrentStateType();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `HUMAN::StateType` |
| **Modifiers** | None |
| **Source Location** | `App/humanoid/Humanoid.cpp:1021` |
| **Subsystem** | `App - Solvers & Humanoids` |

#### How it Works Internally

Executes getCurrentStateType within App - Solvers & Humanoids. Coordinates interactions with `get, getStateType`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `get`, `getStateType`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getCurrentStateType`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---


:::tip Additional Functions
There are **600 additional internal and inline functions** in this subsystem. All functions are indexed and cross-referenced in the **[Complete Function Catalog](./function-catalog.md)**.
:::

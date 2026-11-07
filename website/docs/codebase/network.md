---
sidebar_position: 15
title: Network & Replication
description: RakNet replication stack, Client/Server Replicators, physics senders/receivers.
---

# Network & Replication

RakNet replication stack, Client/Server Replicators, physics senders/receivers.

## Subsystem Metrics

- **Total Documented Functions:** `1546`
- **Functions Exercised in Tests:** `100`
- **Platform-Divergent Implementations:** `168`
- **Component Source Files:** `100`

## Source Files

<details>
<summary>View all 100 source files in this subsystem</summary>

| Source File | Path |
| :--- | :--- |
| `API.cpp` | `Network/API.cpp` |
| `BoostAppend.cpp` | `Network/BoostAppend.cpp` |
| `ChatFilter.cpp` | `Network/ChatFilter.cpp` |
| `Client.cpp` | `Network/Client.cpp` |
| `Client.h` | `Network/Client.h` |
| `ClientReplicator.cpp` | `Network/ClientReplicator.cpp` |
| `ClientReplicator.h` | `Network/ClientReplicator.h` |
| `ClusterUpdateBuffer.cpp` | `Network/ClusterUpdateBuffer.cpp` |
| `ClusterUpdateBuffer.h` | `Network/ClusterUpdateBuffer.h` |
| `Compressor.cpp` | `Network/Compressor.cpp` |
| `ConcurrentRakPeer.cpp` | `Network/ConcurrentRakPeer.cpp` |
| `ConcurrentRakPeer.h` | `Network/ConcurrentRakPeer.h` |
| `CrashReporter.cpp` | `Network/CrashReporter.cpp` |
| `DataBlockEncryptor.cpp` | `Network/DataBlockEncryptor.cpp` |
| `Dictionary.cpp` | `Network/Dictionary.cpp` |
| `Dictionary.h` | `Network/Dictionary.h` |
| `DirectPhysicsReceiver.cpp` | `Network/DirectPhysicsReceiver.cpp` |
| `ErrorCompPhysicsSender.cpp` | `Network/ErrorCompPhysicsSender.cpp` |
| `ErrorCompPhysicsSender2.cpp` | `Network/ErrorCompPhysicsSender2.cpp` |
| `ErrorCompPhysicsSender2.h` | `Network/ErrorCompPhysicsSender2.h` |
| `GameConfigurer.cpp` | `Network/GameConfigurer.cpp` |
| `GamePerfMonitor.cpp` | `Network/GamePerfMonitor.cpp` |
| `GamePerfMonitor.h` | `Network/GamePerfMonitor.h` |
| `InterpolatingPhysicsReceiver.cpp` | `Network/InterpolatingPhysicsReceiver.cpp` |
| `InterpolatingPhysicsReceiver.h` | `Network/InterpolatingPhysicsReceiver.h` |
| `Item.cpp` | `Network/Item.cpp` |
| `Item.h` | `Network/Item.h` |
| `Marker.cpp` | `Network/Marker.cpp` |
| `MechanismItem.cpp` | `Network/MechanismItem.cpp` |
| `MechanismItem.h` | `Network/MechanismItem.h` |
| `MovementHistoryJob.cpp` | `Network/MovementHistoryJob.cpp` |
| `NetPmc.cpp` | `Network/NetPmc.cpp` |
| `NetworkClusterPacketCache.cpp` | `Network/NetworkClusterPacketCache.cpp` |
| `NetworkFilter.cpp` | `Network/NetworkFilter.cpp` |
| `NetworkOwnerJob.cpp` | `Network/NetworkOwnerJob.cpp` |
| `NetworkPacketCache.cpp` | `Network/NetworkPacketCache.cpp` |
| `NetworkProfiler.cpp` | `Network/NetworkProfiler.cpp` |
| `NetworkProfiler.h` | `Network/NetworkProfiler.h` |
| `NetworkSettings.cpp` | `Network/NetworkSettings.cpp` |
| `NetworkSettings.h` | `Network/NetworkSettings.h` |
| `OrderedSet.h` | `Network/OrderedSet.h` |
| `Peer.cpp` | `Network/Peer.cpp` |
| `PersistentDataStore.cpp` | `Network/PersistentDataStore.cpp` |
| `PersistentDataStore.h` | `Network/PersistentDataStore.h` |
| `PhysicsReceiver.cpp` | `Network/PhysicsReceiver.cpp` |
| `PhysicsReceiver.h` | `Network/PhysicsReceiver.h` |
| `PhysicsSender.cpp` | `Network/PhysicsSender.cpp` |
| `Player.cpp` | `Network/Player.cpp` |
| `Players.cpp` | `Network/Players.cpp` |
| `PropertySynchronization.h` | `Network/PropertySynchronization.h` |
| `Replicator.ChangePropertyItem.cpp` | `Network/Replicator.ChangePropertyItem.cpp` |
| `Replicator.DeleteInstanceItem.cpp` | `Network/Replicator.DeleteInstanceItem.cpp` |
| `Replicator.EventInvocationItem.cpp` | `Network/Replicator.EventInvocationItem.cpp` |
| `Replicator.GCJob.cpp` | `Network/Replicator.GCJob.cpp` |
| `Replicator.GCJob.h` | `Network/Replicator.GCJob.h` |
| `Replicator.HashItem.cpp` | `Network/Replicator.HashItem.cpp` |
| `Replicator.ItemSender.cpp` | `Network/Replicator.ItemSender.cpp` |
| `Replicator.JoinDataItem.cpp` | `Network/Replicator.JoinDataItem.cpp` |
| `Replicator.JoinDataItem.h` | `Network/Replicator.JoinDataItem.h` |
| `Replicator.MarkerItem.cpp` | `Network/Replicator.MarkerItem.cpp` |
| `Replicator.NewInstanceItem.cpp` | `Network/Replicator.NewInstanceItem.cpp` |
| `Replicator.NewInstanceItem.h` | `Network/Replicator.NewInstanceItem.h` |
| `Replicator.PingBackItem.cpp` | `Network/Replicator.PingBackItem.cpp` |
| `Replicator.PingItem.cpp` | `Network/Replicator.PingItem.cpp` |
| `Replicator.PingJob.h` | `Network/Replicator.PingJob.h` |
| `Replicator.ProcessPacketsJob.h` | `Network/Replicator.ProcessPacketsJob.h` |
| `Replicator.ReferencePropertyChangedItem.cpp` | `Network/Replicator.ReferencePropertyChangedItem.cpp` |
| `Replicator.RockyItem.cpp` | `Network/Replicator.RockyItem.cpp` |
| `Replicator.SendDataJob.h` | `Network/Replicator.SendDataJob.h` |
| `Replicator.StatsItem.cpp` | `Network/Replicator.StatsItem.cpp` |
| `Replicator.StatsItem.h` | `Network/Replicator.StatsItem.h` |
| `Replicator.StreamJob.cpp` | `Network/Replicator.StreamJob.cpp` |
| `Replicator.StreamJob.h` | `Network/Replicator.StreamJob.h` |
| `Replicator.TagItem.cpp` | `Network/Replicator.TagItem.cpp` |
| `Replicator.cpp` | `Network/Replicator.cpp` |
| `Replicator.h` | `Network/Replicator.h` |
| `ReplicatorStats.cpp` | `Network/ReplicatorStats.cpp` |
| `RoundRobinPhysicsSender.cpp` | `Network/RoundRobinPhysicsSender.cpp` |
| `Server.cpp` | `Network/Server.cpp` |
| `Server.h` | `Network/Server.h` |
| `ServerReplicator.cpp` | `Network/ServerReplicator.cpp` |
| `ServerReplicator.h` | `Network/ServerReplicator.h` |
| `Streaming.cpp` | `Network/Streaming.cpp` |
| `Streaming.h` | `Network/Streaming.h` |
| `TopNErrorsPhysicsSender.cpp` | `Network/TopNErrorsPhysicsSender.cpp` |
| `TopNErrorsPhysicsSender.h` | `Network/TopNErrorsPhysicsSender.h` |
| `Util.cpp` | `Network/Util.cpp` |
| `WebChatFilter.cpp` | `Network/WebChatFilter.cpp` |
| `CompactCFrame.h` | `Network/include/network/CompactCFrame.h` |
| `CrashReporter.h` | `Network/include/network/CrashReporter.h` |
| `CrispProxy.h` | `Network/include/network/CrispProxy.h` |
| `GameConfigurer.h` | `Network/include/network/GameConfigurer.h` |
| `NetPmc.h` | `Network/include/network/NetPmc.h` |
| `NetworkClusterPacketCache.h` | `Network/include/network/NetworkClusterPacketCache.h` |
| `NetworkOwner.h` | `Network/include/network/NetworkOwner.h` |
| `NetworkPacketCache.h` | `Network/include/network/NetworkPacketCache.h` |
| `Player.h` | `Network/include/network/Player.h` |
| `Players.h` | `Network/include/network/Players.h` |
| `RakNetFast.h` | `Network/include/network/RakNetFast.h` |
| `rijndael.cpp` | `Network/rijndael.cpp` |

</details>

---

## Function Reference

### 1. `SafeInitFree`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
public: SafeInitFree();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `public:` |
| **Modifiers** | None |
| **Source Location** | `Network/API.cpp:74` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes SafeInitFree within Network & Replication. Coordinates interactions with `AddReference`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `AddReference`.
- **External Library Dependencies:** `RakNet UDP Networking Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `SafeInitFree`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 2. `RBX::Network::isPlayerAuthenticationEnabled`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool RBX::Network::isPlayerAuthenticationEnabled();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `Network/API.cpp:90` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes isPlayerAuthenticationEnabled within Network & Replication.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isPlayerAuthenticationEnabled`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 3. `RBX::Network::isNetworkClient`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool RBX::Network::isNetworkClient(const Instance* context);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `Network/API.cpp:95` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes isNetworkClient within Network & Replication.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isNetworkClient`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 4. `createSecureReplicator`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
shared_ptr<RBX::Network::ServerReplicator> createSecureReplicator(RakNet::SystemAddress a, RBX::Network::Server* s, RBX::NetworkSettings* networkSettings);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `shared_ptr&lt;RBX::Network::ServerReplicator&gt;` |
| **Modifiers** | `static` |
| **Source Location** | `Network/API.cpp:102` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes createSecureReplicator within Network & Replication.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `createSecureReplicator`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 5. `initVersion1`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void initVersion1();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `Network/API.cpp:107` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes initVersion1 within Network & Replication. Coordinates interactions with `externally, defined, rot13`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `externally`, `defined`, `rot13`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `initVersion1`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 6. `initVersion2`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void initVersion2();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `Network/API.cpp:130` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes initVersion2 within Network & Replication.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `initVersion2`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 7. `RBX::Network::initWithServerSecurity`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void RBX::Network::initWithServerSecurity();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Network/API.cpp:137` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes initWithServerSecurity within Network & Replication. Coordinates interactions with `initVersion1, initWithoutSecurity, defined, initVersion2`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `initVersion1`, `initWithoutSecurity`, `defined`, `initVersion2`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `initWithServerSecurity`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 8. `RBX::Network::initWithPlayerSecurity`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void RBX::Network::initWithPlayerSecurity();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Network/API.cpp:150` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes initWithPlayerSecurity within Network & Replication. Coordinates interactions with `initVersion1, initWithoutSecurity, initVersion2`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `initVersion1`, `initWithoutSecurity`, `initVersion2`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `initWithPlayerSecurity`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 9. `RBX::Network::initWithCloudEditSecurity`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void RBX::Network::initWithCloudEditSecurity();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Network/API.cpp:158` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes initWithCloudEditSecurity within Network & Replication.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `initWithCloudEditSecurity`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 10. `RBX::Network::initWithoutSecurity`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void RBX::Network::initWithoutSecurity();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Network/API.cpp:166` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes initWithoutSecurity within Network & Replication. Coordinates interactions with `VMProtectBeginMutation, classDescriptor, singleton, VMProtectEnd`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `VMProtectBeginMutation`, `classDescriptor`, `singleton`, `VMProtectEnd`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `initWithoutSecurity`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 11. `RBX::Network::setVersion`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void RBX::Network::setVersion(const char* version);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Network/API.cpp:188` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes setVersion within Network & Replication.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setVersion`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 12. `RBX::Network::setSecurityVersions`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void RBX::Network::setSecurityVersions(const std::vector<std::string>& versions);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Network/API.cpp:194` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes setSecurityVersions within Network & Replication. Coordinates interactions with `setAllowedSecurityVersions`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `setAllowedSecurityVersions`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setSecurityVersions`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 13. `RBX::Network::isTrustedContent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool RBX::Network::isTrustedContent(const char* url);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `Network/API.cpp:199` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes isTrustedContent within Network & Replication. Coordinates interactions with `isUrl, urlString, to_lower, find`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `isUrl`, `urlString`, `to_lower`, `find`, `substr`, `size`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isTrustedContent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 14. `isDebuggedDirectThreadFunc`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void isDebuggedDirectThreadFunc(weak_ptr<RBX::DataModel> weakDataModel);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Network/API.cpp:257` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes isDebuggedDirectThreadFunc within Network & Replication. Coordinates interactions with `defined, VMProtectBeginMutation, lock, VMProtectIsDebuggerPresent`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `defined`, `VMProtectBeginMutation`, `lock`, `VMProtectIsDebuggerPresent`, `addHackFlag`, `sleep`, `milliseconds`, `VMProtectEnd`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isDebuggedDirectThreadFunc`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 15. `RBX::spawnDebugCheckThreads`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void RBX::spawnDebugCheckThreads(weak_ptr<RBX::DataModel> dataModel);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Network/API.cpp:277` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes spawnDebugCheckThreads within Network & Replication. Coordinates interactions with `bind`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `bind`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `spawnDebugCheckThreads`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 16. `boost::hash_value`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::size_t boost::hash_value(const shared_ptr<RBX::PartInstance>& b);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::size_t` |
| **Modifiers** | None |
| **Source Location** | `Network/BoostAppend.cpp:6` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes hash_value within Network & Replication. Coordinates interactions with `hasher, get`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `hasher`, `get`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `hash_value`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 17. `ChatFilter::filterMessageBase`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool ChatFilter::filterMessageBase(shared_ptr<Player> sourcePlayer, shared_ptr<Instance> receiver,
		const std::string& message,
		const ChatFilter::FilteredChatMessageCallback callback);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `Network/ChatFilter.cpp:15` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes filterMessageBase within Network & Replication. Coordinates interactions with `chats, starts_with, bind`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `chats`, `starts_with`, `bind`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `filterMessageBase`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 18. `Client::findClient`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Client* Client::findClient(const RBX::Instance* context, bool testInDatamodel);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Client*` |
| **Modifiers** | None |
| **Source Location** | `Network/Client.cpp:75` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes findClient within Network & Replication. Coordinates interactions with `findServiceProvider, RBXASSERT`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `findServiceProvider`, `RBXASSERT`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `findClient`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 19. `Client::clientIsPresent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool Client::clientIsPresent(const RBX::Instance* context, bool testInDatamodel);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `Network/Client.cpp:82` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes clientIsPresent within Network & Replication. Coordinates interactions with `findClient`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `findClient`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `clientIsPresent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 20. `Client::physicsOutBandwidthExceeded`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool Client::physicsOutBandwidthExceeded(const RBX::Instance* context);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `Network/Client.cpp:87` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes physicsOutBandwidthExceeded within Network & Replication. Coordinates interactions with `findClient, isLimitedByOutgoingBandwidthLimit`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `findClient`, `isLimitedByOutgoingBandwidthLimit`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `physicsOutBandwidthExceeded`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 21. `Client::getNetworkBufferHealth`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
double Client::getNetworkBufferHealth(const RBX::Instance* context);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `double` |
| **Modifiers** | None |
| **Source Location** | `Network/Client.cpp:99` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes getNetworkBufferHealth within Network & Replication. Coordinates interactions with `findClient, GetBufferHealth`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `findClient`, `GetBufferHealth`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getNetworkBufferHealth`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 22. `Client::findLocalSimulatorAddress`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
RBX::SystemAddress Client::findLocalSimulatorAddress(const RBX::Instance* context) const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `RBX::SystemAddress` |
| **Modifiers** | `const` |
| **Source Location** | `Network/Client.cpp:108` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes findLocalSimulatorAddress within Network & Replication. Coordinates interactions with `findClient, RakNetToRbxAddress, getClientAddress, Unassigned`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `findClient`, `RakNetToRbxAddress`, `getClientAddress`, `Unassigned`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `findLocalSimulatorAddress`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 23. `Client::playerConnect`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
shared_ptr<Instance> Client::playerConnect(int userId, std::string server, int serverPort, int clientPort, int threadSleepTime);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `shared_ptr&lt;Instance&gt;` |
| **Modifiers** | None |
| **Source Location** | `Network/Client.cpp:118` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes playerConnect within Network & Replication. Coordinates interactions with `FASTLOG3, serverPort, clientPort, threadSleepTime`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** C++ exception throw on invalid state or failure; Standard runtime error exception formulation.
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `FASTLOG3`, `serverPort`, `clientPort`, `threadSleepTime`, `runtime_error`, `createLocalPlayer`, `getPreviousPlaceId`, `rawPeer`, `Startup`, `GetInternalID`, `remoteAddress`, `c_str`.
- **External Library Dependencies:** `RakNet UDP Networking Engine`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `playerConnect`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 24. `Client::disconnect`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Client::disconnect(int blockDuration);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Network/Client.cpp:193` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes disconnect within Network & Replication. Coordinates interactions with `FASTLOG, visitChildren, bind, removeAllChildren`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `FASTLOG`, `visitChildren`, `bind`, `removeAllChildren`, `rawPeer`, `CloseConnection`, `Shutdown`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

This function is exercised in **26 test case(s)**:

- **`CustomEvents::SendValuesOnlyWhenConnected`** (`App.UnitTest/CustomEvents.cpp:127`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(0, callCounter-&gt;calls)`, `BOOST_REQUIRE_EQUAL(0, callCounter-&gt;calls)`
  - **Callsite Snippet:** `conn.disconnect();`
- **`CustomEvents::ValueClamping`** (`App.UnitTest/CustomEvents.cpp:188`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(0, evt-&gt;getPersistedCurrentValue())`, `BOOST_REQUIRE_EQUAL(1, evt-&gt;getPersistedCurrentValue())`
  - **Callsite Snippet:** `conn.disconnect();`
- **`CustomEvents::SettingParentToNullDoesBreakConnection`** (`App.UnitTest/CustomEvents.cpp:239`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(1, callCounter-&gt;calls)`, `BOOST_REQUIRE_EQUAL(.1f, callCounter-&gt;lastValue)`
  - **Callsite Snippet:** `conn.disconnect();`
- **`CustomEvents::BreakingConnectionSetsReceiverToZero`** (`App.UnitTest/CustomEvents.cpp:301`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(1, callCounter-&gt;calls)`, `BOOST_REQUIRE_EQUAL(.1f, callCounter-&gt;lastValue)`
  - **Callsite Snippet:** `conn.disconnect();`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 25. `Client::setGameSessionID`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Client::setGameSessionID(std::string value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Network/Client.cpp:210` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes setGameSessionID within Network & Replication.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setGameSessionID`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 26. `Client::configureAsCloudEditClient`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Client::configureAsCloudEditClient();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Network/Client.cpp:218` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes configureAsCloudEditClient within Network & Replication.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `configureAsCloudEditClient`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 27. `Client::isCloudEdit`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool Client::isCloudEdit() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `Network/Client.cpp:223` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes isCloudEdit within Network & Replication.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isCloudEdit`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 28. `Client::onServiceProvider`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void Client::onServiceProvider(ServiceProvider* oldProvider, ServiceProvider* newProvider);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Network/Client.cpp:228` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes onServiceProvider within Network & Replication. Coordinates interactions with `disconnect, now, setConnection, get`. Employs heap memory deallocation via operator delete.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Multi-case state dispatch, Explicit result return.
- **Memory Management:** Heap memory deallocation via operator delete; Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT); Exception handling block (try/catch recovery).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `disconnect`, `now`, `setConnection`, `get`, `doIt`, `connect`, `bind`, `sendVersionInfo`, `rawPeer`, `Send`, `getDataSendPriority`, `sendTicket`.
- **External Library Dependencies:** `Boost C++ Libraries`, `RakNet UDP Networking Engine`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onServiceProvider`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Behavior branches internally via conditional compilation for: Windows (Win32/x64 API).

- **Platform Preprocessor Guards:** `Windows (Win32/x64 API)`

---

### 29. `Client::sendVersionInfo`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Client::sendVersionInfo();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Network/Client.cpp:261` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes sendVersionInfo within Network & Replication. Coordinates interactions with `rawPeer, Send, getDataSendPriority`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `rawPeer`, `Send`, `getDataSendPriority`.
- **External Library Dependencies:** `RakNet UDP Networking Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `sendVersionInfo`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 30. `Client::sendTicket`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Client::sendTicket();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Network/Client.cpp:270` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes sendTicket within Network & Replication. Coordinates interactions with `serializeStringCompressed, singleton, osPlatform, getRobloxProductName`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `serializeStringCompressed`, `singleton`, `osPlatform`, `getRobloxProductName`, `encryptDataPart`, `rawPeer`, `Send`, `getDataSendPriority`.
- **External Library Dependencies:** `RakNet UDP Networking Engine`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `sendTicket`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 31. `rakIdToString`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string rakIdToString(int id);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `Network/Client.cpp:301` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes rakIdToString within Network & Replication. Coordinates interactions with `format`.

- **Control Flow & Execution:** Multi-case state dispatch, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `format`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `rakIdToString`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 32. `Client::OnFailedConnectionAttempt`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Client::OnFailedConnectionAttempt(RakNet::Packet *packet, RakNet::PI2_FailedConnectionAttemptReason failedConnectionAttemptReason);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Network/Client.cpp:317` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes OnFailedConnectionAttempt within Network & Replication. Coordinates interactions with `rakIdToString, singleton, printf, RakNetAddressToString`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `rakIdToString`, `singleton`, `printf`, `RakNetAddressToString`, `c_str`, `connectionFailedSignal`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `OnFailedConnectionAttempt`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 33. `programMemoryPermissionsHackChecker`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void programMemoryPermissionsHackChecker(weak_ptr<DataModel> weakDataModel);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `Network/Client.cpp:327` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes programMemoryPermissionsHackChecker within Network & Replication. Coordinates interactions with `VMProtectBeginMutation, lock, FASTLOG, areMemoryPagePermissionsSetupForHacking`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `VMProtectBeginMutation`, `lock`, `FASTLOG`, `areMemoryPagePermissionsSetupForHacking`, `FASTLOG1`, `sleep`, `milliseconds`, `VMProtectEnd`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `programMemoryPermissionsHackChecker`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 34. `Client::sendPreferedSpawnName`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Client::sendPreferedSpawnName() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `const` |
| **Source Location** | `Network/Client.cpp:345` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes sendPreferedSpawnName within Network & Replication. Coordinates interactions with `serializeStringCompressed, GetSpawnName, FASTLOGS, RakNetAddressToString`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `serializeStringCompressed`, `GetSpawnName`, `FASTLOGS`, `RakNetAddressToString`, `c_str`, `rawPeer`, `Send`, `getDataSendPriority`.
- **External Library Dependencies:** `RakNet UDP Networking Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `sendPreferedSpawnName`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 35. `Client::HandleConnection`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void Client::HandleConnection(RakNet::Packet *packet);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Network/Client.cpp:357` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes HandleConnection within Network & Replication. Coordinates interactions with `getPreviousPlaceId, rawPeer, Send, getDataSendPriority`. Employs reference-counted heap object ownership (boost::shared_ptr).

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Exception handling block (try/catch recovery).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getPreviousPlaceId`, `rawPeer`, `Send`, `getDataSendPriority`, `sendTicket`, `sendPreferedSpawnName`, `findWorkspace`, `clearTerrain`, `GetExternalID`, `setAndLockParent`, `defined`, `VMProtectBeginMutation`.
- **External Library Dependencies:** `Boost C++ Libraries`, `RakNet UDP Networking Engine`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `HandleConnection`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Behavior branches internally via conditional compilation for: Windows (Win32/x64 API).

- **Platform Preprocessor Guards:** `Windows (Win32/x64 API)`

---

### 36. `Client::OnReceive`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
RakNet::PluginReceiveResult Client::OnReceive(RakNet::Packet *packet);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `RakNet::PluginReceiveResult` |
| **Modifiers** | None |
| **Source Location** | `Network/Client.cpp:410` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes OnReceive within Network & Replication. Coordinates interactions with `singleton, printf, RakNetAddressToString, c_str`.

- **Control Flow & Execution:** Conditional branching, Multi-case state dispatch, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `singleton`, `printf`, `RakNetAddressToString`, `c_str`, `HandleConnection`, `sendVersionInfo`, `connectionFailedSignal`, `rakIdToString`, `connectionRejectedSignal`, `RBXASSERT`.
- **External Library Dependencies:** `RakNet UDP Networking Engine`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `OnReceive`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 37. `setTicket`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void setTicket(const std::string& t);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Network/Client.h:34` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes setTicket within Network & Replication.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setTicket`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 38. `disconnect`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void disconnect();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Network/Client.h:39` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes disconnect within Network & Replication.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

This function is exercised in **26 test case(s)**:

- **`CustomEvents::SendValuesOnlyWhenConnected`** (`App.UnitTest/CustomEvents.cpp:127`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(0, callCounter-&gt;calls)`, `BOOST_REQUIRE_EQUAL(0, callCounter-&gt;calls)`
  - **Callsite Snippet:** `conn.disconnect();`
- **`CustomEvents::ValueClamping`** (`App.UnitTest/CustomEvents.cpp:188`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(0, evt-&gt;getPersistedCurrentValue())`, `BOOST_REQUIRE_EQUAL(1, evt-&gt;getPersistedCurrentValue())`
  - **Callsite Snippet:** `conn.disconnect();`
- **`CustomEvents::SettingParentToNullDoesBreakConnection`** (`App.UnitTest/CustomEvents.cpp:239`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(1, callCounter-&gt;calls)`, `BOOST_REQUIRE_EQUAL(.1f, callCounter-&gt;lastValue)`
  - **Callsite Snippet:** `conn.disconnect();`
- **`CustomEvents::BreakingConnectionSetsReceiverToZero`** (`App.UnitTest/CustomEvents.cpp:301`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(1, callCounter-&gt;calls)`, `BOOST_REQUIRE_EQUAL(.1f, callCounter-&gt;lastValue)`
  - **Callsite Snippet:** `conn.disconnect();`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 39. `doScans`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void doScans(unsigned int scanMask);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Network/ClientReplicator.cpp:149` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes doScans within Network & Replication. Coordinates interactions with `defined, VMProtectBeginMutation, get, isCeBadDll`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new; Reference-counted heap object ownership (boost::shared_ptr); Unique RAII pointer lifetime control (boost::scoped_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `defined`, `VMProtectBeginMutation`, `get`, `isCeBadDll`, `checkAndLocalUpdate`, `kernelUpdate`, `scan`, `detectTitle`, `detectFakeAttach`, `detectEarlyKick`, `isSpeedhack`, `VMProtectEnd`.
- **External Library Dependencies:** `Boost C++ Libraries`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `doScans`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Behavior branches internally via conditional compilation for: Windows (Win32/x64 API).

- **Platform Preprocessor Guards:** `Windows (Win32/x64 API)`

---

### 40. `sleepTime`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
Time::Interval sleepTime(const Stats& stats);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Time::Interval` |
| **Modifiers** | `virtual` |
| **Source Location** | `Network/ClientReplicator.cpp:204` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes sleepTime within Network & Replication. Coordinates interactions with `computeStandardSleepTime`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `computeStandardSleepTime`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `sleepTime`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `App/util/Win/CheatEngine.cpp`, `XboxClient/renderJob.cpp`, `WindowsClient/RenderJob.cpp`.

- **Alternative Implementation Files:** `App/util/Win/CheatEngine.cpp`, `XboxClient/renderJob.cpp`, `WindowsClient/RenderJob.cpp`

---

### 41. `error`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
Error error(const Stats& stats);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Error` |
| **Modifiers** | `virtual` |
| **Source Location** | `Network/ClientReplicator.cpp:209` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes error within Network & Replication. Coordinates interactions with `computeStandardErrorCyclicExecutiveSleeping`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `computeStandardErrorCyclicExecutiveSleeping`.

#### How it is Used in Tests

This function is exercised in **2 test case(s)**:

- **`LuaReflection::ypcallFailure`** (`App.UnitTest/LuaReflection.cpp:261`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(result-&gt;values.size(), 2)`, `BOOST_CHECK_EQUAL(result-&gt;values.at(0).get&lt;bool&gt;(), false)`
  - **Callsite Snippet:** `"return ypcall(function() error('failure') end) "`
- **`LuaReflection::Events2`** (`App.UnitTest/LuaReflection.cpp:636`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(event2Value, 2)`, `BOOST_CHECK_EQUAL(event2Value, 1)`
  - **Callsite Snippet:** `"   error('ha!')\n"`

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `App/util/Win/CheatEngine.cpp`, `XboxClient/async.h`.

- **Alternative Implementation Files:** `App/util/Win/CheatEngine.cpp`, `XboxClient/async.h`

---

### 42. `stepDataModelJob`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
TaskScheduler::StepResult stepDataModelJob(const Stats& stats);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `TaskScheduler::StepResult` |
| **Modifiers** | `virtual` |
| **Source Location** | `Network/ClientReplicator.cpp:214` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes stepDataModelJob within Network & Replication. Coordinates interactions with `VMProtectBeginMutation, doScans, nowFast, VMProtectEnd`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `VMProtectBeginMutation`, `doScans`, `nowFast`, `VMProtectEnd`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `stepDataModelJob`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/renderJob.cpp`, `WindowsClient/RenderJob.cpp`.

- **Alternative Implementation Files:** `XboxClient/renderJob.cpp`, `WindowsClient/RenderJob.cpp`

---

### 43. `getLastRunTime`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Time getLastRunTime() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Time` |
| **Modifiers** | `const` |
| **Source Location** | `Network/ClientReplicator.cpp:224` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes getLastRunTime within Network & Replication.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getLastRunTime`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 44. `sleepTime`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
Time::Interval sleepTime(const Stats& stats);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Time::Interval` |
| **Modifiers** | `virtual` |
| **Source Location** | `Network/ClientReplicator.cpp:267` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes sleepTime within Network & Replication. Coordinates interactions with `computeStandardSleepTime`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `computeStandardSleepTime`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `sleepTime`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `App/util/Win/CheatEngine.cpp`, `XboxClient/renderJob.cpp`, `WindowsClient/RenderJob.cpp`.

- **Alternative Implementation Files:** `App/util/Win/CheatEngine.cpp`, `XboxClient/renderJob.cpp`, `WindowsClient/RenderJob.cpp`

---

### 45. `error`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
Error error(const Stats& stats);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Error` |
| **Modifiers** | `virtual` |
| **Source Location** | `Network/ClientReplicator.cpp:272` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes error within Network & Replication. Coordinates interactions with `computeStandardError`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `computeStandardError`.

#### How it is Used in Tests

This function is exercised in **2 test case(s)**:

- **`LuaReflection::ypcallFailure`** (`App.UnitTest/LuaReflection.cpp:261`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(result-&gt;values.size(), 2)`, `BOOST_CHECK_EQUAL(result-&gt;values.at(0).get&lt;bool&gt;(), false)`
  - **Callsite Snippet:** `"return ypcall(function() error('failure') end) "`
- **`LuaReflection::Events2`** (`App.UnitTest/LuaReflection.cpp:636`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(event2Value, 2)`, `BOOST_CHECK_EQUAL(event2Value, 1)`
  - **Callsite Snippet:** `"   error('ha!')\n"`

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `App/util/Win/CheatEngine.cpp`, `XboxClient/async.h`.

- **Alternative Implementation Files:** `App/util/Win/CheatEngine.cpp`, `XboxClient/async.h`

---

### 46. `stepDataModelJob`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
TaskScheduler::StepResult stepDataModelJob(const Stats& stats);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `TaskScheduler::StepResult` |
| **Modifiers** | `virtual` |
| **Source Location** | `Network/ClientReplicator.cpp:277` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes stepDataModelJob within Network & Replication. Coordinates interactions with `VMProtectBeginMutation, get, getThreadContext, step`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Multi-case state dispatch, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new; Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** TaskScheduler global job queue dispatching.
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT); C++ exception throw on invalid state or failure; Standard runtime error exception formulation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `VMProtectBeginMutation`, `get`, `getThreadContext`, `step`, `getLastCompletedHash`, `updateHsceHash`, `getHsceAndHash`, `getHsceOrHash`, `addHackFlag`, `defined`, `getLastGoldenHash`, `getLastCompletedTime`.
- **External Library Dependencies:** `Boost C++ Libraries`, `RakNet UDP Networking Engine`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `stepDataModelJob`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Behavior branches internally via conditional compilation for: Windows (Win32/x64 API). Alternative platform-specific implementations exist in: `XboxClient/renderJob.cpp`, `WindowsClient/RenderJob.cpp`.

- **Platform Preprocessor Guards:** `Windows (Win32/x64 API)`
- **Alternative Implementation Files:** `XboxClient/renderJob.cpp`, `WindowsClient/RenderJob.cpp`

---

### 47. `getLastRunTime`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Time getLastRunTime() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Time` |
| **Modifiers** | `const` |
| **Source Location** | `Network/ClientReplicator.cpp:366` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes getLastRunTime within Network & Replication.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getLastRunTime`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 48. `getLastHashTime`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Time getLastHashTime() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Time` |
| **Modifiers** | `const` |
| **Source Location** | `Network/ClientReplicator.cpp:370` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes getLastHashTime within Network & Replication.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getLastHashTime`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 49. `memPermissionChanged`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool memPermissionChanged(uintptr_t regionBase, size_t regionSize, size_t protection);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `__forceinline` |
| **Source Location** | `Network/ClientReplicator.cpp:390` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes memPermissionChanged within Network & Replication. Coordinates interactions with `virtualQuery, memset`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `virtualQuery`, `memset`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `memPermissionChanged`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 50. `populateMccReport`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void populateMccReport(RBX::Network::MccReport& report);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `__forceinline` |
| **Source Location** | `Network/ClientReplicator.cpp:405` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes populateMccReport within Network & Replication. Coordinates interactions with `getLastRunTime, timestampSeconds, getLastHashTime, nowFast`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getLastRunTime`, `timestampSeconds`, `getLastHashTime`, `nowFast`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `populateMccReport`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 51. `sleepTime`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
Time::Interval sleepTime(const Stats& stats);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Time::Interval` |
| **Modifiers** | `virtual` |
| **Source Location** | `Network/ClientReplicator.cpp:433` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes sleepTime within Network & Replication. Coordinates interactions with `computeStandardSleepTime`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `computeStandardSleepTime`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `sleepTime`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `App/util/Win/CheatEngine.cpp`, `XboxClient/renderJob.cpp`, `WindowsClient/RenderJob.cpp`.

- **Alternative Implementation Files:** `App/util/Win/CheatEngine.cpp`, `XboxClient/renderJob.cpp`, `WindowsClient/RenderJob.cpp`

---

### 52. `error`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
Error error(const Stats& stats);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Error` |
| **Modifiers** | `virtual` |
| **Source Location** | `Network/ClientReplicator.cpp:438` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes error within Network & Replication. Coordinates interactions with `computeStandardErrorCyclicExecutiveSleeping`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `computeStandardErrorCyclicExecutiveSleeping`.

#### How it is Used in Tests

This function is exercised in **2 test case(s)**:

- **`LuaReflection::ypcallFailure`** (`App.UnitTest/LuaReflection.cpp:261`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_REQUIRE_EQUAL(result-&gt;values.size(), 2)`, `BOOST_CHECK_EQUAL(result-&gt;values.at(0).get&lt;bool&gt;(), false)`
  - **Callsite Snippet:** `"return ypcall(function() error('failure') end) "`
- **`LuaReflection::Events2`** (`App.UnitTest/LuaReflection.cpp:636`)
  - **Usage Pattern:** `Direct Call`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(event2Value, 2)`, `BOOST_CHECK_EQUAL(event2Value, 1)`
  - **Callsite Snippet:** `"   error('ha!')\n"`

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `App/util/Win/CheatEngine.cpp`, `XboxClient/async.h`.

- **Alternative Implementation Files:** `App/util/Win/CheatEngine.cpp`, `XboxClient/async.h`

---

### 53. `stepDataModelJob`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
TaskScheduler::StepResult stepDataModelJob(const Stats& stats);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `TaskScheduler::StepResult` |
| **Modifiers** | `virtual` |
| **Source Location** | `Network/ClientReplicator.cpp:443` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes stepDataModelJob within Network & Replication. Coordinates interactions with `VMProtectBeginMutation, defined, memPermissionChanged, getThreadContext`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `VMProtectBeginMutation`, `defined`, `memPermissionChanged`, `getThreadContext`, `isNtdllAddress`, `populateMccReport`, `reportReadySignal`, `FreeConsole`, `VMProtectEnd`, `VMProtectBeginVirtualization`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `stepDataModelJob`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `XboxClient/renderJob.cpp`, `WindowsClient/RenderJob.cpp`.

- **Alternative Implementation Files:** `XboxClient/renderJob.cpp`, `WindowsClient/RenderJob.cpp`

---

### 54. `ClientReplicator::createStatsItem`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
shared_ptr<Replicator::Stats> ClientReplicator::createStatsItem();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `shared_ptr&lt;Replicator::Stats&gt;` |
| **Modifiers** | None |
| **Source Location** | `Network/ClientReplicator.cpp:568` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes createStatsItem within Network & Replication. Coordinates interactions with `shared_from`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `shared_from`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `createStatsItem`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 55. `ClientReplicator::findTargetPlayer`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Player* ClientReplicator::findTargetPlayer() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Player*` |
| **Modifiers** | `const` |
| **Source Location** | `Network/ClientReplicator.cpp:616` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes findTargetPlayer within Network & Replication. Coordinates interactions with `getLocalPlayer`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getLocalPlayer`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `findTargetPlayer`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 56. `ClientReplicator::isLegalSendInstance`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool ClientReplicator::isLegalSendInstance(const Instance* instance);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `Network/ClientReplicator.cpp:621` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes isLegalSendInstance within Network & Replication. Coordinates interactions with `filterNew, getParent, settings, singleton`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `filterNew`, `getParent`, `settings`, `singleton`, `printf`, `getFullName`, `c_str`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isLegalSendInstance`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 57. `ClientReplicator::isLegalSendProperty`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool ClientReplicator::isLegalSendProperty(Instance* instance, const Reflection::PropertyDescriptor& desc);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `Network/ClientReplicator.cpp:637` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes isLegalSendProperty within Network & Replication. Coordinates interactions with `filterParent, getParent, filterChangedProperty, canReplicate`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `filterParent`, `getParent`, `filterChangedProperty`, `canReplicate`, `settings`, `singleton`, `printf`, `c_str`, `getFullName`, `isCloudEdit`, `getCurrentEditor`, `RBXASSERT`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isLegalSendProperty`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 58. `ClientReplicator::isLegalSendEvent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool ClientReplicator::isLegalSendEvent(Instance* instance, const Reflection::EventDescriptor& desc);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `Network/ClientReplicator.cpp:671` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes isLegalSendEvent within Network & Replication. Coordinates interactions with `filterEvent, settings, singleton, printf`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `filterEvent`, `settings`, `singleton`, `printf`, `c_str`, `getFullName`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isLegalSendEvent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 59. `ClientReplicator::canSendItems`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool ClientReplicator::canSendItems();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `Network/ClientReplicator.cpp:684` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes canSendItems within Network & Replication.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `canSendItems`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 60. `ClientReplicator::isCloudEdit`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool ClientReplicator::isCloudEdit() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `Network/ClientReplicator.cpp:689` |
| **Subsystem** | `Network & Replication` |

#### How it Works Internally

Executes isCloudEdit within Network & Replication. Coordinates interactions with `getParent`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `getParent`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isCloudEdit`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---


:::tip Additional Functions
There are **1486 additional internal and inline functions** in this subsystem. All functions are indexed and cross-referenced in the **[Complete Function Catalog](./function-catalog.md)**.
:::

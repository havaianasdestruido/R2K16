---
sidebar_position: 4
---

# Network — replication stack

**Path:** `Network/` · **Project:** `Network.vcxproj` / `Network.xcodeproj` /
`CMakeLists.txt` · **Status:** ✅ builds

The client/server networking library, built on **RakNet** (vendored under `Network/raknet/`
with `Source`, `Lib`, `Samples`). Full architecture discussion in
[Networking](../architecture/network.md); this page is the file inventory.

```
Network/
├── raknet/                 # Vendored RakNet (Source/Lib/Samples)
├── include/network/        # Public headers
├── Peer.*                  # Peer abstraction
├── ConcurrentRakPeer.*     # Thread-safe RakPeerInterface wrapper
├── Server.* / Client.*     # Server & client cores
├── Replicator.cpp (+TagItem)   # Instance-tree replication core
├── ServerReplicator.* / ClientReplicator.*
├── Item.cpp / MechanismItem.* / Marker.*   # Replicated payload units
├── PhysicsSender.* / PhysicsReceiver.*
├── ErrorCompPhysicsSender(2).*            # error-compensated physics sync
├── RoundRobinPhysicsSender.* / TopNErrorsPhysicsSender.*
├── InterpolatingPhysicsReceiver.* / DirectPhysicsReceiver.*
├── NetworkOwnerJob.* / MovementHistoryJob.*  # ownership & rewind jobs
├── ClusterUpdateBuffer.* / NetworkClusterPacketCache.* / NetworkPacketCache.*
├── Streaming.* / StreamingUtil.h
├── Dictionary.*            # String dictionary compression
├── Compressor.*            # Payload compression
├── DataBlockEncryptor.* + rijndael.cpp + Rijndael*.h   # Encryption
├── ChatFilter.cpp / WebChatFilter.cpp   # Chat moderation
├── PersistentDataStore.*   # DataStore traffic
├── GuidRegistryService.*   # Asset GUID registry
├── API.cpp                 # Web API glue
├── CrashReporter.cpp       # Client crash reporting
├── GameConfigurer.cpp      # Session bootstrap
├── GamePerfMonitor.* / NetworkProfiler.* / ReplicatorStats.*   # Telemetry
├── NetworkFilter.*         # Traffic/address filtering
├── NetworkSettings.cpp     # Settings
├── NetPmc.cpp              # PMC (property mutation cache) support
├── BoostAppend.*           # Boost.Asio/cpp-netlib shims
└── PacketIds.h             # Protocol packet IDs
```

## Where it plugs in

- **Server side:** `RCCService` links `Network` and serves games
  ([RCCService](./rcc.md)); Studio's *Start Server* uses it too.
- **Client side:** `WindowsClient`, mobile and console clients use `Client`/`ClientReplicator`
  to join ([Clients](./clients.md)).
- **Engine side:** replication events mutate the DataModel under the
  [TaskScheduler](../architecture/jobs-and-scheduler.md) rules.

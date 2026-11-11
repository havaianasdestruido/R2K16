---
sidebar_position: 25
title: Test Verification Matrix
description: Comprehensive mapping of all test suites, test cases, and verified engine functions.
---

# Test Verification Matrix

This matrix documents **every test case across the R2K16 test suites** (`App.UnitTest`, `Base.UnitTest`, `RobloxTest`, `Roblox.Test`, `RCCService.Test`), detailing what functions are exercised and what invariants are verified.


## FAQ

### Does a test mapping prove a function is fully tested?

No. The mapping is heuristic; a name match does not prove execution or meaningful assertions. Read and run the relevant test when the target is available.

### How can I investigate this in the repository?

From the repository root, search the relevant tracked files for a starting point (results are leads, not proof of behavior):

```bash
git grep -n -i -F -- 'map_tests_to_function' -- scripts/docgen
```

Read the surrounding implementation and callers, and check relevant tests before making changes. A search may return no matches when terminology or tracked files change.

## Test Suite Overview

| Suite Name | Test Cases | Primary Source File | Target Subsystem |
| :--- | :--- | :--- | :--- |
| `Atomic` | `5` | `Base.UnitTest/atomic.cpp` | Foundations |
| `AutoRCCTest` | `1` | `RCCService.Test/AutoRCCTest.cs` | Integration |
| `AutowedgeTest` | `6` | `App.UnitTest/AutowedgeTest.cpp` | Engine Core |
| `Base64BinaryStreamTest` | `3` | `App.UnitTest/Base64BinaryStreamTest.cpp` | Engine Core |
| `BasicScenarios` | `7` | `RCCService.Test/BasicScenarios.cs` | Integration |
| `CEvent` | `3` | `Base.UnitTest/CEvent.cpp` | Foundations |
| `ChatTests` | `6` | `App.UnitTest/ChatTests.cpp` | Engine Core |
| `ClusterChangeHistoryTest` | `2` | `App.UnitTest/ClusterChangeHistoryTest.cpp` | Engine Core |
| `ClusterDeltaBuffer` | `26` | `App.UnitTest/ClusterReplicationTest.cpp` | Engine Core |
| `ClusterDeprecatedProperty` | `6` | `App.UnitTest/ClusterDeprecatedPropertyTest.cpp` | Engine Core |
| `ContentProvider` | `1` | `App.UnitTest/ContentProviderTest.cpp` | Engine Core |
| `Crypt` | `2` | `Base.UnitTest/Crypt.cpp` | Foundations |
| `CustomEvents` | `15` | `App.UnitTest/CustomEvents.cpp` | Engine Core |
| `DenseHashSet` | `10` | `Base.UnitTest/DenseHashSet.cpp` | Foundations |
| `FastLog` | `10` | `Base.UnitTest/Log.cpp` | Foundations |
| `FastLogSettings` | `2` | `App.UnitTest/FastLogSettingsTest.cpp` | Engine Core |
| `Format` | `8` | `Base.UnitTest/Time.cpp` | Foundations |
| `G3D` | `9` | `App.UnitTest/G3D.cpp` | Engine Core |
| `HTTPSuite` | `9` | `App.UnitTest/HTTPTest.cpp` | Engine Core |
| `HeapValueTest` | `1` | `App.UnitTest/HeapValueTest.cpp` | Engine Core |
| `HttpCacheEntryTest` | `2` | `App.UnitTest/HttpCacheEntryTest.cpp` | Engine Core |
| `HumanoidTest` | `1` | `App.UnitTest/HumanoidTest.cpp` | Engine Core |
| `Instance` | `23` | `App.UnitTest/Instance.cpp` | Engine Core |
| `LogServiceTest` | `1` | `App.UnitTest/LogServiceTest.cpp` | Engine Core |
| `LuaDebugger` | `2` | `App.UnitTest/LuaDebugger.cpp` | Engine Core |
| `LuaReflection` | `36` | `App.UnitTest/LuaReflection.cpp` | Engine Core |
| `LuaSandbox` | `6` | `App.UnitTest/LuaSandbox.cpp` | Engine Core |
| `LuaTokenizer` | `4` | `App.UnitTest/LuaTokenizer.cpp` | Engine Core |
| `LuaVector3Test` | `5` | `App.UnitTest/LuaVector3Test.cpp` | Engine Core |
| `LuaYieldingTest` | `3` | `App.UnitTest/LuaYieldingTest.cpp` | Engine Core |
| `MD5Suite` | `4` | `App.UnitTest/MD5.cpp` | Engine Core |
| `MSUnitProxy` | `4` | `Roblox.Test/MSUnitProxy/MSUnitProxy.cs` | Integration |
| `MakeShared` | `1` | `Base.UnitTest/make_shared.cpp` | Foundations |
| `MiscRegression` | `1` | `App.UnitTest/MiscRegression.cpp` | Engine Core |
| `ModuleScriptTest` | `18` | `App.UnitTest/ModuleScriptTest.cpp` | Engine Core |
| `Network` | `19` | `App.UnitTest/Network.cpp` | Engine Core |
| `NetworkSecurity` | `5` | `App.UnitTest/NetworkSecurity.cpp` | Engine Core |
| `PathfindingTest` | `1` | `App.UnitTest/PathfindingTest.cpp` | Engine Core |
| `PostEffectTest` | `5` | `App.UnitTest/PostEffectTest.cpp` | Engine Core |
| `PropertyChangedSignal` | `9` | `App.UnitTest/PropertyChangedSignal.cpp` | Engine Core |
| `RakNet` | `2` | `App.UnitTest/RakNet.cpp` | Engine Core |
| `RaycastTest` | `15` | `App.UnitTest/RaycastTest.cpp` | Engine Core |
| `Reflection` | `3` | `App.UnitTest/ReflectionTest.cpp` | Engine Core |
| `RemoteSignals` | `2` | `App.UnitTest/RemoteSignal.cpp` | Engine Core |
| `ReplicatorGcJobTest` | `6` | `App.UnitTest/ReplicatorGcJobTest.cpp` | Engine Core |
| `ReplicatorStreamJobTest` | `5` | `App.UnitTest/ReplicatorStreamJobTest.cpp` | Engine Core |
| `SelectionTest` | `3` | `App.UnitTest/SelectionTest.cpp` | Engine Core |
| `SerializationTest` | `2` | `App.UnitTest/SerializationTest.cpp` | Engine Core |
| `ServerClientTests` | `1` | `RCCService.Test/ServerClientTests.cs` | Integration |
| `SettingsTest` | `12` | `App.UnitTest/SettingsTest.cpp` | Engine Core |
| `SettingsUrl` | `3` | `App.UnitTest/SettingsURL.cpp` | Engine Core |
| `SoundEffectTests` | `2` | `App.UnitTest/SoundEffectTest.cpp` | Engine Core |
| `SpatialHash` | `4` | `App.UnitTest/SpatialHashTest.cpp` | Engine Core |
| `SpatialRegionTest` | `2` | `App.UnitTest/SpatialRegionTest.cpp` | Engine Core |
| `StreamRegionTest` | `6` | `App.UnitTest/StreamRegionTest.cpp` | Engine Core |
| `StressSoapTest` | `4` | `RCCService.Test/StressSoapTest.cs` | Integration |
| `StressTests` | `4` | `RCCService.Test/StressTests.cs` | Integration |
| `TaskScheduler` | `1` | `Base.UnitTest/TaskScheduler.cpp` | Foundations |
| `ThreadPoolTest` | `3` | `App.UnitTest/ThreadPoolTest.cpp` | Engine Core |
| `ToolTest` | `1` | `App.UnitTest/ToolTest.cpp` | Engine Core |
| `Trie` | `5` | `Base.UnitTest/trie.cpp` | Foundations |
| `URLParser` | `5` | `App.UnitTest/URLParserTest.cpp` | Engine Core |
| `VoxelCellUtilTest` | `5` | `App.UnitTest/VoxelCellUtilTest.cpp` | Engine Core |
| `WebParser` | `13` | `App.UnitTest/WebParserTest.cpp` | Engine Core |
| `WebSerializer` | `5` | `App.UnitTest/WebSerializerTest.cpp` | Engine Core |
| `Xml` | `2` | `App.UnitTest/XmlElement.cpp` | Engine Core |
| `intrusive_ptr` | `12` | `Base.UnitTest/intrusive_ptr.cpp` | Foundations |
| `signals` | `21` | `Base.UnitTest/signals.cpp` | Foundations |
| `spin_mutex` | `1` | `Base.UnitTest/spin_mutex_test.cpp` | Foundations |

---

## Detailed Test Cases & Function Verification

### `AutowedgeTest::AutowedgeStartingBlock`

- **Location:** `App.UnitTest/AutowedgeTest.cpp:185`
- **Verified Functions:** `applyStandardExteriorWedging`, `autowedgeStartingBlock`, `checkExpectedResult`, `createStartingBlock`, `initializeExpectedResult`
- **Invariants Checked:** *Implicit assertion via execution*

### `AutowedgeTest::RemoveTopCenter`

- **Location:** `App.UnitTest/AutowedgeTest.cpp:200`
- **Verified Functions:** `applyStandardExteriorWedging`, `autowedgeStartingBlock`, `checkExpectedResult`, `createCell`, `createStartingBlock`, `initializeExpectedResult`, `kUniqueEmptyCellRepresentation`, `setCellScript`
- **Invariants Checked:** *Implicit assertion via execution*

### `AutowedgeTest::CornerOfTerrainWorks`

- **Location:** `App.UnitTest/AutowedgeTest.cpp:228`
- **Verified Functions:** `Vector3int16`, `fourCellSquareTest`
- **Invariants Checked:** *Implicit assertion via execution*

### `AutowedgeTest::BelowTerrainWorks`

- **Location:** `App.UnitTest/AutowedgeTest.cpp:239`
- **Verified Functions:** `BOOST_REQUIRE`, `Region3int16`, `Vector3int16`, `autoWedgeCellsScript`
- **Invariants Checked:** `BOOST_REQUIRE(check)`

### `AutowedgeTest::ExplosionBelowTerrainWorks`

- **Location:** `App.UnitTest/AutowedgeTest.cpp:247`
- **Verified Functions:** `BOOST_REQUIRE`, `BOOST_REQUIRE_EQUAL`, `DataModelJob`, `LegacyLock`, `Vector3`, `Vector3int16`, `create`, `get`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(fixture.cluster-&gt;getVoxelGrid()-&gt;getCellMaterial(Vector3int16(kOffset, 0, kOffset)), CELL_MATERIAL_Grass)`, `BOOST_REQUIRE(check)`, `BOOST_REQUIRE_EQUAL(fixture.cluster-&gt;getVoxelGrid()-&gt;getCellMaterial(Vector3int16(kOffset, 0, kOffset)), CELL_MATERIAL_Water)`

### `AutowedgeTest::ExplosionAboveTerrainWorks`

- **Location:** `App.UnitTest/AutowedgeTest.cpp:270`
- **Verified Functions:** `BOOST_REQUIRE`, `BOOST_REQUIRE_EQUAL`, `DataModelJob`, `LegacyLock`, `Vector3`, `Vector3int16`, `create`, `get`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(fixture.cluster-&gt;getVoxelGrid()-&gt;getCellMaterial(Vector3int16(kOffset, 62, kOffset)), CELL_MATERIAL_Grass)`, `BOOST_REQUIRE(check)`, `BOOST_REQUIRE_EQUAL(fixture.cluster-&gt;getVoxelGrid()-&gt;getCellMaterial(Vector3int16(kOffset, 62, kOffset)), CELL_MATERIAL_Water)`

### `Base64BinaryStreamTest::NoExistingData`

- **Location:** `App.UnitTest/Base64BinaryStreamTest.cpp:13`
- **Verified Functions:** `BOOST_REQUIRE_EQUAL`, `RBXASSERT`, `ReadBits`, `WriteBits`, `bis`, `c_str`, `done`, `for`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(test, value)`

### `Base64BinaryStreamTest::FiveBitsExistingData`

- **Location:** `App.UnitTest/Base64BinaryStreamTest.cpp:32`
- **Verified Functions:** `BOOST_REQUIRE_EQUAL`, `ReadBits`, `WriteBits`, `bis`, `c_str`, `done`, `for`, `string`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(prefix, test)`, `BOOST_REQUIRE_EQUAL(test, value)`

### `Base64BinaryStreamTest::LongStreamOfData`

- **Location:** `App.UnitTest/Base64BinaryStreamTest.cpp:57`
- **Verified Functions:** `BOOST_REQUIRE_EQUAL`, `ReadBits`, `WriteBits`, `bis`, `c_str`, `done`, `for`, `numBits`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(read, values[i] & ((1 &lt;&lt; numBits[i]) - 1))`

### `ChatTests::Chat`

- **Location:** `App.UnitTest/ChatTests.cpp:309`
- **Verified Functions:** `test`
- **Invariants Checked:** *Implicit assertion via execution*

### `ChatTests::WebChatFilterChat`

- **Location:** `App.UnitTest/ChatTests.cpp:316`
- **Verified Functions:** `test`
- **Invariants Checked:** *Implicit assertion via execution*

### `ChatTests::Chat2`

- **Location:** `App.UnitTest/ChatTests.cpp:323`
- **Verified Functions:** `test`
- **Invariants Checked:** *Implicit assertion via execution*

### `ChatTests::TeamChat`

- **Location:** `App.UnitTest/ChatTests.cpp:330`
- **Verified Functions:** `test`
- **Invariants Checked:** *Implicit assertion via execution*

### `ChatTests::WhisperChat`

- **Location:** `App.UnitTest/ChatTests.cpp:337`
- **Verified Functions:** `test`
- **Invariants Checked:** *Implicit assertion via execution*

### `ChatTests::ReportAbuse`

- **Location:** `App.UnitTest/ChatTests.cpp:353`
- **Verified Functions:** `BOOST_CHECK`, `CEvent`, `DataModel`, `DataModelJob`, `GetChildren`, `Players`, `ReportAbuse`, `Security`
- **Invariants Checked:** `BOOST_CHECK(event-&gt;Wait(RBX::Time::Interval::from_seconds(10)))`

### `ClusterChangeHistoryTest::FillChunkStressTest`

- **Location:** `App.UnitTest/ClusterChangeHistoryTest.cpp:99`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `DataModelJob`, `LegacyLock`, `base`, `fillChunk`, `for`, `format`, `getNonEmptyCellCount`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(0, chf.cluster-&gt;getNonEmptyCellCount())`

### `ClusterChangeHistoryTest::PartiallyOverlappingChunkTest`

- **Location:** `App.UnitTest/ClusterChangeHistoryTest.cpp:126`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `DataModelJob`, `LegacyLock`, `base1`, `fillChunk`, `getNonEmptyCellCount`, `initWithEmptyCluster`, `lock`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(0, chf.cluster-&gt;getNonEmptyCellCount())`

### `ClusterDeprecatedProperty::AnchoredCannotBeSet`

- **Location:** `App.UnitTest/ClusterDeprecatedPropertyTest.cpp:17`
- **Verified Functions:** `BOOST_REQUIRE_EQUAL`, `Tuple`, `at`, `auto_ptr`, `dataModelSetup`, `execute`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(true, resultTuple-&gt;at(0).get&lt;bool&gt;())`, `BOOST_REQUIRE_EQUAL(true, resultTuple-&gt;at(0).get&lt;bool&gt;())`

### `ClusterDeprecatedProperty::CFrameAndPositionCannotBeSet`

- **Location:** `App.UnitTest/ClusterDeprecatedPropertyTest.cpp:32`
- **Verified Functions:** `BOOST_CHECK`, `BOOST_REQUIRE`, `BOOST_REQUIRE_EQUAL`, `Tuple`, `Vector3`, `at`, `auto_ptr`, `dataModelSetup`
- **Invariants Checked:** `BOOST_CHECK(zeroFrame == resultTuple-&gt;at(0).get&lt;CoordinateFrame&gt;())`, `BOOST_REQUIRE_EQUAL(zeroVector, resultTuple-&gt;at(0).get&lt;Vector3&gt;())`, `BOOST_REQUIRE(zeroFrame == resultTuple-&gt;at(0).get&lt;CoordinateFrame&gt;())`, `BOOST_REQUIRE_EQUAL(zeroVector, resultTuple-&gt;at(0).get&lt;Vector3&gt;())`

### `ClusterDeprecatedProperty::NameCannotBeSet`

- **Location:** `App.UnitTest/ClusterDeprecatedPropertyTest.cpp:54`
- **Verified Functions:** `BOOST_REQUIRE_EQUAL`, `Tuple`, `at`, `auto_ptr`, `dataModelSetup`, `execute`, `string`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL("Terrain", resultTuple-&gt;at(0).get&lt;std::string&gt;())`, `BOOST_REQUIRE_EQUAL("Terrain", resultTuple-&gt;at(0).get&lt;std::string&gt;())`

### `ClusterDeprecatedProperty::ParentCannotBeSet`

- **Location:** `App.UnitTest/ClusterDeprecatedPropertyTest.cpp:69`
- **Verified Functions:** `BOOST_CHECK`, `BOOST_CHECK_EQUAL`, `BOOST_REQUIRE_EQUAL`, `Tuple`, `at`, `auto_ptr`, `catch`, `dataModelSetup`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(dataModel-&gt;getWorkspace(), resultTuple-&gt;at(0).get&lt;shared_ptr&lt;Instance&gt; &gt;().get())`, `BOOST_CHECK_EQUAL("Cannot change Parent of type Terrain", e.what())`, `BOOST_CHECK(checked)`, `BOOST_REQUIRE_EQUAL(dataModel-&gt;getWorkspace(), resultTuple-&gt;at(0).get&lt;shared_ptr&lt;Instance&gt; &gt;().get())`

### `ClusterDeprecatedProperty::SizeCannotBeSet`

- **Location:** `App.UnitTest/ClusterDeprecatedPropertyTest.cpp:92`
- **Verified Functions:** `BOOST_CHECK`, `BOOST_CHECK_EQUAL`, `BOOST_REQUIRE_EQUAL`, `Resize`, `Tuple`, `Vector3`, `at`, `auto_ptr`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(sizeVector, resultTuple-&gt;at(0).get&lt;Vector3&gt;())`, `BOOST_REQUIRE_EQUAL(sizeVector, resultTuple-&gt;at(0).get&lt;Vector3&gt;())`, `BOOST_CHECK_EQUAL("Cannot Resize() Terrain", e.what())`, `BOOST_CHECK(checked)`

### `ClusterDeprecatedProperty::LockedCannotBeSet`

- **Location:** `App.UnitTest/ClusterDeprecatedPropertyTest.cpp:121`
- **Verified Functions:** `BOOST_REQUIRE_EQUAL`, `Tuple`, `at`, `auto_ptr`, `dataModelSetup`, `execute`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(true, resultTuple-&gt;at(0).get&lt;bool&gt;())`, `BOOST_REQUIRE_EQUAL(true, resultTuple-&gt;at(0).get&lt;bool&gt;())`

### `ClusterDeltaBuffer::BitSetConstantsMakeSense`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:248`
- **Verified Functions:** `BOOST_CHECK`, `BOOST_CHECK_EQUAL`, `BitGroup`, `kBitInGroupMask`, `kShiftForGroup`, `sizeof`, `while`
- **Invariants Checked:** `BOOST_CHECK(bits &gt; 0)`, `BOOST_CHECK_EQUAL(UintSet::kBitInGroupMask, bits - 1)`, `BOOST_CHECK_EQUAL(UintSet::kShiftForGroup, shift)`, `BOOST_CHECK_EQUAL(1 &lt;&lt; kXZ_CHUNK_SIZE_AS_BITSHIFT, kXZ_CHUNK_SIZE)`

### `ClusterDeltaBuffer::UintSetEncoding`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:265`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `baseCellOffset`, `computeGlobalLocationFromUintRepresentation`, `computeUintRepresentingLocationInChunk`, `expected`, `for`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(expected.x, actual.x)`, `BOOST_CHECK_EQUAL(expected.y, actual.y)`, `BOOST_CHECK_EQUAL(expected.z, actual.z)`

### `ClusterDeltaBuffer::LengthBitSetOrdering`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:286`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `Vector3int16`, `for`, `pop`, `push`, `size`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(i, updateBuffer.size())`, `BOOST_CHECK_EQUAL(i, out.x)`, `BOOST_CHECK_EQUAL(i, out.x)`

### `ClusterDeltaBuffer::BitSetDoesNotStoreDuplicates`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:309`
- **Verified Functions:** `BOOST_CHECK`, `BOOST_CHECK_EQUAL`, `chk`, `computeUintRepresentingLocationInChunk`, `contains`, `insert`, `push`, `size`
- **Invariants Checked:** `BOOST_CHECK(!s.contains(info))`, `BOOST_CHECK_EQUAL(0, s.size())`, `BOOST_CHECK(s.contains(info))`, `BOOST_CHECK_EQUAL(1, s.size())`

### `ClusterDeltaBuffer::UpdatesGroupedByChunk`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:337`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `BOOST_REQUIRE`, `Vector3int16`, `for`, `pop`, `push`, `size`
- **Invariants Checked:** `BOOST_CHECK_EQUAL((i + 1) * 2, updateBuffer.size())`, `BOOST_REQUIRE(first == Vector3int16(0, 0, 0) || first == Vector3int16(0, 20, 0))`, `BOOST_CHECK_EQUAL(firstY, out.y)`, `BOOST_CHECK_EQUAL(i, out.x)`

### `ClusterDeltaBuffer::UpdatesContinueByChunk`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:370`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `Vector3int16`, `if`, `pop`, `push`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(Vector3int16(40,0,0), read)`, `BOOST_CHECK_EQUAL(Vector3int16(41,0,0), read1)`, `BOOST_CHECK_EQUAL(Vector3int16(42,0,0), read2)`, `BOOST_CHECK_EQUAL(Vector3int16(0,0,0), read3)`

### `ClusterDeltaBuffer::GrowRetainsOrder`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:402`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `Vector3int16`, `for`, `pop`, `push`, `size`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(i + 1, updateBuffer.size())`, `BOOST_CHECK_EQUAL(i / 32, out.y)`, `BOOST_CHECK_EQUAL(i % 32, out.z)`, `BOOST_CHECK_EQUAL(i + 1 - 32, updateBuffer.size())`

### `ClusterDeltaBuffer::CreatingStateSanityCheck`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:456`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `GetNumberOfBitsUsed`, `GetNumberOfBytesUsed`, `client`, `clientCluster`, `clientWrapper`, `createCell`, `getCell`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(1, clientWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(0, serverWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(0, clientWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(32 + (1 + 1 + 48 + 14 + 2 + 16 + 2) + (1 + 1) + 32, buffer.writeStream-&gt;GetNumberOfBitsUsed())`

### `ClusterDeltaBuffer::DuplicateEncoding`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:489`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `Vector3int16`, `client`, `clientCluster`, `clientWrapper`, `createCell`, `getCell`, `getReplicationData`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(4, clientWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(0, serverWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(newCell1, serverCluster-&gt;getVoxelGrid()-&gt;getCell(testCellLocations[0]))`, `BOOST_CHECK_EQUAL(newCell1, serverCluster-&gt;getVoxelGrid()-&gt;getCell(testCellLocations[1]))`

### `ClusterDeltaBuffer::CanSetCellsInLargestChunk`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:529`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `client`, `clientCluster`, `clientWrapper`, `createCell`, `getCell`, `getReplicationData`, `getVoxelGrid`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(2, clientWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(0, serverWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(0, serverWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(Constants::kUniqueEmptyCellRepresentation, serverCluster-&gt;getVoxelGrid()-&gt;getCell(testCellLocation1))`

### `ClusterDeltaBuffer::ShipsInTheNight`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:562`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `client`, `clientCluster`, `clientWrapper`, `countPackets`, `createCell`, `getCell`, `getCellMaterial`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(0, clientWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(0, serverWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(baseCell, serverCluster-&gt;getVoxelGrid()-&gt;getCell(testCellLocation))`, `BOOST_CHECK_EQUAL(baseMaterial, serverCluster-&gt;getVoxelGrid()-&gt;getCellMaterial(testCellLocation))`

### `ClusterDeltaBuffer::ServerReceivesMoreUpdatesBeforeFinishedSendingOlderUpdates`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:630`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `BOOST_REQUIRE`, `BOOST_REQUIRE_GT`, `client`, `clientCluster`, `clientCluster2`, `clientWrapper`, `clientWrapper2`
- **Invariants Checked:** `BOOST_REQUIRE(clientWrapper-&gt;getReplicationData().updateBuffer.size() &gt; 0)`, `BOOST_REQUIRE_GT(remainPackets, 2)`, `BOOST_CHECK_EQUAL(0, serverWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(0, serverWrapper2-&gt;getReplicationData().updateBuffer.size())`

### `ClusterDeltaBuffer::ClientDoesNotAcceptNetworkUpdatesForCellsInQueue`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:699`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `Vector3int16`, `client`, `clientCluster`, `clientWrapper`, `commonLocation`, `createCell`, `getCell`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(2, serverWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(2, clientWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(0, serverWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(2, clientWrapper-&gt;getReplicationData().updateBuffer.size())`

### `ClusterDeltaBuffer::ServerDoesAcceptNetworkUpdatesForCellsInQueue`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:758`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `Vector3int16`, `client`, `clientCluster`, `clientWrapper`, `commonLocation`, `createCell`, `getCell`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(2, serverWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(2, clientWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(0, clientWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(3, serverWrapper-&gt;getReplicationData().updateBuffer.size())`

### `ClusterDeltaBuffer::ClientIsNotClobberedByServerMergingUpdatesAndBouncing`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:815`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `client`, `clientCluster`, `clientWrapper`, `commonLocation`, `createCell`, `getCell`, `getReplicationData`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(0, serverWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(0, clientWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(newClientCell2, clientCluster-&gt;getVoxelGrid()-&gt;getCell(commonLocation))`, `BOOST_CHECK_EQUAL(newClientCell2, serverCluster-&gt;getVoxelGrid()-&gt;getCell(commonLocation))`

### `ClusterDeltaBuffer::ClientIsNotClobberedByQuickServerBounces`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:849`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `client`, `clientCluster`, `clientWrapper`, `commonLocation`, `createCell`, `getCell`, `getReplicationData`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(1, serverWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(0, serverWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(0, clientWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(newClientCell2, clientCluster-&gt;getVoxelGrid()-&gt;getCell(commonLocation))`

### `ClusterDeltaBuffer::EmptyChunkFromNewVoxelStorageDoesNotDisruptNetwork`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:896`
- **Verified Functions:** `BOOST_CHECK`, `BOOST_CHECK_EQUAL`, `Region`, `client`, `clientCluster`, `clientWrapper`, `commonLocation`, `createCell`
- **Invariants Checked:** `BOOST_CHECK(!r.isGuaranteedAllEmpty())`, `BOOST_CHECK(r.isGuaranteedAllEmpty())`, `BOOST_CHECK_EQUAL(Constants::kUniqueEmptyCellRepresentation, serverCluster-&gt;getVoxelGrid()-&gt;getCell(commonLocation))`, `BOOST_CHECK_EQUAL(CELL_MATERIAL_Water, serverCluster-&gt;getVoxelGrid()-&gt;getCellMaterial(commonLocation))`

### `ClusterDeltaBuffer::SendAFewChunksOfRepeats`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:937`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `BOOST_CHECK_MESSAGE`, `Vector3int16`, `client`, `clientCluster`, `clientWrapper`, `countPackets`, `createCell`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(0, serverWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(0, clientWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_MESSAGE(cell == serverCluster-&gt;getVoxelGrid()-&gt;getCell(Vector3int16(x,y,z)), messageBuf)`, `BOOST_CHECK_MESSAGE(material == serverCluster-&gt;getVoxelGrid()-&gt;getCellMaterial(Vector3int16(x,y,z)), messageBuf)`

### `ClusterDeltaBuffer::AllCellPermutations`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:977`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `Vector3int16`, `client`, `clientCluster`, `clientWrapper`, `countPackets`, `for`, `getBlock`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(0, serverWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(0, clientWrapper-&gt;getReplicationData().updateBuffer.size())`, `BOOST_CHECK_EQUAL(clientCluster-&gt;getVoxelGrid()-&gt;getCell(Vector3int16(i, 1, m)),
					serverCluster-&gt;getVoxelGrid()-&gt;getCell(Vector3int16(i, 1, m)))`, `BOOST_CHECK_EQUAL(clientCluster-&gt;getVoxelGrid()-&gt;getCellMaterial(Vector3int16(i, 1, m)),
					serverCluster-&gt;getVoxelGrid()-&gt;getCellMaterial(Vector3int16(i, 1, m)))`

### `ClusterDeltaBuffer::ManyPlayers`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:1028`
- **Verified Functions:** `runPacketCountTest`
- **Invariants Checked:** *Implicit assertion via execution*

### `ClusterDeltaBuffer::SmallerGameIsFast`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:1041`
- **Verified Functions:** `runPacketCountTest`
- **Invariants Checked:** *Implicit assertion via execution*

### `ClusterDeltaBuffer::TinyGameIsRealTime`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:1054`
- **Verified Functions:** `runPacketCountTest`
- **Invariants Checked:** *Implicit assertion via execution*

### `ClusterDeltaBuffer::InitialCachedChunksRemainFifoAcrossBatches`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:1125`
- **Verified Functions:** `BOOST_CHECK`, `ClusterReplicationData`, `Id`, `assign`, `begin`, `end`, `front`, `hasDataToSend`
- **Invariants Checked:** `BOOST_CHECK(data.hasDataToSend())`, `BOOST_CHECK(data.initialChunkIterator.front() == chunks[0])`, `BOOST_CHECK(data.initialChunkIterator.front() == chunks[1])`, `BOOST_CHECK(data.initialChunkIterator.front() == chunks[2])`

### `ClusterDeltaBuffer::ChunkSend`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:1142`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `Vector3int16`, `client`, `clientCluster`, `clientWrapper`, `countChunkPackets`, `for`, `getCell`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(cellOrig, cellReplicated)`

### `ClusterDeltaBuffer::EmptyTerrainDoesNotGetReplicatedToNewPlayers`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:1177`
- **Verified Functions:** `BOOST_CHECK`, `Vector3int16`, `client`, `clientCluster`, `clientWrapper`, `countChunkPackets`, `getVoxelGrid`, `initialize`
- **Invariants Checked:** `BOOST_CHECK(!clientCluster-&gt;isAllocated())`, `BOOST_CHECK(clientCluster-&gt;isAllocated())`, `BOOST_CHECK(!clientCluster-&gt;isAllocated())`, `BOOST_CHECK(!clientCluster-&gt;isAllocated())`

### `ClusterDeltaBuffer::SendRandomTerrain`

- **Location:** `App.UnitTest/ClusterReplicationTest.cpp:1225`
- **Verified Functions:** `Asserts`, `BOOST_CHECK_LE`, `BOOST_WARN_EQUAL`, `client`, `clientCluster`, `clientWrapper`, `countChunkPackets`, `generateReasonableTerrain`
- **Invariants Checked:** `BOOST_CHECK_LE(packets,DesiredSendHertz*TargetSeconds)`, `BOOST_WARN_EQUAL(0, packets)`

### `ContentProvider::UrlReconstruction`

- **Location:** `App.UnitTest/ContentProviderTest.cpp:32`
- **Verified Functions:** `SetBaseURL`, `UrlReconstructToAssetGame`, `if`, `string`, `testContentIdAssetUrlReconstruction`
- **Invariants Checked:** *Implicit assertion via execution*

### `CustomEvents::CreatingStateSanityCheck`

- **Location:** `App.UnitTest/CustomEvents.cpp:78`
- **Verified Functions:** `BOOST_REQUIRE_EQUAL`, `evt`, `getCurrentValue`, `getParent`, `getPersistedCurrentValue`, `receiver`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL((Instance *)NULL, evt-&gt;getParent())`, `BOOST_REQUIRE_EQUAL((Instance *)NULL, evt-&gt;getParent())`, `BOOST_REQUIRE_EQUAL(0, evt-&gt;getPersistedCurrentValue())`, `BOOST_REQUIRE_EQUAL(0, receiver-&gt;getCurrentValue())`

### `CustomEvents::AttachedListMaintenance`

- **Location:** `App.UnitTest/CustomEvents.cpp:89`
- **Verified Functions:** `BOOST_REQUIRE`, `BOOST_REQUIRE_EQUAL`, `at`, `evt`, `get`, `getAttachedReceivers`, `receiver`, `receivers`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(1, receiver.use_count())`, `BOOST_REQUIRE(receiver.unique())`, `BOOST_REQUIRE_EQUAL(1, receivers-&gt;size())`, `BOOST_REQUIRE_EQUAL(receiver.get(), receivers-&gt;at(0).get())`

### `CustomEvents::SendValuesOnlyWhenConnected`

- **Location:** `App.UnitTest/CustomEvents.cpp:127`
- **Verified Functions:** `BOOST_REQUIRE_EQUAL`, `bind`, `call`, `callCounter`, `conn`, `connect`, `disconnect`, `evt`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(0, callCounter-&gt;calls)`, `BOOST_REQUIRE_EQUAL(0, callCounter-&gt;calls)`, `BOOST_REQUIRE_EQUAL(.5f, evt-&gt;getPersistedCurrentValue())`, `BOOST_REQUIRE_EQUAL(.5f, receiver-&gt;getCurrentValue())`

### `CustomEvents::ValueClamping`

- **Location:** `App.UnitTest/CustomEvents.cpp:188`
- **Verified Functions:** `BOOST_REQUIRE_EQUAL`, `bind`, `call`, `callCounter`, `conn`, `connect`, `disconnect`, `evt`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(0, evt-&gt;getPersistedCurrentValue())`, `BOOST_REQUIRE_EQUAL(1, evt-&gt;getPersistedCurrentValue())`, `BOOST_REQUIRE_EQUAL(0, callCounter-&gt;calls)`, `BOOST_REQUIRE_EQUAL(1, callCounter-&gt;calls)`

### `CustomEvents::SettingParentToNullDoesBreakConnection`

- **Location:** `App.UnitTest/CustomEvents.cpp:239`
- **Verified Functions:** `BOOST_REQUIRE_EQUAL`, `DataModel`, `DataModelJob`, `bind`, `call`, `callCounter`, `conn`, `connect`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(1, callCounter-&gt;calls)`, `BOOST_REQUIRE_EQUAL(.1f, callCounter-&gt;lastValue)`, `BOOST_REQUIRE_EQUAL(.1f, evt-&gt;getPersistedCurrentValue())`, `BOOST_REQUIRE_EQUAL(.1f, receiver-&gt;getCurrentValue())`

### `CustomEvents::BreakingConnectionSetsReceiverToZero`

- **Location:** `App.UnitTest/CustomEvents.cpp:301`
- **Verified Functions:** `BOOST_REQUIRE_EQUAL`, `DataModel`, `DataModelJob`, `bind`, `call`, `callCounter`, `conn`, `connect`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(1, callCounter-&gt;calls)`, `BOOST_REQUIRE_EQUAL(.1f, callCounter-&gt;lastValue)`, `BOOST_REQUIRE_EQUAL(.1f, evt-&gt;getPersistedCurrentValue())`, `BOOST_REQUIRE_EQUAL(.1f, receiver-&gt;getCurrentValue())`

### `CustomEvents::SenderRemembersLastState`

- **Location:** `App.UnitTest/CustomEvents.cpp:388`
- **Verified Functions:** `BOOST_REQUIRE`, `BOOST_REQUIRE_EQUAL`, `DataModel`, `DataModelJob`, `at`, `bind`, `call`, `callCounter`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(1, pasted.size())`, `BOOST_REQUIRE(evt != pastedEvent)`, `BOOST_REQUIRE_EQUAL(.5f, pastedEvent-&gt;getPersistedCurrentValue())`, `BOOST_REQUIRE_EQUAL(1, callCounter-&gt;calls)`

### `CustomEvents::CloneEvent`

- **Location:** `App.UnitTest/CustomEvents.cpp:424`
- **Verified Functions:** `BOOST_REQUIRE`, `BOOST_REQUIRE_EQUAL`, `bind`, `call`, `callCounter`, `clonedEvent`, `conn`, `connect`
- **Invariants Checked:** `BOOST_REQUIRE(clonedEvent)`, `BOOST_REQUIRE_EQUAL(0, clonedEvent-&gt;getAttachedReceivers()-&gt;size())`, `BOOST_REQUIRE_EQUAL(evt.get(), receiver-&gt;getSource())`, `BOOST_REQUIRE_EQUAL(1, evt-&gt;getAttachedReceivers()-&gt;size())`

### `CustomEvents::CloneReceiver`

- **Location:** `App.UnitTest/CustomEvents.cpp:458`
- **Verified Functions:** `BOOST_REQUIRE`, `BOOST_REQUIRE_EQUAL`, `bind`, `call`, `callCounter`, `clonedReceiver`, `conn`, `connect`
- **Invariants Checked:** `BOOST_REQUIRE(clonedReceiver)`, `BOOST_REQUIRE_EQUAL(evt.get(), clonedReceiver-&gt;getSource())`, `BOOST_REQUIRE_EQUAL(evt.get(), receiver-&gt;getSource())`, `BOOST_REQUIRE_EQUAL(2, evt-&gt;getAttachedReceivers()-&gt;size())`

### `CustomEvents::CloneEventAndReceiver`

- **Location:** `App.UnitTest/CustomEvents.cpp:491`
- **Verified Functions:** `BOOST_REQUIRE`, `BOOST_REQUIRE_EQUAL`, `ScriptingCreator`, `at`, `bind`, `call`, `callCounter`, `children`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(2, children-&gt;size())`, `BOOST_REQUIRE(clonedEvent)`, `BOOST_REQUIRE(clonedReceiver)`, `BOOST_REQUIRE_EQUAL(1, clonedEvent-&gt;getAttachedReceivers()-&gt;size())`

### `CustomEvents::StudioCopyEvent`

- **Location:** `App.UnitTest/CustomEvents.cpp:543`
- **Verified Functions:** `BOOST_REQUIRE`, `BOOST_REQUIRE_EQUAL`, `DataModel`, `DataModelJob`, `at`, `bind`, `call`, `callCounter`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(1, pasted.size())`, `BOOST_REQUIRE(pastedEvent)`, `BOOST_REQUIRE_EQUAL(0, pastedEvent-&gt;getAttachedReceivers()-&gt;size())`, `BOOST_REQUIRE_EQUAL(evt.get(), receiver-&gt;getSource())`

### `CustomEvents::StudioCopyReceiver`

- **Location:** `App.UnitTest/CustomEvents.cpp:583`
- **Verified Functions:** `BOOST_REQUIRE`, `BOOST_REQUIRE_EQUAL`, `DataModel`, `DataModelJob`, `at`, `bind`, `call`, `callCounter`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(1, pasted.size())`, `BOOST_REQUIRE(pastedReceiver)`, `BOOST_REQUIRE_EQUAL((Instance *)NULL, pastedReceiver-&gt;getSource())`, `BOOST_REQUIRE_EQUAL(evt.get(), receiver-&gt;getSource())`

### `CustomEvents::StudioCopyEventAndReceiver`

- **Location:** `App.UnitTest/CustomEvents.cpp:623`
- **Verified Functions:** `BOOST_REQUIRE`, `BOOST_REQUIRE_EQUAL`, `DataModel`, `DataModelJob`, `at`, `bind`, `call`, `callCounter`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(2, pasted.size())`, `BOOST_REQUIRE(pastedEvent)`, `BOOST_REQUIRE(evt != pastedEvent)`, `BOOST_REQUIRE(pastedReceiver)`

### `CustomEvents::ConnectAndDisconnectSignalsTriggering`

- **Location:** `App.UnitTest/CustomEvents.cpp:678`
- **Verified Functions:** `BOOST_REQUIRE_EQUAL`, `DataModel`, `DataModelJob`, `bind`, `call`, `clonedReceiver`, `conn1`, `conn2`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(0, receiverConnected-&gt;calls)`, `BOOST_REQUIRE_EQUAL(0, receiverDisconnected-&gt;calls)`, `BOOST_REQUIRE_EQUAL(0, eventConnected-&gt;calls)`, `BOOST_REQUIRE_EQUAL(0, eventDisconnected-&gt;calls)`

### `CustomEvents::ConnectAndDisconnectSignalHappensAfterInternalStateUpdate`

- **Location:** `App.UnitTest/CustomEvents.cpp:857`
- **Verified Functions:** `BOOST_REQUIRE`, `ConnectStateChecker`, `DataModel`, `DataModelJob`, `bind`, `checker`, `conn1`, `conn2`
- **Invariants Checked:** `BOOST_REQUIRE(!checker-&gt;checkedReceiverAdded)`, `BOOST_REQUIRE(!checker-&gt;checkedReceiverRemoved)`, `BOOST_REQUIRE(!checker-&gt;checkedEventAdded)`, `BOOST_REQUIRE(!checker-&gt;checkedEventRemoved)`

### `FastLogSettings::Serializer`

- **Location:** `App.UnitTest/FastLogSettingsTest.cpp:21`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `DirExe`, `FetchClientSettingsData`, `FileSystem`, `TestFastFlag`, `TestLogGroup`, `c_str`, `close`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(FLog::TestLogGroup, 0)`, `BOOST_CHECK_EQUAL(FFlag::TestFastFlag, false)`, `BOOST_CHECK_EQUAL(FLog::TestLogGroup, 1)`, `BOOST_CHECK_EQUAL(FFlag::TestFastFlag, true)`

### `FastLogSettings::Lua` (Fixture: `DataModelFixture`)

- **Location:** `App.UnitTest/FastLogSettingsTest.cpp:44`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `BOOST_CHECK_THROW`, `GetFFlag`, `GetFVariable`, `GetFastVariable`, `Reflection`, `at`, `auto_ptr`
- **Invariants Checked:** `BOOST_CHECK_THROW(execute("return settings():GetFastVariable('ThisFlagDoesNotExist')"), std::exception)`, `BOOST_CHECK_EQUAL(result-&gt;values.at(0).convert&lt;std::string&gt;(), "true")`, `BOOST_CHECK_EQUAL(result-&gt;values.at(1).convert&lt;std::string&gt;(), "false")`, `BOOST_CHECK_EQUAL(result-&gt;values.at(2).convert&lt;bool&gt;(), true)`

### `G3D::TestRbxRay`

- **Location:** `App.UnitTest/G3D.cpp:16`
- **Verified Functions:** `BOOST_CHECK_CLOSE`, `BOOST_CHECK_EQUAL`, `RbxRay`, `Vector3`, `closestPoint`, `distance`, `fromOriginAndDirection`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(ray.closestPoint(G3D::Vector3(1, 0, 0)), G3D::Vector3(4, 12, 0))`, `BOOST_CHECK_CLOSE(ray.distance(G3D::Vector3(1, 0, 0)), 12.3693171f, 0.0001f)`

### `G3D::TestCamera`

- **Location:** `App.UnitTest/G3D.cpp:24`
- **Verified Functions:** `BOOST_CHECK_CLOSE`, `Camera`, `RbxRay`, `Rect2D`, `direction`, `origin`, `setFieldOfViewDegrees`, `setViewport`
- **Invariants Checked:** `BOOST_CHECK_CLOSE(rayOrigin.x, -0.681681f, 0.005f)`, `BOOST_CHECK_CLOSE(rayOrigin.y, 19.6904f, 0.005f)`, `BOOST_CHECK_CLOSE(rayOrigin.z, 19.2997f, 0.005f)`, `BOOST_CHECK_CLOSE(direction.x, -0.664961874f, 0.0005f)`

### `G3D::TestAABox`

- **Location:** `App.UnitTest/G3D.cpp:50`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `Vector3`, `aaBox`, `area`, `center`, `corner`, `extent`, `high`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(aaBox.isFinite(), true)`, `BOOST_CHECK_EQUAL(aaBox.low(), G3D::Vector3(0, 0, -8))`, `BOOST_CHECK_EQUAL(aaBox.high(), G3D::Vector3(8, 8, 0))`, `BOOST_CHECK_EQUAL(aaBox.center(), G3D::Vector3(4, 4, -4))`

### `G3D::TestColor3`

- **Location:** `App.UnitTest/G3D.cpp:64`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `Color3`, `color`, `dummy`, `fuzzyEq`, `fuzzyNe`, `isFinite`, `isZero`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(color.isZero(), false)`, `BOOST_CHECK_EQUAL(color.isFinite(), true)`, `BOOST_CHECK_EQUAL(color.max(dummy), Color3(0.7f,0.4f,0.8f))`, `BOOST_CHECK_EQUAL(color.min(dummy), Color3(0.2f,0.2f,0.5f))`

### `G3D::TestColor3uint8`

- **Location:** `App.UnitTest/G3D.cpp:77`
- **Verified Functions:** `BOOST_CHECK`, `BOOST_CHECK_EQUAL`, `Color3`, `Color3uint8`, `asUInt32`, `bgr`, `color`, `floor`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(sizeof(G3D::Color3uint8), 3)`, `BOOST_CHECK_EQUAL(def, G3D::Color3uint8(0, 0, 0))`, `BOOST_CHECK_EQUAL(color.r, 10)`, `BOOST_CHECK_EQUAL(color.g, 20)`

### `G3D::TestCoordinateFrame`

- **Location:** `App.UnitTest/G3D.cpp:110`
- **Verified Functions:** `BOOST_CHECK_CLOSE`, `BOOST_CHECK_EQUAL`, `CoordinateFrame`, `Math`, `Matrix3`, `NORM_X_NEG`, `NORM_Y`, `RbxRay`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(coord.fuzzyEq(dummy), false)`, `BOOST_CHECK_EQUAL(x, 0)`, `BOOST_CHECK_EQUAL(y, -0.5f)`, `BOOST_CHECK_EQUAL(z, 0)`

### `G3D::TestVector3`

- **Location:** `App.UnitTest/G3D.cpp:142`
- **Verified Functions:** `BOOST_CHECK_CLOSE`, `BOOST_CHECK_EQUAL`, `Vector3`, `direction`, `length`, `lerp`, `reflectAbout`, `reflectionDirection`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(v1+v2, G3D::Vector3(7, -2, 7))`, `BOOST_CHECK_EQUAL(v1-v2, G3D::Vector3(1, 6, -5))`, `BOOST_CHECK_CLOSE(v1.length(), 4.5825758f, 0.0001f)`, `BOOST_CHECK_CLOSE(v.x, 0.87287152f, 0.0001f)`

### `G3D::TestFrustum`

- **Location:** `App.UnitTest/G3D.cpp:214`
- **Verified Functions:** `BOOST_CHECK`, `Extents`, `FailsPlane`, `Frustum`, `Math`, `Vector3`, `containsAABB`, `containsPoint`
- **Invariants Checked:** `BOOST_CHECK(fr1.containsAABB(ex))`, `BOOST_CHECK(fr2.containsAABB(ex))`, `BOOST_CHECK(FailsPlane(ex, fr1, RBX::Frustum::kPlaneInvalid))`, `BOOST_CHECK(FailsPlane(ex, fr2, RBX::Frustum::kPlaneInvalid))`

### `G3D::TestFrustumTransformed`

- **Location:** `App.UnitTest/G3D.cpp:390`
- **Verified Functions:** `BOOST_CHECK`, `Frustum`, `Vector3`, `containsPoint`, `fr1`, `fr2`
- **Invariants Checked:** `BOOST_CHECK(fr1.containsPoint(G3D::Vector3(150, 200, 300)))`, `BOOST_CHECK(!fr1.containsPoint(G3D::Vector3( 50, 200, 300)))`, `BOOST_CHECK(!fr2.containsPoint(G3D::Vector3(150, 200, 300)))`, `BOOST_CHECK(fr2.containsPoint(G3D::Vector3( 50, 200, 300)))`

### `HTTPSuite::HTTP_SYNC_GET_TESTS`

- **Location:** `App.UnitTest/HTTPTest.cpp:98`
- **Verified Functions:** `Http`, `Interval`, `RBX_TEST_WITH_TIMEOUT`, `Time`, `a`, `b`, `bind`, `c`
- **Invariants Checked:** *Implicit assertion via execution*

### `HTTPSuite::HTTP_SYNC_GET_EXTERNAL_TESTS`

- **Location:** `App.UnitTest/HTTPTest.cpp:125`
- **Verified Functions:** `Http`, `Interval`, `RBX_TEST_WITH_TIMEOUT`, `Time`, `a`, `b`, `bind`, `c`
- **Invariants Checked:** *Implicit assertion via execution*

### `HTTPSuite::HTTP_SYNC_POST_EXTERNAL_TESTS`

- **Location:** `App.UnitTest/HTTPTest.cpp:146`
- **Verified Functions:** `Http`, `Interval`, `RBX_TEST_WITH_TIMEOUT`, `Time`, `a`, `b`, `bind`, `c`
- **Invariants Checked:** *Implicit assertion via execution*

### `HTTPSuite::HTTP_SYNC_POST_TESTS`

- **Location:** `App.UnitTest/HTTPTest.cpp:175`
- **Verified Functions:** `Interval`, `RBX_TEST_WITH_TIMEOUT`, `Time`
- **Invariants Checked:** *Implicit assertion via execution*

### `HTTPSuite::HTTP_URL_ENCODE_TEST`

- **Location:** `App.UnitTest/HTTPTest.cpp:180`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `Http`, `urlEncode`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(RBX::Http::urlEncode("this is a&#test"), "this%20is%20a%26%23test")`

### `HTTPSuite::HTTP_URL_DECODE_TEST`

- **Location:** `App.UnitTest/HTTPTest.cpp:185`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `BOOST_REQUIRE_EQUAL`, `Http`, `for`, `size`, `string`, `urlDecode`, `urlEncode`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(allChars.size(), 255)`, `BOOST_CHECK_EQUAL(allChars, RBX::Http::urlDecode(RBX::Http::urlEncode(allChars)))`

### `HTTPSuite::API_PROXY_HTTP_SYNC_GET_TESTS`

- **Location:** `App.UnitTest/HTTPTest.cpp:196`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `DataModel`, `DataModelJob`, `GetService`, `HttpRbxApiService`, `PRIORITY_EXTREME`, `Reflection`, `ServiceProvider`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(asset, 28277486)`, `BOOST_CHECK_EQUAL(product, 4678951)`

### `HTTPSuite::API_PROXY_HTTP_ASYNC_GET_TESTS`

- **Location:** `App.UnitTest/HTTPTest.cpp:229`
- **Verified Functions:** `DataModel`, `DataModelJob`, `GetService`, `HttpRbxApiService`, `PRIORITY_EXTREME`, `Reflection`, `ServiceProvider`, `SetBaseUrl`
- **Invariants Checked:** *Implicit assertion via execution*

### `HTTPSuite::API_PROXY_HTTP_ASYNC_POST_TESTS`

- **Location:** `App.UnitTest/HTTPTest.cpp:248`
- **Verified Functions:** `ContentProvider`, `DataModel`, `DataModelJob`, `GetService`, `Http`, `HttpRbxApiService`, `HttpService`, `PRIORITY_EXTREME`
- **Invariants Checked:** *Implicit assertion via execution*

### `HeapValueTest::OperatorOverloads`

- **Location:** `App.UnitTest/HeapValueTest.cpp:9`
- **Verified Functions:** `BOOST_CHECK`, `BOOST_CHECK_EQUAL`, `heapValue`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(nonRef, heapValue)`, `BOOST_CHECK_EQUAL(nonRef, kOriginalValue)`, `BOOST_CHECK(nonRef != heapValue)`, `BOOST_CHECK_EQUAL(nonRef, kOriginalValue)`

### `HttpCacheEntryTest::CACHE_DATA_TOSTRING_TEST` (Fixture: `Fixture`)

- **Location:** `App.UnitTest/HttpCacheEntryTest.cpp:75`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `Cache`, `data`, `headers`, `size`, `toString`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(httpHeaders, headers.toString())`

### `HttpCacheEntryTest::CACHE_UPDATE_TEST` (Fixture: `Fixture`)

- **Location:** `App.UnitTest/HttpCacheEntryTest.cpp:81`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `Cache`, `body`, `c_str`, `data`, `getCacheHeader`, `getResponseBody`, `getResponseHeader`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(200, result.getCacheHeader().responseCode)`, `BOOST_CHECK_EQUAL(httpHeaders, result.getResponseHeader().toString())`, `BOOST_CHECK_EQUAL(httpBody, result.getResponseBody().toString())`, `BOOST_CHECK_EQUAL(httpHeaders.size(), result.getResponseHeader().size())`

### `HumanoidTest::SetVelocityBeforeHumanoidIsPutIntoWorld`

- **Location:** `App.UnitTest/HumanoidTest.cpp:9`
- **Verified Functions:** `BOOST_REQUIRE`, `direction`, `fuzzyEq`, `getWalkDirection`, `setWalkDirection`, `unit`
- **Invariants Checked:** `BOOST_REQUIRE(humanoid-&gt;getWalkDirection().fuzzyEq(direction))`

### `Instance::Clone`

- **Location:** `App.UnitTest/Instance.cpp:86`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `Creatable`, `Diagnostics`, `Instance`, `ScriptingCreator`, `clone`, `getCount`, `shared_ptr`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(count, RBX::Diagnostics::Countable&lt;RBX::Instance&gt;::getCount())`

### `Instance::CastTo`

- **Location:** `App.UnitTest/Instance.cpp:137`
- **Verified Functions:** `BOOST_CHECK`, `BasicPartInstance`, `Creatable`, `Instance`, `PartInstance`, `get`
- **Invariants Checked:** `BOOST_CHECK(RBX::Instance::fastDynamicCast&lt;RBX::Instance&gt;(part.get()))`, `BOOST_CHECK(!RBX::Instance::fastDynamicCast&lt;RBX::PartInstance&gt;(instance.get()))`, `BOOST_CHECK(!RBX::Instance::fastDynamicCast&lt;RBX::PartInstance&gt;(nullInstance))`, `BOOST_CHECK(inst-&gt;fastDynamicCast&lt;RBX::Instance&gt;())`

### `Instance::CastToConst`

- **Location:** `App.UnitTest/Instance.cpp:155`
- **Verified Functions:** `BOOST_CHECK`, `BasicPartInstance`, `Creatable`, `Instance`, `PartInstance`, `get`
- **Invariants Checked:** `BOOST_CHECK(RBX::Instance::fastDynamicCast&lt;RBX::Instance&gt;(part.get()))`, `BOOST_CHECK(!RBX::Instance::fastDynamicCast&lt;RBX::PartInstance&gt;(instance.get()))`, `BOOST_CHECK(!RBX::Instance::fastDynamicCast&lt;RBX::PartInstance&gt;(nullInstance))`, `BOOST_CHECK(inst-&gt;fastDynamicCast&lt;RBX::Instance&gt;())`

### `Instance::SharedCastTo`

- **Location:** `App.UnitTest/Instance.cpp:173`
- **Verified Functions:** `BOOST_CHECK`, `BasicPartInstance`, `Creatable`, `Instance`, `PartInstance`
- **Invariants Checked:** `BOOST_CHECK(RBX::Instance::fastSharedDynamicCast&lt;const RBX::Instance&gt;(part))`, `BOOST_CHECK(!RBX::Instance::fastSharedDynamicCast&lt;const RBX::PartInstance&gt;(instance))`, `BOOST_CHECK(!RBX::Instance::fastSharedDynamicCast&lt;const RBX::PartInstance&gt;(nullInstance))`

### `Instance::LockUnlockDeprecated` (Fixture: `DataModelFixture`)

- **Location:** `App.UnitTest/Instance.cpp:186`
- **Verified Functions:** `BOOST_CHECK`, `BOOST_REQUIRE_EQUAL`, `Lock`, `Reflection`, `Unlock`, `at`, `auto_ptr`, `execute`
- **Invariants Checked:** `BOOST_REQUIRE_EQUAL(result-&gt;values.size(), 1)`, `BOOST_CHECK(result-&gt;values.at(0).get&lt;bool&gt;())`

### `Instance::Parenting`

- **Location:** `App.UnitTest/Instance.cpp:193`
- **Verified Functions:** `BOOST_CHECK`, `BOOST_CHECK_THROW`, `Creatable`, `DataModel`, `DataModelJob`, `Instance`, `exception`, `getParent`
- **Invariants Checked:** `BOOST_CHECK(checkAncestor-&gt;getParent() != NULL)`, `BOOST_CHECK_THROW(instance-&gt;setParent2(dm.dataModel), std::exception)`, `BOOST_CHECK_THROW(checkAncestor-&gt;setParent2(dm.dataModel), std::exception)`, `BOOST_CHECK_THROW(checkAncestor-&gt;setParent2(instance), std::exception)`

### `Instance::ReparentingLock`

- **Location:** `App.UnitTest/Instance.cpp:213`
- **Verified Functions:** `BOOST_CHECK`, `BOOST_CHECK_THROW`, `Creatable`, `Instance`, `exception`, `get`, `getIsParentLocked`, `getParent`
- **Invariants Checked:** `BOOST_CHECK(!parent-&gt;getIsParentLocked())`, `BOOST_CHECK(parent-&gt;getIsParentLocked())`, `BOOST_CHECK(child-&gt;getIsParentLocked())`, `BOOST_CHECK(child-&gt;getParent() == parent.get())`

### `Instance::SetParentNull`

- **Location:** `App.UnitTest/Instance.cpp:251`
- **Verified Functions:** `Creatable`, `Instance`, `get`, `getChild`, `setParent`
- **Invariants Checked:** *Implicit assertion via execution*

### `Instance::WaitForChildReturnsImmediatelyIfChildPresent`

- **Location:** `App.UnitTest/Instance.cpp:264`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `Instance`, `LegacyLock`, `WaitForChild`, `Write`, `create`, `fromTestSource`, `getName`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(part-&gt;getName(), "Renamed")`

### `Instance::WaitForSameChildAfterInitialWaitForChild`

- **Location:** `App.UnitTest/Instance.cpp:289`
- **Verified Functions:** `BOOST_CHECK_EQUAL`, `Instance`, `LegacyLock`, `WaitForChild`, `Write`, `create`, `fromTestSource`, `getName`
- **Invariants Checked:** `BOOST_CHECK_EQUAL(part-&gt;getName(), "Renamed")`

### `Instance::TwoScriptsWaitingForSameChild`

- **Location:** `App.UnitTest/Instance.cpp:314`
- **Verified Functions:** `BOOST_CHECK`, `Instance`, `LegacyLock`, `System`, `WaitForChild`, `Write`, `create`, `findFirstChildByName`
- **Invariants Checked:** `BOOST_CHECK(dm-&gt;getWorkspace()-&gt;findFirstChildByName("Alice") != NULL)`, `BOOST_CHECK(dm-&gt;getWorkspace()-&gt;findFirstChildByName("Bob") != NULL)`

---
sidebar_position: 2
---

# App — the engine

**Path:** `App/` · **Project:** `App.vcxproj` / `App.xcodeproj` / `CMakeLists.txt` ·
**Status:** ✅ builds

`App` is the Roblox engine itself. Everything that makes a Roblox game a Roblox game — the
Instance tree, the DataModel with all its services, Lua scripting, physics, terrain, Studio
tools and the security model — lives here. Both the player clients and `RCCService` link it.

## Layout

```
App/
├── include/          # Public headers, mirrored per subsystem (V8Tree/, V8DataModel/, …)
├── v8tree/           # RBX::Instance base class, Service, Verb, Property, EnumProperty
├── v8datamodel/      # DataModel + every game object & service (biggest folder)
├── v8world/          # Physics world: assemblies, contacts, stages
├── v8kernel/         # Physics kernel: bodies, connectors, links
├── solver/           # Constraint solver (PGS)
├── humanoid/         # Character controller state machine
├── script/           # Lua scripting: ScriptContext, VMs, bridges, debugger
├── reflection/       # The reflection system descriptors
├── v8xml/            # XML/binary serialization of the tree
├── voxel/            # Classic voxel terrain
├── voxel2/           # Smooth terrain (gen-2)
├── gui/              # In-game HUD: chat, scores, equation display
├── tool/             # Studio tools (move/resize/paint/draggers)
├── security/         # SecurityContext, FuzzyTokens
├── util/             # ContentProvider, BrickColor, Http, platform helpers…
├── Lua-5.1.4/        # Vendored Lua interpreter source
├── lz4/              # Vendored LZ4 compression (lz4 + lz4hc)
├── App.vcxproj       # (+ .filters) Visual Studio project
├── App.xcodeproj     # Mac project
└── CMakeLists.txt    # CMake build
```

## Subsystem highlights

### `v8datamodel/` — the game objects

200+ files covering parts, meshes, decals, effects, joints, GUI, characters, animation,
cameras and all the services (`Players`, `Lighting`, `ChatService`, `DataStoreService`,
`BadgeService`, `CollectionService`, `CSGDictionaryService`, …). Detailed in
[The DataModel](../architecture/datamodel.md).

### `script/` — Lua

`ScriptContext`, per-context VMs (`LuaVMClient/Server/Dummy`), the Instance↔Lua bridges,
`ModuleScript`/`CoreScript`, the debugger manager and the script analyzer. Detailed in
[Scripting](../architecture/scripting.md).

### `v8world`, `v8kernel`, `solver`, `humanoid` — physics

The staged simulation world, the rigid-body kernel, the PGS constraint solver and the humanoid
state machine. Detailed in [Physics](../architecture/physics.md).

### `tool/` — Studio tools

One class per editing tool: `AdvMoveTool`, `AdvRotateTool`, `AdvDragTool`, `AdvLuaDragger`,
`ResizeTool`, `CloneTool`, `HammerTool` (delete), `DropTool`/`PartDropTool`,
`MoveResizeJoinTool`, draggers (`Dragger`, `MegaDragger`, `GroupDragTool`, `RunDragger`) and
`ToolsArrow` (the selection arrow). Studio instantiates these against the current selection.

### `gui/` — in-game HUD

`GUI.cpp`, `ChatOutput.cpp`/`ChatWidget.cpp` (chat window), `ScoreHud.cpp`,
`EquationDisplay.cpp`, `ProfanityFilter.cpp` — the client-side 2D overlay layer of the era
(before the full 2D-GUI-in-Lua migration completed).

### `util/` — the toolbox

Big and varied: `ContentProvider.cpp` (+ `ContentProviderJob.cpp`, `AsyncHttpQueue.cpp`,
`CacheableContentProvider.cpp`) for asset loading; `BrickColor.cpp` (the classic palette);
`HttpAsync.cpp`; `Analytics.cpp`; `IndexedTree.cpp`; `Extents.cpp`/`OrientedExtents`;
`HitTest.cpp`; `MD5Hasher.cpp`; `MachineIdUploader*`; per-platform helpers
(`Android/`, `Darwin/`, `Durango/`, `NaCl?`…); `KeyCode.cpp`, `CameraSubject.cpp`,
`GameMode.h` and many more.

### `security/`

`SecurityContext.cpp` (identity/permission contexts), `FuzzyTokens.cpp` (typo-squat detection),
see [Security](../development/security.md).

### `v8xml/`

`XmlSerializer`, `SerializerBinary`, `SerializerV2`, `WebSerializer`/`WebParser`,
`XmlElement` — see [Serialization](../architecture/serialization.md).

## Building it

Part of `Roblox.sln` (project **App**) and the CMake tree; on the "builds" list of the
README.

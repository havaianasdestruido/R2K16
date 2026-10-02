---
sidebar_position: 3
---

# The DataModel

*Where:* `App/v8datamodel/` (headers in `App/include/V8DataModel/`)

The **DataModel** is the root of the Instance tree in a running game. It owns the services
(Workspace, Players, Lighting, …), which in turn own every part, script and GUI. This folder is
the single biggest directory in `App/` — it is "the game" itself.

## Services

`DataModel.cpp` assembles the standard service set. Every service derives from
`RBX::Instance` via `Service` (`App/v8tree/Service.cpp`) and is created as a singleton child
of the DataModel. Representative services in `v8datamodel/`:

| Service file | Role |
| --- | --- |
| `Workspace` | The 3D scene: parts, terrain, camera |
| `Players` / `Player` / `Backpack` | Player & character management |
| `Lighting` | Atmosphere/lighting settings |
| `ScriptService` (see `ScriptContext`) | Hosts user scripts |
| `ChatService` | Server-side chat pipeline (with `Network/ChatFilter`, `WebChatFilter`) |
| `BadgeService`, `DataStoreService`, `AssetService` | Web-backed game services |
| `CollectionService` | Tag-based instance collections |
| `DebrisService` | Timed object destruction |
| `CSGDictionaryService` | Solid-model geometry dictionary |
| `CookiesEngineService` | Client cookie handling |

## Scene objects

The classic part family and everything that dresses them up:

- **Parts:** `BasicPartInstance`, `ExtrudedPartInstance`, `CornerWedgeInstance`, `FormGroupPart`…
- **Meshes:** `BlockMesh`, `CylinderMesh`, `FileMesh`, `SpecialMesh`, `BevelMesh`, `DataModelMesh`
- **Surfaces:** `Decal`, `FaceInstance`, `Texture`
- **Effects:** `Fire`, `Smoke`, `Explosion`, `CustomParticleEmitter`, `Sparkles`
- **Joints & attachments:** `JointInstance`, `Attachment`, `AnimatableRootJoint`, `Weld`-family
- **CSG:** `CSGMesh` — boolean-geometry results (see [Terrain & CSG](./terrain-and-csg.md))

## GUI

2D interface objects: `BillboardGui`, `GuiObject` derivatives, dialogs
(`DialogRoot`, `DialogChoice`). Billboard rendering cooperates with the adornment/billboarder
system in `Rendering/GfxBase` (`AdornBillboarder`, `ViewportBillboarder`).

## Characters & animation

- `CharacterAppearance`, `CharacterMesh`, `Accoutrement` — avatar composition
- `Humanoid` (see [Physics](./physics.md#humanoids) for the state machine in `App/humanoid/`)
- `Animation`, `AnimationController`, `AnimationTrack`, `AnimationTrackState`, `Animator` —
  keyframe animation playback

## Camera & editing

- `Camera` — render camera; `BaseRenderJob` consumes it for rendering jobs
- `ChangeHistory` — Studio undo/redo journal
- `Commands`, `CommonVerbs` — editor command plumbing (verbs, see
  [Instance tree](./instance-tree.md))
- `Selection` — Studio selection service

## Settings & diagnostics

`DebugSettings.cpp` and `FastLogSettings.cpp` expose engine settings & FastLog groups as
reflection-visible objects (see [FastFlags & logging](../development/fastflags-logging.md)).
`Filters.cpp` implements the DataModel query/filter helpers.

## DataModel lifecycle & threading

The DataModel is mutated on its own scheduled job (`DataModelJob.cpp`,
`DataModelEmptySerialize.cpp` in `ClientShared/`) — everything else (rendering, physics,
networking) reads staged copies under the arbitration rules of the
[TaskScheduler](./jobs-and-scheduler.md). Services can also register auxiliary jobs
(e.g. `ContentProviderJob` for async asset fetch, `NetworkOwnerJob` for network ownership).

Continue with [Jobs & the TaskScheduler](./jobs-and-scheduler.md).

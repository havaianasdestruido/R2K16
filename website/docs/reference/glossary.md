---
sidebar_position: 2
---

# Glossary

Terms you'll run into in the code, commit history and docs.

## Engine concepts

| Term | Meaning |
| --- | --- |
| **Instance** | The universal node type (`RBX::Instance`). Everything in a game is one. |
| **DataModel** | The root Instance of a running game; owns all services. |
| **Service** | Singleton child of the DataModel providing subsystem behavior (`Players`, `Lighting`, …). |
| **Reflection** | The descriptor system exposing properties/methods/events to Lua, Studio and serialization. |
| **Descriptor** | A single reflection entry (`PropDescriptor`, `BoundFuncDesc`, `Event`…). |
| **Verb** | Editor action/command abstraction (`App/v8tree/Verb.cpp`). |
| **Adornment** | Renderer overlay primitive — selection boxes, wireframes, billboards (`GfxBase/Adorn*`). |
| **Job** | Unit of scheduled work on the `TaskScheduler`. |
| **Arbiter** | Scheduler component declaring which jobs are mutually exclusive. |
| **Assembly** | Group of parts joined rigidly, simulated as one body in `v8world`. |
| **Kernel** | The low-level physics core (`v8kernel`): bodies, connectors, links, pairs. |
| **PGS** | Projected Gauss–Seidel — the iterative constraint solver (`App/solver`). |
| **DPhysics** | Era-internal name for parts of the distributed physics stack (see `RobloxTest/DPhysicsTests`). |
| **Network ownership** | Which peer (client or server) simulates a given assembly (`NetworkOwnerJob`). |
| **Error compensation** | Physics sync strategy sending corrections sized by divergence (`ErrorCompPhysicsSender`). |
| **Humanoid** | The character controller and its state machine (`App/humanoid`). |
| **Voxel terrain (gen 1/gen 2)** | Blocky cell terrain (`App/voxel`) and smooth terrain (`App/voxel2`). |
| **CSG** | Constructive Solid Geometry — boolean part operations via sgCore. |
| **CoreScript** | Engine-internal Lua script shipped with the client/server (signed). |
| **ModuleScript** | Lua module (`require()`-able) instance type. |
| **FastFlag / DFFlag** | Runtime feature toggle (`DYNAMIC_FASTFLAGVARIABLE`); DFInt/DFString variants for numbers/strings. |
| **FastLog / LOGVARIABLE** | Runtime-tunable logging channels. |
| **FuzzyTokens** | Near-miss detection for protected global names (`App/security`). |
| **BrickColor** | The classic numbered color palette (`App/util/BrickColor.cpp`). |
| **ContentProvider** | Asset fetch/cache subsystem (`App/util/ContentProvider.cpp`). |
| **rbxmx / rbxlx** | XML place/model file formats (human-readable). |
| **rbxm / rbxl** | Binary place/model file formats (`SerializerBinary`). |
| **Teleporter** | Era name for the client's server-hop flow (`WindowsClient/Teleporter.cpp`). |

## Platforms & product names

| Term | Meaning |
| --- | --- |
| **Durango** | Xbox One codename — `PlatformContent/durango`, `Base/rbx/Durango`, `XboxClient`. |
| **NSAL** | Network Security Access List — Xbox Live URL allow-listing (`XboxClient/NSAL.json`). |
| **RCC** | Roblox Cloud Compute — the game-hosting service (`RCCService`). |
| **Arbiter** | C# supervisor managing RCC instances (`Roblox.RccServiceArbiter`). |
| **RbxWebView** | Embedded Gecko web view in the Windows client (xulrunner). |
| **G3D** | The G3D graphics library vendored in `Rendering/g3d`. |
| **QTitanRibbon** | Commercial-style Qt ribbon widget library used by Studio. |
| **Breakpad** | Google's crash-dumping library used by Studio's crash reporters. |
| **VMProtect** | Code-protection/packing SDK used by the engine. |
| **xulrunner** | Mozilla's embeddable Gecko runtime (powers the client's web view). |
| **FMOD** | Audio middleware (`fmod/`). |
| **Team Create / Cloud Edit** | Era names for collaborative editing (`CloudEditAdornable` in Studio). |
| **SafeChat** | Restricted chat mode for young accounts (fork wants to restore it in Studio settings). |
| **Hybrid client** | Web-shell + native player mix (`RobloxHybrid/`). |

## Fork-specific

| Term | Meaning |
| --- | --- |
| **R2K16** | This fork — "Roblox 2016". |
| **git.rip base** | The original public re-upload of the 2016 source the fork is based on. |
| **The 557** | Security findings from the GitHub scanning workflows the README tracks. |

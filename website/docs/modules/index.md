---
sidebar_position: 1
---

# Module reference

A folder-by-folder tour of the repository. Each page describes one module (project or group of
projects): its purpose, notable files, and where it fits in the engine.

| Module | Type | Summary |
| --- | --- | --- |
| [App](./app.md) | C++ static lib | The engine core: Instance tree, DataModel, Lua, physics, terrain, tools |
| [Base](./base.md) | C++ static lib | Foundation: TaskScheduler, platform utilities, asserts, memory |
| [Network](./network.md) | C++ static lib | RakNet-based replication & physics sync (RakNet vendored) |
| [Rendering](./rendering.md) | C++ libs | Graphics stack: GfxCore, GfxRender, GfxBase, RbxG3D, AppDraw, VR |
| [CSG](./csg.md) | C++ lib | Solid boolean geometry via sgCore |
| [App.BulletPhysics](./bullet.md) | C++ lib | Embedded Bullet Physics distribution |
| [RobloxStudio](./studio.md) | C++ app (Qt 4.8) | The Studio editor |
| [RCCService](./rcc.md) | C++ service + C# arbiter | Headless game hosting (Roblox Cloud Compute) |
| [Clients](./clients.md) | apps | WindowsClient, Win, XboxClient, iOS, Android, Mac, RobloxHybrid |
| [Libraries](./libraries.md) | vendored | Boost, Qt, SDL, curl, zlib, FMOD, and friends |
| [Testing](./testing.md) | test suites | Unit tests, RobloxTest harnesses, service tests |
| [Tooling](./tooling.md) | tools | ScriptSigner, CoreScriptConverter2, analyzers, plugins |
| [Content](./content.md) | assets | content/, PlatformContent/, shaders/, BuiltInPlugins |

The [Repository Map](../reference/repo-map.md) additionally lists every top-level entry
including one-off directories (installer, property sheets, CI config, …).

:::tip Solution layout

Almost every C++ module builds from **both** `Roblox.sln` (via `.vcxproj`) and the CMake tree
(via its own `CMakeLists.txt`); several also carry Xcode projects (`.xcodeproj`) for the Mac
build. Many have `*.PrepForUpload` companion projects that produce upload-ready artifacts.
:::

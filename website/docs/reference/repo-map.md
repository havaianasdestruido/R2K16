---
sidebar_position: 1
---

# Repository map

Every top-level entry in the repository, annotated. Deeper dives live in the
[Module Reference](../modules/index.md).

## Engine & foundations

| Entry | Kind | Description |
| --- | --- | --- |
| `App/` | C++ lib | The engine: Instance tree (`v8tree`), DataModel (`v8datamodel`), physics (`v8world`, `v8kernel`, `solver`, `humanoid`), Lua (`script/`, `Lua-5.1.4/`), reflection, serialization (`v8xml`), terrain (`voxel`, `voxel2`), tools, util, security |
| `Base/` | C++ lib | Foundations: TaskScheduler, platform layers, asserts, memory, profiling |
| `Network/` | C++ lib | RakNet-based replication stack (RakNet vendored in `Network/raknet/`) |
| `Rendering/` | C++ libs | `GfxBase`, `GfxCore` (D3D9/D3D11/GL), `GfxRender`, `RbxG3D`, `g3d`, `AppDraw`, `ShaderCompiler`, `LibOVR`, `OpenVR`, `VrApi` |
| `CSG/` | C++ lib | Solid boolean geometry kernel over vendored sgCore |
| `App.BulletPhysics/` | C++ lib | Embedded Bullet Physics distribution |
| `ClientBase/` | C++ lib | Client-side base bits: `MachineConfiguration`, `ReflectionMetadata` (+ `.xml`) |
| `ClientShared/` | C++ lib | Code shared by clients: `DataModelSerialize`, `CookiesEngine` (with `Mac/`, `Mobile/` variants), `SDLGameController`, `InfluxDbHelper`, `RobloxServicesTools`, `CountersClient` |

## Applications

| Entry | Kind | Description |
| --- | --- | --- |
| `RobloxStudio/` | C++ app (Qt) | The Studio editor — see [Studio](../modules/studio.md) |
| `WindowsClient/` | C++ app | Windows player client — see [Clients](../modules/clients.md) |
| `Win/` | C++ lib | Shared Windows launcher code (logging, error upload, video capture, anti-debug) |
| `XboxClient/` | UWP app | Xbox One client (not building) |
| `iOS/` | Xcode | iOS app + tests |
| `Android/` | Gradle | Android app, `libroblox` native build, tests |
| `Mac/`, `RobloxMac/`, `MacClient.xcodeproj` | Xcode | Mac app & workspace scaffolding |
| `RobloxHybrid/` | JS/native | Hybrid web-shell client (Closure-compiled) |
| `GameChat/` | C++ lib | Microsoft Xbox GameChat XDK sources (not building) |
| `Microsoft.Xbox.Samples.NetworkMesh/` | C++ | Xbox mesh-networking samples (not building) |

## Services

| Entry | Kind | Description |
| --- | --- | --- |
| `RCCService/` | C++ service | Headless game host — see [RCCService](../modules/rcc.md) |
| `Roblox.RccServiceArbiter/` | C# | RCC supervisor/arbiter (`JobManager.cs`, …) |
| `RCCService.Test/`, `RCCService.Thumb.Test/` | C# tests | Service & thumbnail tests |
| `RCCService.PrepForUpload/`, `RCCServiceArbiter.PrepForUpload/` | packaging | Release packaging stubs |

## Testing

| Entry | Description |
| --- | --- |
| `App.UnitTest/` + `.Lib/` + `.Run/` | Engine unit tests (not building) |
| `Base.UnitTest/` + `.Lib/` + `.Run/` | Foundation unit tests w/ TeamCity integration (not building) |
| `RobloxTest/` | Big simulation/API/physics test rig (not building) |
| `RobloxTest.Run/`, `RobloxTest.MultiPlayerTest.Run/`, `RobloxTest.PhysicsTests.Run/`, `RobloxTest.PhysicsPerfTest.Run/` | Run-project stubs for the rig |
| `Roblox.Test/` | MSUnit-based aggregate tests (`TestCases/`, `Rig/`, `MSUnitProxy/`, `RemoteTestShim/`) |
| `RbxTestHooks/` | DLL exposing engine hooks for test injection (builds) |
| `RobloxMobileTest/` | Mobile test target |
| `SimulationTestUtility/` | Shared simulation-test utilities |

## Tools & plugins

| Entry | Description |
| --- | --- |
| `CoreScriptConverter2/` | CoreScript compile/conversion tool (not building) |
| `ScriptSigner/` | Script signing tool |
| `IncludeChecker/` | C# include-hygiene checker |
| `RobloxModelAnalyzer/` | Model loading/analysis host |
| `SettingsComparisonTool/` | Settings JSON reader/differ |
| `BuiltInPlugins/` | Plugins bundled with Studio (`.rbxmx`) |
| `StudioPlugins/` | Lua plugins (terrain, water, wiring, utilities) |
| `Installer/` | Bootstrappers for all artifacts |
| `PrepAllForUpload/`, `*.PrepForUpload/`, `RobloxStudio.PrepForUpload/`, `WindowsClient.PrepForUpload/` | Upload-packaging stubs |

## Content & assets

| Entry | Description |
| --- | --- |
| `content/` | Shared runtime content (fonts, music, particles, scripts, sky, sounds, textures) |
| `PlatformContent/` | Per-platform variants (`pc`, `android`, `ios`, `durango`) |
| `shaders/` | Shader sources |
| `fmod/` | FMOD audio SDK (headers + platform libs) |

## Third-party libraries

| Entry | Description |
| --- | --- |
| `Library/` | Boost, Qt 4.8.5 sources, SDL2, curl, zlib, VMProtect, cpp-netlib, Mesa, xulrunner, glsl-optimizer, hlsl2glslfork, cabsdk, SDK, w3c-libwww — see [Libraries](../modules/libraries.md) |
| `boostlibs/` | Solution projects for static Boost & Boost.Test |
| `QTitanRibbon/` | Qt ribbon UI library used by Studio |

## Build system & config

| Entry | Description |
| --- | --- |
| `Roblox.sln` | Master Visual Studio solution (~354 KB, hundreds of projects) |
| `CMakeLists.txt` | Root CMake build (Unix/Android) |
| `cmake/` | CMake helper modules |
| `CustomBuildRules.props/.rules/.targets/.xml` | MSBuild custom build rules |
| `PropertySheets/` | Shared MSBuild property sheets |
| `buildshaders.bat` / `buildshaders.sh` | Shader compilation scripts |
| `RobloxDebugVisualizers.txt` | Visual Studio debug visualizers for engine types |
| `RobloxPlayer-Info.plist` | Player bundle metadata (Mac) |
| `.github/` | Workflows (`msvc`, `semgrep`, `osv-scanner`, `scorecard`, `label`, `stale`, `sync`, `docs-deploy`), labeler config, resources |
| `website/` | This documentation site (Docusaurus) |
| `README.md`, `LICENSE` (Apache-2.0), `.gitattributes`, `.gitignore` | Repo metadata |

## Misc one-offs

| Entry | Description |
| --- | --- |
| `RefreshPolicies/` | Windows tool managing client cache/refresh policies |
| `RbxTestHooks/` | (listed above under Testing) |
| `RobloxHybrid/` | (listed above under Applications) |

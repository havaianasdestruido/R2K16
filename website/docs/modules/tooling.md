---
sidebar_position: 13
---

# Tooling — dev tools & plugins

Auxiliary programs that build, sign, analyze and extend — not part of the runtime engine.

## CoreScriptConverter2 — ❌ not building yet

**Path:** `CoreScriptConverter2/` · `cscmain.cpp`, `tool/`, `rsc.config.template`

Converts the engine's Lua **CoreScripts** (`content/scripts/`) into the compiled form the
runtime embeds. Historically part of the CoreScript build pipeline together with
`ScriptSigner`.

## ScriptSigner

**Path:** `ScriptSigner/` (own solution `ScriptSigner.sln`)

Signs scripts so the runtime can verify that engine-internal scripts (CoreScripts) were not
tampered with. See [Security](../development/security.md#script-signing).

## IncludeChecker

**Path:** `IncludeChecker/` — a **C#** program (`Program.cs`, `IncludeChecker.csproj`)

Repo hygiene tool: verifies include style/ordering conventions across the C++ sources (the
codebase is strict about its include blocks — see
[Conventions](../development/conventions.md#includes)).

## RobloxModelAnalyzer

**Path:** `RobloxModelAnalyzer/` — `main.cpp`, `RobloxPluginHost.cpp/.h`

A host application that loads serialized models (`.rbxmx`/`.rbxm`) and runs analysis over them
— essentially Studio's plugin host minus the editor; useful for batch model inspection.

## SettingsComparisonTool

**Path:** `SettingsComparisonTool/` — `GetClientSettings.bat`, `SettingsReader.exe`,
`diff.exe`, `readme.txt`

A batch utility that downloads/reads client settings (FastFlags/FastLog settings JSONs of the
era) and diffs them between builds/versions — handy when tracking settings drift.

## SimulationTestUtility

**Path:** `SimulationTestUtility/` — shared support code for the simulation test rigs (see
[Testing](./testing.md)).

## BuiltInPlugins

**Path:** `BuiltInPlugins/` — plugins that ship *inside* Studio's plugin manager:

- `PhysicsAnalyzer.rbxmx`
- `TerrainTools.rbxmx` (+ `terrain/` assets)
- `TransformDragger.rbxmx`

These are XML-serialized models (see [Serialization](../architecture/serialization.md)) with
embedded Lua — open them in a text editor to study both the format and 2016-era plugin APIs.

## StudioPlugins

**Path:** `StudioPlugins/` — Lua plugins installed into Studio's `Plugins` folder:
`terrain/`, `water/`, `wiring/`, `utilities/`.

## Installers & packaging

**Path:** `Installer/` — bootstrapper suite for every artifact:

| Folder | Packages |
| --- | --- |
| `Bootstrapper`, `BootstrapperClient(.PrepForUpload)` | Player client |
| `BootstrapperQTStudio(.PrepForUpload)`, `QTStudioBootstrapperTemp` | Studio |
| `BootstrapperRccService`, `RccServiceSetup` | RCCService |
| `BootstrapperMac` | Mac client |
| `RobloxExtensionApp`, `NPRobloxProxy.PrepForUpload` | Browser/launcher helpers |
| `PrepAllForUpload` | Orchestrates all of the above |

Related root-level packaging stubs: `PrepAllForUpload/`, `WindowsClient.PrepForUpload/`,
`RobloxStudio.PrepForUpload/`, `RCCService.PrepForUpload/`,
`RCCServiceArbiter.PrepForUpload/`, `RCCServiceArbiter.PrepForUpload/`.

## Build helper files (repo root)

| File | Role |
| --- | --- |
| `buildshaders.bat` / `buildshaders.sh` | Compile `shaders/` through the ShaderCompiler |
| `CustomBuildRules.props/.rules/.targets/.xml` | MSBuild custom build rules |
| `PropertySheets/` | Shared MSBuild property sheets |
| `RobloxDebugVisualizers.txt` | Visual Studio debug visualizers for engine types |
| `cmake/` | CMake helper modules (`ListFilter`, `IncludeProjectFiles`, `Boost`, `FMOD`, `SSL`, `SDL2`) |

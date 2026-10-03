---
sidebar_position: 1
# Serve the introduction at the docs root (/R2K16/docs/) — docs-only mode
# has no landing page, so this doc claims the '/' route of the docs app.
slug: /
---

# Introduction

**R2K16** is a modded fork of the **2016 Roblox engine source code**. The goal of the project is
to adjust, adapt and polish the engine so it can stand comparison with the modern Roblox Studio
engine, while staying true to the 2016-era architecture.

This site is the **full codebase documentation** for the repository: what every top-level project
is, how the engine fits together, how to build it, and how to work on it.

:::info Where does the source come from?

The base of this fork is the public re-upload of Roblox's source that circulated on
`git.rip` (`exconfidential/roblox`). It is **not** an official Roblox release. Treat the code,
assets and any binaries you build as educational/archival material, and review the repository
`LICENSE` and your local legislation before redistributing anything.

:::

## What's in the repository?

The tree is a snapshot of the entire 2016 Roblox client/server/studio technology stack:

| Area | Examples |
| --- | --- |
| Engine core | `App/` (Instance tree, DataModel, Lua, physics world, terrain, tools) |
| Foundations | `Base/` (TaskScheduler, platform utilities, asserts) |
| Networking | `Network/` (RakNet-based replication, physics sync, chat filtering) |
| Rendering | `Rendering/` (GfxCore device layer, GfxRender, RbxG3D, VR SDKs) |
| Physics | `App/v8world`, `App/v8kernel`, `App/solver`, `App.BulletPhysics/` |
| Editors | `RobloxStudio/` (Qt 4.8 based Studio IDE) |
| Servers | `RCCService/` (Roblox Cloud Compute game host) + C# arbiter |
| Clients | `WindowsClient/`, `XboxClient/`, `iOS/`, `Android/`, `Mac/`, `RobloxHybrid/` |
| Third-party | `Library/` (Boost, Qt, SDL, curl, zlib, VMProtect, cpp-netlib, …), `fmod/`, `boostlibs/` |
| Content | `content/`, `PlatformContent/`, `shaders/`, `BuiltInPlugins/` |
| Testing | `App.UnitTest*`, `Base.UnitTest*`, `RobloxTest/`, `RCCService.Test/` |
| Tooling | `CoreScriptConverter2/`, `ScriptSigner/`, `IncludeChecker/`, CI workflows in `.github/` |

## How to read this documentation

- **New to the repo?** Start with [Getting Started](./getting-started/index.md), then read the
  [Architecture overview](./architecture/index.md) top to bottom.
- **Looking for one specific folder?** Jump to the
  [Module Reference](./modules/index.md) or the [Repository Map](./reference/repo-map.md).
- **Trying to build?** See [Building on Windows](./getting-started/building-windows.md) and
  [Building with CMake](./getting-started/building-cmake.md).
- **Just want the vocabulary?** The [Glossary](./reference/glossary.md) explains *DataModel*,
  *RCC*, *PGS*, *FastFlags*, *rbxmx* and friends.

## Project status at a glance

The fork is a work in progress: most core projects compile (App, Base, Network, Rendering, CSG,
RobloxStudio, WindowsClient, RCCService…), while some peripheral projects (unit tests, Xbox
client, a few converters) still fail to build. The full matrix lives in
[Project Status](./getting-started/project-status.md) and the feature plans in the
[Roadmap](./reference/roadmap.md).

## Credits

R2K16 is maintained by **@havaianasdestruido** (also known as PatoFlamejanteTV / UltimateQuack).
The original engine code is © 2003–2016 Roblox Corporation.

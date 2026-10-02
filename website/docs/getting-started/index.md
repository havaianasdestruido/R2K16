---
sidebar_position: 1
---

# Overview

This section gets you from a fresh clone to a compiling tree.

## The 30-second version

R2K16 is a classic mid-2010s C++ codebase:

- **Language:** C++ (MSVC `v140_xp`-era, with `#ifdef`-based platform layers)
- **Primary build:** Visual Studio solution — `Roblox.sln` on Windows
- **Alternative build:** CMake for Unix/Android (`CMakeLists.txt` at the repo root)
- **Key bundled dependencies:** Boost (see [Libraries](../modules/libraries.md)), Qt 4.8.5
  (Studio UI), SDL2, libcurl, zlib, FMOD (audio), RakNet (networking, vendored in `Network/`)
- **Scripting:** Lua 5.1.4, sources vendored in `App/Lua-5.1.4/`

## Section contents

1. [**Prerequisites**](./prerequisites.md) — the exact toolchain you need installed.
2. [**Building on Windows**](./building-windows.md) — Boost, Qt, then `Roblox.sln`.
3. [**Building with CMake**](./building-cmake.md) — the Unix/Android route.
4. [**Project Status**](./project-status.md) — what compiles, what doesn't (yet).

## Repository tour

The five directories you'll spend most time in:

```
R2K16/
├── App/                 # The engine: Instance tree, DataModel, Lua, physics, terrain, tools
├── Base/                # TaskScheduler, platform abstraction, core utilities
├── Network/             # RakNet-based client/server replication stack
├── Rendering/           # Graphics: GfxCore (device), GfxRender, RbxG3D, VR
└── RobloxStudio/        # The Qt-based Studio editor application
```

Every other folder is either a client (`WindowsClient/`, `XboxClient/`, `iOS/`, `Android/`),
a service (`RCCService/`), a tool (`ScriptSigner/`, `CoreScriptConverter2/`, …), bundled
third-party code (`Library/`, `fmod/`) or content (`content/`, `PlatformContent/`, `shaders/`).

See the [Repository Map](../reference/repo-map.md) for a complete, annotated listing.

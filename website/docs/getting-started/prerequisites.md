---
sidebar_position: 2
---

# Prerequisites

## Windows (recommended path)

Building on Windows requires **both** of these Visual Studio generations:

| Requirement | Why |
| --- | --- |
| **Visual Studio 2019** | Host IDE used to open `Roblox.sln` |
| **Visual Studio 2015 build tools (`v140_xp`)** | The engine projects target the VS2015 toolset with the XP-compatible runtime; this is *mandatory* for building Qt 4.8.5 and the engine itself |

Also make sure the **Windows SDK** is installed and its tools (`rc.exe`, etc.) are reachable from
your `PATH` — the Qt build step in particular will fail with *"`rc` not recognized"* if they are
not (see [Troubleshooting](../reference/troubleshooting.md)).

### Disk and time expectations

The repository vendors most of its dependencies (`Library/` alone contains Boost, Qt, curl, SDL2,
Mesa, xulrunner, …), so a clone is multi-gigabyte. Building Qt and Boost takes a while; the
engine solution itself is large (hundreds of projects) — expect the first full build to run for
tens of minutes even on a fast machine.

## What is already bundled (no download needed)

Everything below ships inside the repository — you do **not** need to fetch them yourself:

- Boost — `Library/boost/` (see the note in [Libraries](../modules/libraries.md) about the
  historical 1.56.0 vs 1.74.0 confusion)
- Qt 4.8.5 sources — `Library/Qt/`
- SDL2, libcurl, zlib, cpp-netlib, VMProtect SDK, Mesa, glsl-optimizer, hlsl2glsl, w3c-libwww,
  cabsdk, the DirectX SDK pieces — all under `Library/`
- FMOD audio SDK — `fmod/`
- RakNet — `Network/raknet/`
- Lua 5.1.4 — `App/Lua-5.1.4/`
- Bullet Physics — `App.BulletPhysics/`

:::tip Library README caveat

`Library/README.md` (inherited from the original tree) suggests replacing the bundled Boost and
Qt archives with fresh downloads from SourceForge / Qt archives *because the copies in the
original upload were broken*. If your build fails deep inside Boost or Qt, re-fetching those two
libraries is the first thing to try.

:::

## CMake builds (Linux / Android)

For the Unix route you need:

- A recent **CMake** (the root `CMakeLists.txt` dates from the CMake 2.8 era; the CI workflow
  passes `-DCMAKE_POLICY_VERSION_MINIMUM=3.5` to build with modern CMake)
- The **Android NDK** if you are targeting Android (see
  [Building with CMake](./building-cmake.md))
- A prebuilt `CONTRIB_PATH` directory with the third-party dependencies compiled for your
  platform — the CMake scripts expect this to exist and will hard-fail without it

## Documentation site (this website)

Only needed if you want to hack on these docs:

- **Node.js ≥ 18** (Node 20/22 recommended)
- npm (bundled with Node)

```bash
cd website
npm install
npm start        # dev server with hot reload
```

See [Maintaining the docs site](../development/docs-site.md) for details.

---
sidebar_position: 11
---

# Libraries — bundled dependencies

**Paths:** `Library/`, `boostlibs/`, `fmod/`

The repository vendors its entire dependency set, so a checkout is self-contained. Versions
below are from the repository README; entries marked \* are known to be out of date.

| Library | Version | Path | Used for |
| --- | --- | --- | --- |
| Boost | v1.74.0 | `Library/boost/` | Threads, smart pointers, function objects — the engine is Boost-heavy (`rbx/boost.hpp` adapts it) |
| libcurl | v7.71.0 | `Library/curl/` | HTTP(S) client for assets/API (`App/util/HttpAsync`) |
| zlib | v1.2.x | `Library/zlib/` | Compression (README lists "v1.12.11") |
| SDL | v2.0.12 | `Library/SDL2/` | Windowing/input abstraction (mobile & desktop) |
| VMProtect | v2.1.3 \* | `Library/VMProtect/` | Code-protection SDK (`VMProtectSDK.h` used by `Instance.cpp` and friends) |
| cpp-netlib | v0.13.0-final | `Library/cpp-netlib/` | Networking atop Boost.Asio (`Network/BoostAppend.*`) |
| Mesa | v7.8.1 \* | `Library/Mesa/` | Software OpenGL for fallback rendering |
| xulrunner-sdk | v1.9.0.11 \* | `Library/xulrunner/` | Embedded Gecko web view (`WindowsClient/RbxWebView`) |
| glsl-optimizer | — \* | `Library/glsl-optimizer/` | Shader optimization (GL path) |
| hlsl2glsl | — \* | `Library/hlsl2glslfork/` | HLSL→GLSL translation |
| cabsdk | — \* | `Library/cabsdk/` | Windows cabinet archives (installer/patching) |
| DirectX SDK | (legacy) | `Library/SDK/` (+ system) | D3D9/D3D11 backends (`Bin/Include/Lib` layout) |
| w3c-libwww | v5.4.2 | `Library/w3c-libwww/` | Legacy web stack (`HTW3C.h` glue in `App/util`) |
| Qt | 4.8.5 \* | `Library/Qt/` | Studio's UI framework — **you must build it first** |
| FMOD | (era build) | `fmod/` (`include/`, `Android/`, `xbox/`) | Audio engine |
| — | — | `boostlibs/` | Solution projects building the **static** Boost libs and Boost.Test the engine links |

Additional vendored components elsewhere in the tree: **RakNet** (`Network/raknet/`),
**Lua 5.1.4** (`App/Lua-5.1.4/`), **lz4** (`App/lz4/`), **Bullet Physics**
(`App.BulletPhysics/`), **sgCore** (`CSG/sgCore/`), **G3D** (`Rendering/g3d/`),
**QTitanRibbon** (`QTitanRibbon/`), **Closure compiler** (`RobloxHybrid/closure-compiler/`).

:::warning The Boost/Qt archive caveat

`Library/README.md` (inherited with the original tree) notes the bundled Boost and Qt sources
were broken in the original upload and recommends replacing them with the Boost **1.56.0**
and Qt **4.8.5** archives from SourceForge/Qt. If builds fail deep inside Boost or Qt, that's
the first thing to retry — see [Troubleshooting](../reference/troubleshooting.md).

:::

## `Library/README.txt` files

Several subfolders ship READMEs from upstream (SDL2, curl, …). They describe the original
library builds, not the engine's use of them.

## Boost usage notes

The engine compiles the Boost pieces it needs via `boostlibs/boost.static.vcxproj` (both
projects are on the ✅ builds list) and pins compatibility through `Base/include/rbx/boost.hpp`
+ `Base/rbx/boost.cpp`. The root CMake's `cmake/Modules/Boost.cmake` resolves Boost for
CMake builds.

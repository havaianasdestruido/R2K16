---
sidebar_position: 4
---

# Building with CMake

Beside the Windows solution, the repository carries a root `CMakeLists.txt` used for the
Unix (and Android) flavors of the engine. It is the same build system the CI code-analysis
workflow exercises.

## What the root CMakeLists expects

The root script is old-school (it declares `cmake_minimum_required(VERSION 2.8)`) and has hard
requirements it will fail on if unmet:

| Variable | Meaning |
| --- | --- |
| `CONTRIB_PATH` | Directory containing **prebuilt third-party libraries** for your platform. Can be set as a CMake variable or an environment variable. The build fails immediately if it is missing. |
| `RBX_STL_INCLUDE_DIRS` | Directories of the C++ standard library to use (needed for the Android NDK toolchains in particular). |
| `CMAKE_BUILD_TYPE` | Lower-cased internally into `RBX_BUILD_TYPE` — configure with `Release` or `Debug`. |
| `RBX_SETTINGS_INITIALIZED` | Escape hatch for toolchain files to pre-seed settings. |

It also loads helper modules from `cmake/Modules/` — `ListFilter`, `IncludeProjectFiles`,
`Boost`, `FMOD`, `SSL`, `SDL2` — which resolve the bundled libraries for your platform.

:::tip Modern CMake compatibility

The CI workflow configures the tree with:

```bash
# Partial Unix configure example — combine with the full configure from the
# table above: -DCONTRIB_PATH=... -DRBX_STL_INCLUDE_DIRS=... -DCMAKE_BUILD_TYPE=Release
cmake -B build -DCMAKE_POLICY_VERSION_MINIMUM=3.5
```

`-DCMAKE_POLICY_VERSION_MINIMUM=3.5` is a workaround that lets a modern CMake accept the
ancient `cmake_minimum_required(2.8)` declaration. Use it locally too.

:::

## Android

The Android build is driven from the `Android/` Gradle project, which invokes the root
`CMakeLists.txt` with the NDK toolchain file. When `ANDROID` is set, the root script prints and
consumes the usual NDK variables:

- `ANDROID_TOOLCHAIN_NAME`, `ANDROID_STL`, `ANDROID_ABI`
- `ANDROID_NATIVE_API_LEVEL`, `ANDROID_SYSROOT`
- `ANDROID_EXCEPTIONS`, `ANDROID_RTTI`, `ANDROID_NDK_HOST_X64`

The native engine code lands in `Android/libroblox/`; the Java/Kotlin shell and tests live in
`Android/NativeShell` and `Android/RobloxAndroidTests` (see
[Clients: Android](../modules/clients.md#android)).

## Unix notes

- The root script hard-fails with *"Unsupported platform."* unless `UNIX` is set by the
  generator — this path targets Linux/Android/macOS toolchains, not MSVC.
- Platform-specific sources are selected through the usual directories (`Base/rbx/Unix`,
  `Base/rbx/Darwin`, `App/util/Android`, etc.).
- Shaders can be built with `buildshaders.sh`.

## Related project files

Many engine subprojects carry their own `CMakeLists.txt` next to their `.vcxproj` files —
`App/`, `Base/`, `Network/`, `Rendering/*`, `App.BulletPhysics/`, `ClientShared/` — so the
CMake build assembles the same module set as the Visual Studio solution.

For what actually compiles today, see [Project Status](./project-status.md).

---
sidebar_position: 3
---

# Building on Windows

The Windows build has three stages: **Boost**, then **Qt**, then the main solution. Boost and Qt
must be built once; afterwards day-to-day work only involves `Roblox.sln`.

:::info Heads-up

This guide follows the instructions in the repository `README.md`. If anything here disagrees
with the README, the README wins — and please open an issue so the docs can be fixed.

:::

## 1. Build Boost

1. Open a command prompt and `cd` into `Library/boost/`.
2. Run `bootstrap.bat` to generate the Boost build scripts.
3. **Edit `build_boost.bat`** so its paths point at wherever you keep this repository.
4. Run `build_boost.bat`.

When it finishes you have the Boost binaries the engine links against (the
`boostlibs/` solution projects build the static/test flavors the engine uses).

## 2. Build Qt 4.8.5

This is where the **VS2015 build tools (`v140_xp`)** are required.

1. Open the **VS2015 x86 Native Tools Command Prompt** (search "VS2015" in the Start Menu).
2. `cd` to the repository's `Library/Qt` folder.
3. Configure Qt, substituting `${path}` with the absolute path of your repository clone:

   ```bat
   .\configure -make nmake -platform win32-msvc2015 -prefix ${path}\Library\Qt ^
     -opensource -confirm-license -opengl desktop -nomake examples -nomake tests ^
     -webkit -xmlpatterns
   ```

   Example, if the repository lives in `D:\Roblox\Source`:

   ```bat
   .\configure -make nmake -platform win32-msvc2015 -prefix D:\Roblox\Source\Library\Qt ^
     -opensource -confirm-license -opengl desktop -nomake examples -nomake tests ^
     -webkit -xmlpatterns
   ```

4. Run `nmake`.

:::warning It *will* break — that's expected

The Qt build stops with an error partway through. By that point all the libraries the engine
needs have already been produced. This is a **partial** Qt build by design (see the README:
*"Congratulations! You partially compiled Qt."*). If `nmake` complains that `rc` is not
recognized, add the Windows SDK binaries to your `PATH`.

:::

## 3. Build the engine

Open **`Roblox.sln`** in Visual Studio 2019 and build.

> "Everything listed as able to compile will compile, unless you're doing something wrong."
> — the README's promise.

Which configurations exist, and which projects build in each, is tracked in
[Project Status](./project-status.md). The core set (`App`, `Base`, `Network`, `Rendering`,
`CSG`, `App.BulletPhysics`, `RobloxStudio`, `WindowsClient`, `RCCService`, …) builds.

### Shaders

Shaders are compiled separately with the helper scripts at the repo root:

```bat
buildshaders.bat     :: Windows
```

See [Shaders & content](../modules/content.md#shaders) for what this produces.

## What to run after building

| Binary | What it is |
| --- | --- |
| `RobloxStudio.exe` (from `RobloxStudio/`) | The Studio editor — main.cpp is the entry point |
| Player client (from `WindowsClient/`) | The standalone Roblox player |
| `RCCService` (from `RCCService/`) | Headless game-hosting service |

Legacy online services (authentication, game join) point at 2016-era Roblox infrastructure and
will not work against today's servers — expect a local/localhost experience unless you bring
your own backend.

## Common problems

- `rc` not recognized → add the Windows SDK to `PATH`.
- Errors inside Boost/Qt sources → see the [Library README caveat](../modules/libraries.md).
- Broken images in the README (an `[ImgBot] Optimize images` commit) → open an issue; the
  maintainer will revert the optimization commit.

More in [Troubleshooting](../reference/troubleshooting.md).

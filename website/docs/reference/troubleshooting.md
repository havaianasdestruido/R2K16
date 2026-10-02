---
sidebar_position: 4
---

# Troubleshooting

Common failure modes, collected from the README and the build system.

## Windows build

### `rc` is not recognized during the Qt `nmake`

The VS2015 command prompt doesn't include the Windows SDK tools. Add the SDK's `bin` folder
(containing `rc.exe`) to `PATH` for that session and re-run `nmake`.

### The Qt build stops with an error partway through

**Expected.** The bundled Qt 4.8.5 doesn't build to completion; by the time it breaks, the
libraries the engine needs exist. Continue to `Roblox.sln`.

### Errors inside Boost / Qt sources themselves

The original upload's bundled Boost and Qt archives were broken; `Library/README.md` recommends
replacing them with the Boost 1.56.0 and Qt 4.8.5 archives from upstream. See
[Libraries](../modules/libraries.md).

### A project fails with toolset errors (`v140_xp`)

Install the **Visual Studio 2015 build tools** with the `v140_xp` toolset — VS2019 alone is not
enough (see [Prerequisites](../getting-started/prerequisites.md)).

### `Roblox.sln` project won't load / build

Check [Project Status](../getting-started/project-status.md) — several projects are known-broken
(unit tests, RobloxTest, XboxClient, GameChat, NetworkMesh, CoreScriptConverter2). Unload them
and build the rest.

## CMake build

### `CONTRIB_PATH is not set`

The root `CMakeLists.txt` requires a directory of prebuilt third-party libraries. Provide it
via `-DCONTRIB_PATH=...` or the environment variable. See
[Building with CMake](../getting-started/building-cmake.md).

### `RBX_STL_INCLUDE_DIRS must be set to stdlib directories`

Pass the standard-library include dirs (mainly relevant for Android NDK builds).

### CMake refuses the project (minimum version)

Modern CMake rejects the ancient `cmake_minimum_required(2.8)`. Configure with
`-DCMAKE_POLICY_VERSION_MINIMUM=3.5` — the same workaround CI uses.

### `Unsupported platform.`

The root CMake build only proceeds when the generator reports `UNIX` (Linux/Android/macOS).
On Windows, use `Roblox.sln` instead.

## Repository & docs

### Broken images in the README

An `[ImgBot] Optimize images` commit corrupted some images. Open an issue and the maintainer
will revert the optimization — per the README's warning section.

### The docs site shows 404 at `/` in a sandbox

The site's default base URL is `/R2K16/` (for GitHub Pages). Serve it with
`DOCUSAURUS_BASE_URL=/ npm run build && DOCUSAURUS_BASE_URL=/ npm run serve`, or use
`npm start` (dev server), which doesn't care. See
[the docs-site guide](../development/docs-site.md#the-base-url-gotcha).

### Docs build fails on a link

`onBrokenLinks: 'throw'` — a moved/deleted doc broke a link governed by that option
(doc-to-doc and anchor links). Fix the link; the error message names the file and target.
Broken **Markdown** links, by contrast, only log a warning — this site sets
`markdown.hooks.onBrokenMarkdownLinks: 'warn'` — so scan the build log for them.

## Runtime

### Client can't authenticate / join games

Expected: the 2016 backend is gone. Run local servers (Studio *Start Server*, or `RCCService`)
and point clients at them.

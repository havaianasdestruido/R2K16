---
sidebar_position: 14
---

# Content — assets & shaders

**Paths:** `content/`, `PlatformContent/`, `shaders/`, `BuiltInPlugins/`

Everything the engine loads at runtime that is *data* rather than code.


## FAQ

### What is the difference between shared and platform content?

Shared assets live under content, while PlatformContent contains platform-specific material. Check how the target packages and resolves an asset before changing its location.

### How can I investigate this in the repository?

From the repository root, search the relevant tracked files for a starting point (results are leads, not proof of behavior):

```bash
git grep -n -i -F -- 'rbxasset' -- PlatformContent
```

Read the surrounding implementation and callers, and check relevant tests before making changes. A search may return no matches when terminology or tracked files change.

## `content/` — shared content

```
content/
├── fonts/      # Font files (the era's legacy fonts)
├── music/      # Ambient/menu music
├── particles/  # Particle textures & configs
├── scripts/    # CoreScripts, ServerCoreScripts, Modules,
│               # StarterScript.lua, ServerStarterScript.lua, LoadingScript.lua
├── sky/        # Skybox textures
├── sounds/     # Sound effects
└── textures/   # Engine textures (decals, UI, cursors…)
```

The `scripts/` subfolder is the engine's own Lua layer — see
[Scripting](../architecture/scripting.md#corescripts-and-signing).

## `PlatformContent/` — per-platform content

Variants of assets that differ by platform:

- `pc/` — desktop
- `android/` — Android
- `ios/` — iOS
- `durango/` — Xbox One (its codename)

## `shaders/` — shader sources {#shaders}

HLSL/GLSL shader sources consumed by `Rendering/ShaderCompiler/`; compiled by:

```bat
buildshaders.bat     :: Windows
```

```bash
./buildshaders.sh    # Unix
```

The GL pipeline runs them through glsl-optimizer / hlsl2glsl
(see [Rendering](../architecture/rendering.md#shaders)).

## `BuiltInPlugins/` & `StudioPlugins/`

Studio plugins shipped with the product vs. installed into the user's Plugins folder —
detailed under [Tooling](./tooling.md#builtinplugins).

## `RobloxStudio/` content bits

`RobloxStudio.qrc` (Qt resource bundle), `RobloxStudio.css` (styling), `AppSettings.xml`
(defaults) and the Studio icons ship inside the Studio project itself.

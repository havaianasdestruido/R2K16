---
sidebar_position: 14
---

# Content — assets & shaders

**Paths:** `content/`, `PlatformContent/`, `shaders/`, `BuiltInPlugins/`

Everything the engine loads at runtime that is *data* rather than code.

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

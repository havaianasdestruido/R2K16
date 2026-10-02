---
sidebar_position: 5
---

# Rendering — graphics stack

**Path:** `Rendering/` · **Status:** GfxBase ✅, GfxCore ✅, GfxRender ✅, RbxG3D ✅,
graphics3D ✅, AppDraw ✅

A directory of related graphics projects rather than one library. Full architecture discussion
in [Rendering](../architecture/rendering.md).

| Subproject | What it is |
| --- | --- |
| `GfxBase/` | Engine-side rendering foundations: `ViewBase`, the **adornment** system, `GfxPart`, `RenderCaps`, `RenderSettings`, `FrameRateManager` |
| `GfxCore/` | Device abstraction with `D3D9/`, `D3D11/`, `GL/` backends (+ `nglew`), `Device`, `Texture`, `Shader`, `Geometry`, `Framebuffer`, `States`, PIX hooks |
| `GfxRender/` | Scene renderer: `CullableSceneNode`, `FastCluster`, `GeometryGenerator`, emitters, `EnvMap`, `AdornRender` |
| `RbxG3D/` | Roblox's integration layer over G3D |
| `g3d/` | Vendored **G3D** graphics library (math & scene utilities) |
| `AppDraw/` | Engine→renderer glue: `Draw`, `DrawAdorn`, `HitTest` |
| `ShaderCompiler/` | Shader build tooling (uses `Library/glsl-optimizer`, `Library/hlsl2glslfork`) |
| `LibOVR/`, `OpenVR/`, `VrApi/` | VR SDKs: Oculus PC, Valve OpenVR, GearVR/mobile |

## Backend status in this fork

- **D3D9** — works (the README's suspected text-render bug "never existed in the first place")
- **D3D11** — present but **does not initialize** yet
- **OpenGL** — the Unix/mobile path (GL backend + `glew`)
- D3D12/Vulkan and a modern pipeline are roadmap items — see
  [Roadmap](../reference/roadmap.md#graphics--rendering)

## Build notes

Each subproject has its own `.vcxproj` (+ Xcode project where relevant); the root
`Rendering/CMakeLists.txt` assembles them for CMake builds. Shader assets are built with
`buildshaders.bat` / `buildshaders.sh` (see [Content](./content.md#shaders)).

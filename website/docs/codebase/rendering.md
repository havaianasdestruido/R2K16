---
sidebar_position: 16
title: Rendering Pipeline
description: GfxBase, GfxCore, D3D/OpenGL backends, GfxRender scene graph, and shaders.
---

# Rendering Pipeline

GfxBase, GfxCore, D3D/OpenGL backends, GfxRender scene graph, and shaders.

## Subsystem Metrics

- **Total Documented Functions:** `6265`
- **Functions Exercised in Tests:** `441`
- **Platform-Divergent Implementations:** `185`
- **Component Source Files:** `442`

## Source Files

<details>
<summary>View all 442 source files in this subsystem</summary>

| Source File | Path |
| :--- | :--- |
| `Draw.cpp` | `Rendering/AppDraw/Draw.cpp` |
| `DrawAdorn.cpp` | `Rendering/AppDraw/DrawAdorn.cpp` |
| `HitTest.cpp` | `Rendering/AppDraw/HitTest.cpp` |
| `Draw.h` | `Rendering/AppDraw/include/appdraw/Draw.h` |
| `DrawAdorn.h` | `Rendering/AppDraw/include/appdraw/DrawAdorn.h` |
| `Adorn.cpp` | `Rendering/GfxBase/Adorn.cpp` |
| `AdornBillboarder.cpp` | `Rendering/GfxBase/AdornBillboarder.cpp` |
| `AdornBillboarder2D.cpp` | `Rendering/GfxBase/AdornBillboarder2D.cpp` |
| `AdornSurface.cpp` | `Rendering/GfxBase/AdornSurface.cpp` |
| `FileMeshData.cpp` | `Rendering/GfxBase/FileMeshData.cpp` |
| `FrameRateManager.cpp` | `Rendering/GfxBase/FrameRateManager.cpp` |
| `GfxPart.cpp` | `Rendering/GfxBase/GfxPart.cpp` |
| `IAdornableCollector.cpp` | `Rendering/GfxBase/IAdornableCollector.cpp` |
| `PartIdentifier.cpp` | `Rendering/GfxBase/PartIdentifier.cpp` |
| `RenderSettings.cpp` | `Rendering/GfxBase/RenderSettings.cpp` |
| `ViewBase.cpp` | `Rendering/GfxBase/ViewBase.cpp` |
| `ViewportBillboarder.cpp` | `Rendering/GfxBase/ViewportBillboarder.cpp` |
| `Adorn.h` | `Rendering/GfxBase/include/GfxBase/Adorn.h` |
| `AdornBillboarder.h` | `Rendering/GfxBase/include/GfxBase/AdornBillboarder.h` |
| `AdornBillboarder2D.h` | `Rendering/GfxBase/include/GfxBase/AdornBillboarder2D.h` |
| `AdornSurface.h` | `Rendering/GfxBase/include/GfxBase/AdornSurface.h` |
| `AsyncResult.h` | `Rendering/GfxBase/include/GfxBase/AsyncResult.h` |
| `FrameRateManager.h` | `Rendering/GfxBase/include/GfxBase/FrameRateManager.h` |
| `GfxPart.h` | `Rendering/GfxBase/include/GfxBase/GfxPart.h` |
| `IAdornable.h` | `Rendering/GfxBase/include/GfxBase/IAdornable.h` |
| `IAdornableCollector.h` | `Rendering/GfxBase/include/GfxBase/IAdornableCollector.h` |
| `Image.h` | `Rendering/GfxBase/include/GfxBase/Image.h` |
| `RenderCaps.h` | `Rendering/GfxBase/include/GfxBase/RenderCaps.h` |
| `RenderSettings.h` | `Rendering/GfxBase/include/GfxBase/RenderSettings.h` |
| `TextureProxyBase.h` | `Rendering/GfxBase/include/GfxBase/TextureProxyBase.h` |
| `Typesetter.h` | `Rendering/GfxBase/include/GfxBase/Typesetter.h` |
| `ViewBase.h` | `Rendering/GfxBase/include/GfxBase/ViewBase.h` |
| `ViewportBillboarder.h` | `Rendering/GfxBase/include/GfxBase/ViewportBillboarder.h` |
| `DeviceContextD3D11.cpp` | `Rendering/GfxCore/D3D11/DeviceContextD3D11.cpp` |
| `DeviceD3D11.cpp` | `Rendering/GfxCore/D3D11/DeviceD3D11.cpp` |
| `DeviceD3D11.h` | `Rendering/GfxCore/D3D11/DeviceD3D11.h` |
| `DeviceD3D11Durango.cpp` | `Rendering/GfxCore/D3D11/DeviceD3D11Durango.cpp` |
| `DeviceD3D11Win32.cpp` | `Rendering/GfxCore/D3D11/DeviceD3D11Win32.cpp` |
| `FramebufferD3D11.cpp` | `Rendering/GfxCore/D3D11/FramebufferD3D11.cpp` |
| `FramebufferD3D11.h` | `Rendering/GfxCore/D3D11/FramebufferD3D11.h` |
| `GeometryD3D11.cpp` | `Rendering/GfxCore/D3D11/GeometryD3D11.cpp` |
| `GeometryD3D11.h` | `Rendering/GfxCore/D3D11/GeometryD3D11.h` |
| `OculusVRD3D11.cpp` | `Rendering/GfxCore/D3D11/OculusVRD3D11.cpp` |
| `OpenVRD3D11.cpp` | `Rendering/GfxCore/D3D11/OpenVRD3D11.cpp` |
| `ShaderD3D11.cpp` | `Rendering/GfxCore/D3D11/ShaderD3D11.cpp` |
| `ShaderD3D11.h` | `Rendering/GfxCore/D3D11/ShaderD3D11.h` |
| `TextureD3D11.cpp` | `Rendering/GfxCore/D3D11/TextureD3D11.cpp` |
| `TextureD3D11.h` | `Rendering/GfxCore/D3D11/TextureD3D11.h` |
| `DeviceContextD3D9.cpp` | `Rendering/GfxCore/D3D9/DeviceContextD3D9.cpp` |
| `DeviceD3D9.cpp` | `Rendering/GfxCore/D3D9/DeviceD3D9.cpp` |
| `DeviceD3D9.h` | `Rendering/GfxCore/D3D9/DeviceD3D9.h` |
| `FramebufferD3D9.cpp` | `Rendering/GfxCore/D3D9/FramebufferD3D9.cpp` |
| `FramebufferD3D9.h` | `Rendering/GfxCore/D3D9/FramebufferD3D9.h` |
| `GeometryD3D9.cpp` | `Rendering/GfxCore/D3D9/GeometryD3D9.cpp` |
| `GeometryD3D9.h` | `Rendering/GfxCore/D3D9/GeometryD3D9.h` |
| `ShaderD3D9.cpp` | `Rendering/GfxCore/D3D9/ShaderD3D9.cpp` |
| `ShaderD3D9.h` | `Rendering/GfxCore/D3D9/ShaderD3D9.h` |
| `TextureD3D9.cpp` | `Rendering/GfxCore/D3D9/TextureD3D9.cpp` |
| `TextureD3D9.h` | `Rendering/GfxCore/D3D9/TextureD3D9.h` |
| `Device.cpp` | `Rendering/GfxCore/Device.cpp` |
| `DeviceCreate.cpp` | `Rendering/GfxCore/DeviceCreate.cpp` |
| `CardboardVRGL.cpp` | `Rendering/GfxCore/GL/CardboardVRGL.cpp` |
| `ContextGL.h` | `Rendering/GfxCore/GL/ContextGL.h` |
| `ContextGLAndroid.cpp` | `Rendering/GfxCore/GL/ContextGLAndroid.cpp` |
| `ContextGLMac.mm` | `Rendering/GfxCore/GL/ContextGLMac.mm` |
| `ContextGLWin32.cpp` | `Rendering/GfxCore/GL/ContextGLWin32.cpp` |
| `ContextGLiOS.mm` | `Rendering/GfxCore/GL/ContextGLiOS.mm` |
| `DeviceContextGL.cpp` | `Rendering/GfxCore/GL/DeviceContextGL.cpp` |
| `DeviceGL.cpp` | `Rendering/GfxCore/GL/DeviceGL.cpp` |
| `DeviceGL.h` | `Rendering/GfxCore/GL/DeviceGL.h` |
| `FramebufferGL.cpp` | `Rendering/GfxCore/GL/FramebufferGL.cpp` |
| `FramebufferGL.h` | `Rendering/GfxCore/GL/FramebufferGL.h` |
| `GearVRGL.cpp` | `Rendering/GfxCore/GL/GearVRGL.cpp` |
| `GeometryGL.cpp` | `Rendering/GfxCore/GL/GeometryGL.cpp` |
| `GeometryGL.h` | `Rendering/GfxCore/GL/GeometryGL.h` |
| `ShaderGL.cpp` | `Rendering/GfxCore/GL/ShaderGL.cpp` |
| `ShaderGL.h` | `Rendering/GfxCore/GL/ShaderGL.h` |
| `TextureGL.cpp` | `Rendering/GfxCore/GL/TextureGL.cpp` |
| `TextureGL.h` | `Rendering/GfxCore/GL/TextureGL.h` |
| `Geometry.cpp` | `Rendering/GfxCore/Geometry.cpp` |
| `Resource.cpp` | `Rendering/GfxCore/Resource.cpp` |
| `Shader.cpp` | `Rendering/GfxCore/Shader.cpp` |
| `Texture.cpp` | `Rendering/GfxCore/Texture.cpp` |
| `glew.c` | `Rendering/GfxCore/glew/glew.c` |
| `glew.cpp` | `Rendering/GfxCore/glew/glew.cpp` |
| `Device.h` | `Rendering/GfxCore/include/GfxCore/Device.h` |
| `Framebuffer.h` | `Rendering/GfxCore/include/GfxCore/Framebuffer.h` |
| `Geometry.h` | `Rendering/GfxCore/include/GfxCore/Geometry.h` |
| `Resource.h` | `Rendering/GfxCore/include/GfxCore/Resource.h` |
| `States.h` | `Rendering/GfxCore/include/GfxCore/States.h` |
| `Texture.h` | `Rendering/GfxCore/include/GfxCore/Texture.h` |
| `pix.cpp` | `Rendering/GfxCore/pix.cpp` |
| `AdornRender.cpp` | `Rendering/GfxRender/AdornRender.cpp` |
| `CullableSceneNode.cpp` | `Rendering/GfxRender/CullableSceneNode.cpp` |
| `CullableSceneNode.h` | `Rendering/GfxRender/CullableSceneNode.h` |
| `CustomEmitter.cpp` | `Rendering/GfxRender/CustomEmitter.cpp` |
| `Emitter.cpp` | `Rendering/GfxRender/Emitter.cpp` |
| `Emitter.h` | `Rendering/GfxRender/Emitter.h` |
| `EnvMap.cpp` | `Rendering/GfxRender/EnvMap.cpp` |
| `EnvMap.h` | `Rendering/GfxRender/EnvMap.h` |
| `ExplosionEmitter.cpp` | `Rendering/GfxRender/ExplosionEmitter.cpp` |
| `FastCluster.cpp` | `Rendering/GfxRender/FastCluster.cpp` |
| `FastCluster.h` | `Rendering/GfxRender/FastCluster.h` |
| `GeometryGenerator.cpp` | `Rendering/GfxRender/GeometryGenerator.cpp` |
| `GeometryGenerator.h` | `Rendering/GfxRender/GeometryGenerator.h` |
| `GlobalShaderData.cpp` | `Rendering/GfxRender/GlobalShaderData.cpp` |
| `Image.cpp` | `Rendering/GfxRender/Image.cpp` |
| `Image.h` | `Rendering/GfxRender/Image.h` |
| `LightGrid.cpp` | `Rendering/GfxRender/LightGrid.cpp` |
| `LightGrid.h` | `Rendering/GfxRender/LightGrid.h` |
| `LightObject.cpp` | `Rendering/GfxRender/LightObject.cpp` |
| `LightObject.h` | `Rendering/GfxRender/LightObject.h` |
| `Material.cpp` | `Rendering/GfxRender/Material.cpp` |
| `Material.h` | `Rendering/GfxRender/Material.h` |
| `MaterialGenerator.cpp` | `Rendering/GfxRender/MaterialGenerator.cpp` |
| `MegaCluster.cpp` | `Rendering/GfxRender/MegaCluster.cpp` |
| `MegaCluster.h` | `Rendering/GfxRender/MegaCluster.h` |
| `ObjectExporter.cpp` | `Rendering/GfxRender/ObjectExporter.cpp` |
| `ObjectExporter.h` | `Rendering/GfxRender/ObjectExporter.h` |
| `ParticleEmitter.cpp` | `Rendering/GfxRender/ParticleEmitter.cpp` |
| `RenderCamera.cpp` | `Rendering/GfxRender/RenderCamera.cpp` |
| `RenderCamera.h` | `Rendering/GfxRender/RenderCamera.h` |
| `RenderNode.cpp` | `Rendering/GfxRender/RenderNode.cpp` |
| `RenderNode.h` | `Rendering/GfxRender/RenderNode.h` |
| `RenderQueue.cpp` | `Rendering/GfxRender/RenderQueue.cpp` |
| `RenderQueue.h` | `Rendering/GfxRender/RenderQueue.h` |
| `RenderView.cpp` | `Rendering/GfxRender/RenderView.cpp` |
| `RenderView.h` | `Rendering/GfxRender/RenderView.h` |
| `SSAO.cpp` | `Rendering/GfxRender/SSAO.cpp` |
| `SSAO.h` | `Rendering/GfxRender/SSAO.h` |
| `SceneManager.cpp` | `Rendering/GfxRender/SceneManager.cpp` |
| `SceneManager.h` | `Rendering/GfxRender/SceneManager.h` |
| `SceneUpdater.cpp` | `Rendering/GfxRender/SceneUpdater.cpp` |
| `SceneUpdater.h` | `Rendering/GfxRender/SceneUpdater.h` |
| `ScreenSpaceEffect.cpp` | `Rendering/GfxRender/ScreenSpaceEffect.cpp` |
| `ShaderManager.cpp` | `Rendering/GfxRender/ShaderManager.cpp` |
| `Sky.cpp` | `Rendering/GfxRender/Sky.cpp` |
| `Sky.h` | `Rendering/GfxRender/Sky.h` |
| `SmoothCluster.cpp` | `Rendering/GfxRender/SmoothCluster.cpp` |
| `SpatialGrid.h` | `Rendering/GfxRender/SpatialGrid.h` |
| `SpatialHashedScene.cpp` | `Rendering/GfxRender/SpatialHashedScene.cpp` |
| `SpatialHashedScene.h` | `Rendering/GfxRender/SpatialHashedScene.h` |
| `SuperCluster.cpp` | `Rendering/GfxRender/SuperCluster.cpp` |
| `SuperCluster.h` | `Rendering/GfxRender/SuperCluster.h` |
| `TextureAtlas.cpp` | `Rendering/GfxRender/TextureAtlas.cpp` |
| `TextureAtlas.h` | `Rendering/GfxRender/TextureAtlas.h` |
| `TextureCompositor.cpp` | `Rendering/GfxRender/TextureCompositor.cpp` |
| `TextureCompositor.h` | `Rendering/GfxRender/TextureCompositor.h` |
| `TextureManager.cpp` | `Rendering/GfxRender/TextureManager.cpp` |
| `TextureManager.h` | `Rendering/GfxRender/TextureManager.h` |
| `TextureRef.cpp` | `Rendering/GfxRender/TextureRef.cpp` |
| `TextureRef.h` | `Rendering/GfxRender/TextureRef.h` |
| `TypesetterBitmap.cpp` | `Rendering/GfxRender/TypesetterBitmap.cpp` |
| `TypesetterBitmap.h` | `Rendering/GfxRender/TypesetterBitmap.h` |
| `TypesetterDynamic.cpp` | `Rendering/GfxRender/TypesetterDynamic.cpp` |
| `Util.h` | `Rendering/GfxRender/Util.h` |
| `VertexStreamer.cpp` | `Rendering/GfxRender/VertexStreamer.cpp` |
| `VisualEngine.cpp` | `Rendering/GfxRender/VisualEngine.cpp` |
| `VisualEngine.h` | `Rendering/GfxRender/VisualEngine.h` |
| `Water.cpp` | `Rendering/GfxRender/Water.cpp` |
| `ftcalc.h` | `Rendering/GfxRender/freetype/include/freetype/internal/ftcalc.h` |
| `ftmemory.h` | `Rendering/GfxRender/freetype/include/freetype/internal/ftmemory.h` |
| `afcjk.c` | `Rendering/GfxRender/freetype/src/autofit/afcjk.c` |
| `afdummy.c` | `Rendering/GfxRender/freetype/src/autofit/afdummy.c` |
| `afglobal.c` | `Rendering/GfxRender/freetype/src/autofit/afglobal.c` |
| `afhints.c` | `Rendering/GfxRender/freetype/src/autofit/afhints.c` |
| `afindic.c` | `Rendering/GfxRender/freetype/src/autofit/afindic.c` |
| `aflatin.c` | `Rendering/GfxRender/freetype/src/autofit/aflatin.c` |
| `aflatin2.c` | `Rendering/GfxRender/freetype/src/autofit/aflatin2.c` |
| `afloader.c` | `Rendering/GfxRender/freetype/src/autofit/afloader.c` |
| `afmodule.c` | `Rendering/GfxRender/freetype/src/autofit/afmodule.c` |
| `afpic.c` | `Rendering/GfxRender/freetype/src/autofit/afpic.c` |
| `afwarp.c` | `Rendering/GfxRender/freetype/src/autofit/afwarp.c` |
| `hbshim.c` | `Rendering/GfxRender/freetype/src/autofit/hbshim.c` |
| `basepic.c` | `Rendering/GfxRender/freetype/src/base/basepic.c` |
| `ftadvanc.c` | `Rendering/GfxRender/freetype/src/base/ftadvanc.c` |
| `ftbbox.c` | `Rendering/GfxRender/freetype/src/base/ftbbox.c` |
| `ftbitmap.c` | `Rendering/GfxRender/freetype/src/base/ftbitmap.c` |
| `ftcalc.c` | `Rendering/GfxRender/freetype/src/base/ftcalc.c` |
| `ftdbgmem.c` | `Rendering/GfxRender/freetype/src/base/ftdbgmem.c` |
| `ftgloadr.c` | `Rendering/GfxRender/freetype/src/base/ftgloadr.c` |
| `ftglyph.c` | `Rendering/GfxRender/freetype/src/base/ftglyph.c` |
| `ftlcdfil.c` | `Rendering/GfxRender/freetype/src/base/ftlcdfil.c` |
| `ftmac.c` | `Rendering/GfxRender/freetype/src/base/ftmac.c` |
| `ftmm.c` | `Rendering/GfxRender/freetype/src/base/ftmm.c` |
| `ftobjs.c` | `Rendering/GfxRender/freetype/src/base/ftobjs.c` |
| `ftoutln.c` | `Rendering/GfxRender/freetype/src/base/ftoutln.c` |
| `ftpatent.c` | `Rendering/GfxRender/freetype/src/base/ftpatent.c` |
| `ftpfr.c` | `Rendering/GfxRender/freetype/src/base/ftpfr.c` |
| `ftrfork.c` | `Rendering/GfxRender/freetype/src/base/ftrfork.c` |
| `ftstroke.c` | `Rendering/GfxRender/freetype/src/base/ftstroke.c` |
| `fttrigon.c` | `Rendering/GfxRender/freetype/src/base/fttrigon.c` |
| `md5.c` | `Rendering/GfxRender/freetype/src/base/md5.c` |
| `bdfdrivr.c` | `Rendering/GfxRender/freetype/src/bdf/bdfdrivr.c` |
| `bdflib.c` | `Rendering/GfxRender/freetype/src/bdf/bdflib.c` |
| `ftbzip2.c` | `Rendering/GfxRender/freetype/src/bzip2/ftbzip2.c` |
| `ftccache.c` | `Rendering/GfxRender/freetype/src/cache/ftccache.c` |
| `ftcmanag.c` | `Rendering/GfxRender/freetype/src/cache/ftcmanag.c` |
| `ftcsbits.c` | `Rendering/GfxRender/freetype/src/cache/ftcsbits.c` |
| `cf2arrst.c` | `Rendering/GfxRender/freetype/src/cff/cf2arrst.c` |
| `cf2font.c` | `Rendering/GfxRender/freetype/src/cff/cf2font.c` |
| `cf2ft.c` | `Rendering/GfxRender/freetype/src/cff/cf2ft.c` |
| `cf2hints.c` | `Rendering/GfxRender/freetype/src/cff/cf2hints.c` |
| `cf2intrp.c` | `Rendering/GfxRender/freetype/src/cff/cf2intrp.c` |
| `cf2read.c` | `Rendering/GfxRender/freetype/src/cff/cf2read.c` |
| `cffdrivr.c` | `Rendering/GfxRender/freetype/src/cff/cffdrivr.c` |
| `cffgload.c` | `Rendering/GfxRender/freetype/src/cff/cffgload.c` |
| `cffload.c` | `Rendering/GfxRender/freetype/src/cff/cffload.c` |
| `cffobjs.c` | `Rendering/GfxRender/freetype/src/cff/cffobjs.c` |
| `cffparse.c` | `Rendering/GfxRender/freetype/src/cff/cffparse.c` |
| `cffpic.c` | `Rendering/GfxRender/freetype/src/cff/cffpic.c` |
| `cidload.c` | `Rendering/GfxRender/freetype/src/cid/cidload.c` |
| `cidobjs.c` | `Rendering/GfxRender/freetype/src/cid/cidobjs.c` |
| `cidriver.c` | `Rendering/GfxRender/freetype/src/cid/cidriver.c` |
| `gxvbsln.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvbsln.c` |
| `gxvcommn.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvcommn.c` |
| `gxvfeat.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvfeat.c` |
| `gxvfgen.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvfgen.c` |
| `gxvjust.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvjust.c` |
| `gxvkern.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvkern.c` |
| `gxvlcar.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvlcar.c` |
| `gxvmod.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvmod.c` |
| `gxvmort.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvmort.c` |
| `gxvmort0.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvmort0.c` |
| `gxvmort1.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvmort1.c` |
| `gxvmort2.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvmort2.c` |
| `gxvmort4.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvmort4.c` |
| `gxvmort5.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvmort5.c` |
| `gxvmorx.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvmorx.c` |
| `gxvmorx0.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvmorx0.c` |
| `gxvmorx1.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvmorx1.c` |
| `gxvmorx2.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvmorx2.c` |
| `gxvmorx5.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvmorx5.c` |
| `gxvopbd.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvopbd.c` |
| `gxvprop.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvprop.c` |
| `gxvtrak.c` | `Rendering/GfxRender/freetype/src/gxvalid/gxvtrak.c` |
| `ftgzip.c` | `Rendering/GfxRender/freetype/src/gzip/ftgzip.c` |
| `zutil.c` | `Rendering/GfxRender/freetype/src/gzip/zutil.c` |
| `ftlzw.c` | `Rendering/GfxRender/freetype/src/lzw/ftlzw.c` |
| `ftzopen.c` | `Rendering/GfxRender/freetype/src/lzw/ftzopen.c` |
| `otvbase.c` | `Rendering/GfxRender/freetype/src/otvalid/otvbase.c` |
| `otvcommn.c` | `Rendering/GfxRender/freetype/src/otvalid/otvcommn.c` |
| `otvgdef.c` | `Rendering/GfxRender/freetype/src/otvalid/otvgdef.c` |
| `otvgpos.c` | `Rendering/GfxRender/freetype/src/otvalid/otvgpos.c` |
| `otvgsub.c` | `Rendering/GfxRender/freetype/src/otvalid/otvgsub.c` |
| `otvjstf.c` | `Rendering/GfxRender/freetype/src/otvalid/otvjstf.c` |
| `otvmath.c` | `Rendering/GfxRender/freetype/src/otvalid/otvmath.c` |
| `otvmod.c` | `Rendering/GfxRender/freetype/src/otvalid/otvmod.c` |
| `pcfdrivr.c` | `Rendering/GfxRender/freetype/src/pcf/pcfdrivr.c` |
| `pcfread.c` | `Rendering/GfxRender/freetype/src/pcf/pcfread.c` |
| `pfrgload.c` | `Rendering/GfxRender/freetype/src/pfr/pfrgload.c` |
| `pfrload.c` | `Rendering/GfxRender/freetype/src/pfr/pfrload.c` |
| `pfrsbit.c` | `Rendering/GfxRender/freetype/src/pfr/pfrsbit.c` |
| `afmparse.c` | `Rendering/GfxRender/freetype/src/psaux/afmparse.c` |
| `psobjs.c` | `Rendering/GfxRender/freetype/src/psaux/psobjs.c` |
| `t1cmap.c` | `Rendering/GfxRender/freetype/src/psaux/t1cmap.c` |
| `t1decode.c` | `Rendering/GfxRender/freetype/src/psaux/t1decode.c` |
| `pshalgo.c` | `Rendering/GfxRender/freetype/src/pshinter/pshalgo.c` |
| `pshglob.c` | `Rendering/GfxRender/freetype/src/pshinter/pshglob.c` |
| `pshpic.c` | `Rendering/GfxRender/freetype/src/pshinter/pshpic.c` |
| `pshrec.c` | `Rendering/GfxRender/freetype/src/pshinter/pshrec.c` |
| `psmodule.c` | `Rendering/GfxRender/freetype/src/psnames/psmodule.c` |
| `pspic.c` | `Rendering/GfxRender/freetype/src/psnames/pspic.c` |
| `pstables.h` | `Rendering/GfxRender/freetype/src/psnames/pstables.h` |
| `ftmisc.h` | `Rendering/GfxRender/freetype/src/raster/ftmisc.h` |
| `ftraster.c` | `Rendering/GfxRender/freetype/src/raster/ftraster.c` |
| `ftrend1.c` | `Rendering/GfxRender/freetype/src/raster/ftrend1.c` |
| `rastpic.c` | `Rendering/GfxRender/freetype/src/raster/rastpic.c` |
| `pngshim.c` | `Rendering/GfxRender/freetype/src/sfnt/pngshim.c` |
| `sfdriver.c` | `Rendering/GfxRender/freetype/src/sfnt/sfdriver.c` |
| `sfntpic.c` | `Rendering/GfxRender/freetype/src/sfnt/sfntpic.c` |
| `sfobjs.c` | `Rendering/GfxRender/freetype/src/sfnt/sfobjs.c` |
| `ttbdf.c` | `Rendering/GfxRender/freetype/src/sfnt/ttbdf.c` |
| `ttcmap.c` | `Rendering/GfxRender/freetype/src/sfnt/ttcmap.c` |
| `ttload.c` | `Rendering/GfxRender/freetype/src/sfnt/ttload.c` |
| `ttpost.c` | `Rendering/GfxRender/freetype/src/sfnt/ttpost.c` |
| `ttsbit.c` | `Rendering/GfxRender/freetype/src/sfnt/ttsbit.c` |
| `ftgrays.c` | `Rendering/GfxRender/freetype/src/smooth/ftgrays.c` |
| `ftsmooth.c` | `Rendering/GfxRender/freetype/src/smooth/ftsmooth.c` |
| `ftspic.c` | `Rendering/GfxRender/freetype/src/smooth/ftspic.c` |
| `apinames.c` | `Rendering/GfxRender/freetype/src/tools/apinames.c` |
| `content.py` | `Rendering/GfxRender/freetype/src/tools/docmaker/content.py` |
| `docbeauty.py` | `Rendering/GfxRender/freetype/src/tools/docmaker/docbeauty.py` |
| `docmaker.py` | `Rendering/GfxRender/freetype/src/tools/docmaker/docmaker.py` |
| `formatter.py` | `Rendering/GfxRender/freetype/src/tools/docmaker/formatter.py` |
| `sources.py` | `Rendering/GfxRender/freetype/src/tools/docmaker/sources.py` |
| `tohtml.py` | `Rendering/GfxRender/freetype/src/tools/docmaker/tohtml.py` |
| `utils.py` | `Rendering/GfxRender/freetype/src/tools/docmaker/utils.py` |
| `ftrandom.c` | `Rendering/GfxRender/freetype/src/tools/ftrandom/ftrandom.c` |
| `glnames.py` | `Rendering/GfxRender/freetype/src/tools/glnames.py` |
| `test_afm.c` | `Rendering/GfxRender/freetype/src/tools/test_afm.c` |
| `test_bbox.c` | `Rendering/GfxRender/freetype/src/tools/test_bbox.c` |
| `test_trig.c` | `Rendering/GfxRender/freetype/src/tools/test_trig.c` |
| `ttdriver.c` | `Rendering/GfxRender/freetype/src/truetype/ttdriver.c` |
| `ttgload.c` | `Rendering/GfxRender/freetype/src/truetype/ttgload.c` |
| `ttgxvar.c` | `Rendering/GfxRender/freetype/src/truetype/ttgxvar.c` |
| `ttinterp.c` | `Rendering/GfxRender/freetype/src/truetype/ttinterp.c` |
| `ttobjs.c` | `Rendering/GfxRender/freetype/src/truetype/ttobjs.c` |
| `ttpic.c` | `Rendering/GfxRender/freetype/src/truetype/ttpic.c` |
| `ttsubpix.c` | `Rendering/GfxRender/freetype/src/truetype/ttsubpix.c` |
| `t1afm.c` | `Rendering/GfxRender/freetype/src/type1/t1afm.c` |
| `t1driver.c` | `Rendering/GfxRender/freetype/src/type1/t1driver.c` |
| `t1gload.c` | `Rendering/GfxRender/freetype/src/type1/t1gload.c` |
| `t1load.c` | `Rendering/GfxRender/freetype/src/type1/t1load.c` |
| `t1objs.c` | `Rendering/GfxRender/freetype/src/type1/t1objs.c` |
| `t1parse.c` | `Rendering/GfxRender/freetype/src/type1/t1parse.c` |
| `t42drivr.c` | `Rendering/GfxRender/freetype/src/type42/t42drivr.c` |
| `t42objs.c` | `Rendering/GfxRender/freetype/src/type42/t42objs.c` |
| `t42parse.c` | `Rendering/GfxRender/freetype/src/type42/t42parse.c` |
| `winfnt.c` | `Rendering/GfxRender/freetype/src/winfonts/winfnt.c` |
| `Frustum.cpp` | `Rendering/RbxG3D/Frustum.cpp` |
| `RbxCamera.cpp` | `Rendering/RbxG3D/RbxCamera.cpp` |
| `RbxRay.cpp` | `Rendering/RbxG3D/RbxRay.cpp` |
| `Frustum.h` | `Rendering/RbxG3D/include/RbxG3D/Frustum.h` |
| `RbxCamera.h` | `Rendering/RbxG3D/include/RbxG3D/RbxCamera.h` |
| `RbxRay.h` | `Rendering/RbxG3D/include/RbxG3D/RbxRay.h` |
| `main.cpp` | `Rendering/ShaderCompiler/main.cpp` |
| `md5.c` | `Rendering/ShaderCompiler/md5/md5.c` |
| `AABox.cpp` | `Rendering/g3d/g3dcpp/AABox.cpp` |
| `BinaryInput.cpp` | `Rendering/g3d/g3dcpp/BinaryInput.cpp` |
| `BinaryOutput.cpp` | `Rendering/g3d/g3dcpp/BinaryOutput.cpp` |
| `Box.cpp` | `Rendering/g3d/g3dcpp/Box.cpp` |
| `Capsule.cpp` | `Rendering/g3d/g3dcpp/Capsule.cpp` |
| `CollisionDetection.cpp` | `Rendering/g3d/g3dcpp/CollisionDetection.cpp` |
| `Color3.cpp` | `Rendering/g3d/g3dcpp/Color3.cpp` |
| `Color4.cpp` | `Rendering/g3d/g3dcpp/Color4.cpp` |
| `CoordinateFrame.cpp` | `Rendering/g3d/g3dcpp/CoordinateFrame.cpp` |
| `Crypto.cpp` | `Rendering/g3d/g3dcpp/Crypto.cpp` |
| `Cylinder.cpp` | `Rendering/g3d/g3dcpp/Cylinder.cpp` |
| `GCamera.cpp` | `Rendering/g3d/g3dcpp/GCamera.cpp` |
| `GImage.cpp` | `Rendering/g3d/g3dcpp/GImage.cpp` |
| `GImage_bayer.cpp` | `Rendering/g3d/g3dcpp/GImage_bayer.cpp` |
| `GImage_bmp.cpp` | `Rendering/g3d/g3dcpp/GImage_bmp.cpp` |
| `GImage_jpeg.cpp` | `Rendering/g3d/g3dcpp/GImage_jpeg.cpp` |
| `GImage_png.cpp` | `Rendering/g3d/g3dcpp/GImage_png.cpp` |
| `GImage_tga.cpp` | `Rendering/g3d/g3dcpp/GImage_tga.cpp` |
| `GLight.cpp` | `Rendering/g3d/g3dcpp/GLight.cpp` |
| `LightingParameters.cpp` | `Rendering/g3d/g3dcpp/LightingParameters.cpp` |
| `Line.cpp` | `Rendering/g3d/g3dcpp/Line.cpp` |
| `LineSegment.cpp` | `Rendering/g3d/g3dcpp/LineSegment.cpp` |
| `Matrix3.cpp` | `Rendering/g3d/g3dcpp/Matrix3.cpp` |
| `Matrix4.cpp` | `Rendering/g3d/g3dcpp/Matrix4.cpp` |
| `MemoryManager.cpp` | `Rendering/g3d/g3dcpp/MemoryManager.cpp` |
| `PhysicsFrame.cpp` | `Rendering/g3d/g3dcpp/PhysicsFrame.cpp` |
| `Plane.cpp` | `Rendering/g3d/g3dcpp/Plane.cpp` |
| `Quat.cpp` | `Rendering/g3d/g3dcpp/Quat.cpp` |
| `Random.cpp` | `Rendering/g3d/g3dcpp/Random.cpp` |
| `Ray.cpp` | `Rendering/g3d/g3dcpp/Ray.cpp` |
| `Sphere.cpp` | `Rendering/g3d/g3dcpp/Sphere.cpp` |
| `System.cpp` | `Rendering/g3d/g3dcpp/System.cpp` |
| `Triangle.cpp` | `Rendering/g3d/g3dcpp/Triangle.cpp` |
| `UprightFrame.cpp` | `Rendering/g3d/g3dcpp/UprightFrame.cpp` |
| `Vector2.cpp` | `Rendering/g3d/g3dcpp/Vector2.cpp` |
| `Vector2int16.cpp` | `Rendering/g3d/g3dcpp/Vector2int16.cpp` |
| `Vector3.cpp` | `Rendering/g3d/g3dcpp/Vector3.cpp` |
| `Vector3int16.cpp` | `Rendering/g3d/g3dcpp/Vector3int16.cpp` |
| `Vector4.cpp` | `Rendering/g3d/g3dcpp/Vector4.cpp` |
| `fileutils.cpp` | `Rendering/g3d/g3dcpp/fileutils.cpp` |
| `format.cpp` | `Rendering/g3d/g3dcpp/format.cpp` |
| `g3dfnmatch.cpp` | `Rendering/g3d/g3dcpp/g3dfnmatch.cpp` |
| `g3dmath.cpp` | `Rendering/g3d/g3dcpp/g3dmath.cpp` |
| `stringutils.cpp` | `Rendering/g3d/g3dcpp/stringutils.cpp` |
| `uint128.cpp` | `Rendering/g3d/g3dcpp/uint128.cpp` |
| `AABSPTree.h` | `Rendering/g3d/include/g3d/AABSPTree.h` |
| `AABox.h` | `Rendering/g3d/include/g3d/AABox.h` |
| `Array.h` | `Rendering/g3d/include/g3d/Array.h` |
| `BinaryFormat.h` | `Rendering/g3d/include/g3d/BinaryFormat.h` |
| `BinaryInput.h` | `Rendering/g3d/include/g3d/BinaryInput.h` |
| `BinaryOutput.h` | `Rendering/g3d/include/g3d/BinaryOutput.h` |
| `Box.h` | `Rendering/g3d/include/g3d/Box.h` |
| `Capsule.h` | `Rendering/g3d/include/g3d/Capsule.h` |
| `CollisionDetection.h` | `Rendering/g3d/include/g3d/CollisionDetection.h` |
| `Color1.h` | `Rendering/g3d/include/g3d/Color1.h` |
| `Color3.h` | `Rendering/g3d/include/g3d/Color3.h` |
| `Color3uint8.h` | `Rendering/g3d/include/g3d/Color3uint8.h` |
| `Color4.h` | `Rendering/g3d/include/g3d/Color4.h` |
| `Color4uint8.h` | `Rendering/g3d/include/g3d/Color4uint8.h` |
| `Cone.h` | `Rendering/g3d/include/g3d/Cone.h` |
| `ConvexPolyhedron.h` | `Rendering/g3d/include/g3d/ConvexPolyhedron.h` |
| `CoordinateFrame.h` | `Rendering/g3d/include/g3d/CoordinateFrame.h` |
| `Crypto.h` | `Rendering/g3d/include/g3d/Crypto.h` |
| `Cylinder.h` | `Rendering/g3d/include/g3d/Cylinder.h` |
| `EqualsTrait.h` | `Rendering/g3d/include/g3d/EqualsTrait.h` |
| `GCamera.h` | `Rendering/g3d/include/g3d/GCamera.h` |
| `GImage.h` | `Rendering/g3d/include/g3d/GImage.h` |
| `GLight.h` | `Rendering/g3d/include/g3d/GLight.h` |
| `HashTrait.h` | `Rendering/g3d/include/g3d/HashTrait.h` |
| `LightingParameters.h` | `Rendering/g3d/include/g3d/LightingParameters.h` |
| `Line.h` | `Rendering/g3d/include/g3d/Line.h` |
| `LineSegment.h` | `Rendering/g3d/include/g3d/LineSegment.h` |
| `Map2D.h` | `Rendering/g3d/include/g3d/Map2D.h` |
| `Matrix2.h` | `Rendering/g3d/include/g3d/Matrix2.h` |
| `Matrix3.h` | `Rendering/g3d/include/g3d/Matrix3.h` |
| `Matrix4.h` | `Rendering/g3d/include/g3d/Matrix4.h` |
| `MeshAlg.h` | `Rendering/g3d/include/g3d/MeshAlg.h` |
| `MeshBuilder.h` | `Rendering/g3d/include/g3d/MeshBuilder.h` |
| `ParseError.h` | `Rendering/g3d/include/g3d/ParseError.h` |
| `PhysicsFrame.h` | `Rendering/g3d/include/g3d/PhysicsFrame.h` |
| `Plane.h` | `Rendering/g3d/include/g3d/Plane.h` |
| `Quat.h` | `Rendering/g3d/include/g3d/Quat.h` |
| `Random.h` | `Rendering/g3d/include/g3d/Random.h` |
| `Ray.h` | `Rendering/g3d/include/g3d/Ray.h` |
| `Rect2D.h` | `Rendering/g3d/include/g3d/Rect2D.h` |
| `Set.h` | `Rendering/g3d/include/g3d/Set.h` |
| `SmallArray.h` | `Rendering/g3d/include/g3d/SmallArray.h` |
| `Sphere.h` | `Rendering/g3d/include/g3d/Sphere.h` |
| `System.h` | `Rendering/g3d/include/g3d/System.h` |
| `Table.h` | `Rendering/g3d/include/g3d/Table.h` |
| `Triangle.h` | `Rendering/g3d/include/g3d/Triangle.h` |
| `UprightFrame.h` | `Rendering/g3d/include/g3d/UprightFrame.h` |
| `Vector2.h` | `Rendering/g3d/include/g3d/Vector2.h` |
| `Vector2int16.h` | `Rendering/g3d/include/g3d/Vector2int16.h` |
| `Vector3.h` | `Rendering/g3d/include/g3d/Vector3.h` |
| `Vector3int16.h` | `Rendering/g3d/include/g3d/Vector3int16.h` |
| `Vector3int32.h` | `Rendering/g3d/include/g3d/Vector3int32.h` |
| `Vector4.h` | `Rendering/g3d/include/g3d/Vector4.h` |
| `Vector4int8.h` | `Rendering/g3d/include/g3d/Vector4int8.h` |
| `WrapMode.h` | `Rendering/g3d/include/g3d/WrapMode.h` |
| `constants.h` | `Rendering/g3d/include/g3d/constants.h` |
| `debug.h` | `Rendering/g3d/include/g3d/debug.h` |
| `enumclass.h` | `Rendering/g3d/include/g3d/enumclass.h` |
| `g3dmath.h` | `Rendering/g3d/include/g3d/g3dmath.h` |
| `platform.h` | `Rendering/g3d/include/g3d/platform.h` |
| `spline.h` | `Rendering/g3d/include/g3d/spline.h` |
| `stringutils.h` | `Rendering/g3d/include/g3d/stringutils.h` |
| `units.h` | `Rendering/g3d/include/g3d/units.h` |
| `vectorMath.h` | `Rendering/g3d/include/g3d/vectorMath.h` |
| `png.c` | `Rendering/g3d/png/png.c` |
| `pngerror.c` | `Rendering/g3d/png/pngerror.c` |
| `pnggccrd.c` | `Rendering/g3d/png/pnggccrd.c` |
| `pngget.c` | `Rendering/g3d/png/pngget.c` |
| `pngmem.c` | `Rendering/g3d/png/pngmem.c` |
| `pngpread.c` | `Rendering/g3d/png/pngpread.c` |
| `pngread.c` | `Rendering/g3d/png/pngread.c` |
| `pngrio.c` | `Rendering/g3d/png/pngrio.c` |
| `pngrtran.c` | `Rendering/g3d/png/pngrtran.c` |
| `pngrutil.c` | `Rendering/g3d/png/pngrutil.c` |
| `pngset.c` | `Rendering/g3d/png/pngset.c` |
| `pngtrans.c` | `Rendering/g3d/png/pngtrans.c` |
| `pngwio.c` | `Rendering/g3d/png/pngwio.c` |
| `pngwrite.c` | `Rendering/g3d/png/pngwrite.c` |
| `pngwutil.c` | `Rendering/g3d/png/pngwutil.c` |

</details>

---

## Function Reference

### 1. `Draw::partAdorn`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Draw::partAdorn(const Part&					part, 
	Adorn*						adorn,
	const G3D::Color3&			controllerColor);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/Draw.cpp:17` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes partAdorn within Rendering Pipeline. Coordinates interactions with `adornSurfaces`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `adornSurfaces`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `partAdorn`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 2. `Draw::setSelectColor`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Draw::setSelectColor(const G3D::Color4& Color);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/Draw.cpp:29` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Set color used for the selection box when a part is selected.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setSelectColor`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 3. `Draw::setHoverOverColor`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Draw::setHoverOverColor(const G3D::Color4& color);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/Draw.cpp:37` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Set the color used for the selection box when a part is mouse hover over.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setHoverOverColor`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 4. `Draw::selectionBox`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Draw::selectionBox(const Part&				part, 
	Adorn*					adorn,
	SelectState				selectState,
	float					lineThickness);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/Draw.cpp:41` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes selectionBox within Rendering Pipeline. Coordinates interactions with `setObjectToWorldMatrix, selectColor, orange`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `setObjectToWorldMatrix`, `selectColor`, `orange`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `selectionBox`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 5. `Draw::selectionBox`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Draw::selectionBox(ModelInstance&				model, 
	Adorn*						adorn,
	const G3D::Color4&			selectColor,
	float						lineThickness);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/Draw.cpp:66` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes selectionBox within Rendering Pipeline. Coordinates interactions with `computePart`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `computePart`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `selectionBox`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 6. `Draw::adornSurfaces`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Draw::adornSurfaces(const Part& part, 
						 Adorn* adorn, 
						 const G3D::Color3& controllerColor);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/Draw.cpp:75` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes adornSurfaces within Rendering Pipeline. Coordinates interactions with `constraint`.

- **Control Flow & Execution:** Iterative loop processing, Multi-case state dispatch.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `constraint`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `adornSurfaces`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 7. `Draw::constraint`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Draw::constraint(const Part& part, 
					  Adorn* adorn, 
					  int face,
					  const G3D::Color3& controllerColor);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/Draw.cpp:90` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes constraint within Rendering Pipeline. Coordinates interactions with `debugAssert, getAxisRotationMatrix, translation, setObjectToWorldMatrix`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `debugAssert`, `getAxisRotationMatrix`, `translation`, `setObjectToWorldMatrix`, `cylinderAlongX`, `yellow`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `constraint`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 8. `Draw::selectionBox`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Draw::selectionBox(const Part&					part, 
	Adorn*						adorn,
	const G3D::Color4&			selectColor,
	float						lineThickness);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/Draw.cpp:127` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes selectionBox within Rendering Pipeline. Coordinates interactions with `getCamera, getCameraCoordinateFrame, squaredLength, primaryAxis`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `getCamera`, `getCameraCoordinateFrame`, `squaredLength`, `primaryAxis`, `setObjectToWorldMatrix`, `outlineBox`, `Extents`, `box`, `AABox`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `selectionBox`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 9. `DrawAdorn::cylinder`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DrawAdorn::cylinder(Adorn*						adorn,
	const						CoordinateFrame& worldC,		
	int							axis,
	float						length,
	float						radius,
	const Color4&				color,
	bool						cap);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:57` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes cylinder within Rendering Pipeline. Coordinates interactions with `getAxisRotationMatrix, rotatedWorldC, setObjectToWorldMatrix, cylinderAlongX`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getAxisRotationMatrix`, `rotatedWorldC`, `setObjectToWorldMatrix`, `cylinderAlongX`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `cylinder`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 10. `DrawAdorn::faceInWorld`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DrawAdorn::faceInWorld(Adorn*			adorn,
							const Face&		face,
							float			thickness,
							const Color4&	color);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:73` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes faceInWorld within Rendering Pipeline. Coordinates interactions with `cross, setColumn, unit, setObjectToWorldMatrix`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `cross`, `setColumn`, `unit`, `setObjectToWorldMatrix`, `magnitude`, `extents`, `Vector3`, `box`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `faceInWorld`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 11. `DrawAdorn::surfaceBorder`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DrawAdorn::surfaceBorder(Adorn*			adorn,
							  const Vector3&	halfRealSize,
							  float				highlight,
							  int				surfaceId,
							  const Color4&		color);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:101` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes surfaceBorder within Rendering Pipeline. Coordinates interactions with `AABox, box`.

- **Control Flow & Execution:** Iterative loop processing.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `AABox`, `box`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `surfaceBorder`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 12. `DrawAdorn::surfaceGridOnFace`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DrawAdorn::surfaceGridOnFace(const Primitive&	prim,
							Adorn*				adorn,
							int					surfaceId,
							const Color4&		color,
							int					boxesPerStud);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:132` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes surfaceGridOnFace within Rendering Pipeline. Coordinates interactions with `getCoordinateFrame, getConstGeometry, getSurfaceCoordInBody, bounds`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getCoordinateFrame`, `getConstGeometry`, `getSurfaceCoordInBody`, `bounds`, `getNumVertsInSurface`, `getSurfaceVertInBody`, `pointToWorldSpace`, `pointToObjectSpace`, `surfaceGridAtCoord`, `unitX`, `unitY`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `surfaceGridOnFace`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 13. `DrawAdorn::zeroPlaneGrid`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DrawAdorn::zeroPlaneGrid(Adorn*						adorn,
	const RBX::Camera&			camera,
	const int					studsPerBox,
	const int					yLevel,
	const G3D::Color4&			smallGridColor,
	const G3D::Color4&			largeGridColor);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:164` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes zeroPlaneGrid within Rendering Pipeline. Coordinates interactions with `getCameraCoordinateFrame, Plane, Vector3, closestPoint`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getCameraCoordinateFrame`, `Plane`, `Vector3`, `closestPoint`, `iRound`, `magnitude`, `setObjectToWorldMatrix`, `zero`, `max`, `line3dAA`, `Color4`, `rgb`.
- **External Library Dependencies:** `G3D Graphics and Math Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `zeroPlaneGrid`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 14. `DrawAdorn::surfaceGridAtCoord`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DrawAdorn::surfaceGridAtCoord(Adorn*						adorn,
	CoordinateFrame&			cF,
	const Vector4&				bounds,
	const Vector3&				gridXDir,
	const Vector3&				gridYDir,
	const G3D::Color4&			color,
	int							boxesPerStud);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:297` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes surfaceGridAtCoord within Rendering Pipeline. Coordinates interactions with `iRound, fromDirectionCosines, cross, unitX`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `iRound`, `fromDirectionCosines`, `cross`, `unitX`, `unitY`, `unitZ`, `zero`, `pointToWorldSpace`, `cylinder`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `surfaceGridAtCoord`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 15. `DrawAdorn::axisWidget`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DrawAdorn::axisWidget(Adorn* adorn, const RBX::Camera& camera);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:364` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes axisWidget within Rendering Pipeline. Coordinates interactions with `getViewport, Vector3, width, height`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getViewport`, `Vector3`, `width`, `height`, `getRenderingCoordinateFrame`, `lookVector`, `project`, `unitX`, `line2d`, `Vector2`, `drawFont2D`, `clear`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `axisWidget`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 16. `DrawAdorn::circularGridAtCoord`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DrawAdorn::circularGridAtCoord(Adorn*                  adorn,
    const CoordinateFrame&  coordFrame,
    const G3D::Vector3&		size,
	const G3D::Vector3&	    cameraPos,
    NormalId                normalId,
    const Color4&           color,
    int                     boxesPerStud);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:408` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes circularGridAtCoord within Rendering Pipeline. Coordinates interactions with `Extents, handlePosInObject, pointToWorldSpace, length`.

- **Control Flow & Execution:** Iterative loop processing.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `Extents`, `handlePosInObject`, `pointToWorldSpace`, `length`, `normalIdToVector3`, `pif`, `fromAxisAngle`, `scaleRelativeToCamera`, `setMaterial`, `cylinder`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `circularGridAtCoord`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 17. `DrawAdorn::lineSegmentRelativeToCoord`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DrawAdorn::lineSegmentRelativeToCoord(Adorn*						adorn,
	const CoordinateFrame&		cF,
	const Vector3&      		pt0,
	const Vector3&      		pt1,
	const G3D::Color3&			color,
	float						lineThickness);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:455` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes lineSegmentRelativeToCoord within Rendering Pipeline. Coordinates interactions with `magnitude, getWellFormedRotForZVector, cylinder`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `magnitude`, `getWellFormedRotForZVector`, `cylinder`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `lineSegmentRelativeToCoord`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 18. `DrawAdorn::verticalLineSegmentSplit`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DrawAdorn::verticalLineSegmentSplit(Adorn*						adorn,
	const CoordinateFrame&		cF,
	const Vector3&      		pt0,
	const Vector3&      		pt1,
	const float&      		    delta,
	const float&      		    dropFactor,
	const short&      		    level,
	const G3D::Color3&			color,
	float						lineThickness);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:473` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes verticalLineSegmentSplit within Rendering Pipeline. Coordinates interactions with `lineSegmentRelativeToCoord`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lineSegmentRelativeToCoord`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `verticalLineSegmentSplit`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 19. `DrawAdorn::surfacePolygon`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DrawAdorn::surfacePolygon(Adorn*						adorn,
	PartInstance&				partInst,
	int							surfaceId,
	const G3D::Color3&			color,
	float						lineThickness);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:502` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes surfacePolygon within Rendering Pipeline. Coordinates interactions with `getConstPrimitive, getConstGeometry, getNumVertsInSurface, push_back`.

- **Control Flow & Execution:** Iterative loop processing.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getConstPrimitive`, `getConstGeometry`, `getNumVertsInSurface`, `push_back`, `getSurfaceVertInBody`, `polygonRelativeToCoord`, `getCoordinateFrame`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `surfacePolygon`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 20. `DrawAdorn::polygonRelativeToCoord`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DrawAdorn::polygonRelativeToCoord(Adorn*						adorn,
	const CoordinateFrame&		cF,
	std::vector<Vector3>&		vertices,
	const G3D::Color4&			color,
	float						lineThickness);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:516` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes polygonRelativeToCoord within Rendering Pipeline. Coordinates interactions with `size, magnitude, getWellFormedRotForZVector, cylinder`.

- **Control Flow & Execution:** Iterative loop processing.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `size`, `magnitude`, `getWellFormedRotForZVector`, `cylinder`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `polygonRelativeToCoord`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 21. `DrawAdorn::partSurface`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DrawAdorn::partSurface(const Part&				part, 
	int						surfaceId,
	Adorn*					adorn,
	const Color4&			color,
	float					thickness);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:537` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes partSurface within Rendering Pipeline. Coordinates interactions with `setObjectToWorldMatrix, surfaceBorder`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `setObjectToWorldMatrix`, `surfaceBorder`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `partSurface`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 22. `DrawAdorn::handlePosInObject`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector3 DrawAdorn::handlePosInObject(const Vector3&  cameraPos,
    const Extents&  localExtents, 
    HandleType      handleType,
    NormalId        normalId);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector3` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:551` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes handlePosInObject within Rendering Pipeline. Coordinates interactions with `size, length, scaleRelativeToCamera, center`.

- **Control Flow & Execution:** Multi-case state dispatch, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `size`, `length`, `scaleRelativeToCamera`, `center`, `normalIdToVector3`, `normalIdToU`, `start_offset`, `RBXASSERT`, `zero`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `handlePosInObject`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 23. `DrawAdorn::scaleHandleRelativeToCamera`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
float DrawAdorn::scaleHandleRelativeToCamera(const Vector3&  cameraPos,
    HandleType      handleType,
    const Vector3&  handlePos);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `float` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:600` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes scaleHandleRelativeToCamera within Rendering Pipeline. Coordinates interactions with `scaleRelativeToCamera`.

- **Control Flow & Execution:** Multi-case state dispatch, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `scaleRelativeToCamera`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `scaleHandleRelativeToCamera`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 24. `DrawAdorn::scaleRelativeToCamera`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
float DrawAdorn::scaleRelativeToCamera(const Vector3&  cameraPos,
    const Vector3&  handlePos,
    float           minAngle,
    float           expectedSize);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `float` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:637` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

visual angle = radius/distance

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `magnitude`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `scaleRelativeToCamera`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 25. `DrawAdorn::handles2d`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DrawAdorn::handles2d(const G3D::Vector3&			size,
	const G3D::CoordinateFrame&	position,
	const RBX::Camera&			camera,		
	Adorn*						adorn,
	HandleType					handleType,
	const G3D::Color4&			color,
    bool                        useAxisColor,
	int							normalIdMask);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:652` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes handles2d within Rendering Pipeline. Coordinates interactions with `localExtents, handlePosInObject, coordinateFrame, pointToWorldSpace`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `localExtents`, `handlePosInObject`, `coordinateFrame`, `pointToWorldSpace`, `scaleRelativeToCamera`, `normalIdToVector3`, `frame`, `project`, `infinity`, `rect2d`, `fromCenterSize`, `toRect2D`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `handles2d`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 26. `DrawAdorn::partInfoText2D`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DrawAdorn::partInfoText2D(const G3D::Vector3&			size,
	const G3D::CoordinateFrame&	position,
	const RBX::Camera&			camera,		
	Adorn*						adorn,
    const std::string&          text,
	const G3D::Color4&			color,
    float                       fontSize,
	int							normalIdMask);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:708` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes partInfoText2D within Rendering Pipeline. Coordinates interactions with `localExtents, max, min, Vector3`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `localExtents`, `max`, `min`, `Vector3`, `Vector2`, `pointToWorldSpace`, `project`, `infinity`, `length`, `drawFont2D`, `clear`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `partInfoText2D`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 27. `DrawAdorn::handles3d`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DrawAdorn::handles3d(const G3D::Vector3&			size,
	const G3D::CoordinateFrame&	position,
	Adorn*						adorn,
	HandleType					handleType,
	const Vector3&				cameraPos,
	const G3D::Color4&			color,
    bool                        useAxisColor,
	int							normalIdMask,
	NormalId                    normalIdTohighlight,
	const G3D::Color4&			highlightColor);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:787` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes handles3d within Rendering Pipeline. Coordinates interactions with `localExtents, intToNormalId, handlePosInObject, pointToWorldSpace`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Multi-case state dispatch, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `localExtents`, `intToNormalId`, `handlePosInObject`, `pointToWorldSpace`, `scaleHandleRelativeToCamera`, `frame`, `setObjectToWorldMatrix`, `setMaterial`, `sphere`, `Sphere`, `zero`, `normalIdToVector3`.
- **External Library Dependencies:** `G3D Graphics and Math Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `handles3d`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 28. `eval`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector3 eval(float t);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector3` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:926` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes eval within Rendering Pipeline. Coordinates interactions with `cos, sin`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `cos`, `sin`.
- **External Library Dependencies:** `G3D Graphics and Math Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `eval`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 29. `evalTangent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector3 evalTangent(float t);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector3` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:932` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

first derivative.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `cos`, `sin`.
- **External Library Dependencies:** `G3D Graphics and Math Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `evalTangent`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 30. `evalNormal`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector3 evalNormal(float t);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector3` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:937` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes evalNormal within Rendering Pipeline. Coordinates interactions with `cos, sin`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `cos`, `sin`.
- **External Library Dependencies:** `G3D Graphics and Math Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `evalNormal`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 31. `evalBinormal`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector3 evalBinormal(float t);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector3` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:942` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes evalBinormal within Rendering Pipeline.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `evalBinormal`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 32. `hashString`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
std::string hashString();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `std::string` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:948` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

string that encodes this function in a unique way.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `CircleRN`, `str`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `hashString`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 33. `DrawAdorn::chatBubble2d`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DrawAdorn::chatBubble2d(Adorn*						adorn,
	const Rect2D&				rect,
	const G3D::Vector2			pointer,
	float						cornerradius,
	const float					linewidth,
	const int					quarterdivs,
	const Color4&				color);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:955` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes chatBubble2d within Rendering Pipeline. Coordinates interactions with `min, width, height, center`.

- **Control Flow & Execution:** Iterative loop processing.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `min`, `width`, `height`, `center`, `push_back`, `Vector2`, `RBXASSERT`, `border`, `cos`, `sin`, `x1y1`, `x1y0`.
- **External Library Dependencies:** `G3D Graphics and Math Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `chatBubble2d`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 34. `DrawAdorn::torus`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DrawAdorn::torus(Adorn*						adorn,
	const						CoordinateFrame& position,		
	NormalId					axis,
	float						radius,
	float						thicknessradius,
	const Color4&				color);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:1036` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes torus within Rendering Pipeline. Coordinates interactions with `trajectory, profile, setObjectToWorldMatrix, extrusion`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `trajectory`, `profile`, `setObjectToWorldMatrix`, `extrusion`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `torus`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 35. `DrawAdorn::star`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DrawAdorn::star(Adorn*                  adorn,
    const Vector3&          center,
    float                   size,
    const Color4&           colorX,
    const Color4&           colorY,
    const Color4&           colorZ);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:1062` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Draws a wire star made up of 3 line segments. @param adorn         object used to generate the geometry @param center        world space center coordinates @param size          lines are -size to +size on the axis @param colorX        color of x axis line @param colorY        color of y axis line @param colorZ        color of z axis line

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `line3d`, `unitX`, `unitY`, `unitZ`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `star`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 36. `DrawAdorn::outlineBox`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DrawAdorn::outlineBox(Adorn*          adorn,
    const AABox&    box,
    const Color4&   color);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:1093` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Draw an outline (wireframe) box in 3D. @param adorn     adornment to use for drawing @param box       box to draw @param color     color of lines

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `low`, `high`, `line3d`, `Vector3`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `outlineBox`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 37. `DrawAdorn::selectionBox`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void DrawAdorn::selectionBox(Adorn*          adorn,
    const AABox&    box,
    const Color4&   color);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/DrawAdorn.cpp:1167` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Draw select indicator around a box similar to 3DS. @param adorn     adornment to use for drawing @param box       box to draw @param color     color of lines

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `low`, `high`, `line3d`, `Vector3`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `selectionBox`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 38. `HitTest::hitTestBox`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool HitTest::hitTestBox(const Part& part, 
					  RBX::RbxRay& rayInPartCoords, 
					  Vector3& hitPointInPartCoords,
					  float gridToReal);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/HitTest.cpp:8` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes hitTestBox within Rendering Pipeline. Coordinates interactions with `collisionLocationForMovingPointFixedAABox, origin, direction, AABox`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `collisionLocationForMovingPointFixedAABox`, `origin`, `direction`, `AABox`.
- **External Library Dependencies:** `G3D Graphics and Math Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `hitTestBox`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 39. `HitTest::hitTestBall`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool HitTest::hitTestBall(const Part& part, 
					   RBX::RbxRay& rayInPartCoords, 
					   Vector3& hitPointInPartCoords,
					   float gridToReal);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/HitTest.cpp:22` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes hitTestBall within Rendering Pipeline. Coordinates interactions with `return, collisionTimeForMovingPointFixedSphere, origin, direction`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`, `collisionTimeForMovingPointFixedSphere`, `origin`, `direction`, `Sphere`, `zero`, `inf`.
- **External Library Dependencies:** `G3D Graphics and Math Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `hitTestBall`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 40. `HitTest::hitTestCylinder`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool HitTest::hitTestCylinder(const Part& part, 
						   RBX::RbxRay& rayInPartCoords, 
						   Vector3& hitPointInPartCoords,
						   float gridToReal);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/HitTest.cpp:42` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

TODO: Big optimization possible here... TODO: Clean up hit test here - offset stuff going on

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `return`, `collisionTimeForMovingPointFixedCapsule`, `origin`, `direction`, `Capsule`, `zero`, `Vector3`, `inf`.
- **External Library Dependencies:** `G3D Graphics and Math Engine`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `hitTestCylinder`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 41. `HitTest::hitTest`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool HitTest::hitTest(const Part& part,
						   RBX::RbxRay& rayInPartCoords, 
						   Vector3& hitPointInPartCoords,
						   float gridToReal);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `Rendering/AppDraw/HitTest.cpp:58` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes hitTest within Rendering Pipeline. Coordinates interactions with `hitTestBox, hitTestBall, hitTestCylinder, debugAssert`.

- **Control Flow & Execution:** Multi-case state dispatch, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `hitTestBox`, `hitTestBall`, `hitTestCylinder`, `debugAssert`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `hitTest`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 42. `selectColor`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
G3D::Color4& selectColor() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `G3D::Color4&` |
| **Modifiers** | `static const` |
| **Source Location** | `Rendering/AppDraw/include/appdraw/Draw.h:38` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes selectColor within Rendering Pipeline.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `selectColor`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 43. `hoverOverColor`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
G3D::Color4& hoverOverColor() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `G3D::Color4&` |
| **Modifiers** | `static const` |
| **Source Location** | `Rendering/AppDraw/include/appdraw/Draw.h:40` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes hoverOverColor within Rendering Pipeline.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `hoverOverColor`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 44. `showHoverOver`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void showHoverOver(bool Show);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `Rendering/AppDraw/include/appdraw/Draw.h:69` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes showHoverOver within Rendering Pipeline.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `showHoverOver`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 45. `isHoverOver`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool isHoverOver();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `static` |
| **Source Location** | `Rendering/AppDraw/include/appdraw/Draw.h:71` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes isHoverOver within Rendering Pipeline.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `isHoverOver`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 46. `resizeColor`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Color3& resizeColor() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Color3&` |
| **Modifiers** | `static const` |
| **Source Location** | `Rendering/AppDraw/include/appdraw/DrawAdorn.h:29` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes resizeColor within Rendering Pipeline.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `resizeColor`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 47. `outlineBox`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void outlineBox(Adorn*          adorn,
            const Extents&  extents,
            const Color4&   color);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `Rendering/AppDraw/include/appdraw/DrawAdorn.h:226` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Draw an outline (wireframe) box in 3D. @param adorn     adornment to use for drawing @param extents   box dimensions @param color     color of lines

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `aa_box`, `min`, `max`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `outlineBox`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 48. `selectionBox`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void selectionBox(Adorn*          adorn,
            const Extents&  extents,
            const Color4&   color);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `Rendering/AppDraw/include/appdraw/DrawAdorn.h:254` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Draw select indicator around a box similar to 3DS. @param adorn     adornment to use for drawing @param extents   box dimensions @param color     color of lines

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `aa_box`, `min`, `max`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `selectionBox`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 49. `outlineRect2dImpl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void outlineRect2dImpl(Adorn* adorn, const Rect2D& rect, float thick, const Color4& color, const Modifier& modifier);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `Rendering/GfxBase/Adorn.cpp:3` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes outlineRect2dImpl within Rendering Pipeline. Coordinates interactions with `rect2d, xyxy`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `rect2d`, `xyxy`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `outlineRect2dImpl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 50. `Adorn::outlineRect2d`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Adorn::outlineRect2d(const Rect2D& rect, float thick, const Color4& color);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/GfxBase/Adorn.cpp:13` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes outlineRect2d within Rendering Pipeline. Coordinates interactions with `outlineRect2dImpl, Rotation2D`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `outlineRect2dImpl`, `Rotation2D`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `outlineRect2d`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 51. `Adorn::outlineRect2d`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Adorn::outlineRect2d(const Rect2D& rect, float thick, const Color4& color, const Rotation2D& rotation);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/GfxBase/Adorn.cpp:18` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes outlineRect2d within Rendering Pipeline. Coordinates interactions with `outlineRect2dImpl`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `outlineRect2dImpl`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `outlineRect2d`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 52. `Adorn::outlineRect2d`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Adorn::outlineRect2d(const Rect2D& rect, float thick, const Color4& color, const Rect2D& clipRect);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/GfxBase/Adorn.cpp:23` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes outlineRect2d within Rendering Pipeline. Coordinates interactions with `outlineRect2dImpl`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `outlineRect2dImpl`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `outlineRect2d`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 53. `Adorn::rect2d`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Adorn::rect2d(const Rect2D& rect, const Color4& color);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/GfxBase/Adorn.cpp:28` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes rect2d within Rendering Pipeline. Coordinates interactions with `Vector2, Rotation2D`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `Vector2`, `Rotation2D`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `rect2d`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 54. `Adorn::rect2d`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Adorn::rect2d(const Rect2D& rect, const Color4& color, const Rotation2D& rotation);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/GfxBase/Adorn.cpp:33` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes rect2d within Rendering Pipeline. Coordinates interactions with `Vector2`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `Vector2`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `rect2d`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 55. `Adorn::rect2d`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Adorn::rect2d(const Rect2D& rect, const Color4& color, const Rect2D& clipRect);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/GfxBase/Adorn.cpp:38` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes rect2d within Rendering Pipeline. Coordinates interactions with `Vector2`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `Vector2`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `rect2d`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 56. `Adorn::rect2d`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Adorn::rect2d(const Rect2D& rect, const Vector2& texul, const Vector2& texbr, const Color4& color);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/GfxBase/Adorn.cpp:43` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes rect2d within Rendering Pipeline. Coordinates interactions with `Rotation2D`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `Rotation2D`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `rect2d`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 57. `Adorn::rect2d`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Adorn::rect2d(const Rect2D& rect, const Vector2& texul, const Vector2& texbr, const Color4& color, const Rotation2D& rotation);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/GfxBase/Adorn.cpp:48` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes rect2d within Rendering Pipeline. Coordinates interactions with `empty, rotate, x0y0, x1y0`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `empty`, `rotate`, `x0y0`, `x1y0`, `x0y1`, `x1y1`, `rect2dImpl`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `rect2d`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 58. `Adorn::rect2d`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void Adorn::rect2d(const Rect2D& rect, const Vector2& texul, const Vector2& texbr, const Color4& color, const Rect2D& clipRect);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `Rendering/GfxBase/Adorn.cpp:65` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes rect2d within Rendering Pipeline. Coordinates interactions with `lowerUV, upperUV, intersect, width`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lowerUV`, `upperUV`, `intersect`, `width`, `height`, `rect2dImpl`, `x0y0`, `x1y0`, `x0y1`, `x1y1`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `rect2d`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 59. `Adorn::drawFont2D`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Vector2 Adorn::drawFont2D(const std::string& s,
    const Vector2& position, float size, bool autoScale, const Color4& color, const Color4& outline,
    Text::Font font, Text::XAlign xalign, Text::YAlign yalign,
	const Vector2& availableSpace, const Rect2D& clippingRect, const Rotation2D& rotation);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Vector2` |
| **Modifiers** | None |
| **Source Location** | `Rendering/GfxBase/Adorn.cpp:96` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes drawFont2D within Rendering Pipeline. Coordinates interactions with `drawFont2DImpl`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `drawFont2DImpl`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `drawFont2D`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 60. `AdornBillboarder::getViewport`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
Rect2D AdornBillboarder::getViewport() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `Rect2D` |
| **Modifiers** | `const` |
| **Source Location** | `Rendering/GfxBase/AdornBillboarder.cpp:21` |
| **Subsystem** | `Rendering Pipeline` |

#### How it Works Internally

Executes getViewport within Rendering Pipeline.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getViewport`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---


:::tip Additional Functions
There are **6205 additional internal and inline functions** in this subsystem. All functions are indexed and cross-referenced in the **[Complete Function Catalog](./function-catalog.md)**.
:::

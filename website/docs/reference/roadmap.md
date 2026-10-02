---
sidebar_position: 3
---

# Roadmap

The fork's plan, transcribed and organized from the repository `README.md`. Checked items are
done in the current tree.

## Build & platform health

- [x] Add all the "Contrib" libraries to the tree
- [ ] Make every project compile and run (unit tests, RobloxTest, XboxClient, GameChat,
      NetworkMesh, CoreScriptConverter2 are the outstanding set)
- [ ] Fix all 557 security findings from the GitHub scanners
- [ ] 64-bit support
- [ ] Compile as VC++ 2019
- [ ] Linux support (client)
- [ ] Modernize the Android client

## Scripting & language

- [ ] Lua 5.3 (or port the Lua 5.3 `utf8` library into 5.1)
- [ ] Unicode / UTF-8 throughout
- [ ] `int64` support

## Gameplay & API

- [x] `WaterWaveSize` / `WaterWaveSpeed` uncapped to `-FLT_MIN`…`FLT_MAX`
- [x] Friction uncapped
- [x] `PlayerGui:SetTopbarTransparency` uncapped
- [ ] `Humanoid.FloorMaterial`
- [ ] Smooth camera scrolling
- [ ] TextBox text selection
- [ ] Bring back SafeChat (Studio Settings → Game Options → ShowSafeChatButton)
- [ ] Unlock `TextureTrail`
- [ ] Mesh format version 3.00 support
- [ ] `Color3.toRGB`
- [ ] Standalone game exporting (incl. FPS uncapping)

## Graphics & rendering

- [ ] Modern graphics pipeline (DirectX 12 / Vulkan)
- [ ] Real-time ray tracing capabilities
- [ ] Enhanced particle effects system
- [ ] Dynamic environment mapping
- [ ] PBR (Physically Based Rendering) materials
- [ ] DirectX 11 initialization fix (D3D9 works; DX11 does not start)
- [ ] Web / WebGL support

## Networking

- [ ] Dedicated server architecture improvements
- [ ] WebSocket support for cross-platform communication
- [ ] Bandwidth optimization algorithms
- [ ] Peer-to-peer networking fallback
- [ ] Improved latency compensation

## Physics

- [ ] Upgrade Bullet Physics to the latest version
- [ ] Enhanced collision detection performance
- [ ] Water/fluid simulation (commented out of the README but planned)
- [ ] Ragdoll physics systems

## Performance & optimization

- [ ] Advanced profiling tools (beyond microprofile)
- [ ] Memory pooling and optimization
- [ ] LOD (Level of Detail) systems
- [ ] Shader caching
- [ ] Multi-threaded rendering support

## Fixed along the way

- [x] SDL Windows-key handling
- [x] Keyboard shortcuts
- [x] Chat output shrinking on minimize
- [x] D3D9 "text render bug" — investigated, never existed

See also [Project Status](../getting-started/project-status.md) for the compile matrix.

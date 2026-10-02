---
sidebar_position: 5
---

# Project Status

This page tracks what actually builds in the R2K16 tree today, plus the fork's feature
checklist. It mirrors the *Extras* section of the repository `README.md` — if the README is
updated, this page should follow.

## Compile status

### ✅ Building

- App
- AppDraw
- Network
- RCCService
- Base
- boost.static
- boost.test
- GfxBase
- RbxG3D
- graphics3D
- RbxTestHooks
- RobloxStudio
- Log
- WindowsClient
- GfxCore
- GfxRender
- CSG
- App.BulletPhysics

### ❌ Not building (yet)

- Base.UnitTest
- App.UnitTest
- RobloxTest
- CoreScriptConverter2
- Microsoft.Xbox.GameChat
- Microsoft.Xbox.Samples.NetworkMesh
- XboxClient

The fork also tracks ~557 issues found by GitHub security scanning workflows (semgrep,
MSVC code analysis, OSV-Scanner, OpenSSF Scorecard) — see
[CI / CD](../development/ci.md) and [Security](../development/security.md).

## Changes already made to the original source

- All the "Contrib" libraries were added to the tree (Boost, Qt, SDL, curl, …).
- `WaterWaveSize` / `WaterWaveSpeed` can now range from `-FLT_MIN` to `FLT_MAX` (previously
  capped).
- Friction values are uncapped.
- `PlayerGui:SetTopbarTransparency` is uncapped.
- SDL Windows-key handling fixed.
- Keyboard shortcuts fixed.
- Chat output shrinking on minimize fixed.
- A DirectX 9 text rendering bug was investigated and found to never have existed.

## Open items (highlights)

- Fix all 557 scanned security "issues".
- Make every project compile and run (unit tests, RobloxTest, XboxClient, GameChat, …).
- Lua 5.3 (or backporting the Lua 5.3 `utf8` library).
- Unicode/UTF-8 support, `int64`, 64-bit builds, compiling as VC++ 2019.
- `Humanoid.FloorMaterial`, smooth camera scrolling, TextBox text selection.
- Bring back SafeChat (Studio Settings → Game Options → ShowSafeChatButton).
- Unlock `TextureTrail`, mesh format version 3.00, `Color3.toRGB`.
- Standalone game exporting (FPS uncapping, Linux support).

The long-form version (graphics, networking, physics, performance, platform plans) lives in the
[Roadmap](../reference/roadmap.md).

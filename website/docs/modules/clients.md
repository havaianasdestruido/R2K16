---
sidebar_position: 10
---

# Clients — player applications

The player-facing applications, one per platform. All of them embed the same `App` engine; the
differences are shells, input, and platform services.

## WindowsClient (Windows player) — ✅ builds

**Path:** `WindowsClient/`

The Win32 player client.

| File | Role |
| --- | --- |
| `main.cpp` | Entry point |
| `Application.cpp`, `Document.cpp`, `View.cpp` | App/document/view architecture (MFC-flavored) |
| `RenderJob.cpp/.h` | Client render job driving the engine |
| `UserInput.cpp/.h` | Keyboard/mouse → engine input |
| `RbxWebView.cpp/.h`, `WebBrowserAxDialog.*`, `html_*.htm` | Embedded web view (xulrunner under `Library/xulrunner`) |
| `Teleporter.cpp/.h` | Server-hop ("teleport") flow |
| `functionHooks.cpp`, `robloxHooks.cpp`, `RobloxHooks.h` | Anti-tamper runtime hooks |
| `Crypt.cpp/.h`, `RandomPadding.cpp` | Client-side obfuscation/crypto |
| `ReleasePatcher.cpp/.h`, `RobloxGoldenHashPatcher/` | Self-patching machinery |
| `GameVerbs.cpp/.h` | Editor verbs for the client |
| `WindowsClient.rc`, `Roblox.ico`, `InvisibleCursor.cur` | Resources |

Companion: **`WindowsClient.PrepForUpload/`** (release packaging) and **`Installer/`**
(bootstrappers — see [Tooling](./tooling.md)).

## `Win/` — shared Windows launcher code

Standalone snippets shared by Windows builds: `LogManager`, `ErrorUploader` /
`DumpErrorUploader` / `ScriptErrorUploader` (crash & error telemetry), `SharedLauncher`,
`DSVideoCaptureEngine` (DirectShow video capture), `CheckDbg` (anti-debug), `sitelock.h`,
`VistaTools`, `ProcessInformation`, `UserInputUtil`, `VersionInfo`, `Tracer`, `dinput.h`
(DirectInput).

## XboxClient (Xbox One / "Durango") — ❌ not building yet

**Path:** `XboxClient/`

The Universal Windows app for Xbox One: `main.cpp`, `renderJob.*`, `XboxMultiplayerManager`,
`XboxService`, `XbLiveUtils`, voice chat (`VoiceChat*`, backed by **`GameChat/`** and
**`Microsoft.Xbox.Samples.NetworkMesh/`**), `ControllerBuffer`, `XboxGameController`,
`KeyboardProvider`, `UserTranslator`, p2p (`p2p.*`), `Package.appxmanifest` + NSAL tooling
(`NSAL.json`, `SetNSAL.bat`, `enforceNSAL`), and `fetchfflags.py` (fetches feature flags at
build time).

## iOS — `iOS/`

Xcode workspace with `RobloxMobile.xcodeproj`: `RobloxMobile/` (app), `SharedCode/`
(platform glue), `RobloxUI/`, `Generic App Launcher/`, `AutomatedTesting/` +
`ROBLOXTests/` (XCTest suites), localization (`en.lproj`, `de.lproj`), `scripts/`.

## Android — `Android/` {#android}

Gradle project: `build.gradle`, `settings.gradle`, `gradlew`; `NativeShell/` (Java/Kotlin
shell), `libroblox/` (the native engine build via CMake + NDK — see
[Building with CMake](../getting-started/building-cmake.md#android)),
`RobloxAndroidTests/`, bundled deps (`circleimageview`, `google_play_services`). The root
CMake build prints the NDK variables it consumes (`ANDROID_ABI`, `ANDROID_STL`, …).

## Mac — `Mac/` & `RobloxMac/`

`Mac/Mac.xcworkspace` and `RobloxMac/` hold the Mac app projects; individual libraries carry
`.xcodeproj` files (`App.xcodeproj`, `Base.xcodeproj`, …). Building the full Mac client in
2024+ requires the era's SDKs.

## RobloxHybrid — `RobloxHybrid/`

The **hybrid** client of the time: a lightweight web shell (`index.html`, `RobloxHybrid.js`,
`hybridlib/`) around the native player, built with the Closure compiler
(`closure-compiler/`, `build_js.sh`). See its own `docs/` folder.

## GameChat — `GameChat/`

`Microsoft.Xbox.GameChat.XDK` — the Xbox chat SDK sources (`Chat`, `ChatAudioThread`,
`ChatClient`, `ChatNetwork`, `ChatEvents`, `ChatUserSerialization`). ❌ Not building yet.

## Microsoft.Xbox.Samples.NetworkMesh — `Microsoft.Xbox.Samples.NetworkMesh/`

Xbox sample code for mesh networking used by the console client. ❌ Not building yet.

## Test clients

`RobloxMobileTest/`, `RobloxTest.MultiPlayerTest.Run` and friends — see
[Testing](./testing.md).

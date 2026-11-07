---
sidebar_position: 26
title: Platform & Cross-File Divergence Matrix
description: Comprehensive matrix of platform-specific behavior and multi-file variants across the codebase.
---

# Platform & Cross-File Divergence Matrix

R2K16 targets multiple platforms: **Windows (x86/x64)**, **macOS**, **iOS**, **Android**, and **Xbox One (Durango)**. This matrix identifies all functions whose behavior or implementation differs across target platforms or code files.

## Divergence Categories

1. **Conditional Preprocessor Guards (`#ifdef _WIN32`, `#ifdef __APPLE__`, `#ifdef ANDROID`, `#ifdef _DURANGO`):**
   The function's implementation branches internally at compile time to utilize platform-native APIs (e.g. WinINet vs WebKit vs POSIX sockets).
2. **Multi-File Platform Variants:**
   The engine defines separate implementation files per platform (e.g., `ClientShared/Win/CookiesEngine.cpp` vs `ClientShared/Mac/CookiesEngine.cpp` vs `ClientShared/Mobile/CookiesEngine.cpp`).
3. **Caller Context Divergence:**
   The function exhibits differing runtime behavior depending on whether it is executed within **RobloxStudio** (Qt UI loop), **WindowsClient** (DirectX VSync loop), or **RCCService** (headless unthrottled loop).

---

## Divergent Functions Directory

| Function | Source File | Platform Preprocessor Flags | Divergence Summary |
| :--- | :--- | :--- | :--- |
| `ChatWidget::process` | `App/gui/ChatWidget.cpp` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.cpp`. |
| `GuiItem::process` | `App/gui/GUI.cpp` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.cpp`. |
| `RelativePanel::init` | `App/gui/GUI.cpp` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/VoiceChat.cpp`, `Win/LogManager.cpp`, `XboxClient/Vo... |
| `TopMenuBar::init` | `App/gui/GUI.cpp` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/VoiceChat.cpp`, `Win/LogManager.cpp`, `XboxClient/Vo... |
| `TopMenuBar::process` | `App/gui/GUI.cpp` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.cpp`. |
| `TopMenuBar::getSize` | `App/gui/GUI.cpp` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `RobloxStudio/RobloxRibbonMainWindow.cpp`. |
| `UnifiedWidget::init` | `App/gui/GUI.cpp` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/VoiceChat.cpp`, `Win/LogManager.cpp`, `XboxClient/Vo... |
| `UnifiedWidget::process` | `App/gui/GUI.cpp` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.cpp`. |
| `TextDisplay::init` | `App/gui/GUI.cpp` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/VoiceChat.cpp`, `Win/LogManager.cpp`, `XboxClient/Vo... |
| `TextDisplay::getSize` | `App/gui/GUI.cpp` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `RobloxStudio/RobloxRibbonMainWindow.cpp`. |
| `Widget::process` | `App/gui/Widget.cpp` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.cpp`. |
| `getState` | `App/humanoid/HumanoidState.cpp` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/UserTranslator.h`. |
| `HumanoidState::create` | `App/humanoid/HumanoidState.cpp` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Rendering/GfxCore/GL/ContextGLAndroid.cpp`, `XboxClient/VoiceCh... |
| `getSize` | `App/include/gui/ChatOutput.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `RobloxStudio/RobloxRibbonMainWindow.cpp`. |
| `getSize` | `App/include/gui/GUI.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `RobloxStudio/RobloxRibbonMainWindow.cpp`. |
| `isEnabled` | `App/include/gui/Widget.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.h`, `WindowsClient/GameVerbs.cpp`. |
| `getComputeEventBaseAddress` | `App/include/humanoid/HumanoidState.h` | `Windows (Win32/x64 API)` | Behavior branches internally via conditional compilation for: Windows (Win32/x64 API). |
| `getValue` | `App/include/lua/LuaBridge.h` | `Windows (Win32/x64 API)` | Behavior branches internally via conditional compilation for: Windows (Win32/x64 API). |
| `getName` | `App/include/reflection/Callback.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `RobloxStudio/RobloxRibbonMainWindow.cpp`. |
| `singleton` | `App/include/reflection/EnumConverter.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `RobloxStudio/MobileDevelopmentDeployer.cpp`. |
| `singleton` | `App/include/reflection/EnumConverter.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `RobloxStudio/MobileDevelopmentDeployer.cpp`. |
| `create` | `App/include/reflection/Event.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Rendering/GfxCore/GL/ContextGLAndroid.cpp`, `XboxClient/VoiceCh... |
| `execute` | `App/include/reflection/Event.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/marshaller.cpp`. |
| `sendEvent` | `App/include/reflection/Event.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/UserInput.cpp`, `XboxClient/XbLiveUtils.cpp`. |
| `getName` | `App/include/reflection/Event.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `RobloxStudio/RobloxRibbonMainWindow.cpp`. |
| `getName` | `App/include/reflection/Function.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `RobloxStudio/RobloxRibbonMainWindow.cpp`. |
| `execute` | `App/include/reflection/Function.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/marshaller.cpp`. |
| `getName` | `App/include/reflection/Property.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `RobloxStudio/RobloxRibbonMainWindow.cpp`. |
| `write` | `App/include/reflection/Property.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.cpp`, `App/util/WinHttp.cpp`... |
| `read` | `App/include/reflection/Property.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.cpp`, `App/util/WinHttp.cpp`... |
| `getDataSize` | `App/include/reflection/Property.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/VoiceChatMaxNet.h`. |
| `getDataSize` | `App/include/reflection/Property.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/VoiceChatMaxNet.h`. |
| `singleton` | `App/include/reflection/Type.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `RobloxStudio/MobileDevelopmentDeployer.cpp`. |
| `get` | `App/include/reflection/Type.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/UserTranslator.cpp`, `RobloxStudio/RobloxMainWindow.... |
| `getName` | `App/include/reflection/YieldFunction.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `RobloxStudio/RobloxRibbonMainWindow.cpp`. |
| `singleton` | `App/include/reflection/reflection.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `RobloxStudio/MobileDevelopmentDeployer.cpp`. |
| `isEnabled` | `App/include/script/DebuggerManager.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.h`, `WindowsClient/GameVerbs.cpp`. |
| `size` | `App/include/script/LuaArguments.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/p2p.h`. |
| `update` | `App/include/script/ScriptContext.h` | `Windows (Win32/x64 API)` | Behavior branches internally via conditional compilation for: Windows (Win32/x64 API). Alternative platform-specific imp... |
| `checkAnchor` | `App/include/script/ScriptContext.h` | `Windows (Win32/x64 API)` | Behavior branches internally via conditional compilation for: Windows (Win32/x64 API). |
| `create` | `App/include/script/ScriptStats.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Rendering/GfxCore/GL/ContextGLAndroid.cpp`, `XboxClient/VoiceCh... |
| `get` | `App/include/script/ThreadRef.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/UserTranslator.cpp`, `RobloxStudio/RobloxMainWindow.... |
| `reset` | `App/include/solver/ConstraintJacobian.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.h`. |
| `reset` | `App/include/solver/ConstraintJacobian.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.h`. |
| `getSize` | `App/include/solver/ConstraintJacobian.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `RobloxStudio/RobloxRibbonMainWindow.cpp`. |
| `reset` | `App/include/solver/ConstraintJacobian.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.h`. |
| `reset` | `App/include/solver/ConstraintJacobian.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.h`. |
| `reset` | `App/include/solver/ConstraintJacobian.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.h`. |
| `reset` | `App/include/solver/ConstraintJacobian.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.h`. |
| `start` | `App/include/solver/SolverProfiler.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Win/DSVideoCaptureEngine.cpp`. |
| `update` | `App/include/solver/SolverSerializer.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `RobloxStudio/filewatcher/FileWatcherWin32.cpp`. |
| `size` | `App/include/util/Average.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/p2p.h`. |
| `size` | `App/include/util/ClusterCellIterator.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/p2p.h`. |
| `size` | `App/include/util/ClusterCellIterator.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/p2p.h`. |
| `size` | `App/include/util/ControlledLRUCache.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/p2p.h`. |
| `size` | `App/include/util/DoubleEndedVector.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/p2p.h`. |
| `reset` | `App/include/util/ExponentialRunningAverage.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.h`. |
| `reset` | `App/include/util/ExponentialRunningAverage.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.h`. |
| `reset` | `App/include/util/ExponentialRunningAverage.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.h`. |
| `size` | `App/include/util/Extents.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/p2p.h`. |
| `contains` | `App/include/util/Extents.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `App/util/IndexBox.cpp`. |
| `size` | `App/include/util/ExtentsInt32.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/p2p.h`. |
| `contains` | `App/include/util/ExtentsInt32.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `App/util/IndexBox.cpp`. |
| `contains` | `App/include/util/ExtentsInt32.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `App/util/IndexBox.cpp`. |
| `size` | `App/include/util/Face.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/p2p.h`. |
| `size` | `App/include/util/FixedArray.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/p2p.h`. |
| `getName` | `App/include/util/Guid.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `RobloxStudio/RobloxRibbonMainWindow.cpp`. |
| `create` | `App/include/util/Guid.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Rendering/GfxCore/GL/ContextGLAndroid.cpp`, `XboxClient/VoiceCh... |
| `size` | `App/include/util/HttpPlatformImpl.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/p2p.h`. |
| `size` | `App/include/util/HttpPlatformImpl.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/p2p.h`. |
| `size` | `App/include/util/IndexArray.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/p2p.h`. |
| `size` | `App/include/util/LRUCache.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/p2p.h`. |
| `maxSize` | `App/include/util/LRUCache.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Base/rbx/Android/ifaddrs.c`. |
| `getName` | `App/include/util/Name.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `RobloxStudio/RobloxRibbonMainWindow.cpp`. |
| `create` | `App/include/util/Object.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Rendering/GfxCore/GL/ContextGLAndroid.cpp`, `XboxClient/VoiceCh... |
| `create` | `App/include/util/Object.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Rendering/GfxCore/GL/ContextGLAndroid.cpp`, `XboxClient/VoiceCh... |
| `create` | `App/include/util/Object.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Rendering/GfxCore/GL/ContextGLAndroid.cpp`, `XboxClient/VoiceCh... |
| `create` | `App/include/util/Object.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Rendering/GfxCore/GL/ContextGLAndroid.cpp`, `XboxClient/VoiceCh... |
| `create` | `App/include/util/Object.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Rendering/GfxCore/GL/ContextGLAndroid.cpp`, `XboxClient/VoiceCh... |
| `create` | `App/include/util/Object.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Rendering/GfxCore/GL/ContextGLAndroid.cpp`, `XboxClient/VoiceCh... |
| `create` | `App/include/util/Object.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Rendering/GfxCore/GL/ContextGLAndroid.cpp`, `XboxClient/VoiceCh... |
| `create` | `App/include/util/Object.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Rendering/GfxCore/GL/ContextGLAndroid.cpp`, `XboxClient/VoiceCh... |
| `contains` | `App/include/util/Rect.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `App/util/IndexBox.cpp`. |
| `size` | `App/include/util/Rect.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/p2p.h`. |
| `getSize` | `App/include/util/Region3.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `RobloxStudio/RobloxRibbonMainWindow.cpp`. |
| `contains` | `App/include/util/Region3Int16.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `App/util/IndexBox.cpp`. |
| `getCenter` | `App/include/util/Rotation2d.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `App/util/IndexBox.cpp`. |
| `run` | `App/include/util/RunStateOwner.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Win/DumpErrorUploader.cpp`, `Win/ScriptErrorUploader.cpp`. |
| `pause` | `App/include/util/RunStateOwner.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Win/VideoControl.cpp`. |
| `stop` | `App/include/util/RunStateOwner.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/RenderJob.cpp`, `XboxClient/renderJob.cpp`, `Win/... |
| `isRunning` | `App/include/util/RunStateOwner.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Win/DSVideoCaptureEngine.cpp`. |
| `get` | `App/include/util/Sound.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/UserTranslator.cpp`, `RobloxStudio/RobloxMainWindow.... |
| `sleepTime` | `App/include/util/SoundService.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `App/util/Win/CheatEngine.cpp`, `XboxClient/renderJob.cpp`, `Win... |
| `error` | `App/include/util/SoundService.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `App/util/Win/CheatEngine.cpp`, `XboxClient/async.h`. |
| `stepDataModelJob` | `App/include/util/SoundService.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/renderJob.cpp`, `WindowsClient/RenderJob.cpp`. |
| `create` | `App/include/util/SoundService.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Rendering/GfxCore/GL/ContextGLAndroid.cpp`, `XboxClient/VoiceCh... |
| `read` | `App/include/util/Utilities.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.cpp`, `App/util/WinHttp.cpp`... |
| `write` | `App/include/util/Utilities.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.cpp`, `App/util/WinHttp.cpp`... |
| `reset` | `App/include/util/Utilities.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Network/Replicator.NewInstanceItem.h`. |
| `get` | `App/include/util/base64.hpp` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `XboxClient/UserTranslator.cpp`, `RobloxStudio/RobloxMainWindow.... |
| `isEnabled` | `App/include/v8datamodel/ChangeHistory.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.h`, `WindowsClient/GameVerbs.cpp`. |
| `start` | `App/include/v8datamodel/ColorSequence.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `Win/DSVideoCaptureEngine.cpp`. |
| `isEnabled` | `App/include/v8datamodel/Commands.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.h`, `WindowsClient/GameVerbs.cpp`. |
| `doIt` | `App/include/v8datamodel/Commands.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.cpp`. |
| `isChecked` | `App/include/v8datamodel/Commands.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.cpp`. |
| `isEnabled` | `App/include/v8datamodel/Commands.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.h`, `WindowsClient/GameVerbs.cpp`. |
| `isChecked` | `App/include/v8datamodel/Commands.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.cpp`. |
| `isEnabled` | `App/include/v8datamodel/Commands.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.h`, `WindowsClient/GameVerbs.cpp`. |
| `isChecked` | `App/include/v8datamodel/Commands.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.cpp`. |
| `doIt` | `App/include/v8datamodel/Commands.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.cpp`. |
| `isEnabled` | `App/include/v8datamodel/Commands.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.h`, `WindowsClient/GameVerbs.cpp`. |
| `isChecked` | `App/include/v8datamodel/Commands.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.cpp`. |
| `doIt` | `App/include/v8datamodel/Commands.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.cpp`. |
| `isEnabled` | `App/include/v8datamodel/Commands.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.h`, `WindowsClient/GameVerbs.cpp`. |
| `isChecked` | `App/include/v8datamodel/Commands.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.cpp`. |
| `doIt` | `App/include/v8datamodel/Commands.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.cpp`. |
| `isEnabled` | `App/include/v8datamodel/Commands.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.h`, `WindowsClient/GameVerbs.cpp`. |
| `isChecked` | `App/include/v8datamodel/Commands.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.cpp`. |
| `doIt` | `App/include/v8datamodel/Commands.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.cpp`. |
| `isEnabled` | `App/include/v8datamodel/Commands.h` | *Multi-File Variant* | Alternative platform-specific implementations exist in: `WindowsClient/GameVerbs.h`, `WindowsClient/GameVerbs.cpp`. |

---

## Case Study: Key Multi-File Implementation Variants

### 1. `CookiesEngine` Subsystem
- **Windows Implementation (`ClientShared/Win/CookiesEngine.cpp`):** Utilizes Microsoft WinINet APIs (`InternetGetCookieEx`, `InternetSetCookieEx`) hooked into Internet Explorer / Win32 cookie cache.
- **Mac Implementation (`ClientShared/Mac/CookiesEngine.cpp`):** Utilizes macOS WebKit / Foundation `NSHTTPCookieStorage` synchronized with user WebKit storage.
- **Mobile Implementation (`ClientShared/Mobile/CookiesEngine.cpp`):** Employs an isolated filesystem-backed cookie jar optimized for iOS / Android sandboxed app environments.

### 2. `Crypt` Cryptography Subsystem
- **Windows Implementation (`Base/rbx/Crypt.cpp` & `WindowsClient/Crypt.cpp`):** Interfaces with Win32 CryptoAPI / Crypt32 for hardware-assisted key storage and verification.
- **Unix / POSIX Implementation (`Base/rbx/Unix/Crypt.cpp`):** Employs portable RC4/AES software ciphers independent of Windows DLLs.

### 3. `FileSystem` Path Resolution
- **Windows (`App/util/Win/FileSystem.cpp`):** Resolves paths via `SHGetFolderPathW` pointing to `C:\Users\<User>\AppData\Local\Roblox`.
- **Android (`App/util/Android/FileSystem.cpp`):** Queries Android JNI context to locate `/data/data/com.roblox.client/files`.

---
sidebar_position: 8
---

# RobloxStudio — the editor

**Path:** `RobloxStudio/` · **Project:** `RobloxStudio.vcxproj` · **Status:** ✅ builds

The **Studio** application: the level editor and IDE where places are built. It is a desktop
app built on **Qt 4.8.5** with the **QTitanRibbon** ribbon UI (`QTitanRibbon/` at the repo
root), hosting the `App` engine in-process.

```
RobloxStudio/
├── main.cpp                     # Entry point
├── RobloxMainWindow.cpp/.h/.ui  # Classic main window
├── RobloxRibbonMainWindow.*     # Ribbon-style main window (QTitanRibbon)
├── RBXMainWindow.ui             # Qt Designer form
├── DocDockManager / DocDockWidget / DocTabManager   # Document & docking management
├── … dozens of dialogs (.ui + .cpp/.h)
├── AppSettings.xml              # Default Studio settings
├── RobloxStudio.css/.qrc/.rc    # Styling, Qt resources, Windows resources
└── RobloxStudio.vcxproj (+ .filters)
```

## Feature areas (selected files)

| Area | Files |
| --- | --- |
| Documents & docking | `DocDockManager`, `DocDockWidget`, `DocTabManager`, `SaveDocumentDialog` |
| Insert / toolbox | `CommonInsertWidget`, `InsertDialog`-family, gallery widgets (`GalleryItem*`) |
| Tools | Consumes `App/tool/*` (see [App](./app.md#tool--studio-tools)); toolbars & options dialogs |
| CSG | `CSGOperations.cpp` — union/negate/subtract commands |
| Script debugging | `DebuggerClient.cpp`, `DebuggerWidgets.cpp` (client of `App/script/DebuggerManager`) |
| Team create (cloud edit) | `CloudEditAdornable.cpp` and related |
| Emulation | `AddEmulationDeviceDialog.*` — device emulation for mobile preview |
| Authoring settings | `AuthoringSettings.*`, `AppSettings.xml` |
| Crash reporting | `BreakpadHandler.cpp`, `BreakpadCrashReporter.*` (Windows/mm), `AppleCrashReporter.*` |
| Launcher helpers | `AuthenticationHelper`, `ExternalHandlers`, `FunctionMarshaller` |

## Settings

`AppSettings.xml` in `RobloxStudio/` holds the default settings tree (the era's Studio
Settings dialog reads/writes this shape); compare with the [SettingsComparisonTool](./tooling.md#settingscomparisontool).

## Companion pieces

- **`QTitanRibbon/`** (repo root) — the commercial-style Qt ribbon widget library used for the
  toolbar UI.
- **`BuiltInPlugins/`** — plugins that ship *inside* Studio (see
  [Tooling](./tooling.md#builtinplugins)); **`StudioPlugins/`** — Lua plugins (terrain, water,
  wiring utilities) installed into the plugins folder.
- **`RobloxStudio.PrepForUpload/`** — packaging project for release uploads.
- **`Installer/BootstrapperQTStudio*`** — the installer bootstrapper for Studio.

## Build

Builds from `Roblox.sln` on Windows. The Qt 4.8.5 dependency must be built first (see
[Building on Windows](../getting-started/building-windows.md#2-build-qt-485)).

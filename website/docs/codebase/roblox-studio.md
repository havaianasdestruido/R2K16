---
sidebar_position: 21
title: Roblox Studio IDE
description: Qt-based Studio editor, ribbon framework, docking widgets, and plugins.
---

# Roblox Studio IDE

Qt-based Studio editor, ribbon framework, docking widgets, and plugins.


## FAQ

### How do I trace a Studio command?

Follow its UI action into the document or engine operation, including undo and state changes where applicable. Generated entries do not capture the full user workflow.

### How can I investigate this in the repository?

From the repository root, search the relevant tracked files for a starting point (results are leads, not proof of behavior):

```bash
git grep -n -i -F -- 'Document' -- RobloxStudio
```

Read the surrounding implementation and callers, and check relevant tests before making changes. A search may return no matches when terminology or tracked files change.

## Subsystem Metrics

- **Total Documented Functions:** `3123`
- **Functions Exercised in Tests:** `153`
- **Platform-Divergent Implementations:** `379`
- **Component Source Files:** `161`

## Source Files

<details>
<summary>View all 161 source files in this subsystem</summary>

| Source File | Path |
| :--- | :--- |
| `AddEmulationDeviceDialog.cpp` | `RobloxStudio/AddEmulationDeviceDialog.cpp` |
| `AppleCrashReporter.cpp` | `RobloxStudio/AppleCrashReporter.cpp` |
| `AuthenticationHelper.cpp` | `RobloxStudio/AuthenticationHelper.cpp` |
| `AuthenticationHelper.h` | `RobloxStudio/AuthenticationHelper.h` |
| `AuthoringSettings.cpp` | `RobloxStudio/AuthoringSettings.cpp` |
| `AuthoringSettings.h` | `RobloxStudio/AuthoringSettings.h` |
| `AutoSaveDialog.cpp` | `RobloxStudio/AutoSaveDialog.cpp` |
| `BreakpadCrashReporter.mm` | `RobloxStudio/BreakpadCrashReporter.mm` |
| `BreakpadHandler.cpp` | `RobloxStudio/BreakpadHandler.cpp` |
| `CSGOperations.cpp` | `RobloxStudio/CSGOperations.cpp` |
| `CloudEditAdornable.cpp` | `RobloxStudio/CloudEditAdornable.cpp` |
| `CommonInsertWidget.cpp` | `RobloxStudio/CommonInsertWidget.cpp` |
| `CommonInsertWidget.h` | `RobloxStudio/CommonInsertWidget.h` |
| `DebuggerClient.cpp` | `RobloxStudio/DebuggerClient.cpp` |
| `DebuggerClient.h` | `RobloxStudio/DebuggerClient.h` |
| `DebuggerWidgets.cpp` | `RobloxStudio/DebuggerWidgets.cpp` |
| `DebuggerWidgets.h` | `RobloxStudio/DebuggerWidgets.h` |
| `DocDockManager.cpp` | `RobloxStudio/DocDockManager.cpp` |
| `DocDockWidget.cpp` | `RobloxStudio/DocDockWidget.cpp` |
| `DocDockWidget.h` | `RobloxStudio/DocDockWidget.h` |
| `DocTabManager.cpp` | `RobloxStudio/DocTabManager.cpp` |
| `ExternalHandlers.cpp` | `RobloxStudio/ExternalHandlers.cpp` |
| `ExternalHandlers.h` | `RobloxStudio/ExternalHandlers.h` |
| `FindDialog.cpp` | `RobloxStudio/FindDialog.cpp` |
| `FindDialog.h` | `RobloxStudio/FindDialog.h` |
| `FunctionMarshaller.cpp` | `RobloxStudio/FunctionMarshaller.cpp` |
| `FunctionMarshaller.h` | `RobloxStudio/FunctionMarshaller.h` |
| `GalleryItemColor.cpp` | `RobloxStudio/GalleryItemColor.cpp` |
| `GalleryItemColor.h` | `RobloxStudio/GalleryItemColor.h` |
| `InsertObjectListWidget.cpp` | `RobloxStudio/InsertObjectListWidget.cpp` |
| `InsertObjectListWidgetItem.cpp` | `RobloxStudio/InsertObjectListWidgetItem.cpp` |
| `InsertObjectListWidgetItem.h` | `RobloxStudio/InsertObjectListWidgetItem.h` |
| `InsertServiceDialog.cpp` | `RobloxStudio/InsertServiceDialog.cpp` |
| `KeepSavedChangesDialog.cpp` | `RobloxStudio/KeepSavedChangesDialog.cpp` |
| `KeepSavedChangesDialog.h` | `RobloxStudio/KeepSavedChangesDialog.h` |
| `LogProvider.cpp` | `RobloxStudio/LogProvider.cpp` |
| `LuaSourceBuffer.cpp` | `RobloxStudio/LuaSourceBuffer.cpp` |
| `LuaSourceBuffer.h` | `RobloxStudio/LuaSourceBuffer.h` |
| `MachineConfig.cpp` | `RobloxStudio/MachineConfig.cpp` |
| `MachineConfig.h` | `RobloxStudio/MachineConfig.h` |
| `ManageEmulationDeviceDialog.cpp` | `RobloxStudio/ManageEmulationDeviceDialog.cpp` |
| `MobileDevelopmentDeployer.cpp` | `RobloxStudio/MobileDevelopmentDeployer.cpp` |
| `NameValueStoreManager.cpp` | `RobloxStudio/NameValueStoreManager.cpp` |
| `NameValueStoreManager.h` | `RobloxStudio/NameValueStoreManager.h` |
| `PairRbxDeviceDialog.cpp` | `RobloxStudio/PairRbxDeviceDialog.cpp` |
| `PlayersDataManager.cpp` | `RobloxStudio/PlayersDataManager.cpp` |
| `PlayersDataManager.h` | `RobloxStudio/PlayersDataManager.h` |
| `PropertyItems.cpp` | `RobloxStudio/PropertyItems.cpp` |
| `PropertyItems.h` | `RobloxStudio/PropertyItems.h` |
| `QtUtilities.cpp` | `RobloxStudio/QtUtilities.cpp` |
| `QtUtilities.h` | `RobloxStudio/QtUtilities.h` |
| `RbxContent.cpp` | `RobloxStudio/RbxContent.cpp` |
| `RbxWorkspace.cpp` | `RobloxStudio/RbxWorkspace.cpp` |
| `RbxWorkspace.h` | `RobloxStudio/RbxWorkspace.h` |
| `RenderStatsItem.cpp` | `RobloxStudio/RenderStatsItem.cpp` |
| `Roblox.cpp` | `RobloxStudio/Roblox.cpp` |
| `RobloxApplicationManager.cpp` | `RobloxStudio/RobloxApplicationManager.cpp` |
| `RobloxBasicDoc.cpp` | `RobloxStudio/RobloxBasicDoc.cpp` |
| `RobloxBasicDoc.h` | `RobloxStudio/RobloxBasicDoc.h` |
| `RobloxBrowser.cpp` | `RobloxStudio/RobloxBrowser.cpp` |
| `RobloxChatWidget.cpp` | `RobloxStudio/RobloxChatWidget.cpp` |
| `RobloxChatWidget.h` | `RobloxStudio/RobloxChatWidget.h` |
| `RobloxContextualHelp.cpp` | `RobloxStudio/RobloxContextualHelp.cpp` |
| `RobloxCookieJar.cpp` | `RobloxStudio/RobloxCookieJar.cpp` |
| `RobloxCustomWidgets.cpp` | `RobloxStudio/RobloxCustomWidgets.cpp` |
| `RobloxCustomWidgets.h` | `RobloxStudio/RobloxCustomWidgets.h` |
| `RobloxDiagnosticsView.cpp` | `RobloxStudio/RobloxDiagnosticsView.cpp` |
| `RobloxDiagnosticsView.h` | `RobloxStudio/RobloxDiagnosticsView.h` |
| `RobloxDocManager.cpp` | `RobloxStudio/RobloxDocManager.cpp` |
| `RobloxDocManager.h` | `RobloxStudio/RobloxDocManager.h` |
| `RobloxFindWidget.cpp` | `RobloxStudio/RobloxFindWidget.cpp` |
| `RobloxFindWidget.h` | `RobloxStudio/RobloxFindWidget.h` |
| `RobloxGameExplorer.cpp` | `RobloxStudio/RobloxGameExplorer.cpp` |
| `RobloxGameExplorer.h` | `RobloxStudio/RobloxGameExplorer.h` |
| `RobloxIDEDoc.cpp` | `RobloxStudio/RobloxIDEDoc.cpp` |
| `RobloxIDEDoc.h` | `RobloxStudio/RobloxIDEDoc.h` |
| `RobloxInputConfigDialog.cpp` | `RobloxStudio/RobloxInputConfigDialog.cpp` |
| `RobloxKeyboardConfig.cpp` | `RobloxStudio/RobloxKeyboardConfig.cpp` |
| `RobloxKeyboardConfig.h` | `RobloxStudio/RobloxKeyboardConfig.h` |
| `RobloxMainWindow.cpp` | `RobloxStudio/RobloxMainWindow.cpp` |
| `RobloxMainWindow.h` | `RobloxStudio/RobloxMainWindow.h` |
| `RobloxMouseConfig.cpp` | `RobloxStudio/RobloxMouseConfig.cpp` |
| `RobloxMouseConfig.h` | `RobloxStudio/RobloxMouseConfig.h` |
| `RobloxNetworkAccessManager.cpp` | `RobloxStudio/RobloxNetworkAccessManager.cpp` |
| `RobloxNetworkAccessManager.h` | `RobloxStudio/RobloxNetworkAccessManager.h` |
| `RobloxNetworkReply.cpp` | `RobloxStudio/RobloxNetworkReply.cpp` |
| `RobloxObjectBrowserDoc.cpp` | `RobloxStudio/RobloxObjectBrowserDoc.cpp` |
| `RobloxObjectBrowserDoc.h` | `RobloxStudio/RobloxObjectBrowserDoc.h` |
| `RobloxPluginHost.cpp` | `RobloxStudio/RobloxPluginHost.cpp` |
| `RobloxPrizeAwarder.cpp` | `RobloxStudio/RobloxPrizeAwarder.cpp` |
| `RobloxPrizeAwarder.h` | `RobloxStudio/RobloxPrizeAwarder.h` |
| `RobloxPropertyWidget.cpp` | `RobloxStudio/RobloxPropertyWidget.cpp` |
| `RobloxPropertyWidget.h` | `RobloxStudio/RobloxPropertyWidget.h` |
| `RobloxQuickAccessConfig.cpp` | `RobloxStudio/RobloxQuickAccessConfig.cpp` |
| `RobloxQuickAccessConfig.h` | `RobloxStudio/RobloxQuickAccessConfig.h` |
| `RobloxReportView.cpp` | `RobloxStudio/RobloxReportView.cpp` |
| `RobloxRibbonMainWindow.cpp` | `RobloxStudio/RobloxRibbonMainWindow.cpp` |
| `RobloxSavingStateDialog.h` | `RobloxStudio/RobloxSavingStateDialog.h` |
| `RobloxScriptDoc.cpp` | `RobloxStudio/RobloxScriptDoc.cpp` |
| `RobloxScriptDoc.h` | `RobloxStudio/RobloxScriptDoc.h` |
| `RobloxScriptReview.cpp` | `RobloxStudio/RobloxScriptReview.cpp` |
| `RobloxSettings.cpp` | `RobloxStudio/RobloxSettings.cpp` |
| `RobloxSettings.h` | `RobloxStudio/RobloxSettings.h` |
| `RobloxSettingsDialog.cpp` | `RobloxStudio/RobloxSettingsDialog.cpp` |
| `RobloxSettingsDialog.h` | `RobloxStudio/RobloxSettingsDialog.h` |
| `RobloxStudioVerbs.cpp` | `RobloxStudio/RobloxStudioVerbs.cpp` |
| `RobloxStudioVerbs.h` | `RobloxStudio/RobloxStudioVerbs.h` |
| `RobloxTabWidget.h` | `RobloxStudio/RobloxTabWidget.h` |
| `RobloxTaskScheduler.cpp` | `RobloxStudio/RobloxTaskScheduler.cpp` |
| `RobloxTaskScheduler.h` | `RobloxStudio/RobloxTaskScheduler.h` |
| `RobloxTeamCreateWidget.cpp` | `RobloxStudio/RobloxTeamCreateWidget.cpp` |
| `RobloxTeamCreateWidget.h` | `RobloxStudio/RobloxTeamCreateWidget.h` |
| `RobloxTextOutputWidget.cpp` | `RobloxStudio/RobloxTextOutputWidget.cpp` |
| `RobloxToolBox.cpp` | `RobloxStudio/RobloxToolBox.cpp` |
| `RobloxTreeWidget.cpp` | `RobloxStudio/RobloxTreeWidget.cpp` |
| `RobloxTreeWidget.h` | `RobloxStudio/RobloxTreeWidget.h` |
| `RobloxTutorials.cpp` | `RobloxStudio/RobloxTutorials.cpp` |
| `RobloxUser.cpp` | `RobloxStudio/RobloxUser.cpp` |
| `RobloxView.cpp` | `RobloxStudio/RobloxView.cpp` |
| `RobloxView.h` | `RobloxStudio/RobloxView.h` |
| `RobloxWebDoc.cpp` | `RobloxStudio/RobloxWebDoc.cpp` |
| `RobloxWebDoc.h` | `RobloxStudio/RobloxWebDoc.h` |
| `RobloxWebPage.cpp` | `RobloxStudio/RobloxWebPage.cpp` |
| `ScopedDebugTimer.h` | `RobloxStudio/ScopedDebugTimer.h` |
| `ScriptAnalysisWidget.cpp` | `RobloxStudio/ScriptAnalysisWidget.cpp` |
| `ScriptAnalysisWidget.h` | `RobloxStudio/ScriptAnalysisWidget.h` |
| `ScriptComboBox.cpp` | `RobloxStudio/ScriptComboBox.cpp` |
| `ScriptComboBox.h` | `RobloxStudio/ScriptComboBox.h` |
| `ScriptPickerDialog.cpp` | `RobloxStudio/ScriptPickerDialog.cpp` |
| `ScriptSideWidget.cpp` | `RobloxStudio/ScriptSideWidget.cpp` |
| `ScriptSyntaxHighlighter.cpp` | `RobloxStudio/ScriptSyntaxHighlighter.cpp` |
| `ScriptTextEditor.cpp` | `RobloxStudio/ScriptTextEditor.cpp` |
| `ScriptTextEditor.h` | `RobloxStudio/ScriptTextEditor.h` |
| `SelectionHighlightAdornable.cpp` | `RobloxStudio/SelectionHighlightAdornable.cpp` |
| `ShortcutHelpDialog.cpp` | `RobloxStudio/ShortcutHelpDialog.cpp` |
| `SplineEditor.cpp` | `RobloxStudio/SplineEditor.cpp` |
| `SplineEditor.h` | `RobloxStudio/SplineEditor.h` |
| `StudioAnalytics.cpp` | `RobloxStudio/StudioAnalytics.cpp` |
| `StudioAnalytics.h` | `RobloxStudio/StudioAnalytics.h` |
| `StudioDeviceEmulator.cpp` | `RobloxStudio/StudioDeviceEmulator.cpp` |
| `StudioDeviceEmulator.h` | `RobloxStudio/StudioDeviceEmulator.h` |
| `StudioIntellesense.cpp` | `RobloxStudio/StudioIntellesense.cpp` |
| `StudioMacUtilities.mm` | `RobloxStudio/StudioMacUtilities.mm` |
| `StudioSerializerHelper.cpp` | `RobloxStudio/StudioSerializerHelper.cpp` |
| `StudioUtilities.cpp` | `RobloxStudio/StudioUtilities.cpp` |
| `UpdateUIManager.cpp` | `RobloxStudio/UpdateUIManager.cpp` |
| `UpdateUIManager.h` | `RobloxStudio/UpdateUIManager.h` |
| `UserInput.cpp` | `RobloxStudio/UserInput.cpp` |
| `UserInput.h` | `RobloxStudio/UserInput.h` |
| `UserInputUtil.cpp` | `RobloxStudio/UserInputUtil.cpp` |
| `WebDialog.cpp` | `RobloxStudio/WebDialog.cpp` |
| `WebDialog.h` | `RobloxStudio/WebDialog.h` |
| `FileWatcher.cpp` | `RobloxStudio/filewatcher/FileWatcher.cpp` |
| `FileWatcher.h` | `RobloxStudio/filewatcher/FileWatcher.h` |
| `FileWatcherImpl.h` | `RobloxStudio/filewatcher/FileWatcherImpl.h` |
| `FileWatcherLinux.cpp` | `RobloxStudio/filewatcher/FileWatcherLinux.cpp` |
| `FileWatcherOSX.cpp` | `RobloxStudio/filewatcher/FileWatcherOSX.cpp` |
| `FileWatcherWin32.cpp` | `RobloxStudio/filewatcher/FileWatcherWin32.cpp` |
| `main.cpp` | `RobloxStudio/main.cpp` |
| `ogrewidget.cpp` | `RobloxStudio/ogrewidget.cpp` |
| `ogrewidget.h` | `RobloxStudio/ogrewidget.h` |

</details>

---

## Function Reference

### 1. `QDialog`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
: QDialog(Parent,Qt::WindowTitleHint | Qt::WindowSystemMenuHint);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `:` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AddEmulationDeviceDialog.cpp:26` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes QDialog within Roblox Studio IDE. Coordinates interactions with `setAttribute, setupUi, setFixedSize, size`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `setAttribute`, `setupUi`, `setFixedSize`, `size`, `setWindowFlags`, `setText`, `QString`, `arg`, `desktop`, `physicalDpiX`, `connect`, `SIGNAL`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `QDialog`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 2. `AddEmulationDeviceDialog::closeEvent`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void AddEmulationDeviceDialog::closeEvent(QCloseEvent* event);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AddEmulationDeviceDialog.cpp:45` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Callback for closing the dialog.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `closeEvent`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `RobloxStudio/RobloxMainWindow.cpp`.

- **Alternative Implementation Files:** `RobloxStudio/RobloxMainWindow.cpp`

---

### 3. `AddEmulationDeviceDialog::onCancel`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AddEmulationDeviceDialog::onCancel();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AddEmulationDeviceDialog.cpp:49` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes onCancel within Roblox Studio IDE. Coordinates interactions with `accept`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `accept`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onCancel`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 4. `AddEmulationDeviceDialog::submitDevice`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AddEmulationDeviceDialog::submitDevice();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AddEmulationDeviceDialog.cpp:54` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes submitDevice within Roblox Studio IDE. Coordinates interactions with `device, text, desktop, physicalDpiX`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `device`, `text`, `desktop`, `physicalDpiX`, `value`, `checkState`, `Instance`, `addDevice`, `accept`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `submitDevice`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 5. `AppleCrashReporter::check`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AppleCrashReporter::check();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AppleCrashReporter.cpp:29` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes check within Roblox Studio IDE. Coordinates interactions with `applicationDirPath, settings, value, toString`.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `applicationDirPath`, `settings`, `value`, `toString`, `getReports`, `qMin`, `count`, `submitFile`, `homePath`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `check`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 6. `AppleCrashReporter::getReports`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AppleCrashReporter::getReports(QStringList& fileList);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AppleCrashReporter.cpp:50` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes getReports within Roblox Studio IDE. Coordinates interactions with `crashReportDir, homePath, entryList`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `crashReportDir`, `homePath`, `entryList`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getReports`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 7. `AppleCrashReporter::submitFile`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AppleCrashReporter::submitFile(QString fileName);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AppleCrashReporter.cpp:58` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes submitFile within Roblox Studio IDE. Coordinates interactions with `file, exists, uploadAndDeletFileAsync, GetDmpUrl`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `file`, `exists`, `uploadAndDeletFileAsync`, `GetDmpUrl`, `getBaseURL`, `toStdString`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `submitFile`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 8. `handler`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void handler(std::exception* ex, std::string file);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | `static` |
| **Source Location** | `RobloxStudio/AppleCrashReporter.cpp:67` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes handler within Roblox Studio IDE. Coordinates interactions with `remove, c_str, replace, find`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `remove`, `c_str`, `replace`, `find`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `handler`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 9. `AppleCrashReporter::uploadAndDeletFileAsync`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AppleCrashReporter::uploadAndDeletFileAsync(std::string url, std::string file);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AppleCrashReporter.cpp:79` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes uploadAndDeletFileAsync within Roblox Studio IDE. Coordinates interactions with `data, fstream, c_str, tellg`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching.
- **Memory Management:** Dynamic heap allocation via C++ operator new; Reference-counted heap object ownership (boost::shared_ptr).
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `data`, `fstream`, `c_str`, `tellg`, `seekg`, `getline`, `substr`, `size`, `find`, `replace`, `filename`, `string`.
- **External Library Dependencies:** `Boost C++ Libraries`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `uploadAndDeletFileAsync`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 10. `AuthenticationHelper::getLoggedInUserUrl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
QString AuthenticationHelper::getLoggedInUserUrl();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `QString` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:52` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes getLoggedInUserUrl within Roblox Studio IDE. Coordinates interactions with `fromStdString, BuildGenericGameUrl, getBaseURL, toStdString`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `fromStdString`, `BuildGenericGameUrl`, `getBaseURL`, `toStdString`, `ReplaceTopSubdomain`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getLoggedInUserUrl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 11. `AuthenticationHelper::verifyUserAndAuthenticate`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool AuthenticationHelper::verifyUserAndAuthenticate(int timeOutTime);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:71` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes verifyUserAndAuthenticate within Roblox Studio IDE. Coordinates interactions with `getLoggedInUserUrl, url, networkRequest, setRawHeader`.

- **Control Flow & Execution:** Conditional branching, Multi-case state dispatch, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Exception handling block (try/catch recovery).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getLoggedInUserUrl`, `url`, `networkRequest`, `setRawHeader`, `toAscii`, `Instance`, `get`, `waitForFinished`, `deleteLater`, `singleton`, `print`, `sendCounterEvent`.
- **External Library Dependencies:** `Apple WebKit / Foundation API`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `verifyUserAndAuthenticate`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 12. `AuthenticationHelper::getHttpUserId`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int AuthenticationHelper::getHttpUserId();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:158` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes getHttpUserId within Roblox Studio IDE. Coordinates interactions with `getLoggedInUserUrl, doHttpGetRequest, toInt`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getLoggedInUserUrl`, `doHttpGetRequest`, `toInt`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getHttpUserId`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 13. `AuthenticationHelper::getWebKitUserId`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int AuthenticationHelper::getWebKitUserId();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:178` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Gets user-id of the user logged into webkit layer @Returns: user-id, 0 if no user is logged in

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getLoggedInUserUrl`, `url`, `networkRequest`, `setRawHeader`, `toAscii`, `Instance`, `get`, `waitForFinished`, `error`, `userIdWebkit`, `readAll`, `toInt`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getWebKitUserId`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 14. `AuthenticationHelper::authenticateHttpLayer`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool AuthenticationHelper::authenticateHttpLayer();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:196` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes authenticateHttpLayer within Roblox Studio IDE. Coordinates interactions with `authenticationChanged, authenticationDone`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `authenticationChanged`, `authenticationDone`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `authenticateHttpLayer`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 15. `AuthenticationHelper::deAuthenticateHttpLayer`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthenticationHelper::deAuthenticateHttpLayer();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:203` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes deAuthenticateHttpLayer within Roblox Studio IDE. Coordinates interactions with `fromStdString, BuildGenericGameUrl, getBaseURL, toStdString`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `fromStdString`, `BuildGenericGameUrl`, `getBaseURL`, `toStdString`, `doHttpGetRequest`, `authenticationChanged`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `deAuthenticateHttpLayer`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 16. `AuthenticationHelper::generateAuthenticationUrl`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
QString AuthenticationHelper::generateAuthenticationUrl(const QString& authUrl, const QString& ticket);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `QString` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:220` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes generateAuthenticationUrl within Roblox Studio IDE. Coordinates interactions with `compoundStr, isEmpty, append`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `compoundStr`, `isEmpty`, `append`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `generateAuthenticationUrl`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 17. `AuthenticationHelper::authenticateWebKitFromUrlWithTicket`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int AuthenticationHelper::authenticateWebKitFromUrlWithTicket(const QString& url, const QString& ticket);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:232` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes authenticateWebKitFromUrlWithTicket within Roblox Studio IDE. Coordinates interactions with `isEmpty, doWebKitAuthentication, generateAuthenticationUrl`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `isEmpty`, `doWebKitAuthentication`, `generateAuthenticationUrl`.
- **External Library Dependencies:** `Apple WebKit / Foundation API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `authenticateWebKitFromUrlWithTicket`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 18. `AuthenticationHelper::doWebKitAuthentication`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int AuthenticationHelper::doWebKitAuthentication(const QString& url);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:247` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Authenticate the webkit layer by making a request to this url.  Follows redirects recursively. @Returns: status code of response

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `networkRequest`, `setRawHeader`, `QByteArray`, `GetBaseURL`, `c_str`, `length`, `toAscii`, `Instance`, `get`, `waitForFinished`, `deleteLater`, `statusCode`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `doWebKitAuthentication`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 19. `AuthenticationHelper::deAuthenticateWebKitLayer`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthenticationHelper::deAuthenticateWebKitLayer();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:265` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

De-authenticate the webkit layer.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `fromStdString`, `BuildGenericGameUrl`, `getBaseURL`, `toStdString`, `networkRequest`, `setRawHeader`, `toAscii`, `Instance`, `get`, `waitForFinished`, `deleteLater`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `deAuthenticateWebKitLayer`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 20. `AuthenticationHelper::authenticateWinINetFromUrlWithTicket`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
QString AuthenticationHelper::authenticateWinINetFromUrlWithTicket(const QString& url, const QString& ticket);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `QString` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:290` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Authenticate the WinINet layer by making a request to this url. @Returns: userId of authenticated user, empty if failed

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `isEmpty`, `generateAuthenticationUrl`, `doHttpGetRequest`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `authenticateWinINetFromUrlWithTicket`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 21. `AuthenticationHelper::doHttpGetRequest`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
QString AuthenticationHelper::doHttpGetRequest(const QString& str, const RBX::HttpAux::AdditionalHeaders& externalHeaders);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `QString` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:300` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes doHttpGetRequest within Roblox Studio IDE. Coordinates interactions with `toAscii, data, http, setAuthDomain`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Exception handling block (try/catch recovery).
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `toAscii`, `data`, `http`, `setAuthDomain`, `GetBaseURL`, `insert`, `begin`, `end`, `get`, `singleton`, `print`, `what`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `doHttpGetRequest`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 22. `AuthenticationHelper::validateMachine`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool AuthenticationHelper::validateMachine();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:340` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes validateMachine within Roblox Studio IDE. Coordinates interactions with `uploadMachineId, qPrintable, getBaseURL`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `uploadMachineId`, `qPrintable`, `getBaseURL`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `validateMachine`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 23. `AuthenticationHelper::eventFilter`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
bool AuthenticationHelper::eventFilter(QObject * watched, QEvent * evt);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:346` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes eventFilter within Roblox Studio IDE. Coordinates interactions with `type, Instance, cookieJar, getCookieValue`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT); Exception handling block (try/catch recovery).
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `type`, `Instance`, `cookieJar`, `getCookieValue`, `getBaseURL`, `compare`, `isEmpty`, `reloadCookies`, `deAuthenticateWebKitLayer`, `getStartPageDoc`, `refreshPage`, `RBXASSERT`.
- **External Library Dependencies:** `Apple WebKit / Foundation API`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `eventFilter`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `RobloxStudio/RobloxMainWindow.cpp`.

- **Alternative Implementation Files:** `RobloxStudio/RobloxMainWindow.cpp`

---

### 24. `AuthenticationHelper::authenticateWebKitFromHttp`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int AuthenticationHelper::authenticateWebKitFromHttp();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:384` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes authenticateWebKitFromHttp within Roblox Studio IDE. Coordinates interactions with `getHttpUserId, getBaseURL, replace, toStdString`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `getHttpUserId`, `getBaseURL`, `replace`, `toStdString`, `doHttpGetRequest`, `isEmpty`, `doWebKitAuthentication`, `onSSLErrors`, `url`, `toString`, `contains`, `ignoreSslErrors`.
- **External Library Dependencies:** `Apple WebKit / Foundation API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `authenticateWebKitFromHttp`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 25. `AuthenticationHelper::onSSLErrors`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthenticationHelper::onSSLErrors(QNetworkReply* networkReply, const QList<QSslError> & errlist);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:403` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes onSSLErrors within Roblox Studio IDE. Coordinates interactions with `url, toString, contains, ignoreSslErrors`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `url`, `toString`, `contains`, `ignoreSslErrors`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onSSLErrors`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 26. `AuthenticationHelper::authenticateUserAsync`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthenticationHelper::authenticateUserAsync(const QString& url, const QString& ticket);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:410` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes authenticateUserAsync within Roblox Studio IDE. Coordinates interactions with `isEmpty, Instance, generateAuthenticationUrl, run`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT); Exception handling block (try/catch recovery).
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `isEmpty`, `Instance`, `generateAuthenticationUrl`, `run`, `setFuture`, `cookieJar`, `getCookieValue`, `getBaseURL`, `authenticateHttpSessionAsync`, `isRunning`, `waitForHttpAuthentication`, `authenticateHttpSession`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `authenticateUserAsync`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 27. `AuthenticationHelper::authenticateHttpSessionAsync`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthenticationHelper::authenticateHttpSessionAsync(bool state);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:446` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes authenticateHttpSessionAsync within Roblox Studio IDE. Coordinates interactions with `isRunning, waitForHttpAuthentication, run, setFuture`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `isRunning`, `waitForHttpAuthentication`, `run`, `setFuture`, `authenticateHttpSession`, `getHttpRequest`, `isEmpty`, `getBaseURL`, `replace`, `networkRequest`, `setRawHeader`, `toAscii`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `authenticateHttpSessionAsync`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 28. `AuthenticationHelper::authenticateHttpSession`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool AuthenticationHelper::authenticateHttpSession(const QString& authenticationURL);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:472` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes authenticateHttpSession within Roblox Studio IDE. Coordinates interactions with `getHttpRequest, isEmpty`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getHttpRequest`, `isEmpty`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `authenticateHttpSession`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 29. `AuthenticationHelper::authenticateHttpSession`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool AuthenticationHelper::authenticateHttpSession();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:477` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes authenticateHttpSession within Roblox Studio IDE. Coordinates interactions with `getBaseURL, replace, networkRequest, setRawHeader`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `getBaseURL`, `replace`, `networkRequest`, `setRawHeader`, `toAscii`, `setCookiesFromUrl`, `Instance`, `cookieJar`, `cookiesForUrl`, `setCookieJar`, `get`, `contains`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `authenticateHttpSession`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 30. `AuthenticationHelper::deAuthenticateHttpSession`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool AuthenticationHelper::deAuthenticateHttpSession();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:523` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes deAuthenticateHttpSession within Roblox Studio IDE. Coordinates interactions with `fromStdString, BuildGenericGameUrl, getBaseURL, toStdString`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `fromStdString`, `BuildGenericGameUrl`, `getBaseURL`, `toStdString`, `getHttpRequest`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `deAuthenticateHttpSession`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 31. `AuthenticationHelper::authenticateQtWebkitSession`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool AuthenticationHelper::authenticateQtWebkitSession(const QString& authenticationUrl);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:538` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes authenticateQtWebkitSession within Roblox Studio IDE. Coordinates interactions with `getBaseURL, networkRequest, setRawHeader, toAscii`. Employs dynamic heap allocation via c++ operator new.

- **Control Flow & Execution:** Iterative loop processing, Conditional branching, Explicit result return.
- **Memory Management:** Dynamic heap allocation via C++ operator new.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT); Exception handling block (try/catch recovery).
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `getBaseURL`, `networkRequest`, `setRawHeader`, `toAscii`, `get`, `contains`, `ignoreSslErrors`, `RobloxNetworkReply`, `waitForFinished`, `statusCode`, `Instance`, `cookieJar`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `authenticateQtWebkitSession`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 32. `AuthenticationHelper::authenticateQtWebkitSession`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool AuthenticationHelper::authenticateQtWebkitSession();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:574` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes authenticateQtWebkitSession within Roblox Studio IDE. Coordinates interactions with `getHttpRequest, getLoggedInUserUrl, toInt, getBaseURL`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getHttpRequest`, `getLoggedInUserUrl`, `toInt`, `getBaseURL`, `replace`, `toStdString`, `isEmpty`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `authenticateQtWebkitSession`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 33. `AuthenticationHelper::getHttpRequest`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
QString AuthenticationHelper::getHttpRequest(const QString& urlString, const RBX::HttpAux::AdditionalHeaders& externalHeaders);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `QString` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:598` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes getHttpRequest within Roblox Studio IDE. Coordinates interactions with `lock, addHeader, GetBaseURL, begin`.

- **Control Flow & Execution:** Iterative loop processing, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Exception handling block (try/catch recovery).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `lock`, `addHeader`, `GetBaseURL`, `begin`, `end`, `get`, `toStdString`, `singleton`, `printf`, `what`, `fromStdString`.
- **External Library Dependencies:** `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getHttpRequest`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 34. `AuthenticationHelper::httpSessionAuthenticationDone`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthenticationHelper::httpSessionAuthenticationDone();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:624` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes httpSessionAuthenticationDone within Roblox Studio IDE. Coordinates interactions with `RBXASSERT, result, authenticationChanged`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `RBXASSERT`, `result`, `authenticationChanged`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `httpSessionAuthenticationDone`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 35. `AuthenticationHelper::waitForHttpAuthentication`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthenticationHelper::waitForHttpAuthentication();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:648` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes waitForHttpAuthentication within Roblox Studio IDE. Coordinates interactions with `isRunning, waitForFinished, httpSessionAuthenticationDone`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Mutates internal member state or instance properties.
- **Key Internal Calls:** `isRunning`, `waitForFinished`, `httpSessionAuthenticationDone`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `waitForHttpAuthentication`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 36. `AuthenticationHelper::waitForQtWebkitAuthentication`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthenticationHelper::waitForQtWebkitAuthentication();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthenticationHelper.cpp:660` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes waitForQtWebkitAuthentication within Roblox Studio IDE. Coordinates interactions with `isRunning, waitForFinished`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `isRunning`, `waitForFinished`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `waitForQtWebkitAuthentication`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 37. `Instance`

**Status:** 🧪 **Tested** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
AuthenticationHelper& Instance();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `AuthenticationHelper&` |
| **Modifiers** | `static` |
| **Source Location** | `RobloxStudio/AuthenticationHelper.h:21` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes Instance within Roblox Studio IDE.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

This function is exercised in **24 test case(s)**:

- **`Instance::Clone`** (`App.UnitTest/Instance.cpp:86`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK_EQUAL(count, RBX::Diagnostics::Countable&lt;RBX::Instance&gt;::getCount())`
  - **Callsite Snippet:** `int count = RBX::Diagnostics::Countable&lt;RBX::Instance&gt;::getCount();`
- **`Instance::CastTo`** (`App.UnitTest/Instance.cpp:137`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(RBX::Instance::fastDynamicCast&lt;RBX::Instance&gt;(part.get()))`, `BOOST_CHECK(!RBX::Instance::fastDynamicCast&lt;RBX::PartInstance&gt;(instance.get()))`, `BOOST_CHECK(!RBX::Instance::fastDynamicCast&lt;RBX::PartInstance&gt;(nullInstance))`, `BOOST_CHECK(inst-&gt;fastDynamicCast&lt;RBX::Instance&gt;())`, `BOOST_CHECK(!instance-&gt;fastDynamicCast&lt;RBX::PartInstance&gt;())`
  - **Callsite Snippet:** `shared_ptr&lt;RBX::PartInstance&gt; part = RBX::Creatable&lt;RBX::Instance&gt;::create&lt;RBX::BasicPartInstance&gt;();`
- **`Instance::CastToConst`** (`App.UnitTest/Instance.cpp:155`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(RBX::Instance::fastDynamicCast&lt;RBX::Instance&gt;(part.get()))`, `BOOST_CHECK(!RBX::Instance::fastDynamicCast&lt;RBX::PartInstance&gt;(instance.get()))`, `BOOST_CHECK(!RBX::Instance::fastDynamicCast&lt;RBX::PartInstance&gt;(nullInstance))`, `BOOST_CHECK(inst-&gt;fastDynamicCast&lt;RBX::Instance&gt;())`, `BOOST_CHECK(!instance-&gt;fastDynamicCast&lt;RBX::PartInstance&gt;())`
  - **Callsite Snippet:** `shared_ptr&lt;const RBX::PartInstance&gt; part = RBX::Creatable&lt;RBX::Instance&gt;::create&lt;RBX::BasicPartInstance&gt;();`
- **`Instance::SharedCastTo`** (`App.UnitTest/Instance.cpp:173`)
  - **Usage Pattern:** `Direct Assertion`
  - **Assertions Checked:** `BOOST_CHECK(RBX::Instance::fastSharedDynamicCast&lt;const RBX::Instance&gt;(part))`, `BOOST_CHECK(!RBX::Instance::fastSharedDynamicCast&lt;const RBX::PartInstance&gt;(instance))`, `BOOST_CHECK(!RBX::Instance::fastSharedDynamicCast&lt;const RBX::PartInstance&gt;(nullInstance))`
  - **Callsite Snippet:** `shared_ptr&lt;const RBX::PartInstance&gt; part = RBX::Creatable&lt;RBX::Instance&gt;::create&lt;RBX::BasicPartInstance&gt;();`

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 38. `AuthoringSettings::configureBasedOnFastFlags`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthoringSettings::configureBasedOnFastFlags();
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:267` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Configure settings after the fast flags have loaded to do any special adjustments/handling. Must be called after RBX::GlobalAdvancedSettings::singleton()-&gt;loadState() has been called.

- **Control Flow & Execution:** Conditional branching, Multi-case state dispatch, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `setEditable`, `setDragMutliplePartsAsSinglePart`, `onPropertyChanged`, `getStringValue`, `trackEvent`, `c_str`, `setDoSettingsChangedGAEvents`, `setRuntimeUndoBehavior`, `getPermissionShown`, `RBXASSERT`, `setPermissionLevelShown`, `raiseChanged`.
- **External Library Dependencies:** `G3D Graphics and Math Engine`, `OpenGL / GLES Graphics API`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `configureBasedOnFastFlags`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 39. `AuthoringSettings::onPropertyChanged`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; ⚠️ **Platform Divergent**

```cpp
void AuthoringSettings::onPropertyChanged(const RBX::Reflection::PropertyDescriptor& pDescriptor);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:280` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes onPropertyChanged within Roblox Studio IDE. Coordinates interactions with `getStringValue, trackEvent, c_str`.

- **Control Flow & Execution:** Conditional branching.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `getStringValue`, `trackEvent`, `c_str`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `onPropertyChanged`.
:::

#### Behavioral Differences Across Code Files

**Divergence Analysis:** Alternative platform-specific implementations exist in: `RobloxStudio/RobloxMainWindow.cpp`.

- **Alternative Implementation Files:** `RobloxStudio/RobloxMainWindow.cpp`

---

### 40. `AuthoringSettings::setDoSettingsChangedGAEvents`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthoringSettings::setDoSettingsChangedGAEvents(bool value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:293` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes setDoSettingsChangedGAEvents within Roblox Studio IDE.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setDoSettingsChangedGAEvents`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 41. `AuthoringSettings::setRuntimeUndoBehavior`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthoringSettings::setRuntimeUndoBehavior(RBX::ChangeHistoryService::RuntimeUndoBehavior value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:298` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes setRuntimeUndoBehavior within Roblox Studio IDE.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setRuntimeUndoBehavior`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 42. `AuthoringSettings::getPermissionShown`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
RBX::Security::Permissions AuthoringSettings::getPermissionShown() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `RBX::Security::Permissions` |
| **Modifiers** | `const` |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:303` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes getPermissionShown within Roblox Studio IDE. Coordinates interactions with `RBXASSERT`.

- **Control Flow & Execution:** Multi-case state dispatch, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Engine invariant assertion check (RBXASSERT).
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `RBXASSERT`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getPermissionShown`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 43. `AuthoringSettings::setPermissionLevelShown`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthoringSettings::setPermissionLevelShown(PermissionLevelShown value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:322` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes setPermissionLevelShown within Roblox Studio IDE. Coordinates interactions with `raiseChanged`.

- **Control Flow & Execution:** Conditional branching, Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `raiseChanged`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setPermissionLevelShown`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 44. `AuthoringSettings::getCameraKeyMoveSpeed`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
float AuthoringSettings::getCameraKeyMoveSpeed() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `float` |
| **Modifiers** | `const` |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:330` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes getCameraKeyMoveSpeed within Roblox Studio IDE.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getCameraKeyMoveSpeed`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 45. `AuthoringSettings::setCameraKeyMoveSpeed`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthoringSettings::setCameraKeyMoveSpeed(float value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:335` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes setCameraKeyMoveSpeed within Roblox Studio IDE. Coordinates interactions with `raiseChanged`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `raiseChanged`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setCameraKeyMoveSpeed`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 46. `AuthoringSettings::getCameraShiftMoveSpeed`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
float AuthoringSettings::getCameraShiftMoveSpeed() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `float` |
| **Modifiers** | `const` |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:341` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes getCameraShiftMoveSpeed within Roblox Studio IDE.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getCameraShiftMoveSpeed`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 47. `AuthoringSettings::setCameraShiftMoveSpeed`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthoringSettings::setCameraShiftMoveSpeed(float value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:346` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes setCameraShiftMoveSpeed within Roblox Studio IDE. Coordinates interactions with `raiseChanged`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `raiseChanged`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setCameraShiftMoveSpeed`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 48. `AuthoringSettings::getCameraMouseWheelMoveSpeed`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
float AuthoringSettings::getCameraMouseWheelMoveSpeed() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `float` |
| **Modifiers** | `const` |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:352` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes getCameraMouseWheelMoveSpeed within Roblox Studio IDE.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getCameraMouseWheelMoveSpeed`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 49. `AuthoringSettings::setCameraMouseWheelMoveSpeed`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthoringSettings::setCameraMouseWheelMoveSpeed(float value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:357` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes setCameraMouseWheelMoveSpeed within Roblox Studio IDE. Coordinates interactions with `raiseChanged`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `raiseChanged`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setCameraMouseWheelMoveSpeed`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 50. `AuthoringSettings::getShowDraggerGrid`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool AuthoringSettings::getShowDraggerGrid() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:363` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes getShowDraggerGrid within Roblox Studio IDE.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getShowDraggerGrid`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 51. `AuthoringSettings::setShowDraggerGrid`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthoringSettings::setShowDraggerGrid(bool value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:368` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes setShowDraggerGrid within Roblox Studio IDE. Coordinates interactions with `raiseChanged`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `raiseChanged`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setShowDraggerGrid`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 52. `AuthoringSettings::getShowHoverOver`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool AuthoringSettings::getShowHoverOver() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:374` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes getShowHoverOver within Roblox Studio IDE. Coordinates interactions with `isHoverOver`.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).
- **Key Internal Calls:** `isHoverOver`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getShowHoverOver`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 53. `AuthoringSettings::setShowHoverOver`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthoringSettings::setShowHoverOver(bool value);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:379` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes setShowHoverOver within Roblox Studio IDE. Coordinates interactions with `showHoverOver, raiseChanged`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `showHoverOver`, `raiseChanged`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setShowHoverOver`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 54. `AuthoringSettings::setHoverAnimateSpeed`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthoringSettings::setHoverAnimateSpeed(HoverAnimateSpeed speed);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:385` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes setHoverAnimateSpeed within Roblox Studio IDE. Coordinates interactions with `raiseChanged`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `raiseChanged`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setHoverAnimateSpeed`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 55. `AuthoringSettings::setBasicObjectsDisplayMode`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthoringSettings::setBasicObjectsDisplayMode(ListDisplayMode mode);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:391` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes setBasicObjectsDisplayMode within Roblox Studio IDE. Coordinates interactions with `raiseChanged`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `raiseChanged`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setBasicObjectsDisplayMode`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 56. `AuthoringSettings::setEditorFont`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthoringSettings::setEditorFont(const QFont& font);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:397` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes setEditorFont within Roblox Studio IDE. Coordinates interactions with `raiseChanged`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `raiseChanged`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setEditorFont`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 57. `AuthoringSettings::setOutputLayoutMode`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthoringSettings::setOutputLayoutMode(OutputLayoutMode mode);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:403` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes setOutputLayoutMode within Roblox Studio IDE. Coordinates interactions with `raiseChanged`.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.
- **Key Internal Calls:** `raiseChanged`.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setOutputLayoutMode`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 58. `AuthoringSettings::getLuaDebuggerEnableState`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
bool AuthoringSettings::getLuaDebuggerEnableState() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `bool` |
| **Modifiers** | `const` |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:409` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes getLuaDebuggerEnableState within Roblox Studio IDE.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getLuaDebuggerEnableState`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 59. `AuthoringSettings::setLuaDebuggerEnableState`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
void AuthoringSettings::setLuaDebuggerEnableState(bool state);
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `void` |
| **Modifiers** | None |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:414` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes setLuaDebuggerEnableState within Roblox Studio IDE.

- **Control Flow & Execution:** Direct sequential execution.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Pure computational logic or modifies passed-in parameters/references.

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `setLuaDebuggerEnableState`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---

### 60. `AuthoringSettings::getDeviceDeploymentPairingCode`

**Status:** ⚪ **Untested in Suites** &nbsp;|&nbsp; 🌐 **Cross-Platform Uniform**

```cpp
int AuthoringSettings::getDeviceDeploymentPairingCode() const;
```

| Property | Value |
| :--- | :--- |
| **Return Type** | `int` |
| **Modifiers** | `const` |
| **Source Location** | `RobloxStudio/AuthoringSettings.cpp:419` |
| **Subsystem** | `Roblox Studio IDE` |

#### How it Works Internally

Executes getDeviceDeploymentPairingCode within Roblox Studio IDE.

- **Control Flow & Execution:** Explicit result return.
- **Memory Management:** Stack-based automatic variable allocation.
- **Concurrency & Thread Safety:** Unsynchronized execution (caller must ensure thread-safety if shared).
- **Error Handling & Invariants:** Relies on standard return codes and caller validation.
- **State Mutation:** Immutable / read-only operation (const member method; does not alter object state).

#### How it is Used in Tests

*No dedicated unit test case directly exercises this function by name.*

:::note Verification Note
This function is invoked indirectly through higher-level simulation or integration workloads. To add direct test coverage, introduce a test case in `App.UnitTest` or `Base.UnitTest` asserting state changes on `getDeviceDeploymentPairingCode`.
:::

#### Behavioral Differences Across Code Files

This function maintains **identical behavior across all target platforms** (`_WIN32`, `macOS`, `iOS`, `Android`, and `Xbox Durango`). It compiles into the same binary instructions without conditional preprocessor branching.

---


:::tip Additional Functions
There are **3063 additional internal and inline functions** in this subsystem. All functions are indexed and cross-referenced in the **[Complete Function Catalog](./function-catalog.md)**.
:::

---
sidebar_position: 3
---

# FastFlags & logging

The engine has two global registries you will meet everywhere: **FastFlags** (runtime feature
toggles) and **FastLog** (log groups). Macros for both are sprinkled through every file.

## FastFlags

Declared with the `DYNAMIC_FASTFLAGVARIABLE` family of macros, e.g. straight from
`App/v8tree/Instance.cpp`:

```cpp
DYNAMIC_FASTFLAGVARIABLE(LockViolationInstanceCrash, false)
```

- The flag (`LockViolationInstanceCrash`) starts with the given default (`false`).
- `DFFlag::` / `DFInt::` / `DFString::` accesses read them at runtime.
- **Dynamic** flags can be flipped without a rebuild — historically via the settings JSONs
  the client fetched (see the [SettingsComparisonTool](../modules/tooling.md#settingscomparisontool)
  and `XboxClient/fetchfflags.py` which pulls them at build time).

The fork uses FastFlags to stage behavior changes (for example uncapping values like
`WaterWaveSize` ranges and `SetTopbarTransparency` noted in
[Project Status](../getting-started/project-status.md)).

## FastLog log groups

Logging is similarly registry-driven:

```cpp
LOGVARIABLE(InstanceTreeManipulation, 0)   // from Instance.cpp

LOGGROUP(TaskSchedulerInit)                // from TaskScheduler.h
LOGGROUP(TaskSchedulerRun)
LOGGROUP(TaskSchedulerFindJob)
```

- `LOGVARIABLE(name, defaultVerbosity)` declares a runtime-tunable log channel.
- `LOGGROUP(name)` groups static log categories.
- `App/v8datamodel/FastLogSettings.cpp` exposes the log/flag state through reflection so
  Studio's settings UI can inspect it; `DebugSettings.cpp` does the same for debug settings.

## Conventions when adding flags

1. Declare the flag/log variable in exactly one translation unit, near first use.
2. Give it a conservative default (off / 0).
3. Remember flags are process-global — server (RCC) and client see independent values.
4. For script-visible behavior changes, pair the flag with reflection-visible settings where
   it makes sense.

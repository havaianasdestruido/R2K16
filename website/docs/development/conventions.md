---
sidebar_position: 5
---

# Coding conventions

Patterns to follow when contributing. The tree is consistent about these — new code that
matches them reads as "native".

## Namespaces & types

- Everything engine-side lives in `RBX::`. Lua bindings wrap it in the `lua` namespaces
  (`Lua::`).
- Classes are `PascalCase`; members carry an `m`-prefix or trailing underscore depending on
  subsystem — follow the file you edit.
- Smart pointers: **Boost** (`boost::shared_ptr`, `scoped_ptr`) in the engine;
  `std::` appears mostly in vendored code. `Base/include/rbx/boost.hpp` is the canonical
  include.

## Reflection-driven everything

Scriptable surface, Studio UI and serialization come from the reflection descriptors. Pattern
for a new property/method — mirror `Instance.cpp`:

```cpp
REFLECTION_BEGIN();  // or REFLECTION_BEGIN_NO_LUA()

Reflection::PropDescriptor<MyClass, float> MyClass::propSpeed(
    "Speed", category_Behavior,
    &MyClass::getSpeed, &MyClass::setSpeed,
    Reflection::PropertyDescriptor::SCRIPTING);

static Reflection::BoundFuncDesc<MyClass, void(std::string)> func_setSpeed(
    &MyClass::setSpeedLua, "SetSpeed", "speed", Security::None);

REFLECTION_END();
```

Include a `Security::` level deliberately. Register deprecated names as duplicate descriptors
(see the lowercase legacy bindings in `Instance.cpp`).

## Instance lifecycle

- New DataModel participants derive from `RBX::Instance` (usually via a mid-level base like
  `PartInstance` or `GuiObject`).
- Services derive from `Service` (`App/v8tree/Service.cpp`) and are registered with the
  DataModel's service list.
- Override serialization hooks rather than inventing side files when data belongs to the
  place.

## Threading

No ad-hoc threads. Recurring work = a `TaskScheduler::Job` with declared arbiter exclusivity
(see [Jobs & the TaskScheduler](../architecture/jobs-and-scheduler.md)). Shared mutable state
goes through `Base/rbx/ThreadSafe` primitives or staging copies.

## Includes

- Each `.cpp` starts with `#include "stdafx.h"` (precompiled header) — except libraries
  without PCH.
- Include paths use the virtual roots: `"V8Tree/Instance.h"`, `"util/standardout.h"`,
  `"rbx/TaskScheduler.h"` — configured through the project include dirs (`App/include`,
  `Base/include`, …).
- Include hygiene is enforced by the `IncludeChecker` tool
  ([Tooling](../modules/tooling.md#includechecker)).

## Platform code

Divergent code goes in per-platform directories (`Base/rbx/{Win,Unix,Darwin,Android,Durango}/`,
`App/util/Android/`, `Win/` for launcher code) rather than `#ifdef` forests when the
implementation is substantial. Small forks (`#ifdef _WIN32`) are fine in place.

## FastFlags & logging

Declare with `DYNAMIC_FASTFLAGVARIABLE` / `LOGVARIABLE` near first use, default-off —
see [FastFlags & logging](./fastflags-logging.md).

## Style details

- Braces on their own line (Allman), tabs in most engine files.
- One class per file, file named after the class.
- `.cpp` next to its `.vcxproj`; public header mirrored under `include/` with the virtual
  path (e.g. `App/include/V8Tree/Instance.h`).

---
sidebar_position: 3
---

# Base — foundations

**Path:** `Base/` · **Project:** `Base.vcxproj` / `Base.xcodeproj` / `CMakeLists.txt` ·
**Status:** ✅ builds

`Base` is the low-level library everything else stands on. It deliberately knows nothing about
Roblox concepts — it is infrastructure.

## Layout

```
Base/
├── include/            # Public headers: rbx/*.h (TaskScheduler, Declarations, …), util/
├── rbx/                # Core implementation
│   ├── TaskScheduler.cpp / .Job.cpp / .Thread.cpp   # the scheduler
│   ├── Profiler.cpp, ProcessPerfCounter.cpp         # profiling
│   ├── Memory.cpp, ThreadSafe.cpp, CEvent.cpp       # memory & synchronization
│   ├── Time.cpp, MathUtil.cpp, Signal.cpp           # time, math, signals
│   ├── Crypt.cpp                                      # crypto helpers
│   ├── boost.cpp                                      # Boost glue
│   ├── Android/ Darwin/ Durango/ Unix/ Win/          # per-platform sources
│   └── Tasks/                                         # task helpers
├── util/               # General utilities
├── RbxAssert.cpp       # Assert & fatal-error machinery
├── RbxFormat.cpp       # printf-style formatting helpers
├── cpucount.cpp        # CPU core detection
└── HardwareInfo.cpp    # CPU/GPU/OS capability probing
```

## Notable pieces

### The TaskScheduler

The heart of the engine's threading model — a singleton scheduling `Job`s onto worker
`Thread`s with `Arbiter`-declared exclusivity. Full write-up in
[Jobs & the TaskScheduler](../architecture/jobs-and-scheduler.md).

### `RbxAssert`

The project-wide assertion/debug-break entry points; engine code includes `RbxAssert.h`
everywhere instead of `<assert.h>`.

### Platform layer

`Base/rbx/{Win,Unix,Darwin,Android,Durango}/` implement the OS-specific parts (threads,
events, crypto, process perf counters). The engine above stays platform-agnostic; this is the
seam where Windows/POSIX/Mac/Xbox diverge.

### Diagnostics

- `Profiler.cpp` + `ProcessPerfCounter.cpp` — sampling & OS counters
- `HardwareInfo.cpp` — feeds `RenderCaps` (see [Rendering](../architecture/rendering.md))
- `cpucount.cpp` — sizes the scheduler's thread pool

## Related

- `Base.UnitTest*` test the library — see [Testing](./testing.md).
- `rbx/boost.cpp` and the `rbx/boost.hpp` header adapt the bundled Boost version to the
  engine's expectations (see [Libraries](./libraries.md)).

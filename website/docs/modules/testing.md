---
sidebar_position: 12
---

# Testing

The tree carries several generations of test infrastructure: C++ unit-test libraries,
simulation/API test rigs, and C# service tests.

## Unit test projects

| Project | Notes |
| --- | --- |
| `App.UnitTest/` + `App.UnitTest.Lib/` + `App.UnitTest.Run/` | Engine-level unit tests. `App.UnitTest.Lib` contains `DataModelFixture.cpp` and `Performance.cpp` fixtures. ❌ Not building yet |
| `Base.UnitTest/` + `Base.UnitTest.Lib/` + `Base.UnitTest.Run/` | Foundation tests; the `.Lib` includes **TeamCity integration** (`teamcity_messages.cpp`, `teamcity_boost.cpp`) so CI can consume Boost.Test results. ❌ Not building yet |

`*.Run` projects are the thin executables that host the `.Lib` test suites; `*.vsmdi` files at
the repo root (`Roblox.Test.vsmdi`) are Visual Studio test metadata.

## `RobloxTest/` — the big simulation & API rig ❌ (not building yet)

A C++ executable (`Tests.cpp`, `main.cpp`, `stdafx.h`) plus categorized suites:

```
RobloxTest/
├── Tests.cpp / main.cpp          # Rig entry
├── Tests/                        # Core tests
├── Scripts/                      # Lua-driven tests
├── LuaApi/                       # Lua API conformance tests
├── MultiPlayerTests/             # Client/server scenarios
├── PhysicsTests/ (+ PhysicsTestsLong/, PhysicsQuickTests/, UnstablePhysicsTests/)
├── PGS/                          # Projected Gauss-Seidel solver tests
├── DPhysicsTests/ (+ DPhysicsTestsManual/)  # "DPhysics" (distributed?) physics scenarios
├── BulletPhysicsTests/ / BulletPhysicsOffTests/   # Simulation with/without Bullet
└── PerformanceTests/             # Perf benchmarks
```

Companion run-project stubs exist at the root: `RobloxTest.Run/`,
`RobloxTest.MultiPlayerTest.Run/`, `RobloxTest.PhysicsTests.Run/`,
`RobloxTest.PhysicsPerfTest.Run/`.

## `Roblox.Test/` & `RobloxTest` friends

`Roblox.Test/` is another aggregate test project; `RbxTestHooks/` (✅ builds) provides the
hooks tests inject into engine binaries.

## Service tests (C#)

- **`RCCService.Test/`** — start/stop RCC instances, run Lua scripts on them, SOAP stress
  tests, multiplayer server/client scenarios (`TestRBXLFiles/` fixtures).
- **`RCCService.Thumb.Test/`** — thumbnail rendering through RCC.
- **`SimulationTestUtility/`** — shared utility for simulation tests (also listed under
  [Tooling](./tooling.md)).

## Mobile tests

- **`Android/RobloxAndroidTests/`** — instrumented Android tests.
- **`iOS/ROBLOXTests/`** and **`iOS/AutomatedTesting/`** — iOS test targets.

## Status & workflow

Per the README, the unit-test projects and `RobloxTest` are on the *not building* list —
repairing them is an explicit goal of the fork (see
[Project Status](../getting-started/project-status.md)). The Windows CI workflow
([CI / CD](../development/ci.md)) currently runs *static analysis* over the CMake build rather
than executing these suites.

---
sidebar_position: 7
---

# App.BulletPhysics — embedded Bullet

**Path:** `App.BulletPhysics/` · **Project:** `App.BulletPhysics.vcxproj` /
`App.BulletPhysics.xcodeproj` / `CMakeLists.txt` · **Status:** ✅ builds

A vendored distribution of the open-source **Bullet Physics** engine, integrated into the
engine's physics stack for advanced collision shapes and simulation features.

```
App.BulletPhysics/
├── BulletCollision/      # Broadphase/narrowphase collision detection
├── BulletDynamics/       # Rigid body dynamics, constraints
├── BulletMultiThreaded/  # Parallel pipelines (Posix/Spu/Win32)
├── BulletSoftBody/       # Soft body simulation
├── MiniCL/               # Embedded OpenCL-like compute
├── LinearMath/           # Math library
├── vectormath/           # Sony's vectormath
├── Extras/               # Auxiliary tools
├── btBulletCollisionCommon.h / btBulletDynamicsCommon.h / Bullet-C-Api.h
└── stdafx.h
```

## How the engine uses it

`App/v8world` contains dedicated integration points — `BulletContact.cpp`,
`BulletShapeContact.cpp`, `BulletShapeCellContact.cpp`, `BulletGeometryPoolObjects.cpp` — that
pair Bullet shapes with the homegrown voxel/kernel world, and `App/v8kernel`'s
`BulletShapeConnectors.cpp` wires them into the kernel. The `RobloxTest` suite has explicit
`BulletPhysicsTests` / `BulletPhysicsOffTests` folders to run the simulation with and without
Bullet.

Upgrading Bullet to a modern release is a stated roadmap goal
([Roadmap](../reference/roadmap.md#physics)).

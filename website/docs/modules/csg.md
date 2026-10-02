---
sidebar_position: 6
---

# CSG — solid geometry

**Path:** `CSG/` · **Project:** `CSG.vcxproj` / `CSG.xcodeproj` · **Status:** ✅ builds

Constructive solid geometry — the *Union* / *Negate* / *Subtract* operations on parts.

```
CSG/
├── CSGKernel.cpp / CSGKernel.h   # Engine-facing kernel API
├── sgCore/                       # Vendored sgCore solid-geometry library
├── CSG.vcxproj (+ .filters)      # Visual Studio project
└── CSG.xcodeproj                 # Mac project
```

## How it fits together

- Studio commands (`RobloxStudio/CSGOperations.cpp`) invoke the kernel with the selected parts.
- `CSGKernel` performs the boolean operations using **sgCore** and produces renderable
  geometry.
- Results become `CSGMesh` instances in the DataModel; `CSGDictionaryService` deduplicates
  them so repeated operations don't bloat place files.
- Physics for the results flows through `App/v8world`'s shape contacts.

Architecture overview: [Terrain & CSG](../architecture/terrain-and-csg.md#csg--constructive-solid-geometry-csg).

---
sidebar_position: 5
---

# FAQ

### What *is* R2K16 exactly?

A community-maintained fork of the 2016 Roblox engine source code (client, Studio, and the RCC
hosting service), with the goal of polishing it toward parity with the modern Roblox Studio
engine. Maintained by [@havaianasdestruido](https://github.com/havaianasdestruido).

### Where did the source come from?

A public re-upload that circulated on `git.rip` (`exconfidential/roblox`). It is not an
official release by Roblox. Use it as an educational/archival artifact; check the repository
`LICENSE` and your local laws before redistributing.

### Can I play on Roblox with it?

No. Authentication, matchmaking, asset and settings services all point at 2016-era Roblox
infrastructure that no longer exists. You can build and run Studio, a local player, and local
servers (RCCService) yourself.

### Why does building require *two* Visual Studio versions?

The projects target the VS2015 `v140_xp` toolset (with its XP-compatible runtime and the
matching Qt 4.8.5 build), while modern machines use VS2019 as the host IDE. See
[Building on Windows](../getting-started/building-windows.md).

### Why does the Qt build fail on purpose?

The bundled Qt 4.8.5 only builds partially — but far enough to produce everything the engine
links against. The README documents this explicitly.

### What's the difference between `voxel` and `voxel2`?

Generation 1 (blocky cell terrain) and generation 2 (2015-era smooth terrain with materials
and meshing). See [Terrain & CSG](../architecture/terrain-and-csg.md).

### Why is there a whole Bullet Physics in the tree?

The engine integrates Bullet for advanced collision shapes alongside its homegrown kernel and
solver; `RobloxTest` runs suites with Bullet on and off. See
[Physics](../architecture/physics.md) and [App.BulletPhysics](../modules/bullet.md).

### What are the "557 issues"?

Security/code-quality findings from the GitHub scanning workflows (MSVC analysis, Semgrep,
OSV-Scanner, Scorecard) tracked in the README. See [CI/CD](../development/ci.md).

### The README mentions PRs — can I contribute?

Yes — the maintainer states pull requests for fixes are accepted. Read
[Development](../development/index.md) first, especially
[Conventions](../development/conventions.md).

### How do I build the docs site?

```bash
cd website && npm install && npm start
```

Details: [Maintaining the docs site](../development/docs-site.md).

### I found a bug in these docs

The docs live in `website/docs/` — PRs welcome, or open an issue. The
[repo map](./repo-map.md) and [module pages](../modules/index.md) are the best places to
report inaccuracies.

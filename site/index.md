---
layout: home
---

## What is R2K16?

**R2K16** is a modded fork of the **2016 Roblox engine source code** (the base
originates from the [git.rip dump](https://git.rip/exconfidential/roblox/roblox)).
The project adjusts, adapts and polishes the engine so it can stand next to the
modern **Roblox Studio** engine.

- **Fixed & modernized** — the original 2016 codebase with ongoing fixes and
  adjustments layered on top.
- **Fully documented** — architecture deep-dives, a reference page for every
  module in the repository, and step-by-step build guides.
- **Buildable today** — Windows builds via Visual Studio 2019 + the v140_xp
  toolset, plus a CMake-based flow.

## Explore the docs

| Section | Contents |
| --- | --- |
| **[Getting started]({{ '/docs/getting-started/' | relative_url }})** | Prerequisites, building on Windows, CMake builds, project status |
| **[Architecture]({{ '/docs/architecture/' | relative_url }})** | Instance tree, DataModel, job pipeline, scripting, physics, rendering, networking, serialization, terrain & CSG |
| **[Modules]({{ '/docs/modules/' | relative_url }})** | A reference page for every top-level project in the repository |
| **[Reference]({{ '/docs/reference/' | relative_url }})** | Repository map, glossary, roadmap, troubleshooting, FAQ |

## Building the engine

Windows builds need **Visual Studio 2019** and the **Visual Studio 2015 build
tools (v140_xp)**, plus locally built Boost and Qt libraries — see the
[Windows build guide]({{ '/docs/getting-started/building-windows/' | relative_url }}).
A [CMake build]({{ '/docs/getting-started/building-cmake/' | relative_url }})
is also available.

## Get involved

Fixes and improvements are welcome — pull requests are being accepted. If a
build breaks or assets (`.png`, `.svg`, …) misbehave, open an issue.

- [GitHub repository](https://github.com/havaianasdestruido/R2K16)
- [Issue tracker](https://github.com/havaianasdestruido/R2K16/issues)
- [Project roadmap]({{ '/docs/reference/roadmap/' | relative_url }})

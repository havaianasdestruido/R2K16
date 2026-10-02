---
sidebar_position: 1
---

# Development

Practices and infrastructure for changing the codebase:

1. [CI / CD](./ci.md) — the GitHub Actions pipelines guarding the repo
2. [FastFlags & logging](./fastflags-logging.md) — runtime feature toggles and log groups
3. [Security model](./security.md) — API security, VMProtect, script signing, hardening
4. [Coding conventions](./conventions.md) — patterns used across the C++ tree
5. [Maintaining the docs site](./docs-site.md) — this website

## The golden rules

- **Match the era.** This is a 2016 codebase: prefer the existing idioms (Boost smart
  pointers, `RBX` namespace, reflection macros) over modern C++ features unless a change is
  specifically about modernizing. The fork deliberately tracks *some* modernization (VC++ 2019
  compilation, 64-bit) as roadmap items.
- **Register everything through reflection.** New scriptable properties/methods/events belong
  in the reflection descriptors, or they won't exist for Studio, serialization or Lua.
- **Jobs, not threads.** New recurring work should be a `TaskScheduler::Job` with proper
  arbiter exclusivity, never an ad-hoc thread.
- **Keep the checklist current.** When a project starts building or a feature lands, update
  the README *Extras* checklist and [Project Status](../getting-started/project-status.md).
- **PRs welcome** — the maintainer accepts fix PRs (see the README warning section).

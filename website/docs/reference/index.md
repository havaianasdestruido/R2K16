---
sidebar_position: 1
---

# Reference

Quick-lookup material for working on and with the R2K16 codebase.

| Page | Contents |
| --- | --- |
| [**Repository map**](./repo-map.md) | Every top-level file and folder, annotated |
| [**Glossary**](./glossary.md) | Engine, platform and fork terminology (DataModel, RCC, PGS, FastFlags, Durango…) |
| [**Roadmap**](./roadmap.md) | The fork's feature plans, transcribed from the README |
| [**Troubleshooting**](./troubleshooting.md) | Common build/runtime failures and their fixes |
| [**FAQ**](./faq.md) | Frequently asked questions |


## FAQ

### Which reference should I consult first?

Use the repository map to locate code, the glossary for unfamiliar terms, and troubleshooting for build or runtime symptoms. The roadmap describes plans, not guaranteed current behavior.

### How can I investigate this in the repository?

From the repository root, search the relevant tracked files for a starting point (results are leads, not proof of behavior):

```bash
git grep -n -i -F -- 'build' -- README.md
```

Read the surrounding implementation and callers, and check relevant tests before making changes. A search may return no matches when terminology or tracked files change.

## Suggested reading order for newcomers

1. [Introduction](../intro.md)
2. [Getting Started](../getting-started/index.md) — especially the
   [overview](../getting-started/index.md#the-30-second-version)
3. [Architecture overview](../architecture/index.md)
4. Keep the [Repository map](./repo-map.md) open in a tab as you browse the source.

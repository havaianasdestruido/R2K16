---
sidebar_position: 2
---

# CI / CD

**Path:** `.github/workflows/` (+ `.github/labeler.yml`)

The repository runs a security-and-hygiene oriented GitHub Actions suite. There is **no
compile-and-test pipeline** yet (the unit-test projects don't build — see
[Project Status](../getting-started/project-status.md)); what exists today:

| Workflow | File | What it does |
| --- | --- | --- |
| **Microsoft C++ Code Analysis** | `msvc.yml` | On push/PR to `main` (and weekly): checks out, configures CMake on `windows-latest` with `-DCMAKE_POLICY_VERSION_MINIMUM=3.5`, runs MSVC static analysis and uploads **SARIF** results to GitHub code scanning |
| **Semgrep** | `semgrep.yml` | Semgrep SAST scanning on push/PR |
| **OSV-Scanner** | `osv-scanner.yml` | Scans dependencies for known vulnerabilities (OSV database) via the reusable Google action (v1.7.1) |
| **Scorecard supply-chain security** | `scorecard.yml` | OpenSSF Scorecard for supply-chain hygiene |
| **Labeler** | `label.yml` + `labeler.yml` | Auto-labels PRs by changed paths |
| **Mark stale issues and pull requests** | `stale.yml` | Stale bot |
| **sync to codeberg** | `sync.yml` | Mirrors the repo to Codeberg |


## FAQ

### Does the documentation deployment prove the engine builds?

No. A docs build validates the website, not the native engine, its platform dependencies or runtime behavior. Inspect each workflow and its jobs before interpreting a green result.

### How can I investigate this in the repository?

From the repository root, search the relevant tracked files for a starting point (results are leads, not proof of behavior):

```bash
git grep -n -i -F -- 'run:' -- .github/workflows
```

Read the surrounding implementation and callers, and check relevant tests before making changes. A search may return no matches when terminology or tracked files change.

## The ~557 "issues"

The README tracks *"Fix all 557 'issues' and stuff scanned by Github"* — these are findings
from the SARIF/semgrep/OSV pipelines above, visible in the repo's **Security → Code scanning**
tab. Triage them there; each workflow's results upload with `security-events: write`.

## Adding a build pipeline

When the unit-test projects build again, the natural next step is a workflow that:

1. Configures CMake (`-DCMAKE_POLICY_VERSION_MINIMUM=3.5` — see
   [Building with CMake](../getting-started/building-cmake.md))
2. Builds the ✅ module set
3. Runs `RobloxTest` / `*.UnitTest.Run` executables, publishing results as artifacts

The `Base.UnitTest.Lib` TeamCity integration (`teamcity_messages.cpp`) shows how the original
team consumed Boost.Test output from CI.

## Docs deployment

A dedicated workflow builds and publishes **this documentation site** to GitHub Pages —
configuration and usage are described in
[Maintaining the docs site](./docs-site.md#deployment-github-pages).

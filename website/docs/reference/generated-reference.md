---
title: Generated code reference
---

import Link from "@docusaurus/Link";

<Link to="/code-reference">Open the generated code reference</Link>.

The Python generator scans **Git-tracked** source files, including vendored code, and extracts recognized function definitions with tree-sitter. The browser groups definitions by project (and by subdirectory in `Library`); filter by name or path, then select a result to see its signature, source range, structural hints, potential test calls, and same-name definitions. Source links point to the indexed commit, not a moving branch. A local build with uncommitted edits may therefore link to older code.

## Interpretation and scope

- Supported extensions are C, C++ (including headers and `.ipp`), Python, Lua, JavaScript, C#, and Java; the manifest lists the exact extensions. Other languages, generated/untracked files, macros, declarations without bodies, anonymous functions, language constructs the parser does not recognize, and some definitions in files with syntax errors are not indexed. C headers are parsed as C++. Preprocessor conditions are not evaluated. Parsing errors are counted per file, not repaired.
- The signature and body hints are extracted mechanically: recognized control flow and up to 30 distinct call names. They are a starting point, **not** a complete explanation of behavior. Read the linked implementation and surrounding code.
- Test uses are calls with the same spelling in paths containing `test` or `spec` (case-insensitive). They are not resolved symbols, may be unrelated or non-test helpers, and can miss indirect, macro-based, or dynamically dispatched uses. No matches does not mean untested. Lists show at most 100 locations.
- Comparisons group definitions by unqualified name, not type, namespace or overload. The body fingerprint collapses whitespace only; differing fingerprints indicate textual differences, not necessarily behavioral differences. Equal fingerprints do not prove equivalent behavior. Inspect the source and platform/configuration guards.

## Regeneration

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r website/scripts/requirements.txt
python website/scripts/generate_reference.py
cd website && npm ci && npm run build
```

Generated JSON under `website/static/generated/` is ignored by Git and is recreated in Pages CI on every push to `main`, including source and test changes. The full repository includes substantial third-party code, so generation can take several minutes and hundreds of megabytes. The generator uses tracked file contents from the checkout and overwrites its own shards on each run. It does not run tests or infer runtime behavior. See the [CI guide](../development/ci) for test workflows.

---
sidebar_position: 4
---

# Security model

The 2016 engine had layered defenses; this fork keeps them (and adds CI scanners on top).
This page is a map, not an audit — and remember the usual disclaimer: this is *leaked,
modded* source, so treat any security property as educational.

:::danger Not production software

Authentication, telemetry, patching and signing in this tree target 2016-era Roblox
infrastructure that no longer exists. Do not expose binaries built from this repo to untrusted
networks.

:::

## Layers

### 1. API security (scripting permissions)

Every reflected binding carries a `Security::` context
(`App/include/security/ApiSecurity.h`):

```cpp
static Reflection::BoundFuncDesc<Instance, bool(std::string)> func_isA(
    &Instance::isA, "IsA", "className", Security::None);
```

`SecurityContext.cpp` evaluates who may call what (game scripts vs. plugins vs. CoreScripts vs.
Studio). `FuzzyTokens.cpp` detects near-miss names of protected globals to defeat
obfuscation-style access attempts.

### 2. Script signing {#script-signing}

CoreScripts are signed (**`ScriptSigner/`**) and converted
(**`CoreScriptConverter2/`**) so the runtime can reject tampered engine scripts
(see [Scripting](../architecture/scripting.md#corescripts-and-signing)).

### 3. Binary hardening (VMProtect & friends)

- **VMProtect SDK** (`Library/VMProtect/`, `VMProtectSDK.h` included by `Instance.cpp` and
  other hot files) — marks code regions for the packer.
- `App/security/JunkCode.cpp`-style junk insertion helpers.
- Client hooks: `WindowsClient/functionHooks.cpp`, `robloxHooks.cpp`,
  `RobloxGoldenHashPatcher`, `Crypt.cpp`, `RandomPadding.cpp`; `Win/CheckDbg` (anti-debug),
  `Win/sitelock.h` (URL allow-listing for the embedded web view).
- Network payload encryption: `Network/DataBlockEncryptor.cpp` over vendored **Rijndael**.

### 4. Host hardening (RCCService)

`RCCService/OperationalSecurity.cpp/.h` locks down the hosting service — least-privilege
runtime, restricted process tokens. The original service ran arbitrary user games, so the
attack surface was the whole Lua API; the security contexts above are the primary containment.

### 5. CI scanning (this fork's addition)

Semgrep, MSVC static analysis with SARIF upload, OSV-Scanner for dependencies and OpenSSF
Scorecard — see [CI / CD](./ci.md). The README tracks ~557 findings to work through.

## Reporting

Use GitHub issues/PRs on the fork. The maintainer accepts fix PRs.

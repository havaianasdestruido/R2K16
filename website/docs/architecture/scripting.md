---
sidebar_position: 5
---

# Scripting (Lua)

*Where:* `App/script/`, `App/Lua-5.1.4/`, `App/include/script/`, `App/include/lua/`

The engine embeds **Lua 5.1.4** — the full interpreter source is vendored in `App/Lua-5.1.4/`
(only `src/` is used). All gameplay, Studio tooling and CoreScripts run on it.

## The VM layer

| File | Role |
| --- | --- |
| `ScriptContext.cpp` | The `ScriptContext` service: creates and manages Lua VMs, runs scripts |
| `LuaVM.cpp`, `LuaVMClient.cpp`, `LuaVMServer.cpp`, `LuaVMDummy.cpp` | VM flavor per context — client, server, and "dummy" (headless/no-op) VMs |
| `LuaLibrary.cpp`, `LuaCoreFunctions.cpp` | Base libraries and global functions injected into every VM |
| `LuaMemory.cpp` | Memory accounting per VM |
| `ThreadRef.cpp` | Cross-VM thread references (coroutine handling) |
| `ScriptStats.cpp`, `LuaSettings.cpp` | VM statistics & settings |

## The bridge to Instances

The magic that makes `workspace.Part.BrickColor = ...` work:

- **`LuaInstanceBridge`** (`LuaInstanceBridge.cpp`) maps `RBX::Instance` to a Lua userdata —
  property reads/writes go through the [reflection](./instance-tree.md#the-reflection-system)
  descriptors.
- **`LuaSignalBridge`** connects reflected `Event`s to Lua functions — `Touched:connect(fn)`.
- **`LuaArguments`** marshals C++ ↔ Lua values; `LuaAtomicClasses` exposes small value types
  (`Vector3`, `CFrame`, `Color3`…) to scripts.
- **`LuaEnum`** exposes engine enums.
- **`LuaBridge`/`luaStubs*.h`** (`App/include/lua/`) — generated binding stubs.

## Script objects

| Class | File | Meaning |
| --- | --- | --- |
| `LuaSourceContainer` | `LuaSourceContainer.cpp` | Common base: anything that holds Lua source |
| `Script` | `Script.cpp` | Classic script (Legacy/RunContext behavior of the era) |
| `LocalScript` flavor | via `Script` + context | Client-side scripts |
| `ModuleScript` | `ModuleScript.cpp` | `require()`-able modules |
| `CoreScript` | `CoreScript.cpp` | Engine-internal scripts (see below) |

`DebuggerManager.cpp` implements the script debugger (server-side; Studio's debug UI is the
client — `RobloxStudio/DebuggerClient.cpp`). `ScriptAnalyzer.cpp` performs static checks on
script source.

## Security contexts

Every reflected binding carries a `Security::` level (`App/include/security/ApiSecurity.h`,
`SecurityContext.cpp`). The engine also fingerprints "fuzzy" API names (`FuzzyTokens.cpp`) to
catch typo-squatting of protected globals. See [Security](../development/security.md) for the
full model.

## CoreScripts and signing

The engine itself is partly written in Lua. `content/scripts/` ships the engine's scripts:

```
content/scripts/
├── CoreScripts/            # client-side engine scripts
├── ServerCoreScripts/      # server-side engine scripts
├── Modules/                # shared Lua modules
├── StarterScript.lua       # client bootstrap
├── ServerStarterScript.lua # server bootstrap
└── LoadingScript.lua       # loading screen script
```

CoreScripts are **not** meant to be editable by users, and the original Roblox shipped them
signed. Two repo tools participate in that pipeline:

- **`CoreScriptConverter2/`** — compiles/converts CoreScript sources into the engine's
  embedded format.
- **`ScriptSigner/`** — signs scripts so the runtime can verify their integrity.

See [Tooling](../modules/tooling.md#scriptsigner).

## Where scripts come from in Studio

The `StarterPlayer`/`StarterGui`-style bootstrap of this era runs
`StarterScript.lua` on the client and `ServerStarterScript.lua` on the server; those scripts
then set up the standard gameplay environment users expect.

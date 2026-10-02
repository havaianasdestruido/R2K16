---
sidebar_position: 2
---

# Instance tree & reflection

*Where:* `App/v8tree/`, `App/reflection/`, headers under `App/include/V8Tree/` and
`App/include/reflection/`

Everything in a Roblox game is a node in one tree. The node type is `RBX::Instance`.

## `RBX::Instance`

`App/v8tree/Instance.cpp` (header: `V8Tree/Instance.h`) implements the base class every game
object derives from — `Part`, `Decal`, `Script`, `Workspace`, `Humanoid`, …

Core responsibilities:

- **Tree membership** — parent/child links, `getChildren`, name-based lookup
  (`FindFirstChild`, `IsA`, …) — the methods you know from the Lua API are bound directly on
  this class.
- **Lifecycle** — `Clone`, `Destroy`/`Remove`, archivability, locking.
- **Reflection registration** — exposes its scripting surface (see below).
- **Serialization hooks** — knows how the XML/binary serializers visit it
  (`V8Xml/Serializer.h`).
- **Change notification** — property and ancestry changes propagate to listeners
  (adornments, replication, the Studio property grid).

Related primitives in `App/v8tree/`:

| File | Purpose |
| --- | --- |
| `Instance.cpp` | The base class (reflection registration of `Instance` itself) |
| `Property.cpp` | Generic property values flowing through reflection |
| `Verb.cpp` | "Verbs" — editor commands/actions (insert, delete, group…) |
| `Service.cpp` | Base class for DataModel services |
| `EnumProperty.cpp` | Enumerated property support |

## The reflection system

Reflection lives in `App/reflection/` (`reflection_object.cpp`, `reflection_property.cpp`,
`reflection_function.cpp`, `Event.cpp`, `Callback.cpp`, `type.cpp`). It is the **single source
of truth** for an object's scripting & editing surface.

A typical registration, from `Instance.cpp`:

```cpp
REFLECTION_BEGIN();

Reflection::PropDescriptor<Instance, bool> Instance::propArchivable(
    "Archivable", category_Behavior,
    &Instance::getIsArchivable, &Instance::setIsArchivable,
    Reflection::PropertyDescriptor::SCRIPTING);

static Reflection::BoundFuncDesc<Instance, bool(std::string)> func_isA(
    &Instance::isA, "IsA", "className", Security::None);

static Reflection::BoundFuncDesc<Instance, shared_ptr<Instance>(std::string, bool)>
    findFirstChild(&Instance::findFirstChildByName2, "FindFirstChild",
                   "name", "recursive", false, Security::None);
```

What this buys the engine:

- **The Lua API** — `LuaInstanceBridge` (see [Scripting](./scripting.md)) binds reflected
  properties/methods/events into the Lua VM automatically. Deprecations are expressed as
  duplicate descriptors (note the lowercase `archivable`/`clone`/`remove` legacy bindings).
- **Security levels** — every descriptor carries a `Security::` context (e.g. `Security::None`
  vs. plugin/core-script-only surfaces). See [Security](../development/security.md).
- **The Studio UI** — property grids, category ordering (`category_Behavior`, …) come straight
  from the descriptors.
- **Serialization** — the XML and binary serializers enumerate reflected properties
  (see [Serialization](./serialization.md)).

### Descriptor flavors

| Descriptor | Describes |
| --- | --- |
| `PropDescriptor<T, V>` | A typed property with getter/setter, category and security |
| `BoundFuncDesc<T, R(Args...)>` | A bound member function (Lua method) |
| `Event` / `Callback` | Scriptable events and callbacks |
| Enums (`EnumProperty.cpp`, `LuaEnum` bridge) | Enum types exposed to scripts |

## Fast tree access

Naïve parent/child traversal is not enough for a scene with millions of parts, so the engine
keeps auxiliary indexes — see `App/util/IndexedTree.*` (indexed name/class lookups) and the
spatial structures described in [Physics](./physics.md).

## Where to read next

- [The DataModel](./datamodel.md) — what actually populates the tree
- [Scripting](./scripting.md) — how reflection becomes the Lua API
- [Serialization](./serialization.md) — how the tree is saved

#pragma once

#include "Lua/LuaBridge.h"
#include "reflection/object.h"
#include "Reflection/Event.h"
#include "Reflection/Property.h"

namespace RBX
{
	class Instance;
	namespace Lua
	{
		struct EventInstance
		{
			const Reflection::EventDescriptor* descriptor;
			// We use a weak pointer because references to a Event shouldn't lock the source of the event.
			// If the source has been collected, then connecting to the Event will return an empty connection.
			weak_ptr<Instance> source;
			// Non-NULL when this signal was created by Instance:GetPropertyChangedSignal(). In that case
			// only changes of this particular property are reported, and the Lua handler receives no
			// arguments (the descriptor is filtered out on the C++ side).
			const Reflection::PropertyDescriptor* propertyFilter;

			EventInstance()
				: descriptor(NULL)
				, propertyFilter(NULL)
			{
			}

			EventInstance(const Reflection::EventDescriptor* descriptor, const weak_ptr<Instance>& source)
				: descriptor(descriptor)
				, source(source)
				, propertyFilter(NULL)
			{
			}

			EventInstance(const Reflection::EventDescriptor* descriptor, const weak_ptr<Instance>& source, const Reflection::PropertyDescriptor* propertyFilter)
				: descriptor(descriptor)
				, source(source)
				, propertyFilter(propertyFilter)
			{
			}

			bool operator== (const EventInstance& other) const
			{
				if (descriptor != other.descriptor || propertyFilter != other.propertyFilter)
					return false;

				shared_ptr<Instance> l = source.lock();
				if (!l)
					return false;

				shared_ptr<Instance> l2 = other.source.lock();
				if (!l2)
					return false;

				return l == l2;
			}
		};

		// specialization
		template<>
		int Bridge<EventInstance>::on_tostring(const EventInstance& object, lua_State *L);

		class EventBridge : public Bridge<EventInstance>
		{
		public:			
			static int connect(lua_State *L);

			static int wait(lua_State *L);
		};

		class SignalConnectionBridge : public Bridge< rbx::signals::connection >
		{
			friend class Bridge< rbx::signals::connection >;
			static int disconnect(lua_State *L);
		};
	}


}

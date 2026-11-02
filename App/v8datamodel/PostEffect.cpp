#include "stdafx.h"

#include "V8DataModel/PostEffect.h"

#include "V8DataModel/Camera.h"
#include "V8DataModel/Lighting.h"

namespace RBX {

const char* const sPostEffect = "PostEffect";
const char* const sBlurEffect = "BlurEffect";

Reflection::PropDescriptor<PostEffect, bool> PostEffect::prop_Enabled("Enabled", category_State, &PostEffect::getEnabled, &PostEffect::setEnabled);

Reflection::PropDescriptor<BlurEffect, float> BlurEffect::prop_Size("Size", category_State, &BlurEffect::getSize, &BlurEffect::setSize);

PostEffect::PostEffect(const char* name)
	: DescribedNonCreatable<PostEffect, Instance, sPostEffect>(name)
	, enabled(true)
{
}

PostEffect::~PostEffect()
{
}

void PostEffect::setEnabled(bool value)
{
	if (enabled != value) {
		enabled = value;
		raisePropertyChanged(prop_Enabled);
	}
}

bool PostEffect::askSetParent(const Instance* instance) const
{
	// Post effects only have an effect under Lighting or a Camera, so only
	// offer those as parents (e.g. in Studio's Insert Object menu). This
	// does not forbid other parents; the effect is simply inert elsewhere.
	return Instance::fastDynamicCast<Lighting>(instance) != NULL
		|| Instance::fastDynamicCast<Camera>(instance) != NULL;
}

BlurEffect::BlurEffect()
	: DescribedCreatable<BlurEffect, PostEffect, sBlurEffect>("BlurEffect")
	, size(24.f)
{
}

BlurEffect::~BlurEffect()
{
}

void BlurEffect::setSize(float value)
{
	// Limit size due to rendering constraints
	value = std::min(std::max(value, 0.f), maxSize());

	if (size != value) {
		size = value;
		raisePropertyChanged(prop_Size);
	}
}

float BlurEffect::getMaxSizeIn(const Instance* container)
{
	float result = 0.f;

	if (container)
	{
		// Snapshot the children; this is called from the render thread while
		// the DataModel may be changing on another thread.
		shared_ptr<const Instances> children = container->getChildren().read();
		if (children)
		{
			Instances::const_iterator end = children->end();
			for (Instances::const_iterator iter = children->begin(); iter != end; ++iter)
			{
				if (const BlurEffect* effect = Instance::fastDynamicCast<BlurEffect>(iter->get()))
				{
					if (effect->getEnabled())
						result = std::max(result, effect->getSize());
				}
			}
		}
	}

	return result;
}

} // namespace RBX

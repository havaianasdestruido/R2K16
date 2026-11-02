#pragma once

#include "V8Tree/Instance.h"

namespace RBX
{
	extern const char* const sPostEffect;

	// Abstract base class for post-processing effects, such as BlurEffect.
	// Post effects change how the world looks after it has been rendered;
	// they do not affect GuiObjects. A post effect only takes effect while
	// it is enabled and parented to the Lighting service or to the current
	// Camera (Workspace.CurrentCamera).
	class PostEffect : public DescribedNonCreatable<PostEffect, Instance, sPostEffect>
	{
	public:
		explicit PostEffect(const char* name);
		virtual ~PostEffect();

		bool getEnabled() const { return enabled; }
		void setEnabled(bool value);

		static Reflection::PropDescriptor<PostEffect, bool> prop_Enabled;

	protected:
		/*override*/ bool askSetParent(const Instance* instance) const;

	private:
		bool enabled;
	};

	extern const char* const sBlurEffect;

	// Applies a Gaussian blur to the entire rendered game world.
	// The strength of the blur is controlled by Size. Only one BlurEffect
	// is applied at once: among the enabled BlurEffects parented to
	// Lighting and to the current Camera, the one with the greatest Size
	// takes priority.
	class BlurEffect : public DescribedCreatable<BlurEffect, PostEffect, sBlurEffect>
	{
	public:
		BlurEffect();
		virtual ~BlurEffect();

		// The blur radius, in pixels. Valid range is 0 (no blur) to maxSize().
		float getSize() const { return size; }
		void setSize(float value);

		static float maxSize() { return 56.f; }

		// Returns the greatest Size among the enabled BlurEffects that are
		// direct children of container, or 0 if there are none. Used by the
		// renderer to resolve which blur (if any) applies to a frame.
		static float getMaxSizeIn(const Instance* container);

		static Reflection::PropDescriptor<BlurEffect, float> prop_Size;

	private:
		float size;
	};

}	// namespace RBX

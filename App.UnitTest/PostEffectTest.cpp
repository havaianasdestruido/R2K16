#include <boost/test/unit_test.hpp>

#include "v8tree/instance.h"
#include "v8datamodel/Camera.h"
#include "v8datamodel/Lighting.h"
#include "v8datamodel/PostEffect.h"
#include "v8datamodel/Sky.h"

using namespace RBX;

BOOST_AUTO_TEST_SUITE( PostEffectTest )

BOOST_AUTO_TEST_CASE( BlurEffectDefaults )
{
	shared_ptr<BlurEffect> effect = Creatable<Instance>::create<BlurEffect>();

	BOOST_CHECK(effect->getEnabled());
	BOOST_CHECK_EQUAL(effect->getSize(), 24.f);
	BOOST_CHECK_EQUAL(effect->getClassNameStr(), "BlurEffect");
	BOOST_CHECK(effect->isA<PostEffect>());
}

BOOST_AUTO_TEST_CASE( BlurEffectCreateByName )
{
	// Instance.new("BlurEffect") must work...
	shared_ptr<Instance> effect = Creatable<Instance>::createByName(Name::lookup("BlurEffect"), ScriptingCreator);
	BOOST_REQUIRE(effect);
	BOOST_CHECK(effect->fastDynamicCast<BlurEffect>() != NULL);

	// ...but the abstract base class must not be creatable.
	shared_ptr<Instance> base = Creatable<Instance>::createByName(Name::lookup("PostEffect"), ScriptingCreator);
	BOOST_CHECK(!base);
}

BOOST_AUTO_TEST_CASE( BlurEffectSizeClamped )
{
	shared_ptr<BlurEffect> effect = Creatable<Instance>::create<BlurEffect>();

	effect->setSize(10.f);
	BOOST_CHECK_EQUAL(effect->getSize(), 10.f);

	effect->setSize(-5.f);
	BOOST_CHECK_EQUAL(effect->getSize(), 0.f);

	effect->setSize(1000.f);
	BOOST_CHECK_EQUAL(effect->getSize(), 56.f);
	BOOST_CHECK_EQUAL(effect->getSize(), BlurEffect::maxSize());
}

BOOST_AUTO_TEST_CASE( BlurEffectParenting )
{
	shared_ptr<BlurEffect> effect = Creatable<Instance>::create<BlurEffect>();
	shared_ptr<Lighting> lighting = Creatable<Instance>::create<Lighting>();
	shared_ptr<Camera> camera = Creatable<Instance>::create<Camera>();

	// Post effects belong under Lighting or a Camera.
	BOOST_CHECK(lighting->canAddChild(effect.get()));
	BOOST_CHECK(camera->canAddChild(effect.get()));

	// Lighting still accepts a Sky, and still rejects unrelated classes.
	shared_ptr<Sky> sky = Creatable<Instance>::create<Sky>();
	BOOST_CHECK(lighting->canAddChild(sky.get()));
	BOOST_CHECK(!lighting->canAddChild(camera.get()));
}

BOOST_AUTO_TEST_CASE( BlurEffectMaxSizeIn )
{
	shared_ptr<Lighting> lighting = Creatable<Instance>::create<Lighting>();

	BOOST_CHECK_EQUAL(BlurEffect::getMaxSizeIn(NULL), 0.f);
	BOOST_CHECK_EQUAL(BlurEffect::getMaxSizeIn(lighting.get()), 0.f);

	shared_ptr<BlurEffect> small = Creatable<Instance>::create<BlurEffect>();
	small->setSize(8.f);
	small->setParent(lighting.get());
	BOOST_CHECK_EQUAL(BlurEffect::getMaxSizeIn(lighting.get()), 8.f);

	// Only one BlurEffect is applied at a time: the greatest Size wins.
	shared_ptr<BlurEffect> large = Creatable<Instance>::create<BlurEffect>();
	large->setSize(40.f);
	large->setParent(lighting.get());
	BOOST_CHECK_EQUAL(BlurEffect::getMaxSizeIn(lighting.get()), 40.f);

	// Disabled effects are ignored.
	large->setEnabled(false);
	BOOST_CHECK_EQUAL(BlurEffect::getMaxSizeIn(lighting.get()), 8.f);

	// Non-BlurEffect children are ignored, as are effects that are not
	// direct children of the container.
	shared_ptr<Sky> sky = Creatable<Instance>::create<Sky>();
	sky->setParent(lighting.get());

	shared_ptr<BlurEffect> nested = Creatable<Instance>::create<BlurEffect>();
	nested->setSize(56.f);
	nested->setParent(sky.get());
	BOOST_CHECK_EQUAL(BlurEffect::getMaxSizeIn(lighting.get()), 8.f);

	// Removing the effect removes it from consideration.
	small->setParent(NULL);
	BOOST_CHECK_EQUAL(BlurEffect::getMaxSizeIn(lighting.get()), 0.f);
}

BOOST_AUTO_TEST_SUITE_END()

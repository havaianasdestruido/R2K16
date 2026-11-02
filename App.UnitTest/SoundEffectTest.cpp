#include <boost/test/unit_test.hpp>
#include <limits>
#include <cstring>

#include "util/SoundEffect.h"
#include "util/SoundChannel.h"
#include "fmod.hpp"
#include "fmod_dsp_effects.h"

using namespace RBX;
using namespace RBX::Soundscape;

BOOST_AUTO_TEST_SUITE(SoundEffectTests)

BOOST_AUTO_TEST_CASE(DistortionPropertiesAndParenting)
{
    shared_ptr<DistortionSoundEffect> effect = Creatable<Instance>::create<DistortionSoundEffect>();
    shared_ptr<SoundChannel> first = Creatable<Instance>::create<SoundChannel>();
    shared_ptr<SoundChannel> second = Creatable<Instance>::create<SoundChannel>();
    BOOST_CHECK(effect->isA<SoundEffect>());
    BOOST_CHECK(effect->getEnabled());
    BOOST_CHECK_EQUAL(effect->getPriority(), 0);
    BOOST_CHECK_EQUAL(effect->getLevel(), 0.75f);
    effect->setLevel(-1.0f);
    BOOST_CHECK_EQUAL(effect->getLevel(), 0.0f);
    effect->setLevel(2.0f);
    BOOST_CHECK_EQUAL(effect->getLevel(), 1.0f);
    effect->setLevel(std::numeric_limits<float>::quiet_NaN());
    BOOST_CHECK_EQUAL(effect->getLevel(), 1.0f);
    effect->setParent(first.get());
    effect->setPriority(3);
    effect->setEnabled(false);
    effect->setParent(second.get());
    BOOST_CHECK_EQUAL(effect->getPriority(), 3);
    BOOST_CHECK(!effect->getEnabled());
    effect->setParent(NULL);
    shared_ptr<Instance> copy = effect->clone(ScriptingCreator);
    DistortionSoundEffect* cloned = Instance::fastDynamicCast<DistortionSoundEffect>(copy.get());
    BOOST_REQUIRE(cloned);
    BOOST_CHECK_EQUAL(cloned->getLevel(), 1.0f);
    BOOST_CHECK_EQUAL(cloned->getPriority(), 3);
    BOOST_CHECK(!cloned->getEnabled());
}

struct EffectAttachment
{
    SoundEffect* effect;
    FMOD::Channel* channel;
    EffectAttachment(SoundEffect* e, FMOD::Channel* c) : effect(e), channel(c) {}
    ~EffectAttachment() { effect->detach(channel); }
};

BOOST_AUTO_TEST_CASE(DistortionDSPUpdatesAndDetach)
{
    FMOD::System* system = NULL;
    BOOST_REQUIRE_EQUAL(FMOD::System_Create(&system), FMOD_OK);
    BOOST_REQUIRE_EQUAL(system->setOutput(FMOD_OUTPUTTYPE_NOSOUND), FMOD_OK);
    BOOST_REQUIRE_EQUAL(system->init(16, FMOD_INIT_NORMAL, NULL), FMOD_OK);
    FMOD_CREATESOUNDEXINFO info;
    std::memset(&info, 0, sizeof(info));
    info.cbsize = sizeof(info);
    info.length = 44100 * 2;
    info.numchannels = 1;
    info.defaultfrequency = 44100;
    info.format = FMOD_SOUND_FORMAT_PCM16;
    FMOD::Sound* sample = NULL;
    BOOST_REQUIRE_EQUAL(system->createSound(NULL, FMOD_OPENUSER | FMOD_LOOP_NORMAL, &info, &sample), FMOD_OK);
    FMOD::Channel* channel = NULL;
    BOOST_REQUIRE_EQUAL(system->playSound(sample, NULL, true, &channel), FMOD_OK);

    shared_ptr<DistortionSoundEffect> effect = Creatable<Instance>::create<DistortionSoundEffect>();
    effect->setLevel(0.25f);
    effect->attach(system, channel);
    EffectAttachment attachment(effect.get(), channel);
    FMOD::DSP* dsp = NULL;
    BOOST_REQUIRE_EQUAL(channel->getDSP(0, &dsp), FMOD_OK);
    FMOD_DSP_TYPE type;
    BOOST_REQUIRE_EQUAL(dsp->getType(&type), FMOD_OK);
    BOOST_CHECK_EQUAL(type, FMOD_DSP_TYPE_DISTORTION);
    float level = 0;
    BOOST_REQUIRE_EQUAL(dsp->getParameterFloat(FMOD_DSP_DISTORTION_LEVEL, &level, NULL, 0), FMOD_OK);
    BOOST_CHECK_CLOSE(level, 0.25f, 0.01f);
    effect->setLevel(0.75f);
    BOOST_REQUIRE_EQUAL(dsp->getParameterFloat(FMOD_DSP_DISTORTION_LEVEL, &level, NULL, 0), FMOD_OK);
    BOOST_CHECK_CLOSE(level, 0.75f, 0.01f);
    effect->setEnabled(false);
    bool bypass = false;
    BOOST_REQUIRE_EQUAL(dsp->getBypass(&bypass), FMOD_OK);
    BOOST_CHECK(bypass);
    effect->setEnabled(true);
    BOOST_REQUIRE_EQUAL(dsp->getBypass(&bypass), FMOD_OK);
    BOOST_CHECK(!bypass);
    int beforeDetach = 0;
    BOOST_REQUIRE_EQUAL(channel->getNumDSPs(&beforeDetach), FMOD_OK);
    effect->detach(channel);
    int afterDetach = 0;
    BOOST_REQUIRE_EQUAL(channel->getNumDSPs(&afterDetach), FMOD_OK);
    BOOST_CHECK_EQUAL(afterDetach, beforeDetach - 1);
    effect->attach(system, channel);
    effect->detach(channel);
    channel->stop();
    sample->release();
    system->close();
    system->release();
}

BOOST_AUTO_TEST_SUITE_END()

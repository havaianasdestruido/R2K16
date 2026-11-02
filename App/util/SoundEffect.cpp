/* Copyright 2003-2014 ROBLOX Corporation, All Rights Reserved */
#include "stdafx.h"
#include "Util/SoundEffect.h"
#include "Util/SoundChannel.h"
#include "Util/SoundService.h"
#include "fmod_dsp_effects.h"

namespace RBX { namespace Soundscape {

const char* const sSoundEffect = "SoundEffect";
const char* const sDistortionSoundEffect = "DistortionSoundEffect";

REFLECTION_BEGIN();
static Reflection::PropDescriptor<SoundEffect, bool> prop_enabled("Enabled", category_Behavior, &SoundEffect::getEnabled, &SoundEffect::setEnabled);
static Reflection::PropDescriptor<SoundEffect, int> prop_priority("Priority", category_Data, &SoundEffect::getPriority, &SoundEffect::setPriority);
static Reflection::PropDescriptor<DistortionSoundEffect, float> prop_level("Level", category_Data, &DistortionSoundEffect::getLevel, &DistortionSoundEffect::setLevel);
REFLECTION_END();

SoundEffect::SoundEffect() : enabled(true), priority(0), dsp(NULL) {}
SoundEffect::~SoundEffect() { RBXASSERT(!dsp); }

void SoundEffect::setEnabled(bool value)
{
    if (enabled == value) return;
    enabled = value;
    if (dsp)
        SoundService::checkResultNoThrow(dsp->setBypass(!enabled), "setBypass", this, dsp);
    raiseChanged(prop_enabled);
}

void SoundEffect::setPriority(int value)
{
    if (priority == value) return;
    priority = value;
    if (SoundChannel* sound = Instance::fastDynamicCast<SoundChannel>(getParent()))
        sound->rebuildEffects();
    raiseChanged(prop_priority);
}

void SoundEffect::attach(FMOD::System* system, FMOD::Channel* channel)
{
    RBXASSERT(!dsp);
    if (!system || !channel) return;
    dsp = createDSP(system);
    if (!dsp) return;
    FMOD_RESULT result = dsp->setBypass(!enabled);
    if (result == FMOD_OK)
        result = channel->addDSP(FMOD_CHANNELCONTROL_DSP_HEAD, dsp);
    if (result != FMOD_OK)
    {
        SoundService::checkResultNoThrow(result, "attach sound effect", this, dsp);
        SoundService::checkResultNoThrow(dsp->release(), "release sound effect", this, dsp);
        dsp = NULL;
    }
}

void SoundEffect::detach(FMOD::Channel* channel)
{
    if (!dsp) return;
    if (channel)
        SoundService::checkResultNoThrow(channel->removeDSP(dsp), "remove sound effect", this, dsp);
    SoundService::checkResultNoThrow(dsp->release(), "release sound effect", this, dsp);
    dsp = NULL;
}

DistortionSoundEffect::DistortionSoundEffect() : level(0.75f)
{
    setName(sDistortionSoundEffect);
}

void DistortionSoundEffect::setLevel(float value)
{
    // Reject NaN as well as clamping values to the range supported by FMOD.
    if (value != value) return;
    value = G3D::clamp(value, 0.0f, 1.0f);
    if (level == value) return;
    level = value;
    if (getDSP())
        SoundService::checkResultNoThrow(getDSP()->setParameterFloat(FMOD_DSP_DISTORTION_LEVEL, level), "set distortion level", this, getDSP());
    raiseChanged(prop_level);
}

FMOD::DSP* DistortionSoundEffect::createDSP(FMOD::System* system)
{
    FMOD::DSP* result = NULL;
    FMOD_RESULT status = system->createDSPByType(FMOD_DSP_TYPE_DISTORTION, &result);
    if (status == FMOD_OK)
        status = result->setParameterFloat(FMOD_DSP_DISTORTION_LEVEL, level);
    if (status != FMOD_OK)
    {
        SoundService::checkResultNoThrow(status, "create distortion effect", this, result);
        if (result) result->release();
        return NULL;
    }
    return result;
}

} }

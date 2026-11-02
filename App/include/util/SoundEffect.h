/* Copyright 2003-2014 ROBLOX Corporation, All Rights Reserved */
#pragma once

#include "v8tree/Instance.h"

namespace FMOD { class Channel; class DSP; class System; }

namespace RBX { namespace Soundscape {

extern const char* const sSoundEffect;
extern const char* const sDistortionSoundEffect;

// Effects are active only when they are direct children of a playing Sound.
class SoundEffect : public DescribedNonCreatable<SoundEffect, Instance, sSoundEffect>
{
    typedef DescribedNonCreatable<SoundEffect, Instance, sSoundEffect> Super;
    bool enabled;
    int priority;
    FMOD::DSP* dsp;

protected:
    virtual FMOD::DSP* createDSP(FMOD::System* system) = 0;
    FMOD::DSP* getDSP() const { return dsp; }

public:
    SoundEffect();
    virtual ~SoundEffect();
    bool getEnabled() const { return enabled; }
    void setEnabled(bool value);
    int getPriority() const { return priority; }
    void setPriority(int value);

    void attach(FMOD::System* system, FMOD::Channel* channel);
    void detach(FMOD::Channel* channel);
};

class DistortionSoundEffect : public DescribedCreatable<DistortionSoundEffect, SoundEffect, sDistortionSoundEffect>
{
    float level;
protected:
    virtual FMOD::DSP* createDSP(FMOD::System* system);
public:
    DistortionSoundEffect();
    float getLevel() const { return level; }
    void setLevel(float value);
};

} }

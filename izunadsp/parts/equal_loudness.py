# External Libraries
from essentia.standard import EqualLoudness as EL
from izunadsp.core.audio_object import AudioSequence
from izunadsp.core.dsp_part import DSPPart


class EqualLoudness(DSPPart):
    def handle(self, audio: AudioSequence) -> AudioSequence:
        audio_filter = EL(sampleRate=audio.freq)
        left, right = map(lambda side: side.apply(audio_filter, seq=True),
                          audio / 2)
        return left * right

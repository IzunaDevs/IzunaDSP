# External Libraries
from essentia.standard import EqualLoudness as EL

# IzunaDSP
from izunadsp.core.audio_object import AudioSequence
from izunadsp.core.dsp_part import DSPPart


class EqualLoudness(DSPPart):
    def handle(self, audio: AudioSequence) -> AudioSequence:
        audio_filter = EL(audio.freq)
        left, right = map(lambda side: side.new(audio_filter(side)), audio / 2)
        return left * right

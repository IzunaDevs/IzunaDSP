# IzunaDSP
from izunadsp.core.audio_object import AudioSequence
from izunadsp.core.dsp_part import DSPPart


class Volume(DSPPart):
    def __init__(self, volume: float = 1.0):
        self.volume = volume

    def handle(self, audio: AudioSequence) -> AudioSequence:
        left, right = audio / 2
        return left**self.volume * right**self.volume

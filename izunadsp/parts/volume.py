# IzunaDSP
from izunadsp import DSPPart, AudioSequence


class Volume(DSPPart):
    def __init__(self, volume: float = 1.0):
        self.volume = volume

    def handle(self, audio: AudioSequence) -> AudioSequence:
        left, right = audio / 2
        return left**self.volume * right**self.volume

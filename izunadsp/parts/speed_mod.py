# IzunaDSP
from izunadsp import AudioSequence, DSPPart


class SpeedModifier(DSPPart):
    def __init__(self, speed: float = 1.0):
        self.speed = speed

    def handle(self, audio: AudioSequence) -> AudioSequence:
        return audio[self.speed]

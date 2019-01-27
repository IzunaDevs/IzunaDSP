# IzunaDSP
from .dsp_part import DSPPart
from .audio_object import AudioSequence


class FunctionPart(DSPPart):
    def __init__(self, alg):
        self.alg = alg

    def handle(self, audio: AudioSequence) -> AudioSequence:
        left, right = map(lambda side: side.apply(self.alg, seq=True),
                          audio / 2)

        return left * right

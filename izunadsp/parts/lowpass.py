import numpy as np
from essentia.standard import LowPass as LowPassFilter

from izunadsp.abc.dsp_part import DSPPart


class LowPass(DSPPart):
    def __init__(self):
        super().__init__()
        self.alg = LowPassFilter()

    def handle(self, audio: np.array) -> np.array:
        left, right = self.to_stereo(audio)

        new_left = self.alg(left)
        new_right = self.alg(right)

        audio = self.to_mono(new_left, new_right)

        return audio

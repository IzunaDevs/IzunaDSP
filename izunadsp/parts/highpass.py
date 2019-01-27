import numpy as np
from essentia.standard import HighPass as HighPassFilter

from izunadsp.abc.dsp_part import DSPPart


class HighPass(DSPPart):
    def __init__(self):
        super().__init__()
        self.alg = HighPassFilter()

    def handle(self, audio: np.array) -> np.array:
        left, right = self.to_stereo(audio)

        new_left = self.alg(left)
        new_right = self.alg(right)

        audio = self.to_mono(new_left, new_right)

        return audio

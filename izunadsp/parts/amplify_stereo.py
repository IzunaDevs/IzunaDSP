import essentia
import numpy as np

from izunadsp.abc.dsp_part import DSPPart


class StereoAmplifier(DSPPart):
    def __init__(self):
        self.mul = 1.2

    def set_amplifier(self, n: float):
        self.mul = max([0, min([2, n])])

    def handle(self, audio: np.array):
        left, right = self.to_stereo(audio)
        diff = (left == right)
        mul_array = (np.array([self.mul] * len(audio)) * (diff - 1)) + 1
        left = left * mul_array
        right = right * mul_array

        left = essentia.array(left)
        right = essentia.array(right)

        return self.to_mono(left, right)

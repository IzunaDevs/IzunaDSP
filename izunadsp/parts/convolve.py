# External Libraries
import numpy as np
from scipy.signal import convolve, hann

# IzunaDSP
from izunadsp.abc.dsp_part import DSPPart


class Convolver(DSPPart):
    def __init__(self):
        super().__init__()
        self.IRS = hann(50)  # HANN as default sample; find better alternative?

    def set_sample(self, sample: np.array):
        self.IRS = sample

    def handle(self, audio: np.array) -> np.array:
        left, right = self.to_stereo(audio)

        new_left = []
        new_right = []

        for (old, new) in zip([left, right], [new_left, new_right]):
            for frame in self.to_frames(old):
                new.append(convolve(old, self.IRS, mode='same') / max(self.IRS))

        audio = self.to_mono(self.to_audio(left), self.to_audio(right))

        return audio

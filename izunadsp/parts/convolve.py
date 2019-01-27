# External Libraries
import numpy as np
from scipy.signal import hann, convolve

# IzunaDSP
from izunadsp import DSPPart, AudioSequence


class Convolver(DSPPart):
    def __init__(self):
        super().__init__()
        self.IRS = hann(50)  # HANN as default sample; find better alternative?

    def set_sample(self, sample: np.array):
        self.IRS = sample

    def transform(self, frame: np.ndarray) -> np.ndarray:
        return convolve(frame, self.IRS, mode='same') / max(self.IRS)

    def handle(self, audio: AudioSequence) -> AudioSequence:
        left, right = audio / 2

        new_left = []
        new_right = []

        for (old, new) in zip([left, right], [new_left, new_right]):
            for frame in old:
                new.append(frame.apply(self.transform, seq=True))

        audio = sum(new_left) * sum(new_right)

        return audio

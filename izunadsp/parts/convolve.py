# External Libraries
from izunadsp.core.audio_object import AudioSequence
from izunadsp.core.dsp_part import DSPPart
import numpy as np
from scipy.signal import hann, convolve


class Convolver(DSPPart):
    def __init__(self, sample: np.ndarray = None):
        self.IRS = sample or hann(
            50)  # HANN as default sample; find better alternative?

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

# External Libraries
import numpy as np
from scipy.signal import hann, convolve

# IzunaDSP
from izunadsp.core.audio_object import AudioSequence
from izunadsp.core.dsp_part import DSPPart


class Convolver(DSPPart):
    def __init__(self, sample: np.ndarray = None):
        self.IRS = sample or hann(
            50)  # HANN as default sample; find better alternative?

    def handle(self, audio: AudioSequence) -> AudioSequence:
        left, right = audio / 2

        new_left = []
        new_right = []

        for (old, new) in zip([left, right], [new_left, new_right]):
            for frame in old:
                new.append(
                    old.new(
                        convolve(frame.audio, self.IRS, mode='same') / max(
                            self.IRS)))

        audio = sum(new_left) * sum(new_right)

        return audio

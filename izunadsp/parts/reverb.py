# External Libraries
import numpy as np
from essentia import array

# IzunaDSP
from izunadsp.abc.dsp_part import DSPPart


class Reverb(DSPPart):
    """ TODO: Speed this up """

    def __init__(self):
        super().__init__()
        self.delay = 250  # in ms
        self.n = 4
        self.decay = 0.5

    def apply_delay(self, audio: np.array):
        offset = int(8 * self.delay * 44100 / 10000)
        audio_bytes = np.append(audio, [0] * offset * self.n)
        delayed_bytes = audio_bytes
        for i in range(self.n):
            beginning = [0] * offset * (i + 1)
            end = audio_bytes[:-offset * (i + 1)]
            multiplied_end = end * ((1 - self.decay) ** (i + 1))
            delayed_bytes += np.append(beginning, multiplied_end)
        return delayed_bytes

    def handle(self, audio: np.array) -> np.array:
        left, right = self.to_stereo(audio)

        left = array(self.apply_delay(left))
        right = array(self.apply_delay(right))

        return self.to_mono(left, right)

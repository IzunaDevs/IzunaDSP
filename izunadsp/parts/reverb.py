# External Libraries
from essentia import array
import numpy as np

# IzunaDSP
from izunadsp.core.audio_object import AudioSequence
from izunadsp.core.dsp_part import DSPPart


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
            multiplied_end = end * ((1 - self.decay)**(i + 1))
            delayed_bytes += np.append(beginning, multiplied_end)
        return delayed_bytes

    def handle(self, audio: AudioSequence) -> AudioSequence:
        left, right = audio / 2

        left = left.new(array(self.apply_delay(left.audio)))
        right = right.new(array(self.apply_delay(right.audio)))

        return left * right

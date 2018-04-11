# External Libraries
import numpy as np

# IzunaDSP
from izunadsp.abc.dsp_part import DSPPart


class Volume(DSPPart):
    def __init__(self):
        super().__init__()
        self.volume = 1.0

    def set_volume(self, volume: float):
        self.volume = volume

    def handle(self, audio: np.array) -> np.array:
        left, right = self.to_stereo(audio)
        return self.to_mono(left * self.volume, right * self.volume)

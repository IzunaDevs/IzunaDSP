# External Libraries
from essentia.standard import Windowing
import numpy as np

# IzunaDSP
from izunadsp.abc.dsp_part import DSPPart


class SpeedModifier(DSPPart):
    def __init__(self):
        super().__init__()
        self._speed = 1.0
        self.speed = 1.0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value: float):
        self.hs = round(self.fs * value)
        self._speed = value

    def set_speed(self, speed: float):
        self.speed = speed

    def handle(self, audio: np.array) -> np.array:
        left, right = self.to_stereo(audio)

        w = Windowing(type="hann")

        left_new = [w(frame) for frame in self.to_frames(left)]
        right_new = [w(frame) for frame in self.to_frames(right)]

        return self.to_mono(self.to_audio(left_new), self.to_audio(right_new))

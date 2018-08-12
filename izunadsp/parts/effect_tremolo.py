import math

import numpy as np

from izunadsp.abc.dsp_part import DSPPart


class Tremolo(DSPPart):
    def __init__(self):
        super().__init__()
        self.rate = 4

    def set_rate(self, rate: float):
        self.rate = rate

    def handle(self, audio: np.array) -> np.array:
        left, right = self.to_stereo(audio)
        left_frames = self.to_frames(left)
        right_frames = self.to_frames(right)

        new_left = []
        new_right = []

        for (old, new) in zip([left_frames, right_frames],
                              [new_left, new_right]):
            _phi = 0

            for frame in old:
                mod = (math.sin(_phi) + 1.5) / 2.5
                _phi += 1/self.rate * math.pi
                frame_mod = frame * mod
                new.append(frame_mod)

        return self.to_mono(self.to_audio(new_left),
                            self.to_audio(new_right))

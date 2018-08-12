import math

import numpy as np

from izunadsp.abc.dsp_part import DSPPart


class Tremolo(DSPPart):
    def __init__(self):
        super().__init__()
        self.rate = 1.0
        self.depth = 2.0

    def set_depth(self, depth: float):
        if (depth > 1) or (depth <= 0):
            raise Exception("Depth has to be 0 < depth =< 1")
        self.depth = depth / 2

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
                offset = 1.0 - self.depth
                mod = offset + self.depth * math.sin(_phi)
                _phi += math.tau / 44100 * self.rate
                frame_mod = frame * mod
                new.append(frame_mod)

        return self.to_mono(self.to_audio(new_left),
                            self.to_audio(new_right))

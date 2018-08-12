import numpy as np

from izunadsp.abc.dsp_part import DSPPart


class Tremolo(DSPPart):
    def __init__(self):
        self.rate = 2.0
        self.depth = 5.0
        self.c = 1

    def handle(self, frame: np.array):
        frames = self.to_frames(audio)

        new_frames = []

        for frame in frames:
            frame_mod = ((self.c * self.depth / self.rate) + (1 - self.depth)) * frame
            self.c = -self.c
            new_frames.append(frame_mod)

        self.c = 1

        return self.to_audio(new_frames)

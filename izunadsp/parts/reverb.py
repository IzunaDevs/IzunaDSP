import numpy as np

from izunadsp.abc.dsp_part import DSPPart


class Reverb(DSPPart):
    def __init__(self):
        super().__init__()
        self.decay = 0.75

    def handle(self, audio: np.array) -> np.array:
        left, right = self.to_stereo(audio)

        cache = None

        new_left = []
        new_right = []

        for (old, new) in zip([left, right], [new_left, new_right]):
            for frame in self.to_frames(old):
                frame = frame if cache is None else frame + (cache * self.decay)

                new.append(frame)

                cache = frame
            cache = None
        return self.to_mono(self.to_audio(new_left), self.to_audio(new_right))

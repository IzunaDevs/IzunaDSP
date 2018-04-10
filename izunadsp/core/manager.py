from io import BytesIO

from essentia.standard import MonoLoader, FrameGenerator, Windowing, MonoWriter
import numpy as np

from izunadsp.abc.DSPPart import DSPPart


class Manager:
    def __init__(self):
        self.parts = []

    def register_part(self, part: DSPPart):
        self.parts.append(part)

    def passthrough(self, filename: str) -> BytesIO:
        audio = MonoLoader(filename=filename)()

        w = Windowing(type="hann")

        frames = []

        for frame in FrameGenerator(audio, frameSize=1024, hopSize=1024):
            for part in self.parts:
                frame = part.handle(frame)

            frames.append(frame)

        new_audio = np.concatenate(frames)

        # b = BytesIO()
        MonoWriter(filename="dubstep_modified.wav")(new_audio)
        # b.seek(0)
        # return b

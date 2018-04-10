from io import BytesIO

from essentia.standard import MonoLoader, FrameGenerator, Windowing, AudioWriter
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

        for frame in FrameGenerator(audio, frameSize=1024, hopSize=512):
            for part in self.parts:
                frame = part.handle(w(frame))

            frames.append(frame)

            break

        audio = np.concatenate(*frames)
        b = BytesIO()
        AudioWriter(filename=b)(audio)

        return b

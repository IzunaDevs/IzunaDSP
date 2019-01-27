# External Libraries
import numpy as np
from essentia.standard import StereoMuxer, StereoDemuxer, FrameGenerator


class DSPPart:
    def __init__(self):
        self.fs = self.hs = 1024

    def handle(self, audio: np.array) -> np.array:
        raise NotImplementedError

    def to_frames(self, audio: np.array) -> list:
        return list(FrameGenerator(audio, frameSize=self.fs, hopSize=self.hs))

    @staticmethod
    def to_audio(frames: list) -> np.array:
        return np.concatenate(frames)

    @staticmethod
    def to_mono(left: np.array, right: np.array) -> np.array:
        return StereoMuxer()(left, right)

    @staticmethod
    def to_stereo(audio: np.array) -> tuple:
        left, right = StereoDemuxer()(audio)
        if not [r for r in right if r != 0]:
            right = left.copy()
        return left, right

# External Libraries
from essentia.standard import FrameGenerator, StereoMuxer, StereoDemuxer
import numpy as np


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
        return StereoDemuxer()(audio)

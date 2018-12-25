# Stdlib
from typing import Tuple, Callable, Iterable

# External Libraries
import essentia
from essentia.standard import Resample, AudioWriter, StereoMuxer, StereoDemuxer, FrameGenerator
import numpy as np


class AudioSequence:
    def __init__(self,
                 audio: np.ndarray,
                 hop_size: int = 1024,
                 frame_size: int = 1024,
                 freq: int = 44100):
        self.audio: np.ndarray = essentia.array(audio)
        self.fs: int = frame_size
        self.hs: int = hop_size
        self.freq: int = freq

    def new(self, audio: np.ndarray) -> 'AudioSequence':
        return AudioSequence(audio, self.hs, self.fs, self.freq)

    def __getitem__(self, item):
        left, right = self / 2
        resample_rate = self.freq / item
        res_func = Resample(outputSampleRate=resample_rate, quality=0)
        left = list(map(lambda frame: left.new(res_func(frame.audio)), left))
        right = list(
            map(lambda frame: right.new(res_func(frame.audio)), right))
        return sum(left) * sum(right)

    def apply(self, func: Callable, seq=False):
        x = func(self.audio)
        if seq:
            x = self.new(x)
        return x

    def __pow__(self, power, _=None):
        return self.new(self.audio * power)

    def __eq__(self, other):
        if isinstance(other, AudioSequence):
            return self.hs == other.hs and self.fs == other.fs and self.freq == other.freq
        return False

    def __ne__(self, other):
        return not self == other

    def __iter__(self) -> Iterable['AudioSequence']:
        return (self.new(x) for x in FrameGenerator(
            self.audio, frameSize=self.fs, hopSize=self.hs))

    def __radd__(self, _):  # for sum() support
        return self

    def __add__(self, other) -> 'AudioSequence':
        if not isinstance(other, (AudioSequence, np.ndarray)):
            raise ValueError("Can only append AudioSequence or numpy.ndarray!")

        if isinstance(other, AudioSequence):
            if self != other:
                raise ValueError(
                    "Frequency, Hopsize and framesize should be equal!")
            other = other.audio

        return self.new(np.concatenate([self.audio, other]))

    def __truediv__(self, other) -> Tuple['AudioSequence', 'AudioSequence']:
        if other != 2:
            raise ValueError("Can only split audio sequence in two tracks!")

        left, right = StereoDemuxer()(self.audio)
        if not list(right):
            right = left.copy()
        return self.new(left), self.new(right)

    def __mul__(self, other) -> 'AudioSequence':
        if not isinstance(other, AudioSequence):
            raise ValueError("Can only concatenate two audio channels!")

        return self.new(StereoMuxer()(self.audio, other.audio))

    def save(self, filename: str):
        AudioWriter(filename=filename)(self.audio)

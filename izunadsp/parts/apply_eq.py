# External Libraries
from essentia.standard import FFT, IFFT
import numpy as np

# IzunaDSP
from izunadsp import DSPPart, AudioSequence


class ApplyEQ(DSPPart):
    def __init__(self):
        super().__init__()
        self._eq = np.array([1])
        self.eq = [1]
        self.fft = FFT()
        self.ifft = IFFT()

    @property
    def eq(self):
        return self._eq

    @eq.setter
    def eq(self, value: list):
        group_size = 513 // len(value) + 1
        v = np.array(value).repeat(group_size)
        too_many = len(v) - 513
        for i in range(too_many):
            v = np.delete(v, i * (group_size - 1))

        self._eq = v

    def set_eq(self, eq: list):
        if not len or len(eq) > 512:
            raise ValueError("Expected a list of size 0 < n <= 512")
        self.eq = eq

    def bands_to_eq_size(self, frame: np.array) -> np.array:
        frame *= self.eq
        return frame / 1000

    def transform(self, frame: np.ndarray) -> np.ndarray:
        fftified = self.fft(frame.copy())
        eq_applied = self.bands_to_eq_size(fftified)
        return self.ifft(eq_applied)

    def handle(self, audio: AudioSequence) -> AudioSequence:
        left, right = audio / 2

        new_left = []
        new_right = []

        for old, new in zip([left, right], [new_left, new_right]):
            for frame in old:
                new.append(frame.apply(self.transform, seq=True))

        return sum(new_left) * sum(new_right)

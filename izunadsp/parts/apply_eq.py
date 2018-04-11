# External Libraries
from essentia.standard import FFT, IFFT
import numpy as np

# IzunaDSP
from izunadsp.abc.dsp_part import DSPPart


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
        if len(eq) > 512 or len(eq) == 0:
            raise ValueError("Expected a list of size 0 < n <= 512")
        self.eq = eq

    def bands_to_eq_size(self, frame: np.array) -> np.array:
        frame *= self.eq
        return frame / 1000

    def handle(self, audio: np.array) -> np.array:
        left, right = self.to_stereo(audio)

        new_left = []
        new_right = []

        for old, new in zip([left, right], [new_left, new_right]):
            for frame in self.to_frames(old):
                fftified = self.fft(frame.copy())

                eq_applied = self.bands_to_eq_size(fftified)

                rev_frame = self.ifft(eq_applied)

                new.append(rev_frame)

        audio = self.to_mono(self.to_audio(new_left), self.to_audio(new_right))

        return audio

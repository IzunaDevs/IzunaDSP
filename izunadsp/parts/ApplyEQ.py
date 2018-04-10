from essentia.standard import FFT, IFFT
import numpy as np


from izunadsp.abc.DSPPart import DSPPart


class ApplyEQ(DSPPart):
    def __init__(self):
        self.eq = [1]

    def set_eq(self, eq: list):
        if len(eq) > 1024:
            raise ValueError("Expected a list of size 0 <= n <= 1024")
        self.eq = eq or [1]

    def bands_to_eq_size(self, frame: np.array) -> np.array:
        group_size = len(frame) // len(self.eq)
        v = np.array(self.eq).repeat(group_size)
        too_many = len(v) - len(frame)
        for i in range(too_many):
            del v[i*group_size]
        x = frame.copy()
        x *= v
        return x / 1000

    def handle(self, frame: np.array) -> np.array:
        fft = FFT()
        ifft = IFFT()

        fftified = fft(frame)

        eq_applied = self.bands_to_eq_size(fftified)

        rev_frame = ifft(eq_applied)

        return rev_frame

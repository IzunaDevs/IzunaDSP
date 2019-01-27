# External Libraries
from essentia.standard import LowPass as LowPassFilter

# IzunaDSP
from izunadsp.core import FunctionPart


class LowPass(FunctionPart):
    def __init__(self):
        super().__init__(LowPassFilter())

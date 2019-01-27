# External Libraries
from essentia.standard import HighPass as HighPassFilter

# IzunaDSP
from izunadsp.core import FunctionPart


class HighPass(FunctionPart):
    def __init__(self):
        super().__init__(HighPassFilter())

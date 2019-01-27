# External Libraries
from essentia.standard import EqualLoudness as EL

# IzunaDSP
from izunadsp import FunctionPart


class EqualLoudness(FunctionPart):
    def __init__(self):
        super().__init__(EL())

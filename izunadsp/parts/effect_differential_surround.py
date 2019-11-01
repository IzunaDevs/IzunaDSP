import math
from izunadsp import DSPPart, AudioSequence

class DifferentialSurround(DSPPart):
    def __init__(self, delay=1):
        self.delay = delay

    def handle(self, audio: AudioSequence) -> AudioSequence:
        """
        Adds a delay to delay frames between the left and right audio sequences.
        """
        raise NotImplementedError("Implementation to be added.")

# Stdlib
import math

# External Libraries
from izunadsp.core.audio_object import AudioSequence
from izunadsp.core.dsp_part import DSPPart


class Tremolo(DSPPart):
    def __init__(self):
        self.rate = 4

    def handle(self, audio: AudioSequence) -> AudioSequence:
        left, right = audio / 2

        new_left = []
        new_right = []

        for (old, new) in zip([left, right], [new_left, new_right]):
            _phi = 0

            for frame in old:
                mod = (math.sin(_phi) + 1.5) / 2.5
                _phi += 1 / self.rate * math.pi
                frame_mod = frame.audio * mod
                new.append(frame.new(frame_mod))

        return sum(new_left) * sum(new_right)

# Stdlib
from io import BytesIO

# External Libraries
from essentia.standard import AudioLoader, AudioWriter

# IzunaDSP
from izunadsp.abc.dsp_part import DSPPart


class Manager:
    def __init__(self):
        self.parts = []

    def register_part(self, part: DSPPart):
        self.parts.append(part)

    def passthrough(self, filename: str) -> BytesIO:
        audio, *_ = AudioLoader(filename=filename)()

        for part in self.parts:
            audio = part.handle(audio)

        # b = BytesIO()
        AudioWriter(filename=f"modified_{filename}")(audio)
        # b.seek(0)
        # return b

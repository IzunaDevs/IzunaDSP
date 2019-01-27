# Stdlib
from io import BytesIO
from tempfile import NamedTemporaryFile
# External Libraries
from typing import Union

from essentia.standard import AudioLoader, AudioWriter

# IzunaDSP
from izunadsp.abc.dsp_part import DSPPart


class Manager:
    def __init__(self):
        self.parts = []

    def register_part(self, part: DSPPart):
        self.parts.append(part)

    def passthrough(self, input_file: Union[str, BytesIO],
                    output_file: str = None) -> Union[BytesIO, None]:
        if isinstance(input_file, BytesIO):
            with NamedTemporaryFile() as file:
                file.write(input_file.read())
                file.seek(0)
                audio, *_ = AudioLoader(filename=file.name)()
        else:
            audio, *_ = AudioLoader(filename=input_file)()

        for part in self.parts:
            audio = part.handle(audio)

        if output_file is not None:
            AudioWriter(filename=output_file)(audio)
            return
        else:
            with NamedTemporaryFile() as file:
                AudioWriter(filename=file.name)(audio)
                file.seek(0)
                return BytesIO(file.read())

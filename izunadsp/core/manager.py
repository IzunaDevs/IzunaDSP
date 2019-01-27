# Stdlib
from io import BytesIO
from tempfile import NamedTemporaryFile

from typing import Union

# External Libraries
from essentia.standard import AudioLoader

# IzunaDSP
from izunadsp import DSPPart, AudioSequence


class Manager:
    def __init__(self):
        self.parts = []

    def register_part(self, part: DSPPart):
        self.parts.append(part)

    def passthrough(self,
                    input_file: Union[BytesIO, str],
                    output_file: str = None) -> Union[BytesIO, str]:
        if isinstance(input_file, BytesIO):
            with NamedTemporaryFile() as file:
                file.write(input_file.read())
                file.seek(0)
                audio, *_ = AudioLoader(filename=file.name)()
        else:
            audio, *_ = AudioLoader(filename=input_file)()

        audio_obj = AudioSequence(audio)

        for part in self.parts:
            audio_obj = part.handle(audio_obj)

        if output_file is not None:
            audio_obj.save(output_file)
            return output_file

        with NamedTemporaryFile() as file:
            audio_obj.save(file.name)
            file.seek(0)
            return BytesIO(file.read())

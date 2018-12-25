# IzunaDSP
from izunadsp.core.manager import Manager
from izunadsp.parts.volume import Volume

man = Manager()
vol = Volume(0.5)

man.register_part(vol)

man.passthrough("dubstep.wav", "dubstep_volume.wav")

# IzunaDSP
from izunadsp.core import Manager
from izunadsp.parts import Tremolo

man = Manager()
tr = Tremolo()

man.register_part(tr)

man.passthrough("dubstep.wav", "dubstep_tremolo.wav")

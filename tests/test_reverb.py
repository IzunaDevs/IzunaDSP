# IzunaDSP
from izunadsp.core.manager import Manager
from izunadsp.parts.reverb import Reverb

man = Manager()
rev = Reverb()

man.register_part(rev)

man.passthrough("dubstep.wav", "dubstep_reverb.wav")

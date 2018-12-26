# IzunaDSP
# External Libraries
from izunadsp.core import Manager
from izunadsp.parts import Reverb

man = Manager()
rev = Reverb()

man.register_part(rev)

man.passthrough("dubstep.wav", "dubstep_reverb.wav")

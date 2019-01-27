# IzunaDSP
# External Libraries
from izunadsp.core import Manager
from izunadsp.parts import EqualLoudness

man = Manager()
eq_loud = EqualLoudness()

man.register_part(eq_loud)

man.passthrough("dubstep.wav", "dubstep_eqloud.wav")

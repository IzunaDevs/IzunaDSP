# IzunaDSP
from izunadsp.core.manager import Manager
from izunadsp.parts.equal_loudness import EqualLoudness

man = Manager()
eq_loud = EqualLoudness()

man.register_part(eq_loud)

man.passthrough("dubstep.wav", "dubstep_eqloud.wav")

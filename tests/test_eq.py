# IzunaDSP
# External Libraries
from izunadsp.core import Manager
from izunadsp.parts import ApplyEQ

man = Manager()
eq = ApplyEQ()
eq.set_eq([1.6, 1.4, 1, 0.7, 0.8, 1, 1, 1.3, 1.4, 1.1])

man.register_part(eq)

man.passthrough("dubstep.wav", "dubstep_eq.wav")

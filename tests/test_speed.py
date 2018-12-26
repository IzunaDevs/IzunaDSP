# IzunaDSP
from izunadsp.core import Manager
from izunadsp.parts import SpeedModifier

man = Manager()
sp = SpeedModifier(2.0)

man.register_part(sp)

man.passthrough("dubstep.wav", "dubstep_speed.wav")

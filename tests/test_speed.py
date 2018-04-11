# IzunaDSP
from izunadsp.core.manager import Manager
from izunadsp.parts.speed_mod import SpeedModifier

man = Manager()
sp = SpeedModifier()
sp.set_speed(2.0)

man.register_part(sp)

man.passthrough("dubstep.wav", "dubstep_speed.wav")

# IzunaDSP
from izunadsp.core.manager import Manager
from izunadsp.parts.effect_tremolo import Tremolo

man = Manager()
tr = Tremolo()

man.register_part(tr)

man.passthrough("Unt.ogg", "dubstep_tremolo.wav")

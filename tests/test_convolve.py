# IzunaDSP
# External Libraries
from izunadsp.core import Manager
from izunadsp.parts import Convolver

man = Manager()
convolver = Convolver()

man.register_part(convolver)

man.passthrough("dubstep.wav", "dubstep_convolver.wav")

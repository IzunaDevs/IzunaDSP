# IzunaDSP
from izunadsp.core.manager import Manager
from izunadsp.parts.convolve import Convolver

man = Manager()
convolver = Convolver()

man.register_part(convolver)

man.passthrough("dubstep.wav", "dubstep_convolver.wav")

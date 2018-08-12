# IzunaDSP
from izunadsp.core.manager import Manager
from izunadsp.parts.amplify_stereo import StereoAmplifier

man = Manager()
amp = StereoAmplifier()
amp.set_amplifier(1.5)

man.register_part(amp)

man.passthrough("dubstep.wav", "dubstep_amp.wav")

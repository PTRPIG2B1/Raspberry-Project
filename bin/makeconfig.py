import ConfigParser
import sys

cfg = ConfigParser.ConfigParser()
cfg.add_section('Section1')
S = 'Section1'
cfg.set(S, 'detectEnMarche','False')
cfg.set(S, 'height', '720')
cfg.set(S, 'width', '1280')
cfg.set(S, 'fps', '30')
cfg.set(S, 'seuil', '50')
cfg.set(S, 'luminosite', '50')
cfg.write(open('config.cfg','w'))

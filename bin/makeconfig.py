#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import sys

CONFIG_PATH = '/home/pi/RaspiWatch/bin/config.cfg'

cfg = ConfigParser.ConfigParser()

S = 'General'
cfg.add_section(S)
cfg.set(S, 'luminosite','50')

S = 'Detection'
cfg.add_section(S)
cfg.set(S, 'enmarche','False')
cfg.set(S, 'seuil', '50')

S = 'Video'
cfg.add_section(S)
cfg.set(S, 'largeur', '1280')
cfg.set(S, 'hauteur', '720')
cfg.set(S, 'ips', '30')

S = 'Photo'
cfg.add_section(S)
cfg.set(S, 'largeur', '1280')
cfg.set(S, 'hauteur', '720')

cfg.write(open(CONFIG_PATH,'w'))


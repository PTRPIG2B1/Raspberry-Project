#!/usr/bin/python2
import os
if not os.path.isfile('config.cfg'):
  print 'Creation'
  os.system("python makeconfig.py")
else : 
  print 'Le fichier existe'
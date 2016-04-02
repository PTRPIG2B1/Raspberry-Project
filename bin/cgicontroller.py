#!/usr/bin/python2
# -*- coding: utf-8 -*-

import ConfigParser
import sys

#Le chemin vers la config doit etre absolu
configPath='/home/pi/RaspiWatch/bin/config.cfg'
nomSection='Section1'

#Parse d'arguments dans un tableau args
str = sys.argv[1]
temp = str.split('&')
temp = [i.split('=') for i in temp]
args = []
for i in temp:
	args += i
	
#ligne suivante inutile donc enlevée, il y aura toujours "submit=submit", et si ce n'est pas le cas
# il y aurait une erreur à str = sys.argv[1] de toute façon
#if len(args) > 0:
cfg = ConfigParser.ConfigParser()
cfg.read(configPath)
action = args[0]

if action == "off":
	print "kill du programme de detection"
	cfg.set('Section1', 'detectenmarche', False)
	cfg.write(open(configPath,'w'))
elif action == "on":
	print "lancement du programme de detection"
	cfg.set('Section1', 'detectenmarche', True)
	cfg.write(open(configPath,'w'))
elif action == "photo":
	print "prise de la bastille(1780)"
		
# "elif len(args)%2 == 0:" inutile, len(args)%2 est toujours divible par 2 en GET
else:
	#i = 1
	#while i < len(args):
	
	#plus propre avec for de pas de 2
	for i in range(0,len(args)-1,2):

		action = args[i]
		if action == "res":
		
			if args[i+1]== '1':
				cfg.set(nomSection, 'width', '1900')
				cfg.set(nomSection, 'height', '1080')
			elif args[i+1]== '2':
				cfg.set(nomSection, 'width', '1280')
				cfg.set(nomSection, 'height', '720')
			elif args[i+1] == '3':
				cfg.set(nomSection, 'width', '640')
				cfg.set(nomSection, 'height', '480')
			else:
				cfg.set(nomSection, 'width', '1900')
				cfg.set(nomSection, 'height', '1080')
				
		elif action == "ips":
			cfg.set(nomSection, 'fps', args[i+1])
			
		elif action == "seuil":
			cfg.set(nomSection, 'seuil', args[i+1])
			
		elif action == "lum":
			cfg.set(nomSection, 'luminosite', args[i+1])
			
	cfg.write(open(configPath,'w'))

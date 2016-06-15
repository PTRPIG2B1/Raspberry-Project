#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser

CONFIG_PATH = '/home/pi/RaspiWatch/bin/config.cfg'

cfg = ConfigParser.ConfigParser()
cfg.read(CONFIG_PATH)
mail = cfg.get('Email','email')

if(mail == ""):
	print 'Saisissez l\'adresse mail sur laquelle vous voulez être notifié : '
	mail = raw_input()
	while (len(mail)==0):
		print 'Merci d\'effectuer une saisie'
		mail = raw_input()
	print 'Vous avez enregistré l\'adresse mail : ' + mail
	cfg.set('Email','email',mail)	
	cfg.write(open(CONFIG_PATH,'w'))
else:
	print 'Voulez vous modifier l\'adresse mail ?(o/n)'
	choix = raw_input()
	while (len(choix)!=1):
		print 'Merci d\'effectuer une saisie'
		choix = raw_input()
	if (choix == 'o'):
            print 'Saisissez l\'adresse mail sur laquelle vous voulez être notifié : '
            mail = raw_input()
            while (len(mail)==0):
                print 'Merci d\'effectuer une saisie'
                mail = raw_input()
            cfg.set('Email','email',mail)
            cfg.write(open(CONFIG_PATH,'w'))
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import actions
import menu
import os
import ConfigParser
import sys
from datetime import datetime

#Constantes 
CONFIG_PATH = '/home/pi/RaspiWatch/bin/config.cfg'
MAKECONFIG_PATH = '/home/pi/RaspiWatch/bin/makecfg.py'
LOG_PATH = "/home/pi/RaspiWatch/log.txt"

#Debut du programme
if not os.path.isfile(CONFIG_PATH):
	os.system("python "+MAKECONFIG_PATH)

#On vérifie que le fichier de log existe sinon on le crée
if not os.path.isfile(LOG_PATH):
	os.system("touch "+LOG_PATH)	
choix = '1'

#Lecture des valeurs du fichier de configuration
#Impossible de le faire dans une fonction car il faudrait tous passer en paramètres
cfg = ConfigParser.ConfigParser()
cfg.read(CONFIG_PATH)

#attribution à des variables pour permettre le traitement au sein du programme
detectEnMarche = cfg.get('Detection', 'enmarche')
vHauteur = cfg.get('Video', 'hauteur')
vLargeur = cfg.get('Video', 'largeur')
ips = cfg.get('Video', 'ips')
seuil = cfg.get('Detection', 'seuil')
luminosite = cfg.get('General', 'luminosite')
pLargeur = cfg.get('Photo', 'largeur')
pHauteur = cfg.get('Photo', 'hauteur')
os.system("clear")

#Début du programme 
while (choix != '0') :
	if (detectEnMarche == 'True'):
		menu.affmenuprincipalActif()
	else:
		menu.affmenuprincipalInactif()
	
	choix = menu.saisir()
	
	os.system("clear")

	if (choix == '1'):
		actions.prendrePhoto()
	elif (choix == '2'):
		print "Duree de la vidéo ? (en secondes)"
		secondes = saisir()
		actions.prendreVideo(secondes)
	elif (choix == '3'):
		actions.demarrerDetec()
	elif (choix == '4'):
		actions.arreterDetec()
	elif (choix == '5'):
		menu.configuration()
	elif (choix == '6'):
		print 'Chargement de la configuration ...'
	elif (choix == '0'):
		print 'Au revoir ...'
	else :
		print 'Erreur de valeur saisie'
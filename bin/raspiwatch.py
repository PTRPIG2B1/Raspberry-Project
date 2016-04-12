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

#Debut du programme
if not os.path.isfile(CONFIG_PATH):
	os.system("python "+MAKECONFIG_PATH)
	
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
		choixconf = '1'

		while(choixconf != '0'):

			menu.affmenuconfiguration()
			choixconf = menu.saisir()

			os.system("clear")

			if (choixconf == '1'):
				print 'Changement de la resolution :'
				menu.affmenuphotovideo()
				choixpv = menu.saisir()
				if (choixpv == '0'):
					choixres = '0'
				else :
					choixres = '1'

				os.system("clear")
				while (choixres != '0'):
					menu.affmenuresolution()

					choixres = menu.saisir()

					os.system("clear")
					if (choixpv == '1'):
						actions.setResPhoto(choixres)
						choixres = '0'
					elif (choixpv == '2'):
						actions.setResVideo(choixres)
						choixres = '0'
					else :
						print 'Erreur de valeur saisie'
					os.system("clear")
			elif (choixconf == '2'):
				#affmenufps()
				print 'Saisir les ips :'
				choixfps = menu.saisir()
				actions.setIps(choixfps)
				os.system("clear")
			elif (choixconf == '3'):
				print "Saisir le seuil en % : "
				seuil = menu.saisir()
				actions.setSeuil(seuil)
			elif (choixconf == '4'):
				print "Saisir la luminosite en % : "
				luminosite = menu.saisir()
				actions.setLuminosite(luminosite)
			elif (choixconf == '0'):
				print 'Retour au menu principal ...'
			else :
				print 'Erreur de valeur saisie'
		#J'enlève la ligne suivante car elle n'est plus nécessaire normalement (l'écriture se fait directement après la modification)
		#cfg.write(open('config.cfg','w'))
	elif (choix == '6'):
		print 'Chargement de la configuration ...'
	elif (choix == '0'):
		print 'Au revoir ...'
	else :
		print 'Erreur de valeur saisie'
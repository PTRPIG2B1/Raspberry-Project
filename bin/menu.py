#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import actions
import os
#CONSTANTES
CONFIG_PATH = '/home/pi/RaspiWatch/bin/config.cfg'

#Fonctions et procedure
def affmenuprincipalActif():
	"""Affiche le menu principal du programme quand la detection est active"""
	print '////////////////MENU PRINCIPAL RASPBERRY////////////////\n'
	print '\t   Etat de la detection : active'
	print '\t   1- Prendre une photo'
	print '\t   2- Prendre une video'
	print '\t   3- Redemarrer la detection'
	print '\t   4- Arreter la detection'
	print '\t   5- Changer la configuration'
	print '\t   6- Charger la configuration'
	print '\t   0- Quitter\n'
	print '////////////////////////////////////////////////////////'
	print 'Votre choix : '

def affmenuprincipalInactif():
	"""Affiche le menu principal du programme quand la detection est inactive"""
	print '////////////////MENU PRINCIPAL RASPBERRY////////////////\n'
	print '\t   Etat de la detection : inactive'
	print '\t   1- Prendre une photo'
	print '\t   2- Prendre une video'
	print '\t   3- Lancer la detection'
	print '\t   4- Forcer l\'arret de la detection'
	print '\t   5- Changer la configuration'
	print '\t   6- Charger la configuration'
	print '\t   0- Quitter\n'
	print '////////////////////////////////////////////////////////'
	print 'Votre choix : '

def affmenuconfiguration():
	"""Affiche le menu de configuration"""
	cfg = ConfigParser.ConfigParser()
	cfg.read(CONFIG_PATH)
	vHauteur = cfg.get('Video', 'hauteur')
	vLargeur = cfg.get('Video', 'largeur')
	ips = cfg.get('Video', 'ips')
	seuil = cfg.get('Detection', 'seuil')
	luminosite = cfg.get('General', 'luminosite')
	print '//////////////////MENU DE CONFIGURATION/////////////////\n'
	print '\t   Quel parametre voulez-vous modifier ?'
	print '\t   1- Resolution '+'('+vLargeur+ '*'+vHauteur+')'
	print '\t   2- Images par secondes (' + str(ips) +')'
	print '\t   3- Seuil de detection (' + str(seuil) +'%)'
	print '\t   4- Luminosite (' + str(luminosite) + '%)'
	print '\t   5- Retablir la configuration par defaut'
	print '\t   0- Retour au menu principal\n'
	print '////////////////////////////////////////////////////////'
	print 'Votre choix : '

def affmenuresolution():
	"""Affiche le menu qui permet le changement de resolution"""
	print '//////////////////MENU CHGMT RESOLUTION//////////////////\n'
	print '\t   1- 1920*1080 (1080p)'
	print '\t   2- 1280*720 (720p)'
	print '\t   3- 640*480 (480p)'
	print '\t   0- Quitter\n'
	print '////////////////////////////////////////////////////////'
	print 'Votre choix : '

def affmenufps():
	"""Affiche le menu qui permet le changement des IPS"""
	print '/////////////////////MENU CHGMT IPS/////////////////////\n'
	print '\t   1- 30 IPS'
	print '\t   2- 25 IPS'
	print '\t   3- 20 IPS'
	print '\t   4- 15 IPS'
	print '\t   0- Quitter\n'
	print '////////////////////////////////////////////////////////'
	print 'Votre choix : '

#def affmenuphotovideo():
#	"""Affiche le menu qui permet le choix entre photo et video pour le changement de resolution"""
#	print '//////////////////MENU CHGMT RESOLUTION//////////////////\n'
#	print '\t   Que voulez-vous modifier ?'
#	print '\t   1- Photo'
#	print '\t   2- Video'
#	print '\t   0- Quitter\n'
#	print '////////////////////////////////////////////////////////'
#	print 'Votre choix : '

#La fonction est inutile normalement
def sauvegarderConfiguration():
	"""Permet d'effectuer une sauvegarde, ecriture dans le fichier"""
	cfg.write(open(CONFIG_PATH,'w'))

def saisir():
	"""Permet d'effectuer une saisie en controlant qu'une valeur a bien ete saisi"""
	saisi = raw_input()
	while (len(saisi)==0):
		print 'Merci d\'effectuer une saisie'
		saisi = raw_input()
	return saisi

def configuration():
	"""Gère le menu de configuration"""
	cfg = ConfigParser.ConfigParser()
	cfg.read(CONFIG_PATH)
	vHauteur = cfg.get('Video', 'hauteur')
	vLargeur = cfg.get('Video', 'largeur')
	ips = cfg.get('Video', 'ips')
	seuil = cfg.get('Detection', 'seuil')
	luminosite = cfg.get('General', 'luminosite')
	choixconf = '1'

	while(choixconf != '0'):

		affmenuconfiguration()
		choixconf = saisir()

		os.system("clear")

		if (choixconf == '1'):
			print 'Changement de la resolution :'
			choixres = '1'
			
			while (choixres != '0'):
				affmenuresolution()

				choixres = saisir()
					
				actions.setResVideo(choixres)
				choixres = '0'
				os.system("clear")
		elif (choixconf == '2'):
		#affmenufps()
			print 'Saisir les ips :'
			choixfps = saisir()
			actions.setIps(int(choixfps))
			os.system("clear")
		elif (choixconf == '3'):
			print "Saisir le seuil en % : "
			seuil = saisir()
			actions.setSeuil(int(seuil))
		elif (choixconf == '4'):
			print "Saisir la luminosite en % : "
			luminosite = saisir()
			actions.setLuminosite(int(luminosite))
		elif (choixconf == '0'):
			print 'Retour au menu principal ...'
		else :
			print 'Erreur de valeur saisie'

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import actions

LOG_PATH = "/home/pi/RaspiWatch/bin/log.txt"

def photo():
	"""Permet d'écrire dans le fichier log qu'une photo à été prise"""
	log = open(LOG_PATH, "a")
	logmsg = "Prise d'une photo "+actions.getDateName()+"\n"
	log.write(logmsg)
	log.close()

def video():
	"""Permet d'écrire dans le fichier log qu'une vidéo à été prise"""
	log = open(LOG_PATH, "a")
	logmsg = "Prise d'une vidéo "+actions.getDateName()+"\n"
	log.write(logmsg)
	log.close()

def demDetect():
	"""Permet d'écrire dans le fichier log que la détection à été lancé"""
	log = open(LOG_PATH, "a")
	logmsg = "Lancement de la detection "+actions.getDateName()+"\n"
	log.write(logmsg)
	log.close()

def arrDetect():
	"""Permet d'écrire dans le fichier log que la detection à été arrété"""
	log = open(LOG_PATH, "a")
	logmsg = "Arret de la detection "+actions.getDateName()+"\n"
	log.write(logmsg)
	log.close()

#Dans actions il n'y a pas de distinction entre arret et arret forcé
# def arrForDetect():
# 	"""Permet d'écrire dans le fichier log qu'une photo à été prise"""
# 	log = open(LOG_PATH, "a")
# 	logmsg = "Prise d'une photo le "+actions.getDateName()+"\n"
# 	log.write(logmsg)
# 	log.close()

#Dans actions il n'y a pas de distinction entre demarrage et redemarrage
# def reDemDetect():
# 	"""Permet d'écrire dans le fichier log qu'une photo à été prise"""
# 	log = open(LOG_PATH, "a")
# 	logmsg = "Prise d'une photo le "+actions.getDateName()+"\n"
# 	log.write(logmsg)
# 	log.close()

def modResPhoto():
	"""Permet d'écrire dans le fichier log que la resolution photo à été modifié"""
	log = open(LOG_PATH, "a")
	logmsg = "Modification de la résolution photo "+actions.getDateName()+"\n"
	log.write(logmsg)
	log.close()

def modResVideo():
	"""Permet d'écrire dans le fichier log que la resolution vidéo à été modifié"""
	log = open(LOG_PATH, "a")
	logmsg = "Modification de la résolution vidéo "+actions.getDateName()+"\n"
	log.write(logmsg)
	log.close()

def modIps():
	"""Permet d'écrire dans le fichier log que le nombre d'images par secondes à été modifié"""
	log = open(LOG_PATH, "a")
	logmsg = "Modification des IPS "+actions.getDateName()+"\n"
	log.write(logmsg)
	log.close()

def modLuminosite():
	"""Permet d'écrire dans le fichier log que la luminosité à été modifié"""
	log = open(LOG_PATH, "a")
	logmsg = "Modification de la luminosité "+actions.getDateName()+"\n"
	log.write(logmsg)
	log.close()

def modSeuil():
	"""Permet d'écrire dans le fichier log que le seuil à été modifié"""
	log = open(LOG_PATH, "a")
	logmsg = "Modification du seuil "+actions.getDateName()+"\n"
	log.write(logmsg)
	log.close()
	
def videoDetec():
	"""Permet d'écrite dans le fichier log qu'une video a été enregistrée après une détection"""
	log = open(LOG_PATH, "a")
	logmsg = "Prise d'une vidéo après détection"+actions.getDateName()+"\n"
	log.write(logmsg)
	log.close()

def erreur(texte):
	"""Permet d'écrire les erreurs dans le fichier log (utilisé dans de multiples modules"""
	log = open(LOG_PATH, "a")
	logmsg = "ERREUR : " + texte + actions.getDateName()+"\n"
	print logmsg
	log.write(logmsg)
	log.close()	

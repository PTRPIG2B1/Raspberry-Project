#!/usr/bin/env python
# -*- coding: utf-8 -*-
import actions

LOG_PATH = "/home/pi/RaspiWatch/bin/log.txt"

def log(msg):
    log = open(LOG_PATH, "a")
    logmsg = msg + " " +actions.getDateName()+"\n"
    log.write(logmsg)
    log.close()

def photo():
	"""Permet d'écrire dans le fichier log qu'une photo à été prise"""
	log("Prise d'une photo")

def video():
	"""Permet d'écrire dans le fichier log qu'une vidéo à été prise"""
	log("Prise d'une vidéo")

def demDetect():
	"""Permet d'écrire dans le fichier log que la détection à été lancé"""
	log("Lancement de la détection")

def arrDetect():
	"""Permet d'écrire dans le fichier log que la detection à été arrété"""
	log("Arret de la détection")

def modResPhoto():
	"""Permet d'écrire dans le fichier log que la resolution photo à été modifié"""
	log("Modification de la résolution photo")

def modResVideo():
	"""Permet d'écrire dans le fichier log que la resolution vidéo à été modifié"""
	log("Modification de la résolution vidéo")

def modIps():
	"""Permet d'écrire dans le fichier log que le nombre d'images par secondes à été modifié"""
	log("Modification des IPS")

def modLuminosite():
	"""Permet d'écrire dans le fichier log que la luminosité à été modifié"""
	log("Modification de la luminosité")

def modSeuil():
	"""Permet d'écrire dans le fichier log que le seuil à été modifié"""
	log("Modification du seuil")
	
def videoDetec():
	"""Permet d'écrite dans le fichier log qu'une video a été enregistrée après une détection"""
	log("Prise d'une vidéo après détection")

def erreur(texte):
	"""Permet d'écrire les erreurs dans le fichier log (utilisé dans de multiples modules)"""
	log("ERREUR : " + texte)


def mouvement():
    """Permet d'écrire dans le fichier lors de la détection d'un mouvement"""
    log("Mouvement détecté")

def suppressionPhoto(nom):
    """Permet de logger une suppression de photo"""
    log("Suppression de la photo "+nom)

def suppressionVideo(nom):
    """Permet de logger une suppression de video"""
    log("Suppression de la vidéo "+nom)

	

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#IMPORTS
import ConfigParser
from datetime import datetime
import os
import sys

#CONSTANTES
BIN_PATH = '/home/pi/RaspiWatch/bin/'
CONFIG_PATH = '/home/pi/RaspiWatch/bin/config.cfg'
PHOTO_PATH = '/home/pi/RaspiWatch/photo/'
VIDEO_PATH = '/home/pi/RaspiWatch/video/'
MINIATURES_PATH = '/home/pi/RaspiWatch/video/miniatures/'


def demarrerDetec():
    """ Execute le script de détection. ATTENTION : On modifie la configuration ici, il est donc inutile de le changer dans "detec.py" """
    print 'Demarrage de la detection ...'
    cfg = ConfigParser.ConfigParser()
    cfg.read(CONFIG_PATH)
    cfg.set('Detection', 'enmarche', 'True')
    cfg.write(open(CONFIG_PATH,'w'))
    os.system("python "+BIN_PATH+"detec.py &")
    
def arreterDetec():
    """ Arrête la détection de mouvement en changeant la valeur "en marche" dans la config """
    print 'Arret de la detection ...'
    cfg = ConfigParser.ConfigParser()
    cfg.read(CONFIG_PATH)
    cfg.set('Detection', 'enmarche', 'False')
    cfg.write(open(CONFIG_PATH,'w'))


def prendrePhoto():
    """ Prend une photo, la nomme avec la date et l'heure, et la place dans le dossier RaspiWatch/photo """
    nomPhoto = "photo" + getDateName() + ".jpg"
    print 'Prise de la photo ...'
    os.system("raspistill -t 500 -o " + PHOTO_PATH + nomPhoto)


def prendreVideo(secondes):
    """ Prend une video, la nomme avec la date et l'heure, et la place dans le dossier RaspiWatch/video
        Prend aussi la miniature correspondante à la vidéo, et la place dans RaspiWatch/video/miniatures """
    tps = secondes*1000
    maintenant = datetime.now()
    nomVideo = "video" + getDateName()
    print 'Prise de la miniature ...'
    os.system("raspistill -t 100 -o " + MINIATURES_PATH + nomVideo + ".jpg")
    print 'Enregistrement de la video ...'
    os.system("raspivid -o " + VIDEO_PATH + nomVideo + ".h264 -t " + str(tps))


def setResVideo(choix):
    """ Change la résolution vidéo dans la configuration, en fonction des 3 choix disponibles. En cas de mauvaise saisie,
        la résolution la plus petite est utilisée """
    if (choix == '1'):
        largeur = 1920
        hauteur = 1080
    elif (choix == '2'):
        largeur = 1280
        hauteur = 720
    elif (choix == '0'):
        #On quitte
        print 'Retour'
    else:
        largeur = 640
        hauteur = 480
    cfg = ConfigParser.ConfigParser()
    cfg.read(CONFIG_PATH)
    cfg.set('Video', 'largeur', largeur)
    cfg.set('Video', 'hauteur', hauteur)
    cfg.write(open(CONFIG_PATH,'w'))


def setResPhoto(choix):
    """ Change la résolution photo dans la configuration, en fonction des 3 choix disponibles. En cas de mauvaise saisie,
        la résolution la plus petite est utilisée """
    if (choix == '1'):
        largeur = 1920
        hauteur = 1080
    elif (choix == '2'):
        largeur = 1280
        hauteur = 720
    elif (choix == '0'):
        #On quitte
        print 'Retour'
    else:
        largeur = 640
        hauteur = 480
    cfg = ConfigParser.ConfigParser()
    cfg.read(CONFIG_PATH)
    cfg.set('Photo', 'largeur', largeur)
    cfg.set('Photo', 'hauteur', hauteur)
    cfg.write(open(CONFIG_PATH,'w'))


def setIps(valeur):
    """ Change la cadence de vidéo dans la configuration. """
    if valeur < 10:
        valeur = 10
    if valeur > 30:
        valeur = 30
    cfg = ConfigParser.ConfigParser()
    cfg.read(CONFIG_PATH)
    cfg.set('Video', 'ips', valeur)
    cfg.write(open(CONFIG_PATH,'w'))

def setLuminosite(pourcentage):
    """ Change la luminosité de détection, de photo et de vidéo en prenant en paramètre le pourcentage voulu. Cette procédure
        contrôle la saisie """
    if pourcentage < 0:
        pourcentage = 0
    if pourcentage > 100:
        pourcentage = 100
    cfg = ConfigParser.ConfigParser()
    cfg.read(CONFIG_PATH)
    cfg.set('General', 'luminosite', pourcentage)
    cfg.write(open(CONFIG_PATH,'w'))

def setSeuil(pourcentage):
    """ Change le seuil de détection en prenant en paramètre le pourcentage voulu. Cette procédure
        contrôle la saisie """
    if pourcentage < 0:
        pourcentage = 0
    if pourcentage > 100:
        pourcentage = 100
    cfg = ConfigParser.ConfigParser()
    cfg.read(CONFIG_PATH)
    cfg.set('Detection', 'seuil', pourcentage)
    cfg.write(open(CONFIG_PATH,'w'))

def getDateName():
    """ Retourne une chaine de type : "_26-01-95_12:20:30" pour faciliter le nommage des photos et des vidéos """
    maintenant = datetime.now()
    nom = "_" + str(maintenant.day) + "-" + str(maintenant.month) + "-" + str(maintenant.year) + "_" + str(maintenant.hour) + ":" + str(maintenant.minute) + ":" + str(maintenant.second)
    return nom
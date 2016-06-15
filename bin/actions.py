#!/usr/bin/env python
# -*- coding: utf-8 -*-

#IMPORTS
import ConfigParser
from datetime import datetime
import os
import sys
import menu
import mail
import log
from time import time, sleep
import picamera

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
    try:
        cfg.set('Detection', 'enmarche', 'True')
    except Exception:
        mail.envoyerMailErreur("Erreur dans le chemin de configuration dans actions.py")
    cfg.write(open(CONFIG_PATH,'w'))

    #ret contient la valeur de retour de la commande. On l'utilise pour voir s'il y a eu une erreur
    ret = os.system("python "+BIN_PATH+"detec.py &")
    if ret != 0:
	    mail.envoyerMailErreur("Ne peut pas lancer la détection")
    log.demDetect()
    
def arreterDetec():
    """ Arrête la détection de mouvement en changeant la valeur "en marche" dans la config """
    print 'Arret de la detection ...'
    cfg = ConfigParser.ConfigParser()
    cfg.read(CONFIG_PATH)
    try:
        cfg.set('Detection', 'enmarche', 'False')
    except Exception:
        mail.envoyerMailErreur("Erreur dans le chemin de configuration dans actions.py")
    cfg.write(open(CONFIG_PATH,'w'))
    log.arrDetect()


def prendrePhoto():
    """ Prend une photo, la nomme avec la date et l'heure, et la place dans le dossier RaspiWatch/photo """
    cfg = ConfigParser.ConfigParser()
    cfg.read(CONFIG_PATH)
    nomPhoto = "photo" + getDateName() + ".jpg"
    print 'Prise de la photo ...'
    try:
        LARGEUR = cfg.get('Video','largeur')
        HAUTEUR = cfg.get('Video','hauteur')
        LUMINOSITE = cfg.get('General','luminosite')
        ret = os.system("raspistill -t 500 -w "+LARGEUR+" -h "+HAUTEUR+" -br "+LUMINOSITE+" -o " + PHOTO_PATH + nomPhoto)
        if ret != 0:
	        mail.envoyerMailErreur("Ne peut pas prendre une photo")
        log.photo()
    except NoSectionError:
        mail.envoyerMailErreur("Erreur dans le chemin de configuration dans actions.py")
    except IOError:
        mail.envoyerMailErreur("Erreur dans le chemin des logs dans actions.py")


def prendreVideo(secondes):
    """ Prend une video, la nomme avec la date et l'heure, et la place dans le dossier RaspiWatch/video
        Prend aussi la miniature correspondante à la vidéo, et la place dans RaspiWatch/video/miniatures """
    cfg = ConfigParser.ConfigParser()
    cfg.read(CONFIG_PATH)
    tps = int(secondes)*1000
    maintenant = datetime.now()
    nomVideo = "video" + getDateName()
    print 'Prise de la miniature ...'
    try:
        LARGEUR = cfg.get('Video','largeur') 
        HAUTEUR = cfg.get('Video','hauteur')
        LUMINOSITE = cfg.get('General','luminosite')
        IPS = cfg.get('Video','ips')
    except NoSectionError:
        mail.envoyerMailErreur("Erreur dans le chemin de configuration dans actions.py")

    ret = os.system("raspistill -t 100 -w "+LARGEUR+" -h "+HAUTEUR+" -br "+LUMINOSITE+" -o " + MINIATURES_PATH + nomVideo + ".jpg")
    print 'Enregistrement de la video ...'
    #ret += os.system("raspivid -t 5000 -fps 30 -w 640 -h 480 -br 50 -o test.h264")
    ret += os.system("raspivid -t "+str(tps)+" -fps "+IPS+" -w "+LARGEUR+" -h "+HAUTEUR+" -br "+LUMINOSITE+" -o " + VIDEO_PATH + "temp.h264")
    ret += os.system("MP4Box -add " + VIDEO_PATH + "temp.h264 "+ VIDEO_PATH + nomVideo+".mp4")
    ret += os.system("rm " + VIDEO_PATH + "temp.h264")

    if ret != 0:
	        mail.envoyerMailErreur("Ne peut pas enregister la vidéo")

    try:
        log.video()
    except IOError:
        mail.envoyerMailErreur("Erreur dans le chemin des logs dans actions.py")


def supprimerPhoto(nom):
    '''Cette fonction permet de supprimer une photo'''
    ret = os.system("rm /home/pi/RaspiWatch/photo/"+nom)

    if ret != 0:
	        mail.envoyerMailErreur("Ne peut pas supprimer la photo")

    try:
        log.suppressionPhoto(nom)
    except IOError:
        mail.envoyerMailErreur("Erreur dans le chemin des logs dans actions.py")


def supprimerVideo(nom):
    '''Cette fonction permet de supprimer une vidéo. Il supprime aussi la miniature associé à la vidéo'''
    ret = os.system("rm /home/pi/RaspiWatch/video/"+nom)
    ret += os.system("rm /home/pi/RaspiWatch/video/miniatures/"+nom)
    if ret != 0:
	        mail.envoyerMailErreur("Ne peut pas supprimer la vidéo")

    try:
        log.suppressionVideo(nom)
    except IOError:
        mail.envoyerMailErreur("Erreur dans le chemin des logs dans actions.py")
    

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
    try:
        cfg.set('Video', 'largeur', largeur)
        cfg.set('Video', 'hauteur', hauteur)
        cfg.write(open(CONFIG_PATH,'w'))
        log.modResVideo()
    except NoSectionError:
        mail.envoyerMailErreur("Erreur dans le chemin de configuration dans actions.py")
    except IOError:
        mail.envoyerMailErreur("Erreur dans le chemin des logs dans actions.py")
         
def setIps(valeur):
    """ Change la cadence de vidéo dans la configuration. """
    if valeur < 10:
        valeur = 10
    if valeur > 30:
        valeur = 30
    cfg = ConfigParser.ConfigParser()
    cfg.read(CONFIG_PATH)
    try:
        cfg.set('Video', 'ips', valeur)
        cfg.write(open(CONFIG_PATH,'w'))
        log.modIps()
    except NoSectionError:
        mail.envoyerMailErreur("Erreur dans le chemin de configuration dans actions.py")
    except IOError:
        mail.envoyerMailErreur("Erreur dans le chemin des logs dans actions.py")

def setLuminosite(pourcentage):
    """ Change la luminosité de détection, de photo et de vidéo en prenant en paramètre le pourcentage voulu. Cette procédure
        contrôle la saisie """
    if pourcentage < 0:
        pourcentage = 0
    if pourcentage > 100:
        pourcentage = 100
    cfg = ConfigParser.ConfigParser()
    cfg.read(CONFIG_PATH)
    try:
        cfg.set('General', 'luminosite', pourcentage)
        cfg.write(open(CONFIG_PATH,'w'))
        log.modLuminosite()
    except NoSectionError:
        mail.envoyerMailErreur("Erreur dans le chemin de configuration dans actions.py")
    except IOError:
        mail.envoyerMailErreur("Erreur dans le chemin des logs dans actions.py")

def setSeuil(pourcentage):
    """ Change le seuil de détection en prenant en paramètre le pourcentage voulu. Cette procédure
        contrôle la saisie """
    if pourcentage < 0:
        pourcentage = 0
    if pourcentage > 100:
        pourcentage = 100
    cfg = ConfigParser.ConfigParser()
    cfg.read(CONFIG_PATH)
    try:
        cfg.set('Detection', 'seuil', pourcentage)
        cfg.write(open(CONFIG_PATH,'w'))
        log.modSeuil()
    except NoSectionError:
        mail.envoyerMailErreur("Erreur dans le chemin de configuration dans actions.py")
    except IOError:
        mail.envoyerMailErreur("Erreur dans le chemin des logs dans actions.py")

def getDateName():
    """ Retourne une chaine de type : "_26-01-95_12:20:30" pour faciliter le nommage des photos et des vidéos """
    maintenant = datetime.now()
    nom = "_" + str(maintenant.year) + "-" + str('%02d' % maintenant.month) + "-" + str('%02d' % maintenant.day) + "_" + str('%02d' % maintenant.hour) + ":" + str('%02d' % maintenant.minute) + ":" + str('%02d' % maintenant.second)
    return nom
    
#def videoDetec():
#    """Lance une video au moment de la detection la video durera 10sec"""
#    cfg = ConfigParser.ConfigParser()
#    cfg.read(CONFIG_PATH)
#    mouvement = cfg.get('Detection','mouvement')
#    
#    camera = picamera.PiCamera()
#    print 'Before While'
#    while mouvement : 
#        print 'Dans le while'
#        if not camera.recording :
#            print 'Dans le if'
#            nomVideo = "videoDetecAuto" + getDateName()
#            camera.start_recording(VIDEO_PATH + nomVideo + ".h264")
#        print 'Plus dans le if lol'
#        cfg.read(CONFIG_PATH)
#        mouvement = cfg.get('Detection','mouvement')
#        
#    camera.stop_recording()
#    print 'Stop video'
#    log.videoDetec()
#    time.sleep(10)

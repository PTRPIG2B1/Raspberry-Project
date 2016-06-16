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
import subprocess

#CONSTANTES
BIN_PATH = '/home/pi/RaspiWatch/bin/'
CONFIG_PATH = '/home/pi/RaspiWatch/bin/config.cfg'
PHOTO_PATH = '/home/pi/RaspiWatch/photo/'
VIDEO_PATH = '/home/pi/RaspiWatch/video/'
MINIATURES_PATH = '/home/pi/RaspiWatch/video/miniatures/'


def executerCommande(cmd):
    '''Cette procédure permet d'éxécuter une commande plus proprement qu'avec os.system. On peut retrouver les erreurs grave au code de retour.'''
    cmd = cmd.split(" ")
    #Exécution de la commande
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    #Attente de la fin de l'exec, puis récupération des retours (STDOUT et STDERR)
    rc = 0
    if "detec.py" not in cmd[1]:
        out, err = p.communicate()

        rc = p.returncode

    #Un code de retour différent de 0 signifie qu'il y a eu une erreur
        if rc != 0:
            mail.envoyerMailErreur("Code retour : " + str(rc) + " --- STDOUT : " + str(out) + " --- STDERR : " + str(err))
    return rc

def ecrireConfig(section, key, value):
    cfg = ConfigParser.ConfigParser()
    cfg.read(CONFIG_PATH)
    try:
        cfg.set(section, key, value)
        cfg.write(open(CONFIG_PATH,'w'))
    except:
        mail.envoyerMailErreur("Erreur dans le chemin de configuration dans actions.py")


def lireConfig(section, key):
    val = 0
    try:
        cfg = ConfigParser.ConfigParser()
        cfg.read(CONFIG_PATH)
        val = cfg.get(section, key)
    except:
        mail.envoyerMailErreur("Erreur dans le chemin de configuration dans actions.py")
    return val


def demarrerDetec():
    """ Execute le script de détection """
    print 'Demarrage de la detection ...'
    ecrireConfig('Detection', 'enmarche', 'True')
    rc = executerCommande("python "+BIN_PATH+"detec.py &")
    if rc == 0:
        log.demDetect()
    


def arreterDetec():
    """ Arrête la détection de mouvement en changeant la valeur "en marche" dans la config """
    print 'Arret de la detection ...'
    ecrireConfig('Detection', 'enmarche', 'False')
    log.arrDetect()



def prendrePhoto():
    """ Prend une photo, la nomme avec la date et l'heure, et la place dans le dossier RaspiWatch/photo """
    nomPhoto = "photo" + getDateName() + ".jpg"
    print 'Prise de la photo ...'
  
    LARGEUR = lireConfig('Video', 'largeur')
    HAUTEUR = lireConfig('Video', 'hauteur')
    LUMINOSITE = lireConfig('General','luminosite')

    rc = executerCommande("raspistill -t 500 -w "+LARGEUR+" -h "+HAUTEUR+" -br "+LUMINOSITE+" -o " + PHOTO_PATH + nomPhoto)

    if rc == 0:
        log.photo()



def prendreVideo(secondes):
    """ Prend une video, la nomme avec la date et l'heure, et la place dans le dossier RaspiWatch/video
        Prend aussi la miniature correspondante à la vidéo, et la place dans RaspiWatch/video/miniatures """
    tps = int(secondes)*1000
    maintenant = datetime.now()
    nomVideo = "video" + getDateName()
    print 'Prise de la miniature ...'

    LARGEUR = lireConfig('Video', 'largeur')
    HAUTEUR = lireConfig('Video', 'hauteur')
    LUMINOSITE = lireConfig('General','luminosite')
    IPS = lireConfig('Video','ips')


    rc = executerCommande("raspistill -t 100 -w "+LARGEUR+" -h "+HAUTEUR+" -br "+LUMINOSITE+" -o " + MINIATURES_PATH + nomVideo + ".jpg")
    print 'Enregistrement de la video ...'
    #executerCommande("raspivid -t 5000 -fps 30 -w 640 -h 480 -br 50 -o test.h264")
    rc += executerCommande("raspivid -t "+str(tps)+" -fps "+IPS+" -w "+LARGEUR+" -h "+HAUTEUR+" -br "+LUMINOSITE+" -o " + VIDEO_PATH + "temp.h264")
    rc += executerCommande("MP4Box -add " + VIDEO_PATH + "temp.h264 "+ VIDEO_PATH + nomVideo+".mp4")
    rc += executerCommande("rm " + VIDEO_PATH + "temp.h264")

    if rc == 0:
        log.video()


def supprimerPhoto(nom):
    '''Cette fonction permet de supprimer une photo'''
    rc = executerCommande("rm /home/pi/RaspiWatch/photo/"+nom)

    if rc == 0:
        log.suppressionPhoto(nom)
 


def supprimerVideo(nom):
    '''Cette fonction permet de supprimer une vidéo. Il supprime aussi la miniature associé à la vidéo'''
    rc = executerCommande("rm /home/pi/RaspiWatch/video/"+nom)
    rc += executerCommande("rm /home/pi/RaspiWatch/video/miniatures/"+nom)
    if rc == 0:
        log.suppressionVideo(nom)

    

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
    ecrireConfig('Video', 'largeur', largeur)
    ecrireConfig('Video', 'hauteur', hauteur)
    
    log.modResVideo()

         
def setIps(valeur):
    """ Change la cadence de vidéo dans la configuration. """
    if valeur < 10:
        valeur = 10
    if valeur > 30:
        valeur = 30
    ecrireConfig('Video', 'ips', valeur)
    log.modIps()

def setLuminosite(pourcentage):
    """ Change la luminosité de détection, de photo et de vidéo en prenant en paramètre le pourcentage voulu. Cette procédure
        contrôle la saisie """
    if pourcentage < 0:
        pourcentage = 0
    if pourcentage > 100:
        pourcentage = 100

    ecrireConfig('General', 'luminosite', pourcentage)

    log.modLuminosite()


def setSeuil(pourcentage):
    """ Change le seuil de détection en prenant en paramètre le pourcentage voulu. Cette procédure
        contrôle la saisie """
    if pourcentage < 0:
        pourcentage = 0
    if pourcentage > 100:
        pourcentage = 100

    ecrireConfig('Detection', 'seuil', pourcentage)

    log.modSeuil()


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

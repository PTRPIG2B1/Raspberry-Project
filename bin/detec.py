#!/usr/bin/env python
# -*- coding: utf-8 -*-

# imports
from PIL import Image
import math
import sys
import time
import os
import mail
import ConfigParser
import actions
import log

# Declaration CONSTANTES / variables
#Lire les valeurs dans les fichiers

CONFIG_PATH = '/home/pi/RaspiWatch/bin/config.cfg'
IMAGE1_PATH='/home/pi/RaspiWatch/bin/image1.jpg'
IMAGE2_PATH='/home/pi/RaspiWatch/bin/image2.jpg'
IMAGEMOUVEMENT_PATH='/home/pi/RaspiWatch/photo/Image_Mouvement_'+actions.getDateName()+'.jpg'

cfg = ConfigParser.ConfigParser()
cfg.read(CONFIG_PATH)
try:
    SEUIL_CONF = cfg.get('Detection', 'seuil')
except NoSectionError:
    SEUIL_CONF = 50
    print "Erreur de configuration, utilisation du seuil défaut (50)"
LARGEUR = 640
HAUTEUR = 480

os.system('raspistill -w '+str(LARGEUR)+' -h '+str(HAUTEUR)+' -t 500 -o '+IMAGE1_PATH)
os.system('raspistill -w '+str(LARGEUR)+' -h '+str(HAUTEUR)+' -t 500 -o '+IMAGE2_PATH)

enFonctionnement = 'True'
while enFonctionnement == 'True' : 
    image1 = Image.open(IMAGE1_PATH)
    image2 = Image.open(IMAGE2_PATH)
    rgb_im1 = image1.convert('RGB')
    rgb_im2 = image2.convert('RGB')
    
    nbMouvement = 0
    
    for i in range (0,30):
      ligne = i*LARGEUR/30
      for j in range (0,30):
        colonne = j*HAUTEUR/30
        difference = 0
	for k in range(0, (LARGEUR/30)/5):	
          for l in range(0,(HAUTEUR/30)/5):
            (rouge1,vert1,bleu1) = rgb_im1.getpixel((k+ligne,l+colonne))
            (rouge2,vert2,bleu2) = rgb_im2.getpixel((k+ligne,l+colonne))
            difference += math.fabs(rouge1-rouge2)+math.fabs(vert1-vert1)+math.fabs(bleu1-bleu2)

        if difference > 1500 + 1500*(50-int(SEUIL_CONF))/100:
            #print "Mouvement"
            nbMouvement = nbMouvement + 1 
       # print "Zone ("+str(i)+","+str(j)+") : "+str(difference)
    if nbMouvement > 5 :
        print "Mouvement"
        log.mouvement()
        actions.prendreVideo(10)
        os.system('cp '+IMAGE2_PATH+' '+IMAGEMOUVEMENT_PATH)    
        os.system('raspistill -w '+str(LARGEUR)+' -h '+str(HAUTEUR)+' -t 500 -o '+IMAGE1_PATH)
        os.system('raspistill -w '+str(LARGEUR)+' -h '+str(HAUTEUR)+' -t 500 -o '+IMAGE2_PATH)
    else :
        os.system('mv '+IMAGE2_PATH+' '+IMAGE1_PATH)
        os.system('raspistill -w '+str(LARGEUR)+' -h '+str(HAUTEUR)+' -t 500 -o '+IMAGE2_PATH)
    
    cfg.read(CONFIG_PATH)
    try:
        enFonctionnement = cfg.get('Detection', 'enmarche')
    except NoSectionError:
        mail.envoyerMailErreur("ERREUR : Configuration de config.cfg dans detec.py. Arrêt de la détection")
        exit()
    
os.system('rm '+IMAGE1_PATH+' && rm '+IMAGE2_PATH)


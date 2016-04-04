#!/usr/bin/env python
# -*- coding: utf-8 -*-

# imports
from PIL import Image
import math
import sys
import time
import os
import ConfigParser

# Declaration CONSTANTES / variables
difference = 0
WIDTH = 640
HEIGHT = 480
SLEEPTIME = 5000

SEUILMIN = 100000
SEUILMAX = 2000000
SEUILECART = SEUILMAX - SEUILMIN


cfg = ConfigParser.ConfigParser()
cfg.read('config.cfg')

enFonctionnement = cfg.get('Section1', 'detectEnMarche')

SEUILCONF = cfg.get('Section1', 'seuil')
SEUIL = (SEUILCONF/100*SEUILECART + SEUILMIN)

os.system('raspistill -w '+str(WIDTH)+' -h '+str(height)+' -o image1.jpg')
os.system('raspistill -w '+str(WIDTH)+' -h '+str(height)+' -o image2.jpg')

while enFonctionnement == 'True' : 
    image1 = Image.open("photo1.jpg")
    image2 = Image.open("photo2.jpg")
    rgb_im1 = image1.convert('RGB')
    rgb_im2 = image2.convert('RGB')
    
    for i in range (0,10):
      ligne = i*WIDTH/10
      for j in range (0,10):
        colonne = j*HEIGHT/10
        difference = 0
        for k in range (0,(WIDTH/10-1)):
          for l in range(0,(HEIGHT/10-1)):
            (rouge1,vert1,bleu1) = rgb_im1.getpixel((k+ligne,l+colonne))
            (rouge2,vert2,bleu2) = rgb_im2.getpixel((k+ligne,l+colonne))
            difference += math.fabs(rouge1-rouge2)
            difference += math.fabs(vert1-vert1)
            difference += math.fabs(bleu1-bleu2)

    
        print "Zone ("+str(i)+","+str(j)+") : "+str(difference)
    
    os.system('mv image2.jpg image1.jpg')
    os.system('raspistill -w '+str(WIDTH)+' -h '+str(height)+' -o image2.jpg')
    
    cfg.read('config.cfg')
    enFonctionnement = cfg.get('Section1', 'detectEnMarche')
    time.sleep(SLEEPTIME)

os.system('rm image1.jpg && rm image2.jpg')



#Fonction decomparaison retourne un booleen (true si mouvement)

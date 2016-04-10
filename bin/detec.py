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
SLEEPTIME = 1
SEUILMIN = 100000
SEUILMAX = 2000000
SEUILECART = SEUILMAX - SEUILMIN

CONFIGPATH = '/home/pi/RaspiWatch/bin/config.cfg'
SECTIONVIDEO ='Section1'
IMAGE1PATH='/home/pi/RaspiWatch/bin/image1.jpg'
IMAGE2PATH='/home/pi/RaspiWatch/bin/image2.jpg'

cfg = ConfigParser.ConfigParser()
cfg.read(CONFIGPATH)
cfg.set(SECTIONVIDEO,'detectenmarche','True')
cfg.write(open(CONFIGPATH, 'w'))

enFonctionnement = cfg.get(SECTIONVIDEO, 'detectenmarche')


SEUILCONF = cfg.get(SECTIONVIDEO, 'seuil')
SEUIL = (int(SEUILCONF)/100*SEUILECART + SEUILMIN)

os.system('raspistill -w '+str(WIDTH)+' -h '+str(HEIGHT)+' -t 500 -o '+IMAGE1PATH)
os.system('raspistill -w '+str(WIDTH)+' -h '+str(HEIGHT)+' -t 500 -o '+IMAGE2PATH)

while enFonctionnement == 'True' : 
    image1 = Image.open(IMAGE1PATH)
    image2 = Image.open(IMAGE2PATH)
    rgb_im1 = image1.convert('RGB')
    rgb_im2 = image2.convert('RGB')
    
    nbMouvement = 0
    
    for i in range (0,10):
      ligne = i*WIDTH/10
      for j in range (0,10):
        colonne = j*HEIGHT/10
        difference = 0
	for k in range(0, (WIDTH/10-1)/3):	
          for l in range(0,(HEIGHT/10-1)/3):
            (rouge1,vert1,bleu1) = rgb_im1.getpixel((k+ligne,l+colonne))
            (rouge2,vert2,bleu2) = rgb_im2.getpixel((k+ligne,l+colonne))
            difference += math.fabs(rouge1-rouge2)+math.fabs(vert1-vert1)+math.fabs(bleu1-bleu2)

        if difference > 10000 :
            #print "Mouvement"
            nbMouvement = nbMouvement + 1 
       # print "Zone ("+str(i)+","+str(j)+") : "+str(difference)
    if nbMouvement > 20 :
        print "Mouvement"
        
    os.system('mv '+IMAGE2PATH+' '+IMAGE1PATH)
    os.system('raspistill -w '+str(WIDTH)+' -h '+str(HEIGHT)+' -t 500 -o '+IMAGE2PATH)
    
    cfg.read(CONFIGPATH)
    enFonctionnement = cfg.get(SECTIONVIDEO, 'detectenmarche')
    #time.sleep(SLEEPTIME)

os.system('rm '+IMAGE1PATH+' && rm '+IMAGE2PATH)



#Fonction decomparaison retourne un booleen (true si mouvement)

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


cfg = ConfigParser.ConfigParser()
cfg.read('config.cfg')
cfg.set('Section1','detectenmarche','True')
cfg.write(open('config.cfg', 'w'))

enFonctionnement = cfg.get('Section1', 'detectenmarche')


SEUILCONF = cfg.get('Section1', 'seuil')
SEUIL = (int(SEUILCONF)/100*SEUILECART + SEUILMIN)

os.system('raspistill -w '+str(WIDTH)+' -h '+str(HEIGHT)+' -t 500 -o image1.jpg')
os.system('raspistill -w '+str(WIDTH)+' -h '+str(HEIGHT)+' -t 500 -o image2.jpg')

while enFonctionnement == 'True' : 
    image1 = Image.open("image1.jpg")
    image2 = Image.open("image2.jpg")
    rgb_im1 = image1.convert('RGB')
    rgb_im2 = image2.convert('RGB')
    list1 = list(image1.getdata())
    list2 = list(image2.getdata())
    print list1[0]
    print list1[0][0]
    print list1[0][2]
    nbMouvement = 0
    
    for i in range (0,10):
      for j in range (0,10):
        difference = 0
        for k in range (0,(HEIGHT/10)):
            (rouge1,vert1,bleu1) = list1[]
            (rouge2,vert2,bleu2) = rgb_im2.getpixel((k+ligne,l+colonne))
            difference += math.fabs(rouge1-rouge2)+math.fabs(vert1-vert1)+math.fabs(bleu1-bleu2)

        if difference > 100000 :
            #print "Mouvement"
            nbMouvement = nbMouvement + 1 
            #print "Zone ("+str(i)+","+str(j)+") : "+str(difference)
    if nbMouvement > 20 :
        print "Mouvement"
        
    os.system('mv image2.jpg image1.jpg')
    os.system('raspistill -w '+str(WIDTH)+' -h '+str(HEIGHT)+' -t 500 -o image2.jpg')
    
    cfg.read('config.cfg')
    enFonctionnement = cfg.get('Section1', 'detectenmarche')
    #time.sleep(SLEEPTIME)

os.system('rm image1.jpg && rm image2.jpg')



#Fonction decomparaison retourne un booleen (true si mouvement)

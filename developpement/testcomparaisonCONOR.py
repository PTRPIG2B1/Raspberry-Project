#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from PIL.Image import *
from PIL import Image
import math
import sys

#Note impossible de faire deux imports
#Impossible de faire new ET getpixel
constSeuil = 1000
Seuil = 0.5
difference = 0
vert = 0
rouge = 0
bleu = 0

try:
  image1 = Image.open("image1.png")
except IOError:
  print 'Erreur sur ouverture du fichier ' 
  sys.exit(1)

try:
  image2 = Image.open("image2.png")
except IOError:
  print 'Erreur sur ouverture du fichier ' 
  sys.exit(1)

rgb_im1 = image1.convert('RGB')
rgb_im2 = image2.convert('RGB')

#erreur si les deux images sont de tailles différentes, !!! à coder plus tard !!!
if rgb_im1.size != rgb_im2.size:
  print 'Erreur, images de tailles différentes' 
  sys.exit(1)
  
WIDTH = rgb_im1.size[0]
HEIGHT = rgb_im1.size[1]

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
      



#!/usr/bin/python2
# -*- coding: utf-8 -*-

import ConfigParser
import sys
import os
import actions

#Le chemin vers la config doit etre absolu
CONFIG_PATH='/home/pi/RaspiWatch/bin/config.cfg'

#Parse d'arguments dans un tableau args
str = sys.argv[1]
temp = str.split('&')
temp = [i.split('=') for i in temp]
args = []
for i in temp:
    args += i

action = args[0]

if action == "off":
    actions.arreterDetec()
elif action == "on":
    actions.demarrerDetec()
elif action == "photo":
    actions.prendrePhoto()
elif action == "video":
    duree = args[3]
    actions.prendreVideo(duree)
elif action == "delphoto":
    nom = args[1]
    actions.supprimerPhoto(nom)
elif action == "delvideo":
    nom = args[1]
    actions.supprimerVideo(nom)
else:
    for i in range(0,len(args)-1,2):

        action = args[i]
        if action == "res":
            actions.setResVideo(args[i+1])
            #actions.setResPhoto(args[i+1])
                
        elif action == "ips":
            actions.setIps((int)(args[i+1]))
            
        elif action == "seuil":
            actions.setSeuil((int)(args[i+1]))
            
        elif action == "lum":
            actions.setLuminosite((int)(args[i+1]))

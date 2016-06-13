#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import os
import getpass
import smtplib
import subprocess
from time import gmtime, strftime


#CONSTANTES
CONFIG_PATH = '/home/pi/RaspiWatch/bin/config.cfg'

GMAIL_USER = "ptrpig2b1@gmail.com"
GMAIL_PWD = "groupeg2b"

cfg = ConfigParser.ConfigParser()
cfg.read(CONFIG_PATH)

GMAIL_TO = cfg.get('Email', 'email')

def envoyerEmail(objet, corps, mailtype):
    FROM = GMAIL_USER
    TO = GMAIL_TO if type(GMAIL_TO) is list else [GMAIL_TO]
    SUBJECT = objet
    TEXT = corps

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PWD)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'Mail envoyé, type : ' + mailtype
    except:
        print "Erreur de l'envoi du mail, type : " + mailtype

def getIp():

	ips = "Local : " + subprocess.check_output("hostname -I", shell=True)
	ips += "Extérieur : " + subprocess.check_output("wget http://ipecho.net/plain -O - -q", shell=True)
	return ips

def envoyerMailErreur(corps):
	envoyerEmail('Erreur RaspiWatch', corps, 'ERREUR')

def envoyerMailDetection():
	corps = 'Détection le : ' + strftime("%d-%m-%Y à %H:%M:%S", gmtime()) +'.\n'
	corps += 'Consulter les vidéos/photos avec ces IP :\n' + getIp()
	envoyerEmail('Détection RaspiWatch', corps, 'DETECTION')

def envoyerMailIP():
	corps = "Vos IP :\n"
	corps += getIp()
	envoyerEmail('Vos IPs de connexion RaspiWatch', corps, 'IP')


envoyerMailIP()

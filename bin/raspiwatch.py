import os
import ConfigParser
import sys

#Fonctions et procedure
def affmenuprincipalActif():
	print '////////////////MENU PRINCIPAL RASPBERRY////////////////\n'
	print '\t   Etat de la detection : active'
	print '\t   1- Prendre une photo'
	print '\t   2- Prendre une video'
	print '\t   3- Redemarrer la detection'
	print '\t   4- Arreter la detection'
	print '\t   5- Changer la configuration'
	print '\t   6- Charger la configuration'
	print '\t   0- Quitter\n'
	print '////////////////////////////////////////////////////////'
	print 'Votre choix : '

def affmenuprincipalInactif():
	print '////////////////MENU PRINCIPAL RASPBERRY////////////////\n'
	print '\t   Etat de la detection : inactive'
	print '\t   1- Prendre une photo'
	print '\t   2- Prendre une video'
	print '\t   3- Lancer la detection'
	print '\t   4- Changer la configuration'
	print '\t   5- Charger la configuration'
	print '\t   0- Quitter\n'
	print '////////////////////////////////////////////////////////'
	print 'Votre choix : '

def affmenuconfiguration():
	print '//////////////////MENU DE CONFIGURATION/////////////////\n'
	print '\t   Quel parametre voulez-vous modifier ?'
	print '\t   1- Resolution (' + str(width)+'*'+ str(height) +')'
	print '\t   2- Images par secondes (' + str(fps) +')'
	print '\t   3- Seuil de detection (' + str(seuil) +'%)'
	print '\t   4- Luminosite (' + str(luminosite) + '%)'
	print '\t   5- Retablir la configuration par defaut'
	print '\t   0- Retour au menu principal\n'
	print '////////////////////////////////////////////////////////'
	print 'Votre choix : '

def affmenuresolution():
	print '//////////////////MENU CHGMT RESOLUTION//////////////////\n'
	print '\t   1- 1920*1080 (1080p)'
	print '\t   2- 1280*720 (720p)'
	print '\t   3- 640*480 (480p)'
	print '\t   0- Quitter\n'
	print '////////////////////////////////////////////////////////'
	print 'Votre choix : '

def affmenufps():
	print '/////////////////////MENU CHGMT FPS/////////////////////\n'
	print '\t   1- 30 FPS'
	print '\t   2- 25 FPS'
	print '\t   3- 20 FPS'
	print '\t   4- 15 FPS'
	print '\t   0- Quitter\n'
	print '////////////////////////////////////////////////////////'
	print 'Votre choix : '

def sauvegarderConfiguration():
	cfg.write(open('config.cfg','w'))



















#Debut du programme
if not os.path.isfile('config.cfg'):
	os.system("python makeconfig.py")
	
choix = '1'

cfg = ConfigParser.ConfigParser()
cfg.read('config.cfg')
#print cfg.items('Section1')


detectEnMarche = cfg.get('Section1', 'detectEnMarche')
height = cfg.get('Section1', 'height')
width = cfg.get('Section1', 'width')
fps = cfg.get('Section1', 'fps')
seuil = cfg.get('Section1', 'seuil')
luminosite = cfg.get('Section1', 'luminosite')
os.system("clear")

#print detectEnMarche


while (choix != '0') :
	#Changement de dossier pour se positionner dans le repertoire ou seront tous les prorgrammes (c'est bcp plus propre)
	#os.system("cd ./Users/pi/")
	#os.system("clear")
	if (detectEnMarche == 'True'):
		affmenuprincipalActif()
		choix = raw_input("")
		while (len(choix)==0):
			print 'Merci d\'effectuer une saisie'
			choix = raw_input("")
		
		os.system("clear")

		if (choix == '1'):
			print 'Prise de la photo ...'
			os.system("raspistill -t 100 -o photo.jpg")
		elif (choix == '2'):
			print 'Enregistrement de la video ...'
			tps = input("Combien de temps ?(en s)")
			tps = tps*1000
			cmd = "raspivid -o video.h264 -t " + str(tps)
			os.system(cmd)
		elif (choix == '3'):
			print 'Redemarrage de la detection ...'
		elif (choix == '4'):
			print 'Arret de la detection ...'
			detectEnMarche = False
			cfg.set('Section1', 'detectEnMarche', 'False')
			cfg.write(open('config.cfg','w'))
		elif (choix == '5'):
			choixconf = '1'

			while(choixconf != '0'):

				affmenuconfiguration()

				choixconf = raw_input()
				while not choixconf:
					print 'Merci d\'effectuer une saisie'
					choixconf = raw_input()

				os.system("clear")

				if (choixconf == '1'):
					print 'Changement de la resolution :'
					choixres = '1'
					while (choixres != '0'):
						affmenuresolution()

						choixres = raw_input()
						while not choixres:
							print 'Merci d\'effectuer une saisie'
							choixres = raw_input()

						os.system("clear")
						if (choixres == '1'):
							width = 1920
							height = 1080
						elif (choixres == '2'):
							width = 1280
							height = 720
						elif (choixres == '3'):
							width = 640
							height = 480
						else :
							print 'Erreur de saisie'
						cfg.set('Section1', 'width', width)
						cfg.set('Section1', 'height', height)
						choixres = '0'
						os.system("clear")
				elif (choixconf == '2'):
					affmenufps()

					choixfps = raw_input("Saisir le nombres d'images par secondes : ")
					while not choixfps:
						print 'Merci d\'effectuer une saisie'
						choix = raw_input("Saisir le nombres d'images par secondes : ")

					if (choixfps == '1'):
						fps = 30
					elif (choixfps == '2'):
						fps = 25
					elif (choixfps == '3'):
						fps = 20
					elif (choixfps == '4'):
						fps = 15
					else : 
						print 'Erreur de choix'
					cfg.set('Section1', 'fps', fps)
					os.system("clear")
				elif (choixconf == '3'):
					print 'Modification du seuil'
					seuil = input("Saisir le seuil en % : ")
					cfg.set('Section1', 'seuil', seuil)
				elif (choixconf == '4'):
					print 'Modification de la luminosite'
					luminosite = input("Saisir la luminosite en % : ")
					cfg.set('Section1', 'luminosite', luminosite)
				elif (choixconf == '0'):
					print 'Retour au menu principal ...'
				else :
					print 'Erreur de valeur saisie'
			cfg.write(open('config.cfg','w'))
		elif (choix == '6'):
			print 'Chargement de la configuration ...'
		elif (choix == '0'):
			print 'Au revoir ...'
		else :
			print 'Erreur de valeur saisie'







	else :
		affmenuprincipalInactif()
		choix = raw_input()
		while not choix:
			print 'Merci d\'effectuer une saisie'
			choix = raw_input()

		os.system("clear")
		if (choix == '1'):
			print 'Prise de la photo ...'
			os.system("raspistill -t 100 -o photo.jpg")
		elif (choix == '2'):
			print 'Enregistrement de la video ...'
			tps = input("Combien de temps ?(en s)")
			tps = tps*1000
			cmd = "raspivid -o video.h264 -t " + str(tps)
			os.system(cmd)
		elif (choix == '3'):
			print 'Demarrage de la detection ...'
			detectEnMarche = True
			cfg.set('Section1', 'detectEnMarche', detectEnMarche)
			cfg.write(open('config.cfg','w'))
			os.system("python detec.py &")
			detectEnMarche = 'True'			
		elif (choix == '4'):
			choixconf = '1'
			while(choixconf != '0'):
				affmenuconfiguration()
				choixconf = raw_input()
				while not choixconf:
					print 'Merci d\'effectuer une saisie'
					choixconf = raw_input()

				os.system("clear")

				if (choixconf == '1'):
					print 'Changement de la resolution :'
					choixres = '1'
					while (choixres != '0'):

						affmenuresolution()

						choixres = raw_input()
						while not choixres:
							print 'Merci d\'effectuer une saisie'
							choixres = raw_input()

						if (choixres == '1'):
							width = 1920
							height = 1080
						elif (choixres == '2'):
							width = 1280
							height = 720
						elif (choixres == '3'):
							width = 640
							height = 480
						elif (choixres == '0'):
							print 'Retour a la configuration ..'
						else :
							print 'Erreur de saisie'
						cfg.set('Section1', 'width', width)
						cfg.set('Section1', 'height', height)
						choixres = '0'
						os.system("clear")
				elif (choixconf == '2'):
					affmenufps()

					choixfps = raw_input("Saisir le nombres d'images par secondes : ")
					while not choixfps:
						print 'Merci d\'effectuer une saisie'
						choix = raw_input("Saisir le nombres d'images par secondes : ")

					if (choixfps == '1'):
						fps = 30
					elif (choixfps == '2'):
						fps = 25
					elif (choixfps == '3'):
						fps = 20
					elif (choixfps == '4'):
						fps = 15
					else : 
						print 'Erreur de choix'
					cfg.set('Section1', 'fps', fps)
					os.system("clear")
				elif (choixconf == '3'):
					print 'Modification du seuil'
					seuil = input("Saisir le seuil en % : ")
					cfg.set('Section1', 'seuil', seuil)
				elif (choixconf == '4'):
					print 'Modification de la luminosite'
					luminosite = input("Saisir la luminosite en % : ")
					cfg.set('Section1', 'luminosite', luminosite)
				elif (choixconf == '5'):
					print 'Reinitialisation ...'
					os.system("python makeCFG.py")
				elif (choixconf == '0'):
					print 'Retour au menu principal ...'
				else :
					print 'Erreur de valeur saisie'
			cfg.write(open('config.cfg','w'))
		elif (choix == '5'):
			print 'Chargement de la configuration ...'	
		elif (choix == '0'):
			print 'Au revoir ...'
		else :
			print 'Erreur de valeur saisie'


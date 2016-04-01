#Les importations 
import os
import time
import ConfigParser
from PIL import Image

#Declaration des variables
#enFonctionnement = True

#Debut du programme

cfg = ConfigParser.ConfigParser()
cfg.read('config.cfg')

enFonctionnement = cfg.get('Section1', 'detectEnMarche')

#Rajouter la gestion des erreurs (probleme camera)
#im = Image.new("RGB", (500,500), "red")
#im.save("imagecree.png", format="png")
while enFonctionnement == 'True' :
	os.system('raspistill -o photo1.jpg -t 500')
	while enFonctionnement == 'True' : 
		os.system('raspistill -o photo2.jpg -t 500')
		image1 = Image.open("photo1.jpg")
		image2 = Image.open("photo2.jpg")
		cfg.read('config.cfg')
		enFonctionnement = cfg.get('Section1', 'detectEnMarche')
		os.system('mv photo1.jpg temp')
		os.system('mv photo2.jpg photo1.jpg')
	os.system('rm temp')  
	os.system('rm photo1.jpg')
      



#Fonction decomparaison retourne un booleen (true si mouvement)

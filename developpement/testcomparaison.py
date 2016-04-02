#from PIL.Image import *
from PIL import Image

#Note impossible de faire deux imports
#Impossible de faire new ET getpixel
constSeuil = 1000
Seuil = 0.5
res1 = 0
res2 = 0
vert = 0
rouge = 0
bleu = 0
width = 640
height = 480

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




for i in range (0,10):
  ligne = i*width/10
  for j in range (0,10):
    colonne = j*height/10
    zoneVert1=0
    zoneRouge1=0
    zoneBleu1=0
    zoneVert2=0
    zoneBleu2=0
    zoneRouge2=0
    for k in range (0,63):
      for l in range(0,47):
        (rouge1,vert1,bleu1) = rgb_im1.getpixel((k+ligne,l+colonne))
        (rouge2,vert2,bleu2) = rgb_im2.getpixel((k+ligne,l+colonne))
        zoneRouge1=zoneRouge1+rouge1
        zoneRouge2=zoneRouge2+rouge2
        zoneVert1=zoneVert1+vert1
        zoneVert2=zoneVert2+vert2
        zoneBleu1=zoneBleu1+bleu1
        zoneBleu2=zoneBleu2+bleu2
    if(zoneVert2<=zoneVert1+zoneVert1*(Seuil) and zoneVert2>=zoneVert1-zoneVert1*(Seuil)):
      vert = 0
    else:
      vert = abs(zoneVert2-zoneVert1)

    if(zoneRouge2<=zoneRouge1+zoneRouge1*(Seuil) and zoneRouge2>=zoneRouge1-zoneRouge1*(Seuil)):
      rouge= 0
    else:
      rouge= abs(zoneRouge2-zoneRouge1)

    if(zoneBleu2<=zoneBleu1+zoneBleu1*(Seuil) and zoneBleu2>=zoneBleu1-zoneBleu1*(Seuil)):
      bleu = 0
    else:
      bleu = abs(zoneBleu2-zoneBleu1)
				
    res = vert+bleu+rouge 
    
    if res == 0:
      print "pas de mouv"
    else:
      print "mouv"
      



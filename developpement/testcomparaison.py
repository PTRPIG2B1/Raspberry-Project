#from PIL.Image import *
from PIL import Image

#Note impossible de faire deux imports
#Impossible de faire new ET getpixel

SEUIL = 20
res1 = 0
res2 = 0
width = 640
height = 480

image1 = Image.new("RGB", (width,height), "white")
image2 = Image.new("RGB", (width,height), "red")

image1.save("image1.png", format="png")
image2.save("image2.png", format="png")

data1 = image1.getdata()
type(data1)

data2 = image2.getdata()
type(data2)

l1 = list(data1)
l2 = list(data2)

for i in range (0,9):
  ligne = i*width/10
  for j in range (0,9):
    colonne = j*height/10
    for k in range (0,63):
      for l in range(0,47):
        (rouge1,vert1,bleu1) = image1.getpixel((k+ligne,l+colonne))
        (rouge2,vert2,bleu2) = image2.getpixel((k+ligne,l+colonne))
        res1 = res1 + rouge1 + vert1 + bleu1
        res2 = res2 + rouge2 + vert2 + bleu2
res = abs(res2 - res1)
print(res)

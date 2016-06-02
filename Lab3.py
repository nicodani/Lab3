from SimpleCV import * ## Se cargan paquetes de SimpleCV en python
import time ##importamos tiempo

##
## BLOBS
##

img=Image("foto555.jpg") ##Carga imagen en img
(red, green, blue)=img.splitChannels(False) ## Separa los canales RGB de la imagen
red.save("imgred.jpg") ## Se guarda canal rojo de la imagen 
green.save("imggreen.jpg") ## Se guarda canal verde de la imagen
blue.save("imgblue.jpg") ## Se guarda canal azul de la imagen
imggreen1=Image("imggreen.jpg") ##Carga la imagen del canal verde en imggreen1
##Comando Blobs con binarize en imagen  aplicada con canal verde
imginvgreen1=imggreen1.binarize() ## se convierte imagen a blanco y negro
blobs1=imginvgreen1.findBlobs() ## se buscan los grupos de pixeles
blobs1.draw((200,0,0),width=3) ## se dibujan los grupos en la imagen binarizada
img.addDrawingLayer(imginvgreen1.dl()) ## se dibujan en la imagen original
img.save("FBbingreen.jpg") ## se guarda imagen original con la deteccion
img=Image("foto555.jpg") ##Carga imagen en img
imgred1=Image("imgred.jpg") ##Carga imagen del canal rojo en imgred1
##Comando Blobs con binarize en imagen aplicada con canal rojo
imginvred1=imgred1.binarize() ## se convierte imagen a blanco y negro
blobs2=imginvred1.findBlobs() ## se buscan los grupos de pixeles
blobs2.draw((200,0,0),width=3) ## se dibujan los grupos en la imagen binarizada
img.addDrawingLayer(imginvred1.dl()) ## se dibujan en la imagen original
img.save("FBbinred.jpg") ## se guarda imagen original con la deteccion
img=Image("foto555.jpg") ##Carga imagen en img
imgblue1=Image("imgblue.jpg") ##Carga imagen del canal azul en imgblue1
##Comando Blobs con binarize en imagen aplicada con canal azul
imginvblue1=imgblue1.binarize() ## se convierte imagen a blanco y negro
blobs3=imginvblue1.findBlobs() ## se buscan los grupos de pixeles
blobs3.draw((200,0,0),width=3) ## se dibujan los grupos en la imagen binarizada
img.addDrawingLayer(imginvblue1.dl()) ## se dibujan en la imagen original
img.save("FBbinblue.jpg") ## se guarda imagen original con la deteccion
##Comando Blobs con binarize en imagen aplicada a escala de grises
img=Image("foto555.jpg") ##Carga imagen en img
imggray=img.grayscale() ## Aplica escala de grises a la imagen
imggray1=imggray.binarize() ## se convierte imagen a blanco y negro
blobs4=imggray1.findBlobs() ## se buscan los grupos de pixeles
blobs4.draw((200,0,0),width=3) ## se dibujan los grupos en la imagen binarizada
img.addDrawingLayer(imggray1.dl()) ## se dibujan en la imagen original
img.save("FBbingray.jpg") ## se guarda imagen original con la deteccion


##
##  COLOR DISTANCE CON BLOBS
##


##Comando Blobs para color especifico con imagen invertida para imagen original
img=Image("foto555.jpg") ##Carga imagen en img
imginvCS=img.invert() ## La imagen original se invierte
imgdist=imginvCS.colorDistance((65,32,32)) ## Calcula la distancia del color que se le da con respecto al color de cada pixel de la imagen y se invierte
blobs5=imgdist.findBlobs() ## Se buscan los grupos de pixeles
blobs5.draw((200,0,0),width=3) ## Se dibujan los grupos en rojo sobre la imagen de tipo FeatureSet
img.addDrawingLayer(imgdist.dl()) ## se dibujan sobre la imagen original
img.save("FBSCimgdistinv.jpg") ## se guarda imagen original con la deteccion

##
##  CANNY
##

img=Image("foto555.jpg") ##Carga imagen en img
(R,G,B)=img.splitChannels(False)
imga=Image("mascara.png")
imga.resize(img.width,img.height)
## Canal Rojo
imgedges1=R.edges(t1=20,t2=60)
fin1=(imga*imgedges1)+img
fin1.save("CanRoj.jpg")
## Canal verde
imgedges2=G.edges(t1=30,t2=150)
fin2=(imga*imgedges2)+img
fin2.save("CanVer.jpg")
## Canal azul
imgedges3=B.edges(400,0)
fin3=(imga*imgedges3)+img
fin3.save("CanAzu.jpg")
## Escala de grises
imggr=img.grayscale()
imgedges4=imggr.edges(200,80)
fin4=(imga*imgedges4)+img
fin4.save("Cangris.jpg")

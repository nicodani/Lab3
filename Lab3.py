from SimpleCV import * ## Se cargan paquetes de SimpleCV en python
import time ##importamos tiempo

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

##Comando Blobs para color especifico con imagen invertida para imagen aplicada para canal verde
img=Image("foto777.jpg") ##Carga imagen en img
(red, green, blue)=img.splitChannels(False) ## Separa los canales RGB de la imagen
imginvgreen2=green.invert() ## La imagen original se invierte
greendist=imginvgreen2.colorDistance((65,32,32)) ## Calcula la distancia del color que se le da con respecto al color de cada pixel de la imagen y se invierte
blobs5=greendist.findBlobs() ## Se buscan los grupos de pixeles
blobs5.draw((200,0,0),width=3) ## Se dibujan los grupos en rojo sobre la imagen de tipo FeatureSet
img.addDrawingLayer(greendist.dl()) ## se dibujan sobre la imagen original
img.save("FBSCgreendistinv.jpg") ## se guarda imagen original con la deteccion
##Comando Blobs para color especifico con imagen invertida para imagen aplicada para canal rojo
img=Image("foto777.jpg") ##Carga imagen en img
imginvred2=red.invert() ## La imagen original se invierte
reddist=imginvred2.colorDistance((65,32,32)) ## Calcula la distancia del color que se le da con respecto al color de cada pixel de la imagen y se invierte
blobs5=reddist.findBlobs() ## Se buscan los grupos de pixeles
blobs5.draw((200,0,0),width=3) ## Se dibujan los grupos en rojo sobre la imagen de tipo FeatureSet
img.addDrawingLayer(reddist.dl()) ## se dibujan sobre la imagen original
img.save("FBSCreddistinv.jpg") ## se guarda imagen original con la deteccion
##Comando Blobs para color especifico con imagen invertida para imagen aplicada para canal azul
img=Image("foto777.jpg") ##Carga imagen en img
imginvblue2=blue.invert() ## La imagen original se invierte
bluedist=imginvblue2.colorDistance((65,32,32)) ## Calcula la distancia del color que se le da con respecto al color de cada pixel de la imagen y se invierte
blobs5=bluedist.findBlobs() ## Se buscan los grupos de pixeles
blobs5.draw((200,0,0),width=3) ## Se dibujan los grupos en rojo sobre la imagen de tipo FeatureSet
img.addDrawingLayer(bluedist.dl()) ## se dibujan sobre la imagen original
img.save("FBSCbluedistinv.jpg") ## se guarda imagen original con la deteccion
##Comando Blobs para color especifico con imagen invertida para imagen aplicada para gris
img=Image("foto777.jpg") ##Carga imagen en img
imginvgray2=blue.grayscale() ## La imagen original se invierte
graydist=imginvgray2.colorDistance((65,32,32)) ## Calcula la distancia del color que se le da con respecto al color de cada pixel de la imagen y se invierte
blobs5=graydist.findBlobs() ## Se buscan los grupos de pixeles
blobs5.draw((200,0,0),width=3) ## Se dibujan los grupos en rojo sobre la imagen de tipo FeatureSet
img.addDrawingLayer(graydist.dl()) ## se dibujan sobre la imagen original
img.save("FBSCgraydistinv.jpg") ## se guarda imagen original con la deteccion




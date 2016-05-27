from SimpleCV import * ## Se cargan paquetes de SimpleCV en python
import time ##importamos tiempo

##c=Camera() ## Se le asigna variable a la camara
##img=c.live() ## Se visualiza en tiempo real, para enfocar lunar
##time.sleep(2) ## Se hace esperar dos segundos
##img=c.getImage() ## Se captura imagen
##n = raw_input("Numero de foto") ## Se solicita numero de imagen para guardar archivo
##img.save("foto"+n+".jpg")## Se guarda foto

img=Image("foto111.jpg") ##Carga imagen en img
##Comando Blobs con binarize
imginv=img.binarize() ## se convierte imagen a blanco y negro
blobs2=imginv.findBlobs() ## se buscan los grupos de pixeles
blobs2.draw((200,0,0),width=3) ## se dibujan los grupos en la imagen binarizada
img.addDrawingLayer(imginv.dl()) ## se dibujan en la imagen original
img.save("FBbin.jpg") ## se guarda imagen original con la deteccion
##Comando Blobs
img=Image("foto111.jpg") ##Carga imagen en img
blobs=img.findBlobs() ## se buscan los grupos de pixeles
blobs.draw((200,0,0),width=3) ## se dibujan los grupos en rojo sobre la imagen de tipo FeatureSet
img.addDrawingLayer(img.dl()) ## se dibujan sobre la imagen original
img.save("FB.jpg") ## se guarda imagen original con la deteccion
##Comando Blobs para color especifico
img=Image("foto111.jpg") ##Carga imagen en img
luncafe=img.colorDistance((65,32,32)) ## Calcula la distancia del color que se le da con respecto al color de cada pixel de la imagen
blobs3=luncafe.findBlobs() ## Se buscan los grupos de pixeles
blobs3.draw((200,0,0),width=3) ## Se dibujan los grupos en rojo sobre la imagen de tipo FeatureSet
img.addDrawingLayer(luncafe.dl()) ## se dibujan sobre la imagen original
img.save("FBSCcafe.jpg") ## se guarda imagen original con la deteccion
##Comando Blobs para color especifico con imagen invertida
img=Image("foto111.jpg") ##Carga imagen en img
imginv2=img.invert()
luncafe2=imginv2.colorDistance((65,32,32)) ## Calcula la distancia del color que se le da con respecto al color de cada pixel de la imagen y se invierte
blobs32=luncafe2.findBlobs() ## Se buscan los grupos de pixeles
blobs32.draw((200,0,0),width=3) ## Se dibujan los grupos en rojo sobre la imagen de tipo FeatureSet
img.addDrawingLayer(luncafe2.dl()) ## se dibujan sobre la imagen original
img.save("FBSCcafeinv.jpg") ## se guarda imagen original con la deteccion
##Comando Blobs para color especifico con hue
img=Image("foto111.jpg") ##Carga imagen en img
luncafe=img.hueDistance((180,32,32)) ## Calcula la distancia del color que se le da con respecto al color de cada pixel de la imagen
blobs3=luncafe.findBlobs() ## Se buscan los grupos de pixeles
blobs3.draw((200,0,0),width=3) ## Se dibujan los grupos en rojo sobre la imagen de tipo FeatureSet
img.addDrawingLayer(luncafe.dl()) ## se dibujan sobre la imagen original
img.save("FBSCcafehue.jpg") ## se guarda imagen original con la deteccion
##Comando Blobs para color especifico con imagen invertida con hue
img=Image("foto111.jpg") ##Carga imagen en img
imginv2=img.invert()
luncafe2=imginv2.hueDistance((180,32,32)) ## Calcula la distancia del color que se le da con respecto al color de cada pixel de la imagen y se invierte
blobs32=luncafe2.findBlobs() ## Se buscan los grupos de pixeles
blobs32.draw((200,0,0),width=3) ## Se dibujan los grupos en rojo sobre la imagen de tipo FeatureSet
img.addDrawingLayer(luncafe2.dl()) ## se dibujan sobre la imagen original
img.save("FBSCcafeinvhue.jpg") ## se guarda imagen original con la deteccion
##Comando findCircles
img=Image("foto111.jpg") ##Carga imagen en img
luncir=img.findCircle(canny=200,thresh=250,distance=15)
luncir.draw(width=3)
luncir[0].draw(color=Color.RED,width=3)
imgfin=img.applyLayers()
edginimg=img.edges()
imgfinal=img.sideBySide(edgeinimg.sideBySide(imgfin)).scale(0.5)
imgfinal.save("FC.jpg")

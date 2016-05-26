from SimpleCV import Camera, Display, Image ## Se cargan paquetes de SimpleCV en python
import time ##importamos tiempo

c=Camera() ## Se le asigna variable a la camara
img=c.live() ## Se visualiza en tiempo real, para enfocar lunar
time.sleep(2) ## Se hace esperar dos segundos
img=c.getImage() ## Se captura imagen
n = raw_input("Numero de foto") ## Se solicita numero de imagen para guardar archivo
img.save("foto"+n+".jpg")## Se guarda foto


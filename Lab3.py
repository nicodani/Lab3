from SimpleCV import Camera, Display, Image
import time

c=Camera()
img=c.live()
time.sleep(2)
img=c.getImage()
n = raw_input("Numero de foto")
img.save("foto"+n+".jpg")


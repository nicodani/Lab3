from SimpleCV import Image, Display, Camera ## Se cargan paquetes de SimpleCV en python
import time ## se importa tiempo
import numpy as np ## se importa paquete numpy de python

def calcrho(A,B): ## Se crea una funcion que determine el rho 
    Ar=A[0]
    Ag=A[1]
    Ab=A[2]  ## Se guardan los valores del material A y B en sus respectivos canales RGB
    Br=B[0]
    Bg=B[1]
    Bb=B[2]
    r=np.array([Ar/Br, Ag/Br, Ab/Br, Ar/Bg, Ag/Bg, Ab/Bg, Ar/Bb, Ag/Bb, Ab/Bb]) ## Se calcula el vector rho

    return r ## la funcion retorna el rho

c=Camera(0,{"width":320,"height":240}) ## Se abre el objeto camara para caputrar imagenes de 320x240
img=c.live() ## Deja operando al camara en vivo, hasta que el usuario haga click derecho sobre la imagen
time.sleep(2) ## Se deja esperando 2 segundos a la camara 
img=c.getImage() ## Se toma la foto
fot=img.show() ## se muestra la imagen capturada
time.sleep(4) ## por 4 segundos
fot.quit() ## se cierra la ventana de imagen

mat=img.getNumpy().astype(dtype='float64') ## se guarda la imagen en una matris de 3 dimensiones con elementos double
siz=mat.shape ## se calcula las filas y columnas de la matriz
fil=siz[1] ## se guardan dichos datos en las variables
col=siz[0]
bor=np.zeros((col,fil,3)) ## Se crea una matriz de 3 dimensiones de ceros para crear la mascara del lunar
red=np.array([200,0,0],dtype='float64') ## se crea un vector de color rojo para destacar el borde
A=np.array([86,53,36],dtype='float64') ## se crea el vector de material A(lunar) encontrado mediante entrenamiento del algoritmo en Matlab
B=np.array([133,119,63],dtype='float64') ## Se crea el vector del material B(piel) encontrado mediante entrenamiento del algoritmo en Matlab
rho=calcrho(A,B) ## Se calcula el Rho determinado mediante entrenamiento del algoritmo en Matlab
tol=1 ## se configura la tolerancia media resultante del entrenamiento del algoritmo en Matlab
for j in range(0,col-2): 
    for i in range(0,fil-2): ## se hace un ciclo iterativo para recorrer la imagen en una ventana de 3x3, cabe destacar que es hasta dos valores menos
                             ## que el tamaño de la matriz, para no hacer la comparacion con el borde de la imagen, puesto que se
                             ## asume que no afectara en la deteccion si el lunar se encuentra dentro de la imagen

## A continuacion se prueban las opciones de comparacion para detectar borde

## Opcion 1: borde horizontal
        
        Atemp=mat[j+1,i,:] ## se selecciona pixel del material A
        Btemp=mat[j+1,i+2,:] ## se selecciona pixel del material B
        rhotemp=calcrho(Atemp,Btemp) ## se calcula el rho entre A y B
        rhotemp2=calcrho(Btemp,Atemp) ## se calcula el rho entre B y A, para el caso en que los materiales se encuentren en el otro sentido
        if (np.linalg.norm(rho-rhotemp)<tol): ## se comprueba si la diferencia entre el rho determinado y el de los pixeles es menor que la tolerancia
            bor[j+1,i+1,:]=red ##si es así, se marca el pixel central de la ventana de 3x3 como un borde
        elif(np.linalg.norm(rho-rhotemp2)<tol): ## si no, se comprueba si la diferencia entre el rho determinado por entrenamiento y el determinado en sentido inverso
            bor[j+1,i+1,:]=red ##si es así, se marca el pixel central de la ventana de 3x3 como borde
## se repite el mismo procedimiento para el resto de opciones

## Opcion 2: borde vertical
        Atemp=mat[j,i+1,:]
        Btemp=mat[j+2,i+1,:]
        rhotemp=calcrho(Atemp,Btemp)
        rhotemp2=calcrho(Btemp,Atemp)        
        if (np.linalg.norm(rho-rhotemp)<tol):
            bor[j+1,i+1,:]=red
        elif (np.linalg.norm(rho-rhotemp2)<tol):    
            bor[j+1,i+1,:]=red
## Opcion 3: borde de diagonal con esquina superior izquierda el material A, esquina inferior derecha material B
        Atemp=mat[j,i,:]
        Btemp=mat[j+2,i+2,:]
        rhotemp=calcrho(Atemp,Btemp)
        rhotemp2=calcrho(Btemp,Atemp)
        if (np.linalg.norm(rho-rhotemp)<tol):
            bor[j+1,i+1,:]=red
        elif (np.linalg.norm(rho-rhotemp2)<tol):
            bor[j+1,i+1,:]=red
## Opcion 3: borde de diagonal con esquina superior derecha el material A, esquina inferior izquierda material B
        Atemp=mat[j+2,i,:]
        Btemp=mat[j,i+2,:]
        rhotemp=calcrho(Atemp,Btemp)
        rhotemp2=calcrho(Btemp,Atemp)        
        if (np.linalg.norm(rho-rhotemp)<tol):
            bor[j+1,i+1,:]=red
        elif (np.linalg.norm(rho-rhotemp2)<tol):
            bor[j+1,i+1,:]=red


            
imgbor=Image(bor) ## se transforma la matriz con el borde a una imagen
imgdet=img+imgbor ## se aplica el borde detectado a la imagen original
imgfinal=img.sideBySide(imgbor.sideBySide(imgdet)) ## se junta a la imagen original(izq), con detector de borde(centro) e imagen con borde detectado (der).
fot2=imgfinal.show() ## se muestra dicha imagen


import cv2
import numpy as np
import imutils

imagen = cv2.imread('Evil-Toddler-Meme.jpeg')
ancho = imagen.shape[1] # Columnas
alto = imagen.shape[0] # Filas


# desplazomiento se necesita warpAffine
# matriz M es una matriz 2x3 done los utimos valore corresponse al desplazamiento en x y y (invertidos)
M = np.float32([[1,0,100],[0,1,150]])
# print(M)
imagenOut = cv2.warpAffine(imagen, M, (ancho, alto))


# rotacion de una imagen
Mr = cv2.getRotationMatrix2D((ancho // 2, alto // 2), 30, 1)
imagenRotada = cv2.warpAffine(imagen, Mr, (ancho, alto))


# escalando una imagen
imagenEscalada = cv2.resize(imagen,(600, 300), interpolation=cv2.INTER_CUBIC)

# USANDO LA LIBRERIA IMUTILS LA FUNCION RESIZE
imageOut1 = imutils.resize(imagen,width=300)
imageOut2 = imutils.resize(imagen,height=300)

# recortando una imagen, como un array con nunpy

imageOut = imagen[100:220,280:480]



cv2.imshow('meme', imagen)
cv2.imshow('meme1', imageOut)
# cv2.imshow('meme1', imageOut1)
# cv2.imshow('meme2', imageOut2)
# cv2.imshow('meme', imagenEscalada)
# cv2.imshow('se movio', imagenOut)
# cv2.imshow('rotada', imagenRotada)
cv2.waitKey(0)
cv2.destroyAllWindows()
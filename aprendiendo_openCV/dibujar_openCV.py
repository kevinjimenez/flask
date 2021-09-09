import cv2
import numpy as np


imagen_propia = 255*np.ones((400, 600, 3), dtype=np.uint8)

# dibujar linea
cv2.line(imagen_propia, (0,0), (600, 400), (255, 0, 0), 4)
cv2.line(imagen_propia, (300,0), (300, 200), (255, 100, 255), 10)

# rectangulo

cv2.rectangle(imagen_propia, (50,80), (200, 200), (0, 255, 0), 1)
cv2.rectangle(imagen_propia, (300,80), (450, 230), (0, 0, 0), -1)

#Dibujando un círculos
cv2.circle(imagen_propia,(300,200),50,(255,255,0),-1)
cv2.circle(imagen_propia,(300,20),10,(255,0,255),3)

# fuentes

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagen_propia,'Practicando con OpenCV',(10,30),font,1,(0,255,255),2,cv2.LINE_AA)
cv2.putText(imagen_propia,'Practicando con OpenCV',(10,30),0,1,(255,0,0),2)
cv2.putText(imagen_propia,'Practicando con OpenCV',(10,60),1,1,(255,0,0),2)
cv2.putText(imagen_propia,'Practicando con OpenCV',(10,90),2,1,(255,0,0),2)
cv2.putText(imagen_propia,'Practicando con OpenCV',(10,120),3,1,(255,0,0),2)
cv2.putText(imagen_propia,'Practicando con OpenCV',(10,150),4,1,(255,0,0),2)
cv2.putText(imagen_propia,'Practicando con OpenCV',(10,180),5,1,(255,0,0),2)
cv2.putText(imagen_propia,'Practicando con OpenCV',(10,210),6,1,(255,0,0),2)
cv2.putText(imagen_propia,'Practicando con OpenCV',(10,240),7,1,(255,0,0),2)

cv2.imshow('hahaha',imagen_propia)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

img = cv2.imread('lunares.png')

def dibujar(ctns, color):
    for (i, c) in enumerate(ctns):
        M = cv2.moments(c)
        if (M["m00"]==0): M["m00"]==1
        x = int(M["m10"]/M["m00"])
        y = int(M["m01"]/M["m00"])
        cv2.drawContours(img, c, -1, color, 3)
        cv2.putText(img, str(i+1), (x-10,y+10), 1, 2,(0,0,0),2)

imagenHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
amarilloBajo = np.array([20, 100, 20], np.uint8)
amarilloAlto = np.array([32, 255, 255], np.uint8)
maskAmarillo = cv2.inRange(imagenHSV, amarilloBajo, amarilloAlto)
# cv2.imshow('mask', maskAmarillo)
violetaBajo = np.array([130, 100, 20], np.uint8)
violetaAlto = np.array([145, 255, 255], np.uint8)
maskVioleta = cv2.inRange(imagenHSV, violetaBajo, violetaAlto)
# cv2.imshow('mask', maskVioleta)
verdeBajo = np.array([36, 100, 20], np.uint8)
verdeAlto = np.array([70, 255, 255], np.uint8)
maskVerde = cv2.inRange(imagenHSV, verdeBajo, verdeAlto)
# cv2.imshow('mask', maskVerde)
rojoBajo1 = np.array([0, 100, 20], np.uint8)
rojoAlto1 = np.array([10, 255, 255], np.uint8)
rojoBajo2 = np.array([175, 100, 20], np.uint8)
rojoAlto2 = np.array([180, 255, 255], np.uint8)
maskRojo1 = cv2.inRange(imagenHSV, rojoBajo1, rojoAlto1)
maskRojo2 = cv2.inRange(imagenHSV, rojoBajo2, rojoAlto2)
maskRojo =  cv2.add(maskRojo1, maskRojo2)
# cv2.imshow('mask', maskRojo)

# obtner los contonros
ctnsA = cv2.findContours(maskAmarillo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
# dibujar(ctnsA, (0, 255,255))
ctnsV = cv2.findContours(maskVioleta, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
# dibujar(ctnsV, (0, 255,255))
ctnsG = cv2.findContours(maskVerde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
# dibujar(ctnsG, (0, 255,255))
ctnsR = cv2.findContours(maskRojo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
dibujar(ctnsR, (0, 255,255))

imgResumen = 255 * np.ones((210,100,3), dtype = np.uint8)
cv2.circle(imgResumen, (30,30), 15, (0,255,255), -1)
cv2.circle(imgResumen, (30,70), 15, (140,40,120), -1)
cv2.circle(imgResumen, (30,110), 15, (0,255,0), -1)
cv2.circle(imgResumen, (30,150), 15, (0,0,255), -1)
cv2.putText(imgResumen,str(len(ctnsA)),(65,40), 1, 2,(0,0,0),2)
cv2.putText(imgResumen,str(len(ctnsV)),(65,80), 1, 2,(0,0,0),2)
cv2.putText(imgResumen,str(len(ctnsG)),(65,120), 1, 2,(0,0,0),2)
cv2.putText(imgResumen,str(len(ctnsR)),(65,160), 1, 2,(0,0,0),2)

totalCnts = len(ctnsA) + len(ctnsV) + len(ctnsG) + len(ctnsR)
cv2.putText(imgResumen,str(totalCnts),(55,200), 1, 2,(0,0,0),2)

cv2.imshow('img', img)
cv2.imshow('img 1', imgResumen)

cv2.waitKey(0)
cv2.destroyAllWindows()


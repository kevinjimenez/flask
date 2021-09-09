import cv2
import numpy as np

img = cv2.imread('figContorno.png')
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,th = cv2.threshold(gris,100, 255, cv2.THRESH_BINARY)
# print(cv2.__version__)

# contornos1,hierarchy1 = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# contornos2,hierarchy2 = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# cv2.drawContours(img, contornos1, -1, (0,255,0), 3)
# cv2.drawContours(img, contornos2, -1, (0,255,0), 3)

# print ('len(contornos1[2])=',len(contornos1[2]))
# print ('len(contornos1[2])=',len(contornos2[2]))

# Aplicando cv2.RETR_EXTERNAL
contornos1,hierarchy1 = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Aplicando cv2.RETR_LIST
contornos1,hierarchy1 = cv2.findContours(th, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Aplicando cv2.RETR_CCOMP
contornos1,hierarchy1 = cv2.findContours(th, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# Aplicando cv2.RETR_TREE
contornos1,hierarchy1 = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print('hierarchy1=', hierarchy1)
print('contornos1=', hierarchy1)
for i in range(len(contornos1)):
    print (i)
    cv2.drawContours(img, contornos1, i, (0, 255, 0), 3)
    cv2.imshow('img' + str(i), img)
    cv2.waitKey(0)



cv2.imshow('aaa', img)
# cv2.imshow('bbb', th)
cv2.waitKey(0)
cv2.destroyAllWindows()
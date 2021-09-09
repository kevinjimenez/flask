import cv2
import numpy as np

# suma de imagenes

img_1 = cv2.imread('cadena.jpeg')
img_2 = cv2.imread('img3.jpeg')

img_1_ = cv2.imread('cadena.jpeg', 0)
img_2_ = cv2.imread('img3.jpeg', 0)

resA = cv2.add(img_1, img_2)
resA_ = cv2.add(img_1_, img_2_)

# print('img1[0,0]= ', img_1_[0,0])
# print('img2[0,0]= ', img_2_[0,0])
# print('resA[0,0]= ', resA_[0,0])

# cv2.imshow('imagenes', np.hstack([img_1, img_2, resA]))
# cv2.imshow('imagenes gris', np.hstack([img_1_, img_2_, resA_]))

# Mezcla de imágenes con cv2.addWeighted

# resAW = cv2.addWeighted(img_1, 0.5, img_2, 0.9, 0)

# Sustracción de imágenes con cv2.subtract

# resultado2 = cv2.subtract(img_1_,img_2_)
# print('img1[0,0]= ', img_1_[0,0])
# print('img2[0,0]= ',img_2_[0,0])
# print('resultado2[0,0]= ',resultado2[0,0])

# Sustracción de imágenes con cv2.absdiff

resultado2 = cv2.absdiff(img_1_,img_2_)
print('img1[0,0]= ', img_1_[0,0])
print('img2[0,0]= ',img_2_[0,0])
print('resultado2[0,0]= ',resultado2[0,0])

cv2.imshow('hahah', resultado2)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import imutils

img1 = cv2.imread('imagen_01.jpeg')
img2 = cv2.imread('imagen_02.jpeg')
img3 = cv2.imread('img3.jpeg')
img3 = imutils.resize(img3, width=800, height=320)
# print(img2.shape)
print(img3.shape)
# concatenar de forma horizontal
cv2.imshow('aaa', img3)

concate_h = cv2.hconcat([img1, img2])


# concatenar de forma vertical

concate_v = cv2.vconcat([img1, img2])

# conbinar

concate2 = cv2.hconcat([img1, img2, img2, img1])
print(concate2.shape)
concate3 = cv2.hconcat([img1, img2, img1, img2])
concate4 = cv2.vconcat([concate2, concate3])
concate2 = imutils.resize(concate2, height=532)
concate5 = cv2.hconcat([concate2, img3])


cv2.imshow('concate_h', concate_h)
cv2.imshow('concate_v', concate_v)
cv2.imshow('mix', concate4)
cv2.imshow('mix 2', concate5)
cv2.waitKey(0)
cv2.destroyAllWindows()
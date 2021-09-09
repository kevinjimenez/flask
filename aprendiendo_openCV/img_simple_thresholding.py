import cv2
import imutils
import numpy as np

img = cv2.imread('img3.jpeg')
img_resize = imutils.resize(img, width=400)


_, binary = cv2.threshold(img_resize, 210, 255, cv2.THRESH_BINARY)
_, binary_inv = cv2.threshold(img_resize, 210, 255, cv2.THRESH_BINARY_INV)

_, truc = cv2.threshold(img_resize, 210, 255, cv2.THRESH_TRUNC)
_, tozero = cv2.threshold(img_resize, 210, 255, cv2.THRESH_TOZERO)
_, tozero_inv = cv2.threshold(img_resize, 210, 255, cv2.THRESH_TOZERO_INV)




cv2.imshow('img - THRESH_BINARY - THRESH_BINARY_INV', np.hstack([img_resize, binary, binary_inv]))
cv2.imshow('THRESH_TRUNC - THRESH_TOZERO - THRESH_TOZERO_INV', np.hstack([truc, tozero, tozero_inv]))
# cv2.imshow('THRESH_BINARY', binary)
# cv2.imshow('THRESH_BINARY_INV', binary_inv)
# cv2.imshow('img', img_resize)
# cv2.imshow('img', img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()



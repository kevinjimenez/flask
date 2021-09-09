import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen_leer = cv2.imread('mandrill_colour.png')
# print(imagen_leer)
print(type(imagen_leer))
print(imagen_leer.shape)
plt.imshow(imagen_leer)
plt.show()
img_original = cv2.cvtColor(imagen_leer, cv2.COLOR_BGR2RGB)
plt.imshow(img_original)
plt.show()

cv2.imwrite('hahaha.png', img_original)
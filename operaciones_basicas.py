import numpy as np
import cv2
import matplotlib.pyplot as plt

imagen_negra = np.zeros(shape=(512, 512, 3), dtype=np.int16)
print(imagen_negra)

# dibujar linea roja
line_red = cv2.line(imagen_negra,(0,0),(511,511),(255,0,0),5)
# plt.imshow(line_red)
line_green = cv2.line(imagen_negra,(0,0),(511,511),(0,255,0),5)
# plt.imshow(line_green)
rectagulo = cv2.rectangle(imagen_negra,(384,0),(510,128),(0,0,255),5)

circulo = cv2.circle(imagen_negra,(447,63),63,(0,0,255),-1)

font = cv2.FONT_ITALIC
tex_img = cv2.putText(imagen_negra, 'hahaha', (10, 500), font, 2, (255,255,255), 2, lineType=cv2.LINE_AA)

plt.imshow(tex_img)
plt.show()
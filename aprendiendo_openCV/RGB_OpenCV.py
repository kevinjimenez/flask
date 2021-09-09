import cv2
import numpy as np

# El orden en el que OpenCV usa estos componentes es en BGR, no RGB
# bgr = np.zeros((300, 300, 3), dtype=np.uint8)
# bgr[:,:] = (255, 0, 0)
# print(bgr)

# IMAGENS
bgr = cv2.imread('mandrill_colour.png')
C1 = bgr[:,:,0] # CANAL EN B
C2 = bgr[:,:,1] # CANAL EN G
C3 = bgr[:,:,2] # CANAL EN R

cv2.imshow('BGR', np.hstack([C1,C2,C3]))

# paso de bgr a rgb

rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
C1 = rgb[:,:,0] # CANAL EN R
C2 = rgb[:,:,1] # CANAL EN G
C3 = rgb[:,:,2] # CANAL EN B

cv2.imshow('RBG', np.hstack([C1,C2,C3]))
cv2.waitKey(0)
cv2.destroyAllWindows()

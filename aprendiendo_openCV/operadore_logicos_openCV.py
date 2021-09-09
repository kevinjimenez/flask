import cv2
import numpy as np

# Operadores BITWISE (AND-OR-NOT-XOR)
img = np.zeros((400,600), dtype=np.uint8)
img[100:300,200:400] = 255
img2 = np.zeros((400,600), dtype=np.uint8)
img2 = cv2.circle(img2, (300, 200), 125, (255), -1)

# cv2.imshow('1', img)
# cv2.imshow('2', img2)

# and
AND = cv2.bitwise_and(img,img2)
# cv2.imshow('AND', AND)

# NOT
NOT = cv2.bitwise_not(img)
# cv2.imshow('NOT', NOT)

# OR

OR = cv2.bitwise_or(img,img2)
# cv2.imshow('OR', OR)

# XOR

XOR = cv2.bitwise_xor(img,img2)
# cv2.imshow('XOR', XOR)

# cv2.waitKey(0)

# con video

video = cv2.VideoCapture(0)
mask1 = np.zeros((720, 1280), dtype=np.uint8)
mask1 = cv2.circle(mask1, (320,240), 125, (255), -1)
# mask1 = cv2.bitwise_not(mask1) # punto negro
# cv2.imshow('mask', mask1)
print(video)
while video.isOpened():
    ret, frame = video.read()
    if ret == True:

        imgMask = cv2.bitwise_and(frame, frame, mask=mask1)
        cv2.imshow('imgMask', imgMask)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else: break

video.release()    
cv2.destroyAllWindows()
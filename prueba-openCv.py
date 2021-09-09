import cv2
import imutils
import os
# import numpy as np
cap = cv2.VideoCapture(0)

while(True):
    ref, frame =  cap.read()

    print(len(frame))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    cv2.imshow('frame', gray)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
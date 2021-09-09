import cv2
import numpy as np

video = cv2.VideoCapture(0)

# azulBajo = np.array([100,100,20], np.uint8)
# azulAlto = np.array([125,255,255], np.uint8)
redBajo1 = np.array([0, 100, 20], np.uint8)
redAlto1 = np.array([8, 255, 255], np.uint8)
redBajo2 = np.array([175, 100, 20], np.uint8)
redAlto2 = np.array([179, 255, 255], np.uint8)


while True:
    ret, frame = video.read()
    if ret == True:

        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1)
        maskRed2 = cv2.inRange(frameHSV, redBajo2, redAlto2)
        maskRed = cv2.add(maskRed1, maskRed2)
        contornos, _  = cv2.findContours(maskRed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contornos:
            area = cv2.contourArea(c)
            if area > 3000:
                M = cv2.moments(c)
                if (M["m00"]==0): M["m00"]=1
                x = int(M["m10"]/M["m00"])
                y = int(M['m01']/M['m00'])
                cv2.circle(frame, (x,y), 7, (0,255,0), -1)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, '{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)
                nuevoContorno = cv2.convexHull(c)
                cv2.drawContours(frame, [nuevoContorno], 0, (255,0,0), 3)


        cv2.imshow('video', frame)
        # cv2.imshow('mascara verde', maskGreen)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video.release()
cv2.destroyAllWindows()

# LO DE LA EXPLIACION # 

# # import cv2
# # import numpy as np

# # video = cv2.VideoCapture(0)

# # coloMin = np.array([100, 100, 20], np.uint8)
# # coloMax = np.array([125, 225, 255], np.uint8)

# # while True:
# #     ref, frame = video.read()
# #     if ref == True:
# #         frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# #         mask = cv2.inRange(frameHSV, coloMin, coloMax)
# #         contorno, h = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# #         # cv2.drawContours(frame, contorno, -1, (0,255,0), 2)


# #         for c in contorno:
# #             # print(c)
# #             # print(type(c))
# #             area = cv2.contourArea(c)
# #             # print(area)
# #             if area > 3000:
# #                 M = cv2.moments(c)
# #                 print(M)
# #                 if (M["m00"]==0): M["m00"]=1
# #                 x = int(M["m10"]/M["m00"])
# #                 y = int(M['m01']/M['m00'])
# #                 cv2.circle(frame, (x,y), 7, (0,255,0), -1)
# #                 font = cv2.FONT_HERSHEY_SIMPLEX
# #                 cv2.putText(frame, '{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)
# #                 nuevoContorno = cv2.convexHull(c)
# #                 cv2.drawContours(frame, [nuevoContorno], 0, (255,0,0), 3)

# #         cv2.imshow('', frame)
# #         cv2.imshow('mask', mask)
# #         if cv2.waitKey(1) & 0xFF == ord('q'):
# #             break

# # video.release()
# # cv2.destroyAllWindows()

# import cv2
# import numpy as np
# cap = cv2.VideoCapture(0)
# azulBajo = np.array([100,100,20],np.uint8)
# azulAlto = np.array([125,255,255],np.uint8)
# amarilloBajo = np.array([15,100,20],np.uint8)
# amarilloAlto = np.array([45,255,255],np.uint8)
# redBajo1 = np.array([0,100,20],np.uint8)
# redAlto1 = np.array([5,255,255],np.uint8)
# redBajo2 = np.array([175,100,20],np.uint8)
# redAlto2 = np.array([179,255,255],np.uint8)
# font = cv2.FONT_HERSHEY_SIMPLEX
# def dibujar(mask,color):
#     contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
#         cv2.CHAIN_APPROX_SIMPLE)
#     for c in contornos:
#         area = cv2.contourArea(c)
#         if area > 3000:
#             M = cv2.moments(c)
#             if (M["m00"]==0): M["m00"]=1
#             x = int(M["m10"]/M["m00"])
#             y = int(M['m01']/M['m00'])
#             nuevoContorno = cv2.convexHull(c)
#             cv2.circle(frame,(x,y),7,(0,255,0),-1)
#             cv2.putText(frame,'{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)
#             cv2.drawContours(frame, [nuevoContorno], 0, color, 3)
# while True:
#     ret,frame = cap.read()
#     if ret == True:
#         frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#         maskAzul = cv2.inRange(frameHSV,azulBajo,azulAlto)
#         maskAmarillo = cv2.inRange(frameHSV,amarilloBajo,amarilloAlto)
#         maskRed1 = cv2.inRange(frameHSV,redBajo1,redAlto1)
#         maskRed2 = cv2.inRange(frameHSV,redBajo2,redAlto2)
#         maskRed = cv2.add(maskRed1,maskRed2)
#         dibujar(maskAzul,(255,0,0))
#         dibujar(maskAmarillo,(0,255,255))
#         dibujar(maskRed,(0,0,255))
#         cv2.imshow('frame',frame)
#         if cv2.waitKey(1) & 0xFF == ord('s'):
#             break
# cap.release()
# cv2.destroyAllWindows()

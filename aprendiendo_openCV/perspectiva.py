# # import cv2
# # import numpy as np

# # # cambio perpertiva

# # img = cv2.imread('gato.jpeg')

# # cv2.circle(img, (84, 69), 7, (255,0,0), 2)
# # cv2.circle(img, (513, 77), 7, (0,255,0), 2)
# # cv2.circle(img, (113, 358), 7, (0,0,255), 2)
# # cv2.circle(img, (542, 366), 7, (255,255,0), 2)

# # puntos_cuadrangulares_entradaImg = np.float32(([84,69],[513,77],[113,358],[542,366]))
# # puntos_cuadrangulares_salidaImg = np.float32(([0,0],[480,0],[0,300],[480, 300]))

# # M = cv2.getPerspectiveTransform(puntos_cuadrangulares_entradaImg, puntos_cuadrangulares_salidaImg)
# # nueva_img = cv2.warpPerspective(img, M, (480, 300))

# # # pts1 = np.float32([[84,69], [513,77], [113, 358], [542,366]])
# # # pts2 = np.float32([[0,0], [480,0], [0,300], [480,300]])

# # cv2.imshow('', img)
# # cv2.imshow('cambio', nueva_img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# import cv2
# import numpy as np
# def clics(event,x,y,flags,param):
#     global puntos
#     if event == cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(imagen,(x,y),5,(0,255,0),2)
#         puntos.append([x,y])
# def uniendo4puntos(puntos):
#     cv2.line(imagen,tuple(puntos[0]),tuple(puntos[1]),(255,0,0),1)
#     cv2.line(imagen,tuple(puntos[0]),tuple(puntos[2]),(255,0,0),1)
#     cv2.line(imagen,tuple(puntos[2]),tuple(puntos[3]),(255,0,0),1)
#     cv2.line(imagen,tuple(puntos[1]),tuple(puntos[3]),(255,0,0),1)
# puntos = []
# imagen = cv2.imread('gato.jpeg')
# aux = imagen.copy()
# cv2.namedWindow('Imagen')
# cv2.setMouseCallback('Imagen',clics)
# while True:
#     if len(puntos) == 4:
#         uniendo4puntos(puntos)
#         pts1 = np.float32([puntos])
#         pts2 = np.float32([[0,0], [480,0], [0,300], [480,300]])
#         M = cv2.getPerspectiveTransform(pts1,pts2)
#         dst = cv2.warpPerspective(imagen, M, (480,300))
#         cv2.imshow('dst', dst)
#     cv2.imshow('Imagen',imagen)
    
#     k = cv2.waitKey(1) & 0xFF
#     if k == ord('n'): # Limpiar el contenido de la imagen
#         imagen = aux.copy()
#         puntos = []
        
#     elif k == 27:
#         break
# cv2.destroyAllWindows()

import cv2
import numpy as np
def clics(event,x,y,flags,param):
    global puntos
    if event == cv2.EVENT_LBUTTONDOWN:
        puntos.append([x,y])
def dibujando_puntos(puntos):
    for x, y in puntos:
        cv2.circle(frame,(x,y),5,(0,255,0),2)
def uniendo4puntos(puntos):
    cv2.line(frame,tuple(puntos[0]),tuple(puntos[1]),(255,0,0),1)
    cv2.line(frame,tuple(puntos[0]),tuple(puntos[2]),(255,0,0),1)
    cv2.line(frame,tuple(puntos[2]),tuple(puntos[3]),(255,0,0),1)
    cv2.line(frame,tuple(puntos[1]),tuple(puntos[3]),(255,0,0),1)
puntos = []
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('Video1.mp4')
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',clics)
while True:
    ret, frame = cap.read()
    if ret == False: break
    dibujando_puntos(puntos)
    if len(puntos) == 4:
        uniendo4puntos(puntos)
        pts1 = np.float32([puntos])
        pts2 = np.float32([[0,0], [500,0], [0,300], [500,300]])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        dst = cv2.warpPerspective(frame, M, (500,300))
        cv2.imshow('dst', dst)
    cv2.imshow('frame',frame)
    
    k = cv2.waitKey(1) & 0xFF
    if k == ord('n'): # Limpiar el contenido de la frame
        puntos = []
        
    elif k == 27:
        break
cap.release()
cv2.destroyAllWindows()
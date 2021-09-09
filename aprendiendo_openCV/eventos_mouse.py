import cv2
import numpy as np

# imagen = np.zeros((480,640, 3), np.uint8)
imagen = cv2.imread('cadena.jpeg')
imagen_a_rotar = imagen.copy() 
ancho = imagen.shape[1] # columnas
alto = imagen.shape[0]  # filas
angulo = 0

# def dibujando (event, x, y, bandera, param):
    # print('-----------------')
    # print('event', event)
    # print('x', x)
    # print('y', y)
    # print('bandera', bandera)
    
    # if event == cv2.EVENT_LBUTTONDOWN:
    #     cv2.circle(imagen, (x,y), 20, (255,255,255), 2)
    # if event == cv2.EVENT_RBUTTONDOWN:
    #     cv2.circle(imagen,(x,y),20,(0,0,255),2)
    # if event == cv2.EVENT_LBUTTONDBLCLK:
    #     cv2.circle(imagen,(x,y),10,(255,0,0),-1)
    # if event == cv2.EVENT_RBUTTONDBLCLK:
    #     cv2.circle(imagen,(x,y),10,(0,255,0),-1)

    # if event == cv2.EVENT_LBUTTONUP:
    #     cv2.putText(imagen,'Ha dejado de presionar (Izquierdo)',(x,y),2,0.4,(255,255,0),1,cv2.LINE_AA)
    # if event == cv2.EVENT_RBUTTONUP:
    #     cv2.putText(imagen,'Ha dejado de presionar (Derecho)',(x,y),2,0.4,(0,255,255),1,cv2.LINE_AA)

def rotar(event,x,y,flag,param):
    global angulo, imagen_a_rotar
    if event == cv2.EVENT_LBUTTONDOWN:
        angulo = angulo + 15
        M = cv2.getRotationMatrix2D((ancho//2,alto//2), angulo, 1)
        imagen_a_rotar = cv2.warpAffine(imagen, M, (ancho,alto))

    if event == cv2.EVENT_RBUTTONDOWN:
        angulo = angulo - 15
        M = cv2.getRotationMatrix2D((ancho//2,alto//2), angulo, 1)
        imagen_a_rotar = cv2.warpAffine(imagen, M, (ancho,alto))

cv2.namedWindow('hahah')
cv2.setMouseCallback('hahah', rotar)

while True:
    cv2.imshow('hahah', imagen_a_rotar)
    # k = cv2.waitKey(1) & 0xFF
    # if k == ord('l'):
        # imagen = np.zeros((480,640, 3), np.uint8)
    # elif k == 27:
        # break
    print('Ángulo=',angulo)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
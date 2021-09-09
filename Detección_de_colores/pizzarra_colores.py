import cv2
import numpy as np

video = cv2.VideoCapture(0)

amarilloBajo = np.array([15,100,20],np.uint8)
amarilloAlto = np.array([45,255,255],np.uint8)

# Colores para pintar
colorCeleste = (255,113,82)
colorAmarillo = (89,222,255)
colorRosa = (128,0,255)
colorVerde = (0,255,36)
colorLimpiarPantalla = (29,112,246) # Solo se usará para el cuadro superior de 'Limpiar Pantalla'
# Grosor de línea recuadros superior izquierda (color a dibujar)
grosorCeleste = 6
grosorAmarillo = 2
grosorRosa = 2
grosorVerde = 2
# Grosor de línea recuadros superior derecha (grosor del marcador para dibujar)
grosorPeque = 6
grosorMedio = 1
grosorGrande = 1
#--------------------- Variables para el marcador / lápiz virtual -------------------------
color = colorCeleste  # Color de entrada, y variable que asignará el color del marcador
grosor = 3 # Grosor que tendrá el marcador
#------------------------------------------------------------------------------------------
x1 = None
y1 = None
imAux = None

while video.isOpened():
    ret, frame = video.read()
    if ret == True:
        if imAux is None: imAux = np.zeros(frame.shape, dtype=np.uint8)
        frame = cv2.flip(frame, 1)
        cv2.rectangle(frame, (0,0), (100,100), colorRosa, grosorRosa)
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        maskAmarilla = cv2.inRange(frameHSV, amarilloBajo, amarilloAlto)
        maskAmarilla = cv2.erode(maskAmarilla, None, iterations=1)
        maskAmarilla = cv2.dilate(maskAmarilla, None, iterations=2)
        maskAmarilla = cv2.medianBlur(maskAmarilla, 13)
        contornos, _ = cv2.findContours(maskAmarilla, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contornos = sorted(contornos, key=cv2.contourArea, reverse=True)[:1]
        # # cv2.drawContours(frame, contornos, -1, (255,0,0), 3)
        for c in contornos:
            area = cv2.contourArea(c)
            if area > 1000:
                x, y2, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y2), (x + w, y2 + h), (0,255,0), 3)
                x2 = x + w//2
                if x1 is not None:
                    if 0 < x2 < 100 and 0 < y2 < 100:
                        color = colorRosa # Color del lápiz/marcador virtual
                        grosorAmarillo = 2
                        grosorRosa = 6
                        grosorVerde = 2
                        grosorCeleste = 2
                # M = cv2.moments(c)
                # if (M["m00"]==0): M["m00"]=1
                # x = int(M["m10"]/M["m00"])
                # y = int(M['m01']/M['m00'])
                # cv2.circle(frame, (x,y), 7, (0,255,0), -1)
                # nuevoContorno = cv2.convexHull(c)
                # cv2.drawContours(frame,[nuevoContorno], 0, (255,0,0), 3)
                    if 0 < y2 < 110 or 0 < y1 < 110 :
                        imAux = imAux
                    else:
                        imAux = cv2.line(imAux,(x1,y1),(x2,y2),color,grosor)
                cv2.circle(frame,(x2,y2),grosor,color,3)
                x1 = x2
                y1 = y2
            else:
                x1 = None
                y1 = None
        
        
        imAuxGris = cv2.cvtColor(imAux, cv2.COLOR_BGR2GRAY)
        _, th = cv2.threshold(imAuxGris, 10, 255, cv2.THRESH_BINARY)
        th_inv = cv2.bitwise_not(th)
        frame = cv2.bitwise_and(frame, frame, mask=th_inv)
        frame = cv2.add(frame, imAux)

        cv2.imshow('lienzo', imAux)
        cv2.imshow('video', frame)
        # cv2.imshow('video hsv', maskAmarilla)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else: break

video.release()
cv2.destroyAllWindows()
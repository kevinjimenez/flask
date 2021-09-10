import cv2

img = cv2.imread('figurasColores2.png')

gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gris, 10, 150)
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)

contornos, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# cv2.drawContours(img, contornos, -1,(0,0,255), 3)
for c in contornos:
    epsilon = 0.01*cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    print(len(approx))

    x,y,w,h = cv2.boundingRect(approx)
    if len(approx)==3:
        cv2.putText(img,'Triangulo', (x,y-5),1,1.5,(0,255,0),2)
    if len(approx)==4:
        aspect_ratio = float(w)/h
        print('aspect_ratio= ', aspect_ratio)
        if aspect_ratio == 1:
            cv2.putText(img,'Cuadrado', (x,y-5),1,1.5,(0,255,0),2)
        else:
            cv2.putText(img,'Rectangulo', (x,y-5),1,1.5,(0,255,0),2)
    
    if len(approx)==5:
        cv2.putText(img,'Pentagono', (x,y-5),1,1.5,(0,255,0),2)
    if len(approx)==6:
        cv2.putText(img,'Hexagono', (x,y-5),1,1.5,(0,255,0),2)
    if len(approx)>10:
        cv2.putText(img,'Circulo', (x,y-5),1,1.5,(0,255,0),2)

    cv2.drawContours(img, [approx], -1, (0,0,255), 3)
    cv2.imshow('img', img)
    cv2.waitKey(0)    

# cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
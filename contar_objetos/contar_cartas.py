import cv2

img = cv2.imread('cartas.png')


gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bordes = cv2.Canny(gris, 100, 200)

ctns, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, ctns, -1, (0,0,255), 3)
print('Número de contornos encontrados: ', len(ctns))
texto = 'Contornos encontrados: '+ str(len(ctns))
cv2.putText(img, texto, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 1)
cv2.imshow('img', img)
# cv2.imshow('img 1', gris)
# cv2.imshow('img 2', bordes)



cv2.waitKey(0)
cv2.destroyAllWindows()
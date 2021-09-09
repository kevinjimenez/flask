import cv2

imagen = cv2.imread('monedas.jpeg')
font = cv2.FONT_HERSHEY_SIMPLEX

imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

_,th = cv2.threshold(imagen_gris, 240, 255, cv2.THRESH_BINARY_INV)
contornos, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen, contornos, -1, (255,0,0), 3)
print('Contornos: ', len(contornos))
i = 0
for c in contornos:
    i = i+1
    M = cv2.moments(c)
    # print(M)
    if (M["m00"]==0): M["m00"]=1
    x=int(M["m10"]/M["m00"])
    y=int(M['m01']/M['m00'])
    mensaje = f'moneda {i}'
    cv2.putText(imagen, mensaje,(x-40,y),font, 0.75, (0,0,255), 2, cv2.LINE_AA)

cv2.imshow('imagen',imagen)
# cv2.imshow('imagen gis',imagen_gris)
# cv2.imshow('th',th)
cv2.waitKey(0)
cv2.destroyAllWindows()

# video = cv2.VideoCapture(0)

# while True:
#     ret, frame = video.read()
#     if ret == True:
#         # cv2.imshow('video', frame)
#         gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         # cv2.flip(gris)
#         # cv2.imshow('video', gris)
#         _, th = cv2.threshold(gris, 240, 255, cv2.THRESH_BINARY_INV, cv2.CHAIN_APPROX_SIMPLE)
#         # cv2.imshow('video rh', th)
#         cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#         cv2.drawContours(frame, cnts, -1, (255,0,0), 3)
#         # cv2.flip(th)
#         # cv2.flip(frame, flipMode=-1)
#         cv2.imshow('video rh', frame)

#         if cv2.waitKey(1) & 0xFF == ord('s'):
#             break
#     else:
#         break

# video.release()


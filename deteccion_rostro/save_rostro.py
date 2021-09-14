import cv2

# faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# image = cv2.imread('imagen_000.jpeg')
# imageAux = image.copy()
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# faces = faceClassif.detectMultiScale(gray, 1.1, 5)

# count = 0
# for (x,y,w,h) in faces:
#     cv2.rectangle(image, (x,y),(x+w,y+h),(128,0,255),2)
#     rostro = imageAux[y:y+h,x:x+w]
#     # rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
#     cv2.imwrite('rostro_{}.jpg'.format(count),rostro)
#     count = count + 1
#     cv2.imshow('rostro',rostro)
#     cv2.imshow('image',image)
#     cv2.waitKey(0)
# cv2.destroyAllWindows()

import os
images_path = "/Users/macbookpro/Documents/desarrollo/personal/flask-and-openCV/deteccion_rostro/image"
images_path_list = os.listdir(images_path)

if not os.path.exists('Rostros encontrados'):
    print('Carpeta creada: Rostros encontrados')
    os.makedirs('Rostros encontrados')

# print(images_path_list)
# faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

# count = 0

# for image_name in images_path_list:
#     print(image_name)
#     ruta = f'{images_path}/{image_name}'
#     img = cv2.imread(ruta)
#     img_aux = img.copy()
#     img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = faceClassif.detectMultiScale(img_gris, 1.1, 5)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(img,(10,5),(450,25),(255,255,255),-1)
#     cv2.putText(img,'Presione s, para alamacenar los rostros encontrados',(10,20), 2, 0.5,(128,0,255),1,cv2.LINE_AA)
#     cv2.imshow('image',img)
#     k = cv2.waitKey(0)
#     if  k == ord('s'):
#         for (x,y,w,h) in faces:
#             rostro = img_aux[y:y+h,x:x+w]
#             rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
#             #cv2.imshow('rostro',rostro)
#             #cv2.waitKey(0)
#             cv2.imwrite('Rostros encontrados/rostro_{}.jpg'.format(count),rostro)
#             count = count +1
#     elif k == 27:
#         break

#     # cv2.imshow('img', img)
#     # cv2.waitKey(0)

# cv2.destroyAllWindows()

# faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# count = 0
# for imageName in images_path_list:
#     image = cv2.imread(images_path+'/'+imageName)
#     imageAux = image.copy()
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
#     faces = faceClassif.detectMultiScale(gray, 1.1, 5)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(image, (x,y),(x+w,y+h),(128,0,255),2)
#     cv2.rectangle(image,(10,5),(450,25),(255,255,255),-1)
#     cv2.putText(image,'Presione s, para alamacenar los rostros encontrados',(10,20), 2, 0.5,(128,0,255),1,cv2.LINE_AA)
#     cv2.imshow('image',image)
#     k = cv2.waitKey(0)
#     if  k == ord('s'):
#         for (x,y,w,h) in faces:
#             rostro = imageAux[y:y+h,x:x+w]
#             rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
#             #cv2.imshow('rostro',rostro)
#             #cv2.waitKey(0)
#             cv2.imwrite('Rostros encontrados/rostro_{}.jpg'.format(count),rostro)
#             count = count +1
#     elif k == 27:
#         break
# cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0
while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()
    faces = faceClassif.detectMultiScale(gray, 1.1, 4)
    k = cv2.waitKey(1)
    if k == 27:
        break
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(128,0,255),2)
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
        if k == ord('s'):
            cv2.imwrite('Rostros encontrados/rostro_{}.jpg'.format(count),rostro)
            cv2.imshow('rostro',rostro)
            count = count +1
    cv2.rectangle(frame,(10,5),(450,25),(255,255,255),-1)
    cv2.putText(frame,'Presione s, para almacenar los rostros encontrados',(10,20), 2, 0.5,(128,0,255),1,cv2.LINE_AA)
    cv2.imshow('frame',frame)
cap.release()
cv2.destroyAllWindows()
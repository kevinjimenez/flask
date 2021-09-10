import cv2

# cargar el clasificardor modelo
# facesClassif = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
# facesClassif = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
# facesClassif = cv2.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')
# facesClassif = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
# facesClassif = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
facesClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



# img = cv2.imread('oficina.png')
# gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# faces = facesClassif.detectMultiScale(gris, scaleFactor=1.1,minNeighbors=5,minSize=(30,30),maxSize=(100,100))

# for (x,y,w,h) in faces:
#     cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 3)

# # concat = cv2.hconcat([img, gris])
# cv2.imshow('img', img)
# cv2.waitKey(0)

video = cv2.VideoCapture(0)
while True:
    ret, frame = video.read()
    if ret == True:
        gris_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.flip(frame,1)
        faces = facesClassif.detectMultiScale(gris_frame, scaleFactor=1.3,minNeighbors=5)
        print(faces)
        print(type(faces))

        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        
        cv2.imshow('video', frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else :
        break


video.release()
cv2.destroyAllWindows()

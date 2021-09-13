import cv2

# img = cv2.imread('oficina.png')
# def escuchar(val):
#     print(val)
#     pass


# cv2.namedWindow('image')
# cv2.createTrackbar('BLUR', 'image', 0, 7, escuchar)

# # cv2.imshow('', img)

# while True:
#     val = cv2.getTrackbarPos('BLUR', 'image')
#     print(val)
#     if val > 0:
#         img1 = cv2.blur(img.copy(), (val, val))
#     else:
#         img1 = img.copy()
#     cv2.imshow('image', img1)
#     k = cv2.waitKey(1)
#     if k == 27:
#         break

# # cv2.waitKey(0)
# cv2.destroyAllWindows()


# def escuchar():
#     pass



# facesClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# cv2.namedWindow('img')
# cv2.createTrackbar('blur', 'img', 0, 10, escuchar)
# cv2.createTrackbar('gray', 'img', 0,1, escuchar)

# while True:
#     val_blur = cv2.getTrackbarPos('blur', 'img')
#     val_gray = cv2.getTrackbarPos('gray', 'img')
#     if val_gray == 1:
#         img1 = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)
#     else : 
#         img1 = img.copy()
#     faces = facesClassif.detectMultiScale(img, 1.1,5)
#     for (x,y,w,h) in faces:
#         if val_blur > 0:
#             img1[y:y+h, x:x+w] = cv2.blur(img1[y:y+h, x:x+w], (val_blur, val_blur))
#         # cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 3)
#         else :
#             break
#     cv2.imshow('img', img1)
#     if cv2.waitKey(1) == 27:
#         break

# cv2.destroyAllWindows()


def nothing(x):
    pass
cap = cv2.VideoCapture(0)
faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cv2.namedWindow('frame')
cv2.createTrackbar('Blur','frame',0,15,nothing)
cv2.createTrackbar('Gray','frame',0,1,nothing)
while True:    
    ret,frame = cap.read()    
    val = cv2.getTrackbarPos('Blur','frame')
    grayVal = cv2.getTrackbarPos('Gray','frame')
    if grayVal == 1:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceClassif.detectMultiScale(frame, 1.1, 4)
    for (x,y,w,h) in faces:
        if val > 0: 
            frame[y:y+h,x:x+w] = cv2.blur(frame[y:y+h,x:x+w],(val,val))
    cv2.imshow('frame',frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
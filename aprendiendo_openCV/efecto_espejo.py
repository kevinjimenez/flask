import cv2

imagen = cv2.imread('mandrill_colour.png')


# invierte horizontalmente
flipImg =  cv2.flip(imagen, 0)

# Invierte verticalmente

flipImg1 =  cv2.flip(imagen, 1)

# Invierte la imagen tanto vertical como horizontalmente
flipImg2 =  cv2.flip(imagen, -1)

# cv2.imshow('original', imagen)
# cv2.imshow('invierte horizontalmente', flipImg)
# cv2.imshow('invierte verticalmente', flipImg1)
# cv2.imshow('valor negativo', flipImg2)


# efecto epero en video
video_streamer = cv2.VideoCapture(0)

while True:
    ref, frame = video_streamer.read()
    if ref == False: break
    ancho_frame = frame.shape[1] // 2
    frame[:,:ancho_frame] = cv2.flip(frame[:,ancho_frame:], 1)
    cv2.imshow('video espejo', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# cv2.waitKey(0)
cv2.release()
cv2.destroyAllWindows()
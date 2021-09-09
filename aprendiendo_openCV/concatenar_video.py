import cv2
import imutils

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # cv2.imshow('video', frame)

    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, th = cv2.threshold(gris, 100, 255, cv2.THRESH_BINARY)
    gris = cv2.cvtColor(gris, cv2.COLOR_GRAY2BGR)
    th = cv2.cvtColor(th, cv2.COLOR_GRAY2BGR)
    gris = imutils.resize(gris, height=gris.shape[0]//2)
    th = imutils.resize(th, height=th.shape[0]//2)
    cv2.putText(gris, 'gRIS', (10,100), cv2.FONT_ITALIC, 2, (0, 255,0), 2)
    cv2.putText(th, 'BINARIA', (10,100), cv2.FONT_ITALIC, 2, (0, 255,0), 2)
    cv2.putText(frame, 'NORMAL', (10,100), cv2.FONT_ITALIC, 2, (0, 255,0), 2)
    con_h = cv2.vconcat([gris, th])
    con_v = cv2.hconcat([frame, con_h])
    cv2.imshow('video GRIS', con_v)
    # cv2.imshow('video GRIS', gris)
    # cv2.imshow('video BINARIA', th)
    print(frame.shape)
    print(gris.shape)
    print(th.shape)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
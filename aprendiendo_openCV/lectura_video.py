import cv2

## lectura de video,
# valor del cero es por el numero de la camara
# captura = cv2.VideoCapture(0)

# lectura de video guardado
captura = cv2.VideoCapture('video-salida.avi')

# guarda el video, (nombre video, fuente, fps, size)
salida = cv2.VideoWriter('video-salida.avi', cv2.VideoWriter_fourcc(*'XVID'), 60.0, (640, 480))


# Aquí tenemos la estructura de repetición while, 
# la cual será infinita mientras se esté capturando el video hasta que sea presionada una tecla como veremos a continuación.
while (captura.isOpened()):
#La función .read(), en este caso captura.read(), desempaqueta dos valores, 
# el primero es una variable booleana, 
# y el segundo la imagen en sí. 
# A continuación brevemente las dos variables obtenidas en este programa:
#ret: Esta variable booleana es True cuando SÍ se ha capturado una imagen, mientras que es False cuando NO se ha capturado una imagen con la cual trabajar.
#imagen: En sí es la imagen con la cual se puede trabajar.

#Este condicionante: if ret == True, 
# nos permite seguir si es que existe una imagen capturada, 
# también se podría comparar con False, y aplicar break, en caso que no se tenga la imagen

    ret, imagen = captura.read()
    if ret == True:
        cv2.imshow('mi video', imagen)
        # Este condicionante va a permitir salir del programa o terminar la visualización, hasta que sea presionada la tecla s. Se añade & 0xFF, cuando la máquina en la que se está realizando el programa es de 64 bits.
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else : break
captura.release()    
cv2.destroyAllWindows()
    
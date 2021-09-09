import cv2
##  leer imagen 
## exites un segundo parametro, 0 = imagen en gris
imagen = cv2.imread('mandrill_colour.png', 0)

# visualizar imgen
# param 1 = nombre ventana, param 2 = imgen a visualizar
cv2.imshow('mi imahnes', imagen)

# guarda la imgen hahah 
cv2.imwrite('Grises.png',imagen)

## tiempo que se muestre la imagen,
# con el valor 0 se ve infinitamente hasta que presiones cualquier tecla.
cv2.waitKey(0)

# Finalmente para cerrar la visualización creada usamos cv2.destroyAllWindows
cv2.destroyAllWindows()

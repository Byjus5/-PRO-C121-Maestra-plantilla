import cv2
import time
import numpy as np

#Para guardar el output en un archivo output.avi
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

#Iniciar la cámara web
cap = cv2.VideoCapture(0)

#Permitir a la cámara web iniciar haciendo que el código tenga un retraso de 2 segundos
time.sleep(2)
bg = 0

#Capturar fondo para 60 cuadros
for i in range(60):
    ret, bg = cap.read()
#Voltear el fondo
bg = np.flip(bg, axis=1)

#Leer el cuadro captado hasta que la cámara esté abierta
while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    #Voltear la imagen para consistencia
    img = np.flip(img, axis=1)



    #Generar el output final
    final_output = img
    output_file.write(img)
    #Mostrar el output al usuario
    cv2.imshow("magia", final_output)
    cv2.waitKey(1)


cap.release()
out.release()
cv2.destroyAllWindows()


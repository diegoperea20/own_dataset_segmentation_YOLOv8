# Importamos las librerias
from ultralytics import YOLO
import cv2
import os

# Leer nuestro modelo
# originalmente esta en: runs\segment\train2\weights\best.pt
model = YOLO("best.pt")      

# Ruta de la carpeta que contiene las imágenes
ruta_imagenes = "own_dataset_segmentation_YOLOv8/Data/train/images"

# Listar los archivos en la carpeta de imágenes
archivos_imagenes = os.listdir(ruta_imagenes)

# Bucle para procesar cada imagen
for archivo in archivos_imagenes:
    # Leer la imagen
    ruta_imagen = os.path.join(ruta_imagenes, archivo)
    frame = cv2.imread(ruta_imagen)

    # Leemos resultados
    resultados = model.predict(frame, imgsz=640, conf=0.98)

    # Mostramos resultados
    anotaciones = resultados[0].plot()

    # Creamos una ventana para mostrar la detección y segmentación
    cv2.namedWindow("DETECCION Y SEGMENTACION", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("DETECCION Y SEGMENTACION", 800, 600)

    # Mostramos nuestros fotogramas
    cv2.imshow("DETECCION Y SEGMENTACION", anotaciones)

    # Esperar a que se presione una tecla (0 indica esperar indefinidamente)
    key = cv2.waitKey(0)

    # Cerrar la ventana al presionar 'q' (113 en el código ASCII)
    if key == 113:
        break

# Cerrar nuestra ventana
cv2.destroyAllWindows()

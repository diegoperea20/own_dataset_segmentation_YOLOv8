# own_dataset_segmentation_YOLOv8

<p align="justify">
    Segmentacion y detection de objetos con propio dataset usando YOLOV8  , en el que se utiliza un dataset propio de una moneda de 200 pesos colombianos del año 2023.
</p>
<p align="center">
  <img src="README-images\coin-detect.PNG"  alt="StepLast">
</p>

<p align="center">
  <img src="README-images\coin-detect1.PNG"  alt="StepLast">
</p>

La organizacion de los archivos y el etiquetado como su entrenamiento se siguió los pasos de un video de [segmentacion de instancias](https://www.youtube.com/watch?v=rk7zOBRJWCc)


<p align="center">
  <a href="https://www.youtube.com/watch?v=rk7zOBRJWCc">
    <img src="https://i.ytimg.com/vi/rk7zOBRJWCc/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAFzMmbtHbHMzDep1jBpUPig2GHSg" alt="SEGMENTACIÓN DE INSTANCIAS Y DETECCIÓN DE OBJETOS PERSONALIZADA | Entrenamiento paso a paso YoloV8">
  </a>
</p>



<p align="justify">
En el entrenamiento de este proyecto propio de monedas de 200 pesos colombianos  se realizó con CPU ,cabe aclarar que cuando se realiza el cambio de imagenes a .json el archivo dataset.yaml no se crea , por esto se creó y editó según la caracteristicas del proyecto; Y para el uso de GPU se creó un notebook segmentation_detect_colab.ipynb (si lo usas modificar direcciones donde se ubican tus archivos)
</p>

<p align="justify">
La segmentacion en este caso la realiza cuando se identifica la moneda , pero el dataset que creó solo fue de 25 imagenes por lo que lo mejor es usar más de 1000 imagenes , 800 en train y 200 en val 
</p>

Para ver version [pytorch](https://pytorch.org/get-started/locally/) si quieres usar GPU en local


---

<p align="justify">
De forma local, realizarlo con un entorno virtual como por ejemplo conda con python:3.8.17
</p>

# Steps to implement it

1. Usar Dockerfile 
2. Utilice entornos virtuales y aplique requisitos.txt
```python
#Con conda python 3.8

conda create -n mi_entorno python=3.8

pip install -r requirements.txt
```


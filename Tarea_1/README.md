INFORME TAREA 1
================

### Consideraciones

- En esta tarea se implemento una red neuronal. Nuestra implementación se realizó en base a 3 clases, a saber: Neurona, Capa de Neuronas y Red Neuronal. 
- Se desarrollaron unit test para cada una de estas implementaciones donde se puso énfasis en lograr robustez con respecto a los parámetros de entrada.

### Instrucciones

- El lenguaje ocupado para el desarrollo de esta tarea es Python 3.7 en Windows. 
Se recomienda descargar la distribución anaconda desde [aquí](https://repo.anaconda.com/archive/Anaconda3-2019.07-Windows-x86_64.exe) ya que al usar esta distribución no será necesario instalar las librerías por separado.
- Las librerías ocupadas para el desarrollo de la tarea son numpy, sklearn y matplotlib. Estas podemos instalarlas (en caso de necesitarlo) con facilidad al usar en la consola los siguientes comandos respectivamente:
- Para instalar numpy usamos el comando `pip install numpy`
- Para instalar matplotlib usamos el comando `pip install matplotlib`
- Para instalar sklearn debemos asegurarnos de tener instalado previamente numpy y scipy por lo que debemos primero usar el comando `pip install scipy`. 
Luego podemos ejecutar el comando `pip install -U scikit-learn`


### Dataset

- El dataset ocupado fue el recomendado en el enunciado de la tarea, es decir, Iris dataset. El cual corresponde a las mediciones de las semillas de 3 tipos de flores de iris, las cuales son:
-
-
-
-
-Podemos obtener una descripción más detallada [acá](https://archive.ics.uci.edu/ml/datasets/seeds)

### Análisis de resultados

Entrenamos la red con un 80% del dataset. Es decir, nuestra partición del dataset fue 80% para entrenamiento y 20% para testeo.

Al entrenar la red obtuvimos el siguiente comportamiento:

al evaluar en el dataset de testeo obtuvimos:
- Un error MSE igual a 0.08950901338195494
- un porcentaje de acierto igual a 0.8095238095238095

Los aprendizajes realizados en el desarrollo de esta tarea pueden resumirse en lo siguiente:
- Fue complejo generar los métodos de back propagation de manera correcta
- Tambíen fue difícil hacer que el programa sea robusto con respecto a los inputs
- Nuestra implementación da buenos resultados aunque reconocemos que al no haber usando una implementación matricial no es tan eficiente. Además en nuestro código, dada está condición, tampoco 
fijamos el foco en la eficiencia sino en maximizar la comprensión del funcionamiento de la red.
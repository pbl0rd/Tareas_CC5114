INFORME TAREA 2
================

### Consideraciones

- En esta tarea se implementó un algoritmo genético. La implementación se realizó creando una clase GENALG. 


### Instrucciones

- El lenguaje ocupado para el desarrollo de esta tarea es Python 3.7 en Windows. 
Se recomienda descargar la distribución anaconda desde [aquí](https://repo.anaconda.com/archive/Anaconda3-2019.07-Windows-x86_64.exe) ya que al usar esta distribución no será necesario instalar las librerías por separado.
- Las librerías ocupadas para el desarrollo de la tarea son numpy, seaborn y matplotlib. Estas podemos instalarlas (en caso de necesitarlo) con facilidad al usar en la consola los siguientes comandos respectivamente:
- Para instalar numpy usamos el comando `pip install numpy`
- Para instalar matplotlib usamos el comando `pip install matplotlib`
- Para instalar seaborn debemos asegurarnos de tener instalado previamente numpy, matplotlib, pandas y scipy por lo que debemos primero ejecutar los comandos (en caso de no tener instalados estos últimos) `pip install pandas` y `pip install scipy`. 
Luego podemos ejecutar el comando `pip install seaborn`

### Análisis de resultados

Mejora de fitness por generación: 

![alt text](https://github.com/pbl0rd/Tareas_CC5114/blob/master/Tarea_2/Images/Fitness_por_Generacion.png)

Heatmap de configuraciones: 

![alt text](https://github.com/pbl0rd/Tareas_CC5114/blob/master/Tarea_2/Images/Heatmap.png)

Los aprendizajes realizados en el desarrollo de esta tarea pueden resumirse en lo siguiente:
 - El algoritmo genético se puede implementar de forma que tenga la flexibilidad de adaptarse a una gran cantidad de aplicaciones.
 - La implementación realizada permite modificaciones futuras con el fin de añadir nuevas formas de selección y reproducción que pueden ser útiles para ciertas aplicaciones.

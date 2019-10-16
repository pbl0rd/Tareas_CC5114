INFORME TAREA 2
================

### Consideraciones

- En esta tarea se implementó un algoritmo genético. 
- La implementación se realizó creando una clase GENALG. Esta recibe como entrada el tamaño de la población, función de fitness, función de creacion de genes, función de creación de individuos, diccionario que caracteriza a un individuo, diccionario con la condición de parada, tasa de mutación y una tasa de elitismo
- Se implementaron dos métodos para realizar la selección: mediante ruleta o mediante torneo. El metodo a usar se puede elegir al hacer correr al algoritmo.
- Se permite fijar el número de competidores en el método de torneo si se elige para realizar la selección.
- Se permite elegir la condición de finalización del algoritmo: ya sea por alcanzar un número determinado de iteraciones o por alcanzar un umbral de fitness.
- A pesar de no ser necesario para los ejercicios resueltos se deja la posibilidad de construir individuos cuyos genes son de diversos tipos.



### Instrucciones

- El lenguaje ocupado para el desarrollo de esta tarea es Python 3.7 en Windows. 
Se recomienda descargar la distribución anaconda desde [aquí](https://repo.anaconda.com/archive/Anaconda3-2019.07-Windows-x86_64.exe) ya que al usar esta distribución no será necesario instalar las librerías por separado.
- Las librerías ocupadas para el desarrollo de la tarea son numpy, seaborn y matplotlib. Estas podemos instalarlas (en caso de necesitarlo) con facilidad al usar en la consola los siguientes comandos respectivamente:
- Para instalar numpy usamos el comando `pip install numpy`
- Para instalar matplotlib usamos el comando `pip install matplotlib`
- Para instalar seaborn debemos asegurarnos de tener instalado previamente numpy, matplotlib, pandas y scipy por lo que debemos primero ejecutar los comandos (en caso de no tener instalados estos últimos) `pip install pandas` y `pip install scipy`. 
Luego podemos ejecutar el comando `pip install seaborn`

### Análisis de resultados
Primer Ejercicio: (Secuencia de bits) Dada una secuencia de bits, se pide que el algoritmo encuentre la secuencia.
Para este problema un individuo consiste en un diccionario de genes de largo igual al de la secuencia entregada, donde cada gen es un bit.
El fitness de un individuo corresponde a un ponderador por el valor absoluto de la diferencia entre el número entero que representa la secuencia entregada y el número entero que representa la secuencia del individuo.

Mejora de fitness por generación: 

![alt text](https://github.com/pbl0rd/Tareas_CC5114/blob/master/Tarea_2/Images/Fitness_por_Generacion_EX1.png)

El gráfico anterior muestra la evolución del fitness (máximo, promedio y mínimo) a medida que avanzan las generaciones. Se puede observar que ya a partir de aproximadamente la iteración/generación 10 el fitness máximo (verde) se estanca en las cercanías de 0. Se puede notar también que el fitness promedio (azul) sube rápidamente en las primeras generaciones y después se mantiene oscilando en un arngo acotado.
Heatmap de configuraciones: 

![alt text](https://github.com/pbl0rd/Tareas_CC5114/blob/master/Tarea_2/Images/Heatmap.png)

Los aprendizajes realizados en el desarrollo de esta tarea pueden resumirse en lo siguiente:
 - El algoritmo genético se puede implementar de forma que tenga la flexibilidad de adaptarse a una gran cantidad de aplicaciones.
 - La implementación realizada permite modificaciones futuras con el fin de añadir nuevas formas de selección y reproducción que pueden ser útiles para ciertas aplicaciones.

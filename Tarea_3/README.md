INFORME TAREA 3
================

## Consideraciones

- En esta tarea se implementaron técnicas de programación genética. 
- La implementación se realizó creando una clase GENALG. Esta recibe como entrada el tamaño de la población, función de fitness, función de creacion de genes, función de creación de individuos, diccionario que caracteriza a un individuo, diccionario con la condición de parada, tasa de mutación y una tasa de elitismo
- Se implementaron dos métodos para realizar la selección: mediante ruleta o mediante torneo. El metodo a usar se puede elegir al hacer correr al algoritmo.
- Se permite fijar el número de competidores en el método de torneo si se elige para realizar la selección.
- Se permite elegir la condición de finalización del algoritmo: ya sea por alcanzar un número determinado de iteraciones o por alcanzar un umbral de fitness.
- A pesar de no ser necesario para los ejercicios resueltos se deja la posibilidad de construir individuos cuyos genes son de diversos tipos.



## Instrucciones

- El lenguaje ocupado para el desarrollo de esta tarea es Python 3.7 en Windows. 
Se recomienda descargar la distribución anaconda desde [aquí](https://repo.anaconda.com/archive/Anaconda3-2019.07-Windows-x86_64.exe) ya que al usar esta distribución no será necesario instalar las librerías por separado.
- Las librerías ocupadas para el desarrollo de la tarea son copy, numpy, seaborn y matplotlib. Estas podemos instalarlas (en caso de necesitarlo) con facilidad al usar en la consola los siguientes comandos respectivamente:
- El módulo copy viene preinstalado en python
- Para instalar numpy usamos el comando `pip install numpy`
- Para instalar matplotlib usamos el comando `pip install matplotlib`
- Para instalar seaborn debemos asegurarnos de tener instalado previamente numpy, matplotlib, pandas y scipy por lo que debemos primero ejecutar los comandos (en caso de no tener instalados estos últimos) `pip install pandas` y `pip install scipy`. 
Luego podemos ejecutar el comando `pip install seaborn`

## Análisis de resultados

### Primer Ejercicio: (Secuencia de bits) 
Dada una secuencia de bits, se pide que el algoritmo encuentre dicha secuencia.

Para este problema un individuo consiste en un diccionario de genes de largo igual al de la secuencia entregada, donde cada gen es un bit (0 o 1).

El fitness de un individuo corresponde a un ponderador por el valor absoluto de la diferencia entre el número entero que representa la secuencia entregada y 
el número entero que representa la secuencia del individuo.

Se ejecuta una prueba del algoritmo para encontrar la secuencia 00101010110101.

Mejora de fitness por generación: Se ejecuta el algoritmo durante 100 iteraciones, tasa de mutación = 0.1, usando torneo con 5 competidores, tamaño de población igual a 50 y sin elitismo.

![alt text](https://github.com/pbl0rd/Tareas_CC5114/blob/master/Tarea_2/Images/Fitness_por_Generacion_EX1.png)

El gráfico anterior muestra la evolución del fitness (máximo, promedio y mínimo) a medida que avanzan las generaciones. 
Se puede observar que ya a partir de aproximadamente la iteración/generación 10 el fitness máximo (verde) se estanca en las cercanías de 0. 
Se puede notar también que el fitness promedio (azul) sube rápidamente en las primeras generaciones y después se mantiene oscilando en un rango acotado.
Por último, el fitness mínimo (rojo) mantiene una oscilación descontrolada a lo largo de las iteraciones.

### Segundo Ejercicio: (Encontrar una palabra o frase) 
Dada una frase, se pide que el algoritmo encuentre dicha frase.

Para este problema un individuo consiste en un diccionario de genes de largo igual al número de letras (incluyendo espacios) de la frase entregada, 
donde cada gen es un letra (esta letra puede ser mayúscula, minúscula o un espacio).

El fitness de un individuo corresponde al número de coincidencias entre la frase entregada y la frase formada por los genes del individuo. 

Se ejecuta una prueba del algoritmo para encontrar la frase 'helloworld'.

Mejora de fitness por generación: Se ejecuta el algoritmo durante 100 iteraciones, tasa de mutación = 0.2, usando torneo con 5 competidores, tamaño de población igual a 50 y sin elitismo.

![alt text](https://github.com/pbl0rd/Tareas_CC5114/blob/master/Tarea_2/Images/Fitness_por_Generacion_EX2.png)

El gráfico anterior muestra la evolución del fitness (máximo, promedio y mínimo) a medida que avanzan las generaciones. 
Se puede observar que cerca de la iteración/generación 30 el fitness máximo (verde) alcanza el valor máximo 10, es decir, encuentra la frase pedida y después este individuo desaparece de la población. 
Se puede notar también que las 3 curvas suben velozmente en un principio y luego empiezan oscilar en torno a un rango acotado. 

Mejora de fitness por generación: Se ejecuta el algoritmo durante 100 iteraciones, tasa de mutación = 0.2, usando torneo con 5 competidores, tamaño de población igual a 50 y tasa de elitismo 0.2.

![alt text](https://github.com/pbl0rd/Tareas_CC5114/blob/master/Tarea_2/Images/Fitness_por_Generacion_EX2_Elitismo.png)

A diferencia del caso anterior, en este se ocupó una tasa de elitismo, lo que se ve reflejado en  que el la curva del fitness máximo es no decreciente. 
Cabe resaltar que la subida es levemente más lenta y que el máximo del fitness (se encuentra la frase) se alcanza cerca de la generación 70. 
Sin embargo, el rango de oscilación de las demás curvas se encuentra en un nivel más elevado y es más controlado que en el caso anterior. Por último, se ve que una vez encontrada la solución
está no se pierde, a diferencia del caso sin elitismo. 


### Tercer Ejercicio: (Unbound-Knapsack) 
Problema de optimización combinatorial que consiste en que se dispone de una mochila la cual tiene una capacidad máxima establecida, y un set de items con distinto valor y peso.
El problema consiste en determinar cuántos items de cada tipo llevar en la mochila con tal de maximizar la utilidad obtenida de estos sin sobrepasar la capacidad de la mochila. 
Se llama Unbound porque se puede poner la cantidad de veces que uno quiera el mismo item (solo sujeto a la capacidad de la mochila). 
Más información sobre el problema [aquí](https://en.wikipedia.org/wiki/Knapsack_problem)

Para este problema se modeló a un individuo como en un diccionario de genes de largo igual al número de items distintos disponibles en el set (en este caso, existen 5 tipos de cajas), 
donde cada gen corresponde a la cantidad de items de ese tipo que se añadirán a la mochila (número entero entre 0 y un límite superior dado por la oferta de items y la capacidad de la mochila, en este caso 15).

El fitness de un individuo corresponde al valor obtenido por los items que se llevan en la mochila menos una penalización por cada kilo que sobrepase la capacidad de la mochila. 
Este valor puede ser multiplicado por un ponderador para obtener un rango más acotado de valores y poder realizar mejores visualizaciones.

El ejemplo a resolver consiste en: Una mochila de capacidad 15 kg. y 5 tipos de cajas distintas de las cuales elegir: 
- Una de peso 12 y valor 4.
- Otra de peso 2 y valor 2.
- Otra con peso 1 y valor 2.
- Otra con peso 1 y valor 1.
- Por último, una con peso 4 y valor 10.

Mejora de fitness por generación: Se ejecuta el algoritmo durante 100 iteraciones, tasa de mutación = 0.2, usando torneo con 5 competidores, tamaño de población igual a 50 y tasa de elitismo 0.2.

![alt text](https://github.com/pbl0rd/Tareas_CC5114/blob/master/Tarea_2/Images/Fitness_por_Generacion_EX3.png)

Se puede observar que el comportamiento de las curvas es similar al exhibido en los ejercicios anteriores, las curvas de máximo fitness y fitness promedio suben velozmente y se mueven en un rango acotado cercano al 0. jercicios anteriores A diferencia del caso anterior, en este se ocupó una tasa de elitismo, lo que se ve reflejado en  que el la curva del fitness máximo es no decreciente. 
Cabe resaltar que el máximo del fitness (se encuentra la solución del probelma) se alcanza cerca de la generación 85. Por último, la curva de fitness mínimo sube ligeramente al principio y se estanca variando en torno al -8.

Heatmap de configuraciones: Se ejecuta el algoritmo fijando el umbral de fitness en 0.36 (cuando se encuentra la solución) (y forzando a terminar el algoritmo si se superan las 10000 generaciones) usando torneo con 5 competidores, y tasa de elitismo 0.2. 
Esto para cada combinación de tasa de mutación en [0.0, 0.1, ..., 0.9, 1.0] y tamaño de población en [50, 100, 150, ..., 900, 950 , 1000]

![alt text](https://github.com/pbl0rd/Tareas_CC5114/blob/master/Tarea_2/Images/Heatmap_EX3.png)

En el gráfico se muestra el número de la generación en la cual se encuentra la solución del problema al ejecutar el algoritmo con la combinación tasa de mutación y tamaño de población correspondiente. 
Notar que las casillas con el número 20000 corresponden a configuraciones que no lograron encontrar algún individuo que alcance o supere el umbral establecido, en este caso, esto significa que no pudieron encontrar la solución.
Se puede observar que a medida que aumenta el tamaño de población la tasa de mutación se vuelve menos importante. 
También se puede notar que en valores extremos de la tasa de mutación (0.0 y 1.0) el comportamiento no es idóneo ya sea porque no hay mucho cambio o por la volatilidad excesiva.

Los aprendizajes realizados en el desarrollo de esta tarea pueden resumirse en lo siguiente:
 - El algoritmo genético se puede implementar de forma que tenga la flexibilidad de adaptarse a una gran cantidad de aplicaciones. Como se pudo observar, solo cambiando levemente 
 el modelamiento de los individuos y de la función de fitness se puede resolver una gran gama de problemas de distinta índole.
 - En particular, se visualiza inmensa utilidad para resolver problemas en los que la cantidad de combinaciones posibles para formar soluciones crece exponencialmente, tales como el problema del vendedor viajero.
 - La implementación realizada permite modificaciones futuras con el fin de añadir nuevas formas de selección y reproducción que pueden ser útiles para ciertas aplicaciones. 
   Por ejemplo, si modificamos la forma de modelar a los individuos del problema 3, ahora teniendo un rango de valore factibles para cada gen en particular, es decir, el número de cajas posibles del tipo i va a variar entre 0 y la función piso de capacidad/peso_i .
   Para esto, también debemos quitar la restricción de la función de creación de genes. Al hacer esto, el heatmap de configuraciones mejora significativamente resultando en que en la mayoría de los casos la solución se encuentra adentro de la población inicial
   ![alt text](https://github.com/pbl0rd/Tareas_CC5114/blob/master/Tarea_2/Images/Heatmap_EX3_1.png)

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
Primer Ejercicio: (Secuencia de bits) Dada una secuencia de bits, se pide que el algoritmo encuentre dicha secuencia.

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

Segundo Ejercicio: (Encontrar una palabra o frase) Dada una frase, se pide que el algoritmo encuentre dicha frase.

Para este problema un individuo consiste en un diccionario de genes de largo igual al número de letras (incluyendo espacios) de la frase entregada, 
donde cada gen es un letra (esta letra puede ser mayúscula, minúscula o un espacio).

El fitness de un individuo corresponde al número de coincidencias entre la frase entregada y la frase formada por los genes del individuo. 
'helloworld'.

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
está no se pierda a diferencia del caso sin elitismo. 

Heatmap de configuraciones: 

![alt text](https://github.com/pbl0rd/Tareas_CC5114/blob/master/Tarea_2/Images/Heatmap.png)

Los aprendizajes realizados en el desarrollo de esta tarea pueden resumirse en lo siguiente:
 - El algoritmo genético se puede implementar de forma que tenga la flexibilidad de adaptarse a una gran cantidad de aplicaciones.
 - La implementación realizada permite modificaciones futuras con el fin de añadir nuevas formas de selección y reproducción que pueden ser útiles para ciertas aplicaciones.

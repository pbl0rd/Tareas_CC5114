INFORME TAREA 3
================

## Consideraciones

- En esta tarea se implementaron técnicas de programación genética. Un algoritmo de programación tiene 3 componentes: librería de árboles, generador aleatorio de árboles y un algoritmo genético adaptado.

- Se utilizó como librería de árboles, la librería arboles.py disponible en el material del curso. Se le realizaron 2 modificaciones: Se agregó un nodo de división y se modificó el método de evaluación de los árboles.
- Se utilizó como generador aleatorio de arboles ast.py disponible en el material del curso. Solo se modificó el uso de la librería random por el modulo random de numpy.
- Se modificó la implementación de la clase GENALG (TAREA 2) correspondiente al algoritmo genético. Esencialmente se modificaron solo dos cosas el método crossover y la mutación, adaptando ambos ahora para poder trabajar con árboles.


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
Para todos los problemas que se analizarán un individuo consiste en un árbol, solo se diferencian en los terminales y las funciones que los componen.

### Encontrar Número 
Dada un número, se pide que el algoritmo encuentre una expresión que se acerque a este usando solamente un conjunto de valores y funciones reducido. Se resolverán 3 variantes de este problema.

### Ejercicio 1 (2.1.1) Encontrar número sin límite de repeticiones
Se debe ocupar las funciones {+,-,*,max(.)} y los terminales {25,7,8,100,4,2} pudiendo repetir los terminales sin restricción.

El fitness de un individuo corresponde al opuesto de un ponderador por el valor absoluto de la diferencia entre el número a encontrar y el número correspondiente a la evaluación del individuo (árbol).

Se ejecuta una prueba del algoritmo para encontrar el número 65346.

Mejora de fitness por generación: Se ejecuta el algoritmo durante 200 iteraciones, tasa de mutación = 0.1, tasa de elitismo =0.1, usando torneo con 5 competidores, tamaño de población igual a 30. Para la generación de árboles se uso probabilidad de que un árbol deje de crecer =0.3 y máxima profundidad=10.

![alt text](https://github.com/pbl0rd/Tareas_CC5114/blob/master/Tarea_3/Images/Fitness_por_Generacion_EX1.png)

El gráfico anterior muestra la evolución del fitness (máximo, promedio y mínimo) a medida que avanzan las generaciones. 
Se usaron 2 escalas una para el máximo y otra para el resto. Sin embargo, se puede observar que al incorporar el mínimo, dado que este tiene un rango de variación gigante, se pierde de vista como varían las otras curvas.
Por esto se decidió hacer otro gráfico sin incorporar el fitness mínimo por generación.

![alt text](https://github.com/pbl0rd/Tareas_CC5114/blob/master/Tarea_3/Images/Fitness_por_Generacion_EX1_V2.png)

El gráfico anterior muestra la evolución del fitness (máximo y promedio) a medida que avanzan las generaciones.
Se puede observar que ya a partir de aproximadamente la iteración/generación 175 el fitness máximo (verde) se estanca en 0, esto es, alcanza la solución. 
Se puede notar también que el fitness promedio (azul) presenta un baja en valor muy significativa cerca de la generación 15 esto hace que comparativamente durante el resto del tiempo se mantenga "estable"


A partir de ahora, para términos de este informe, se utilizará este tipo de gráficos para mostrar la evolución del fitness (solo máximo y promedio), no obstante en el repositorio se encuentra la otra versión del gráfico

### Ejercicio 2 (2.1.2) Encontrar número sin límite de repeticiones
Se debe ocupar las funciones {+,-,*,max(.)} y los terminales {25,7,8,100,4,2} pudiendo repetir los terminales sin restricción pero esta vez se castiga el tamaño de los árboles favoreciendo soluciones más pequeñas.

El fitness de un individuo corresponde el opuesto de la suma entre la multiplicación de un ponderador y el valor absoluto de la diferencia entre el número a encontrar y el número correspondiente a la evaluación del individuo (árbol), y la multiplicación de otro ponderador por el tamaño del árbol (considerado como el número de nodos).

Se ejecuta una prueba del algoritmo para encontrar el número 65346.

Mejora de fitness por generación: Se ejecuta el algoritmo durante 200 iteraciones, tasa de mutación = 0.1, tasa de elitismo =0.1, usando torneo con 5 competidores, tamaño de población igual a 30. Para la generación de árboles se uso probabilidad de que un árbol deje de crecer =0.3 y máxima profundidad=10.

![alt text](https://github.com/pbl0rd/Tareas_CC5114/blob/master/Tarea_3/Images/Fitness_por_Generacion_EX2_V2.png)

El gráfico anterior muestra la evolución del fitness (máximo y promedio) a medida que avanzan las generaciones.
Se puede observar que ya a partir de aproximadamente la iteración/generación 110 el fitness máximo (verde) se estanca en las cercanías de 0. 
Al igual que en el ejercicio 1 vemos que el fitness promedio (azul) se mantiene relativamente estable presentando una baja cerca de la generacion 165, sin embargo, esto es solo en apariencia debido a la escala.
Podemos extraer como conclusión en base al ejercicio 1 y al 2 que en general las soluciones son malas pero dentro de ellas se encuentran unas pocas que son buenas.

### Ejercicio 3 (2.1.3) Encontrar número sin repetición
Se debe ocupar las funciones {+,-,*} y los terminales {25,7,8,100,4,2} restringiendo a los árboles de modo que exista a lo más 1 de cada terminal en ellos.

El fitness de un individuo corresponde al opuesto de la suma ponderada entre el valor absoluto de la diferencia entre el número a encontrar y el número correspondiente a la evaluación del individuo (árbol), y la suma de veces que el árbol viola la restricción de unicidad de los terminales.

Se ejecuta una prueba del algoritmo para encontrar el número 65346.

Mejora de fitness por generación: Se ejecuta el algoritmo durante 1000 iteraciones, tasa de mutación = 0.2, tasa de elitismo =0.1, usando torneo con 5 competidores, tamaño de población igual a 50. Para la generación de árboles se uso probabilidad de que un árbol deje de crecer =0.3 y máxima profundidad=10.

![alt text](https://github.com/pbl0rd/Tareas_CC5114/blob/master/Tarea_3/Images/Fitness_por_Generacion_EX3_V2.png)

El gráfico anterior muestra la evolución del fitness (máximo y promedio) a medida que avanzan las generaciones.
Se puede observar que ya a partir de aproximadamente la iteración/generación 700 el fitness máximo (verde) se estanca en las cercanías de 0. 
Se puede notar también que el fitness promedio (azul) presenta varias bajadas significativas por lo que se puede decir que hay volatilidad en cuanto a la calidad de los individuos de una generación como conjunto.

### Implementar variables
Para implementar variables se modificó el método de evaluación que venía en la librería de árboles. 
Puntualmente se añadió la posibilidad de recibir un diccionario de valores para las variables, por ejemplo si las variables son 'x' e 'y' el método de evaluación ahora recibe como entrada un diccionario {'x':x_val, 'y':y_val}. Por defecto el método funciona sin diccionario de valores y por lo tanto se comporta igual que antes. En caso de recibir un diccionario como entrada entonces recursivamente evalua los nodos hijos entregandoles el diccionario.
También fue necesario modificar este método de evaluación para los nodos terminales. De la misma manera ahora es posible entregarle un diccionario de valores como entrada. En este caso, el método intenta devolver el valor númerico del nodo (funciona si el nodo es númerico y falla en caso de que sea variable) y en caso de no poder (caso en que el nodo es una variable) busca el valor en el diccionario de entrada y devuelve ese valor.

### Symbolic Regression
Dada una ecuación, se pide que el algoritmo encuentre una expresión que obtenga el mismo valor que la ecuación buscada para un conjunto de puntos.

### Ejercicio 4 (2.3): Encontrar una ecuación
Se debe ocupar las funciones {+,-,*} y los terminales {-10,...,10,'x'} pudiendo repetir los terminales a gusto

El fitness de un individuo corresponde al opuesto de la multiplicación de un ponderador por la suma para cada punto del intervalo de evaluación del valor absoluto de la diferencia entre el número correspondiente a la evaluación del individuo (árbol) y el valor de la función en el punto.

Se ejecuta una prueba del algoritmo para encontrar la ecuación x**2+x-6 evaluada en [-100,...,100].

Mejora de fitness por generación: Se ejecuta el algoritmo durante 100 iteraciones, tasa de mutación = 0.2, tasa de elitismo = 0.1, usando torneo con 5 competidores, tamaño de población igual a 50. Para la generación de árboles se uso probabilidad de que un árbol deje de crecer =0.3 y máxima profundidad=10.


![alt text](https://github.com/pbl0rd/Tareas_CC5114/blob/master/Tarea_3/Images/Fitness_por_Generacion_EX4_V2.png)

El gráfico anterior muestra la evolución del fitness (máximo, promedio y mínimo) a medida que avanzan las generaciones. 
Se puede observar que cerca de la iteración/generación 10 el fitness máximo (verde) alcanza el valor máximo 0, es decir, encuentra una expresión que coincide con la ecuación buscada en todos los puntos evaluados. 
Se puede notar también que la curva de fitness promedio (azul) sigue un comportamiento similar al evidenciado en los ejercicios anteriores. 

### Implementar el nodo división
Para implementar el nodo de división se modificó la librería de arboles agregando el nodo DivNode. También se modificó el método de evaluación que venía en la librería de árboles. Puntualmente se intenta realizar la evaluación tal como se describe arriba y en caso de no ser posible se eleva un error.
Al modificar de esta forma para penalizar la división por cero en la función de fitness capturamos el error en caso de que se eleve y categorizamos al árbol como inviable gatillando una penalización en su fitness.

### Ejercicio 5 (2.4.3): Encontrar una ecuación penalizando la división por cero
Se debe ocupar las funciones {+,-,*,/} y los terminales {-10,...,10,'x'} pudiendo repetir los terminales a gusto

El fitness de un individuo corresponde al opuesto de la suma entre la multiplicación de un ponderador por la suma para cada punto del intervalo de evaluación del valor absoluto de la diferencia entre el número correspondiente a la evaluación del individuo (árbol) y el valor de la función en el punto, y  otro ponderador por un indicador de si el árbol es inviable o no ( es inviable si se divide por 0)

Se ejecuta una prueba del algoritmo para encontrar la ecuación x**2+x-6 evaluada en [-100,...,100].

Mejora de fitness por generación: Se ejecuta el algoritmo durante 100 iteraciones, tasa de mutación = 0.2, tasa de elitismo = 0.1, usando torneo con 5 competidores, tamaño de población igual a 50. Para la generación de árboles se uso probabilidad de que un árbol deje de crecer =0.3 y máxima profundidad=10.

![alt text](https://github.com/pbl0rd/Tareas_CC5114/blob/master/Tarea_3/Images/Fitness_por_Generacion_EX5_V2.png)

El gráfico anterior muestra la evolución del fitness (máximo, promedio y mínimo) a medida que avanzan las generaciones. 
Se puede observar que cerca de la iteración/generación 25 el fitness máximo (verde) alcanza el valor máximo 0, es decir, encuentra una expresión que coincide con la ecuación buscada en todos los puntos evaluados. 
Se ve que al incorporar el nodo de división le tomó más generaciones encontrar la expresión. Con respecto al fitness promedio (azul) observamos un mejor comportamiento que en casos anteriores, estabilizandose rápidamente sin caídas bruscas.

### Heatmap de configuraciones: Ejercicio 1 
Heatmap de configuraciones: Se ejecuta el algoritmo fijando el umbral de fitness en 0 (cuando se encuentra la solución) (y forzando a terminar el algoritmo si se superan las 100 generaciones) usando torneo con 5 competidores, y tasa de elitismo 0.1. Para la generación de árboles se uso probabilidad de que un árbol deje de crecer =0.3 y máxima profundidad=10.
Esto para cada combinación de tasa de mutación en [0.0, 0.1, ..., 0.9, 1.0] y tamaño de población en [50, 100, 150, ..., 900, 950 , 1000]

![alt text](https://github.com/pbl0rd/Tareas_CC5114/blob/master/Tarea_3/Images/Heatmap_EX1.png)

En el gráfico se muestra el número de la generación en la cual se encuentra la solución del problema al ejecutar el algoritmo con la combinación tasa de mutación y tamaño de población correspondiente. 
Notar que las casillas con el número 200 corresponden a configuraciones que no lograron encontrar algún individuo que alcance o supere el umbral establecido, en este caso, esto significa que no pudieron encontrar la solución.
Se puede observar que a medida que aumenta el tamaño de población la tasa de mutación se vuelve menos importante. 
También se puede notar que en valores extremos de la tasa de mutación (0.0 y 1.0) el comportamiento no es idóneo ya sea porque no hay mucho cambio o por la volatilidad excesiva.

Los aprendizajes realizados en el desarrollo de esta tarea pueden resumirse en lo siguiente:
 - Esta implementación expande las posibilidades de uso del algoritmo génetico previamente implementado. 
   Ahora es aplicable a la generación de programas lo que es de suma utilidad en la práctica.
 - Trabajar con el algoritmo genético y árboles es mucho más versátil que lo visto en la tarea 2. Sin embargo, también es mucho más demandante para el ordenador, por lo que sería interesante como trabajo futuro optimizar las implementaciones con el fin de mejorar el rendimiento y eficiencia de estas.

 

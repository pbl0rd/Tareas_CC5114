# coding=utf-8
import numpy as np
from arboles import *


# Definimos una clase GENALG para nuestro algoritmo genético
class GENALG(object):

    # Método inicializador para la clase algoritmo genético : recibe 8 inputs, 2 de ellos opcionales
    # - Un número entero positivo pop_sz_0 con el tamaño de población
    # - Una función fit_fn que permite obtener el fitness de un individuo
    # - Una función cr_genes que permite crear los genes de un individuo
    # - Una función cr_indv que permite crear a los individuos de la población
    # - Un diccionario de diccionarios indv_chars que para cada gen del individuo posee un diccionario con información
    #   acerca del tipo de gen y del conjunto de posibles valores que este puede tomar este gen.
    # - Un diccionario term_cond que entrega información sobre el criterio de parada, específicamente,
    #   el tipo de criterio a ocupar ('iterations' o 'fitness_th'), un valor de fitness a alcanzar fitness_th (No
    #   necesariamente el óptimo) y el número de iteraciones máximo.
    # - (Opcional) Tasa de mutación mut_rate (float entre 0.0 y 1.0) que da la probabilidad de que un gen de un
    #    individuo tenga una mutación (por defecto toma el valor 0.2)
    # - (Opcional) Tasa de elitismo elitism_rate (float entre 0.0 y 1.0) que da el porcentaje de la población que será
    #    ocupado para conservar a los mejores individuos de la generación pasada (por defecto toma el valor 0.0,
    #    esto es, por defecto no se ocupa elitismo)
    def __init__(self, pop_sz_0: int, fit_fn, cr_genes, cr_indv, indv_chars, term_cond, mut_rate=0.2, elitism_rate=0.0):
        # Verificamos que los parámetros de entrada del constructor sean los correctos
        if type(pop_sz_0) != int:
            raise ValueError("Input n_weights debe ser un número entero positivo")
        # atributo con el tamaño de la población
        self.__pop_sz = pop_sz_0
        # atributo con un diccionario de la población actual
        self.__pop = None
        # atributo con un diccionario del fitness de cada individuo de la población actual
        self.__pop_fitness = None
        # atributo con el fitness máximo dentro de la población actual
        self.__max_fitness = None
        # atributo con el fitness promedio de la población actual
        self.__mean_fitness = None
        # atributo con el fitness mínimo dentro de la población actual
        self.__min_fitness = None
        # atributo con el individuo con el fitness máximo dentro de la población actual
        self.__fittest_indv = None
        # atributo con la función de fitness
        self.__fit_fn = fit_fn
        # atributo con la función de creación de genes
        self.__cr_genes = cr_genes
        # atributo con la función de creación de individuos
        self.__cr_indv = cr_indv
        # atributo con el diccionario que caracteriza a un individuo
        self.__indv_chars = indv_chars        
        # atributo con el diccionario del criterio de parada
        self.__term_cond = term_cond
        # atributo con la tasa de mutación
        self.__mut_rate = mut_rate
        # atributo con la cantidad de individuos para aplicar elitismo
        self.__elitism = int(np.ceil(elitism_rate * pop_sz_0))

        # Métodos get para obtener los atributos del algoritmo genético.

    # Función para obtener el tamaño de la población
    def get_pop_sz(self):
        return self.__pop_sz

    # Función para obtener la población
    def get_pop(self):
        if self.__pop is None:
            raise ValueError("la población no ha sido creada")
        else:
            return self.__pop

    # Función para obtener la tasa de mutación
    def get_mut_rate(self):
        return self.__mut_rate

    # Función para obtener condición de terminación
    def get_term_cond(self):
        return self.__term_cond

        # Función para obtener la función de fitness del algoritmo

    def get_fit_fn(self):
        return self.__fit_fn

    # Función para obtener la función de creación de genes del algoritmo
    def get_cr_genes(self):
        return self.__cr_genes

    # Función para obtener la función de creación de individuos del algoritmo
    def get_cr_indv(self):
        return self.__cr_indv

    # Función para obtener el número de individuos al aplicar elitismo
    def get_etilitsm(self):
        return self.__elitism

    # Función para obtener el fitness de la población
    def get_pop_fitness(self):
        if self.__pop_fitness is None:
            raise ValueError("El fitness de la población no ha sido calculado")
        else:
            return self.__pop_fitness

    # Función para obtener el fitness máximo de la población
    def get_max_fitness(self):
        if self.__max_fitness is None:
            raise ValueError("El fitness de la población no ha sido calculado")
        else:
            return self.__max_fitness

    # Función para obtener el fitness mínimo de la población
    def get_min_fitness(self):
        if self.__min_fitness is None:
            raise ValueError("El fitness de la población no ha sido calculado")
        else:
            return self.__min_fitness

    # Función para obtener el fitness promedio de la población
    def get_mean_fitness(self):
        if self.__mean_fitness is None:
            raise ValueError("El fitness de la población no ha sido calculado")
        else:
            return self.__mean_fitness

    # Función para obtener el individuo con el fitness máximo de la población
    def get_fitness_indv(self):
        if self.__fitness_indv is None:
            raise ValueError("El fitness de la población no ha sido calculado")
        else:
            return self.__fitness_indv

    # Métodos para aplicar el algoritmo genético

    # Función para generar la población inicial
    def gen_pop(self):
        pop = {}  # Diccionario vacío para guardar la población
        # Generamos individuos acorde con el número de individuos de la población
        for i in range(self.__pop_sz):
            # Creamos un nuevo individuo con la función de creación de individuos, notar que la función recibe la
            # función de creación de genes y el diccionario de características de un individuo.
            pop[i] = self.__cr_indv(self.__cr_genes, self.__indv_chars)
        self.__pop = pop  # se actualiza el atributo con la población

    # Función para calcular el fitness de la población. Recibe un diccionario con parámetros especificos de la
    # función de fitness.
    def comp_pop_fitness(self, fit_params):
        pop_fitness = {}  # Diccionario vacío para guardar el fitness de la población
        new_pop = {}  # Diccionario vacío para guardar la población ordenada de manera descendiente en fitness
        l_pfitness = []  # lista para guardar los fitness de la población
        # Calculamos el fitness de cada individuo de la población y lo guardamos en una lista
        for i in range(self.__pop_sz):
            fitness = self.__fit_fn(self.__pop[i], fit_params)
            l_pfitness.append(fitness)
        mean_fitness = np.mean(l_pfitness)  # calculamos fitness promedio
        max_fitness = max(l_pfitness)  # calculamos fitness máximo
        min_fitness = min(l_pfitness)  # calculamos fitness mínimo
        fittest_indv = self.__pop[l_pfitness.index(max_fitness)].copy()  # copiamos el individuo con mayor fitness
        # actualizamos atributos de la clase
        self.__max_fitness = max_fitness
        self.__min_fitness = min_fitness
        self.__mean_fitness = mean_fitness
        self.__fittest_indv = fittest_indv
        # creamos una copia de la lista con los fitness para hacer operaciones
        l_aux = l_pfitness[:]
        # Generamos los diccionarios con la población ordenada de manera descendiente en fitness y con sus fitness
        for i in range(self.__pop_sz):
            max_ind = l_aux.index(max(l_aux))  # buscamos el lugar correspondiente al individuo con fitness máximo
            new_pop[i] = self.__pop[max_ind].copy()  # guardamos al individuo del lugar max_ind en su nueva posición
            pop_fitness[i] = l_aux[max_ind]  # guardamos el fitness del individuo en su nuevo lugar
            # actualizamos el valor de fitness del ind. en la lista para no volver a considerarlo
            l_aux[max_ind] = -np.inf
        # actualizamos la población y el fitness
        self.__pop = new_pop.copy()
        self.__pop_fitness = pop_fitness.copy()

    # Método para aplicar la selección mediante torneo de los individuos de la población. Recibe de entrada el número 
    # de competidores (entero positivo). Asume que la poblacíon está ordenada en base al fitness de manera
    # decreciente (paso que ocurre al calcular el fitness de la población con el método comp_pop_fitness)
    def tournament_sel(self, slots: int):
        if slots > self.__pop_sz:
            raise ValueError("slots debe ser un número entero positivo menor que el tamaño de la población")
        else:
            # elegimos un conjunto de índices al azar de tamaño igual al número de competidores
            chosen_set = np.random.randint(0, self.__pop_sz, slots)
            # Como la población está ordenada el ganador es el menor de los índices del conjunto
            winner = min(chosen_set)
            return self.__pop[winner]  # retornamos al individuo ganador

    # Método para aplicar la selección mediante ruleta de los individuos de la población.
    def roulette_sel(self):
        fit_vals = list(self.__pop_fitness.values()) # lista con valores de fitness
        num_neg_vals = sum(n < 0 for n in fit_vals)
        # si hay fitness negativos debemos normalizar estos valores conservando las distancias
        if num_neg_vals > 0:
            min_val = abs(min(fit_vals))
            new_fit_vals = [min_val + item for item in fit_vals]
        else:
            new_fit_vals = fit_vals[:]
        total_fit = sum(new_fit_vals)  # calculamos la suma de los fitness
        # si todas las fitness son iguales a 0 retornamos un individuo al azar
        if total_fit == 0:
            idx = np.random.randint(0, self.__pop_sz)
            return self.__pop[idx]
        else:
            sum_fit = 0  # llevamos la cuenta parcial de la suma de los fitness
            th = total_fit * np.random.rand()  # obtenemos un punto aleatorio entre 0 y la suma total de fitness
            for i in range(self.__pop_sz):
                sum_fit += new_fit_vals[i]
                if sum_fit > th:  # retornamos al individuo en la posición que logra superar el umbral th
                    return self.__pop[i]

    # Método para aplicar la operación crossover a 2 individuos y generar un nuevo individuo.
    def crossover(self, indv1, indv2):
        new_element = indv1.copy()  # Hacemos una copìa del padre 1
        p2 = np.random.choice(indv2.serialize()).copy()  # Hacemos una copia de un sub-arbol del padre 2
        np.random.choice(new_element.serialize()).replace(p2)  # Reemplazamos en un nodo al azar el sub-arbol
                                                               # obtenido del padre 2
        return new_element.copy()  # Retornamos una copia del hijo creado

    # Método para aplicar la operación mutation a 1 individuo y generar un nuevo individuo.
    def mutation(self, indv):
        # Vemos si la mutación ocurre
        if np.random.rand() > self.__mut_rate:
            return indv.copy()		
        else:
            new_element = indv.copy() # Hacemos una copìa del individuo
            params = self.__indv_chars.copy() # Hacemos una copia de las caracteristicas de un individuo
            params['max_depth'] = np.random.randint(0, self.__indv_chars['max_depth']+1) #Generamos un tamaño al azar
            p2 = self.__cr_indv(self.__cr_genes, params) # Creamos un arbol aleatorio
            np.random.choice(new_element.serialize()).replace(p2)  # Reemplazamos en un nodo al azar del individuo el
                                                                   # arbol obtenido p2
            return new_element.copy()  # Retornamos una copia del individuo mutado

    # Método para aplicar el algortimo genético. Recibe los parametros de la función de fitness en fit_params, el tipo
    # de selección selection_type a ocupar ('tournament' o 'roulette', por defecto tournament), una semilla para la
    # reproducibilidad de los resultados y la cantidad de ompetidores de la seleccion tournament en caso de necesitarlo
    # (por defecto 3)
    def apply(self, fit_params, selection_type='tournament', random_state=None, slots=3):
        if type(random_state) == int:
            np.random.seed(random_state)  # fijamos la semilla de ser ingresada
        self.gen_pop()   # generamos la población inicial
        self.comp_pop_fitness(fit_params)  #calculamos el fitness de la población inicial
        generations = {}  # gereramos un diccionario vacío para ir guardando la información de cada generación
        iters = 0  # fijamos el contador de generaciones en 0
        overall_max_fitness = self.__max_fitness  # inicializamos el registro del fitness máximo alcanzado
        overall_fittest_indv = self.__fittest_indv  # inicializamos el registro del individuo de máximo fitness
        generations[iters] = {}  # generamos un diccionario vacío para guardar la información de la generación
        generations[iters]['max_fitness'] = self.__max_fitness  # registramos fitness máximo de la generación actual
        generations[iters]['min_fitness'] = self.__min_fitness  # registramos fitness mínimo de la generación actual
        generations[iters]['mean_fitness'] = self.__mean_fitness  # registramos fitness promedio de la generación actual
        if self.__term_cond['type'] == 'iterations':  # Si el criterio de parada es un número de iteraciones máximo
            # fijamos el contador de la generación en la cual se alcanza por primera vez la meta de fitness en el doble
            # de la cantidad de iteraciones a realizar para distinguir los casos en los que no se alcanza la meta
            goal_cross = 2 * self.__term_cond['iters']
            # actualizamos el valor del contador de la generación de cruce de meta en caso que corresponda
            if self.__max_fitness >= self.__term_cond['fitness_th'] and goal_cross == 2 * self.__term_cond['iters']:
                goal_cross = iters
            while iters < self.__term_cond['iters']:  # iteramos hasta llegar al número de iteraciones máximo
                new_pop = {}  # generamos diccionario vacío para guardar nueva población
                # copiamos los mejores individuos de la generacion anterior de acuerdo a lo establecido en nuestra tasa
                # de elitismo
                for i in range(0, self.__elitism):
                    new_pop[i] = self.__pop[i].copy()
                # Los cupos restantes los producimos mediante reproducción
                for i in range(self.__elitism, self.__pop_sz):
                    # si elegimos la selección roulette sorteamos 2 padres mediante este método
                    if selection_type == 'roulette':
                        parent_1 = self.roulette_sel()
                        parent_2 = self.roulette_sel()
                    # en caso contrario sorteamos 2 padres mediante el método de selección tournament
                    else:
                        parent_1 = self.tournament_sel(slots)
                        parent_2 = self.tournament_sel(slots)
                    # creamos un hijo mediante crossover de estos 2 padres
                    child = self.crossover(parent_1, parent_2)
                    # Si la tasa de mutación es mayor a 0 aplicamos la operacion de mutacion al hijo para obtener los
                    # valores finales de sus genes
                    if self.__mut_rate > 0.0:
                        child = self.mutation(child)
                    new_pop[i] = child.copy()  # añadimos al hijo a la nueva población
                self.__pop = new_pop.copy()  # actualizamos la poblacion
                self.comp_pop_fitness(fit_params)  # recalculamos el fitness de la poblacion
                iters += 1  # aumentamos en 1 el contador de generación
                generations[iters] = {}  # generamos un diccionario vacío para guardar la información de la generación
                # registramos fitness máximo de la generación actual
                generations[iters]['max_fitness'] = self.__max_fitness
                # registramos fitness mínimo de la generación actual
                generations[iters]['min_fitness'] = self.__min_fitness
                # registramos fitness promedio de la generación actual
                generations[iters]['mean_fitness'] = self.__mean_fitness
                # Si se encontró un individuo que supere el máximo fitness alcanzado en generaciones anteriores
                # se actualiza el registro del mejor individuo y del valor de fitness máximo
                if self.__max_fitness > overall_max_fitness:
                    overall_max_fitness = self.__max_fitness
                    overall_fittest_indv = self.__fittest_indv
                # actualizamos el valor del contador de la generación de cruce de meta en caso que corresponda
                if self.__max_fitness >= self.__term_cond['fitness_th'] and goal_cross == 2 * self.__term_cond['iters']:
                    goal_cross = iters
        else: # en caso contrario, es decir, el criterio de parada es un umbral para el fitness
            while overall_max_fitness < self.__term_cond['fitness_th']:  # iteramos hasta superar el umbral de fitness
                new_pop = {}  # generamos diccionario vacío para guardar nueva población
                # copiamos los mejores individuos de la generacion anterior de acuerdo a lo establecido en nuestra tasa
                # de elitismo
                for i in range(0, self.__elitism):
                    new_pop[i] = self.__pop[i].copy()
                # Los cupos restantes los producimos mediante reproducción
                for i in range(self.__elitism, self.__pop_sz):
                    # si elegimos la selección roulette sorteamos 2 padres mediante este método
                    if selection_type == 'roulette':
                        parent_1 = self.roulette_sel()
                        parent_2 = self.roulette_sel()
                    # en caso contrario sorteamos 2 padres mediante el método de selección tournament
                    else:
                        parent_1 = self.tournament_sel(slots)
                        parent_2 = self.tournament_sel(slots)
                    # creamos un hijo mediante crossover de estos 2 padres
                    child = self.crossover(parent_1, parent_2)
                    # Si la tasa de mutación es mayor a 0 aplicamos la operacion de mutacion al hijo para obtener los
                    # valores finales de sus genes
                    if self.__mut_rate > 0.0:
                        child = self.mutation(child)
                    new_pop[i] = child.copy()  # añadimos al hijo a la nueva población
                self.__pop = new_pop.copy()  # actualizamos la poblacion
                self.comp_pop_fitness(fit_params)  # recalculamos el fitness de la poblacion
                iters += 1  # aumentamos en 1 el contador de generación
                generations[iters] = {}  # generamos un diccionario vacío para guardar la información de la generación
                # registramos fitness máximo de la generación actual
                generations[iters]['max_fitness'] = self.__max_fitness
                # registramos fitness mínimo de la generación actual
                generations[iters]['min_fitness'] = self.__min_fitness
                # registramos fitness promedio de la generación actual
                generations[iters]['mean_fitness'] = self.__mean_fitness
                # Si se encontró un individuo que supere el máximo fitness alcanzado en generaciones anteriores
                # se actualiza el registro del mejor individuo y del valor de fitness máximo
                if self.__max_fitness > overall_max_fitness:
                    overall_max_fitness = self.__max_fitness
                    overall_fittest_indv = self.__fittest_indv
                # Ponemos una condición adicional para terminar en caso que no encuentre a algún individuo que supere
                # el umbral de fitness
                if self.__term_cond['iters'] < iters:
                    break
            # actualizamos el valor del contador de la generación de cruce de meta en caso que corresponda
            if overall_max_fitness >= self.__term_cond['fitness_th']:
                goal_cross = iters
            else:
                goal_cross = 2 * self.__term_cond['iters']
        # retornamos la información de las generaciones, el valor del contador de la generación de cruce de meta,
        # el valor de fitness máximo y el registro del mejor individuo.
        return generations, goal_cross, overall_max_fitness, overall_fittest_indv

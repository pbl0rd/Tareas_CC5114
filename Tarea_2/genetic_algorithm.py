import numpy as np

class GENALG(object):
    # Método inicializador para la clase algoritmo genético 

    def __init__(self, pop_sz_0: int, fit_fn, cr_genes, cr_indv, indv_chars, term_cond, mut_rate=0.0, elitism_rate=0.0):
        # Verificamos que los parámetros de entrada del constructor sean los correctos
        if type(pop_sz_0) != int:
            raise ValueError("Input n_weights debe ser un número entero positivo")        
        self.__pop_sz = pop_sz_0
        self.__pop = None
        self.__pop_fitness = None
        self.__max_fitness = None
        self.__mean_fitness = None
        self.__min_fitness = None
        self.__fittest_indv = None
        self.__fit_fn = fit_fn
        self.__cr_genes = cr_genes
        self.__cr_indv = cr_indv
        self.__indv_chars = indv_chars
        self.__num_genes = len(list(indv_chars.keys()))        
        self.__term_cond = term_cond
        self.__mut_rate = mut_rate
        self.__elitism = int(np.ceil(elitism_rate*pop_sz_0))

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
    
    # Función para obtener el número de genes de los individuos del algoritmo
    def get_num_genes(self):
        return self.__num_genes    
           
            
    # Función para generar la población inicial
    def gen_pop(self):
        pop = {}
        for i in range(self.__pop_sz):
            pop[i] = self.__cr_indv(self.__cr_genes, self.__indv_chars)
        self.__pop = pop

    def comp_pop_fitness(self, fit_params):   
        pop_fitness = {} 
        new_pop = {}
        l_pfitness = []
        ranking = {}
        fittest_indv = None
        for i in range(self.__pop_sz):
            fitness = self.__fit_fn(self.__pop[i], fit_params)           
            l_pfitness.append(fitness)        
        mean_fitness = np.mean(l_pfitness)
        max_fitness = max(l_pfitness)
        min_fitness = min(l_pfitness)
        fittest_indv = self.__pop[l_pfitness.index(max_fitness)].copy()
        self.__max_fitness = max_fitness
        self.__min_fitness = min_fitness
        self.__mean_fitness = mean_fitness
        self.__fittest_indv = fittest_indv
        l_aux = l_pfitness[:]
        for i in range(self.__pop_sz):
            max_ind = l_aux.index(max(l_aux))
            new_pop[i] = self.__pop[max_ind].copy()
            pop_fitness[i]= l_aux[max_ind]
            l_aux[max_ind] =-np.inf
        self.__pop = new_pop.copy()
        self.__pop_fitness = pop_fitness.copy()
    
    # Método para aplicar la selección mediante torneo de los individuos de la población. Recibe de entrada el número 
    # de competidores (entero positivo). Asume que la poblacíon está reordenada en base al fitness de manera decreciente 
    # (paso que ocurre al calcular el fitness de la población con el método comp_pop_fitness)
    def tournament_sel(self, slots: int):
        if slots > self.__pop_sz:
            raise ValueError("slots debe ser un número entero positivo menor que el tamaño de la población")
        else:
            chosen_set = np.random.randint(0, self.__pop_sz, slots)            
            winner = min(chosen_set)
            return self.__pop[winner]
    
    # Método para aplicar la selección mediante ruleta de los individuos de la población.
    def roulette_sel(self):
        fit_vals = list(self.__pop_fitness.values())
        num_neg_vals = sum(n < 0 for n in fit_vals)
        # si hay fitness negativos debemos normalizar estos valores conservando las distancias
        if num_neg_vals>0:
            min_val = abs(min(fit_vals))
            new_fit_vals = [min_val +item for item in fit_vals]
        else:
            new_fit_vals = fit_vals[:]               
        total_fit = sum(new_fit_vals)
        # si todas las fitness son iguales a 0 retornamos un individuo al azar
        if total_fit == 0:
            idx = np.random.randint(0,self.__pop_sz)
            return self.__pop[idx]
        else:
            sum_fit = 0
            th = total_fit*np.random.rand()
            for i in range(self.__pop_sz):
                sum_fit += new_fit_vals[i]
                if sum_fit>th:
                    return self.__pop[i]    
            
            
    
    def crossover(self, indv1, indv2):
        vals1 = list(indv1.values())
        vals2 = list(indv2.values())        
        cut = np.random.randint(1, self.__num_genes)
        new_vals = vals1[:cut] + vals2[cut:]
        keys = list(indv1.keys())
        new_ind = dict(zip(keys, new_vals))
        return new_ind
    
    def mutation(self, indv):
        vals = list(indv.values())        
        new_vals = []
        for i in range(self.__num_genes):            
            if np.random.rand() > self.__mut_rate:
                new_vals.append(vals[i])
            else:
                cond = True
                while cond:
                    new_val = self.__cr_genes(self.__indv_chars[i]['gene_type'],self.__indv_chars[i]['fact_range'])
                    if new_val != vals[i]:
                        cond = False
                new_vals.append(new_val)
        keys = list(indv.keys())
        new_ind = dict(zip(keys, new_vals))
        return new_ind

    def apply(self,fit_params, selection_type='tournament', random_state=None, slots=3):
        if type(random_state) == int:
            np.random.seed(random_state)
        self.gen_pop()
        self.comp_pop_fitness(fit_params)
        generations = {}        
        iters = 0
        overall_max_fitness = self.__max_fitness
        overall_fittest_indv = self.__fittest_indv
        generations[iters] = {}
        generations[iters]['max_fitness'] = self.__max_fitness
        generations[iters]['min_fitness'] = self.__min_fitness
        generations[iters]['mean_fitness'] = self.__mean_fitness
        if self.__term_cond['type']== 'iterations':
            goal_cross = 2*self.__term_cond['iters']            
            if self.__max_fitness >= self.__term_cond['fitness_th'] and goal_cross == 2*self.__term_cond['iters']:
                goal_cross = iters
            while iters < self.__term_cond['iters']:
                new_pop = {}
                for i in range(0, self.__elitism):
                    new_pop[i] = self.__pop[i].copy()            
                for i in range(self.__elitism, self.__pop_sz):
                    if selection_type == 'roulette':
                        parent_1 = self.roulette_sel()
                        parent_2 = self.roulette_sel()
                    else:
                        parent_1 = self.tournament_sel(slots)
                        parent_2 = self.tournament_sel(slots)
                    child = self.crossover(parent_1, parent_2)
                    if self.__mut_rate > 0.0:
                        child = self.mutation(child)
                    new_pop[i] = child
                self.__pop = new_pop.copy()
                self.comp_pop_fitness(fit_params)
                iters += 1
                generations[iters] = {}
                generations[iters]['max_fitness'] = self.__max_fitness
                generations[iters]['min_fitness'] = self.__min_fitness
                generations[iters]['mean_fitness'] = self.__mean_fitness
                if self.__max_fitness > overall_max_fitness:
                    overall_max_fitness = self.__max_fitness
                    overall_fittest_indv = self.__fittest_indv                
                if self.__max_fitness >= self.__term_cond['fitness_th'] and goal_cross == 2*self.__term_cond['iters']:
                    goal_cross = iters
        else:
            while overall_max_fitness < self.__term_cond['fitness_th']:
                new_pop = {}
                for i in range(0, self.__elitism):
                    new_pop[i] = self.__pop[i].copy()            
                for i in range(self.__elitism, self.__pop_sz):
                    if selection_type == 'roulette':
                        parent_1 = self.roulette_sel()
                        parent_2 = self.roulette_sel()
                    else:
                        parent_1 = self.tournament_sel(slots)
                        parent_2 = self.tournament_sel(slots)
                    child = self.crossover(parent_1, parent_2)
                    if self.__mut_rate > 0.0:
                        child = self.mutation(child)
                    new_pop[i] = child
                self.__pop = new_pop.copy()
                self.comp_pop_fitness(fit_params)
                iters += 1
                generations[iters] = {}
                generations[iters]['max_fitness'] = self.__max_fitness
                generations[iters]['min_fitness'] = self.__min_fitness
                generations[iters]['mean_fitness'] = self.__mean_fitness
                if self.__max_fitness > overall_max_fitness:
                    overall_max_fitness = self.__max_fitness
                    overall_fittest_indv = self.__fittest_indv
                if self.__term_cond['iters']< iters:
                    break
            if overall_max_fitness >= self.__term_cond['fitness_th']:
                goal_cross = iters
            else:
                goal_cross = 2*self.__term_cond['iters']            
        return generations, goal_cross, overall_max_fitness, overall_fittest_indv
    
    
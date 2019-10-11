import numpy as np


class GENALG(object):
    # Método inicializador para la clase algoritmo genético 

    def __init__(self, pop_sz_0: int, fit_fn, cr_genes, cr_indv, mut_rate, term_cond, indv_chars):
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
        self.__mut_rate = mut_rate
        self.__term_cond = term_cond

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
           
            
    # Función para generar la población inicial
    def gen_pop(self):
        pop = {}
        for i in range(self.__pop_sz):
            pop[i] = self.__cr_indv(self.__cr_genes, indv_chars)
        self.__pop = pop

    def comp_pop_fitness(self, fit_params):   
        pop_fitness = {}
        max_fitness = -np.inf
        min_fitness = np.inf
        fittest_indv = None
        for i in range(self.__pop_sz):
            fitness = self.__fit_fn(self.__pop[i], fit_params)
            if fitness > max_fitness:
                max_fitness = fitness
                fittest_indv = self.__pop[i]
            if fitness < min_fitness:
                min_fitness = fitness
            pop_fitness[i] = fitness
        mean_fitness = np.mean(list(pop_fitness.values()))
        self.__pop_fitness = pop_fitness
        self.__max_fitness = max_fitness
        self.__min_fitness = min_fitness
        self.__mean_fitness = mean_fitness
        self.__fittest_indv = fittest_indv
    
    def tournament_sel(self, slots):
        if slots > self.__pop_sz:
            raise ValueError("slots debe ser un número entero positivo menor que el tamaño de la población")
        else:
            chosen_set = np.random.randint(0, self.__pop_sz, slots)
            chosen_set_fitness = [self.__pop_fitness[i] for i in chosen_set]
            max_set_fitness = max(chosen_set_fitness)        
            aux_dict = dict(zip(chosen_set_fitness, chosen_set))
            winner = aux_dict[max_set_fitness]
            return self.__pop[winner]
    
    def crossover(self, indv1, indv2):
        vals1 = list(indv1.values())
        vals2 = list(indv2.values())
        num_genes = len(vals1)
        cut = np.random.randint(1,num_genes)
        new_vals = vals1[:cut] + vals2[cut:]
        keys = list(indv1.keys())
        new_ind = dict(zip(keys, new_vals))
        return new_ind
    
    def mutation(self, indv):
        vals = list(indv.values())
        num_genes = len(vals)
        new_vals = []
        for i in range(num_genes):            
            if np.random.rand() > self.__mut_rate:
                new_vals.append(vals[i])
            else:
                new_val = self.__cr_genes(self.__indv_chars[i]['gene_type'],self.__indv_chars[i]['fact_range'])
                new_vals.append(new_val)
        keys = list(indv.keys())
        new_ind = dict(zip(keys, new_vals))
        return new_ind
    
    def apply(self,fit_params, slots, random_state=42):
        np.random.seed(random_state)
        self.gen_pop()
        self.comp_pop_fitness(fit_params)
        generations = {}        
        iters = 0
        goal_cross = -1
        overall_max_fitness = self.__max_fitness
        overall_fittest_indv = self.__fittest_indv
        generations[iters] = {}
        generations[iters]['max_fitness'] = self.__max_fitness
        generations[iters]['min_fitness'] = self.__min_fitness
        generations[iters]['mean_fitness'] = self.__mean_fitness
        if self.__max_fitness >= self.__term_cond['max_fitness'] and goal_cross == -1:
            goal_cross = iters
        while iters < self.__term_cond['iters']:
            new_pop = {}
            for i in range(self.__pop_sz):
                parent_1 = self.tournament_sel(slots)
                parent_2 = self.tournament_sel(slots)
                child = self.crossover(parent_1, parent_2)
                mut_child = self.mutation(child)
                new_pop[i] = mut_child
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
            if self.__max_fitness >= self.__term_cond['max_fitness'] and goal_cross == -1:
                goal_cross = iters
        return generations, goal_cross, overall_max_fitness, overall_fittest_indv
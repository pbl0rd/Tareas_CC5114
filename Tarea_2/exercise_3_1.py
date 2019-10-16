import numpy as np
from genetic_algorithm import GENALG


def gene_factory_ex3(gene_type, fact_range):
    if fact_range != [0,15] or gene_type != int:
        raise ValueError("Parámetros incorrectos")
    else:
        gene = np.random.randint(fact_range[0], fact_range[1]+1)
        return gene
		
def indv_factory(gene_factory, indv_chars):    
    vals = list(indv_chars.values())
    num_genes = len(vals)
    new_indv = {}
    for i in range(num_genes):
        new_indv[i] = gene_factory(indv_chars[i]['gene_type'],indv_chars[i]['fact_range'])
    return new_indv    
	
def fitness_ex3(indv, objective):    
    vals = list(indv.values())
    pesos = objective['pesos']
    valores = objective['valores']
    fitness = np.dot(vals,valores)
    penalizacion = 0 
    peso_total = np.dot(vals,pesos)
    if peso_total > objective['capacidad']:
        penalizacion = objective['castigo']*(peso_total - objective['capacidad']) 
    fitness -= penalizacion
    return objective['ponderador']*fitness
	
	
if __name__ == '__main__':
	# Prueba ejercicio 3 con ejemplo mencionado en readme
	random_state = 42
	pesos = [12,2,1,1,4]
	valores = [4,2,2,1,10]
	capacidad = 15
	castigo = 5
	slots=5
	ponderador = 1/100
	selection_type='tournament'
	fit_params ={'pesos':pesos, 'valores':valores, 'capacidad':capacidad, 'castigo':castigo, 'ponderador':ponderador}
	pop_sz_0 = 40
	fit_fn = fitness_ex3 
	cr_genes = gene_factory_ex3
	cr_indv = indv_factory
	mut_rate = 0.2
	elitism_rate = 0.2
	term_cond = {'type':'iterations','fitness_th':0.36, 'iters':100} 
	indv_chars = {}
	for i in range(len(pesos)):
		aux_dict = {}
		aux_dict['gene_type'] = int
		aux_dict['fact_range'] = [0,15]
		indv_chars[i] = aux_dict.copy()
	GA = GENALG(pop_sz_0, fit_fn, cr_genes, cr_indv, indv_chars, term_cond, mut_rate, elitism_rate)
	generations, goal_cross, overall_max_fitness, overall_fittest_indv = GA.apply(fit_params, selection_type, random_state, slots)
	print(overall_max_fitness)
	print(overall_fittest_indv)
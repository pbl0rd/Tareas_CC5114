import numpy as np
from genetic_algorithm import GENALG


def gene_factory_ex1(gene_type, fact_range):
    if fact_range != [0,1] or gene_type != 'binary':
        raise ValueError("Parámetros incorrectos")
    else:
        gene = np.random.choice(fact_range)
        return gene

def indv_factory(gene_factory, indv_chars):    
    vals = list(indv_chars.values())
    num_genes = len(vals)
    new_indv = {}
    for i in range(num_genes):
        new_indv[i] = gene_factory(indv_chars[i]['gene_type'],indv_chars[i]['fact_range'])
    return new_indv

def fitness_ex1(indv, objective):
    vals = list(indv.values())
    vals_str = ''.join(str(i) for i in vals)
    fitness = abs(int(objective, 2)-int(vals_str, 2))
    return -fitness
	
if __name__ == '__main__':
	# Prueba ejercicio 1
	secuencia_bits = '00101010110101'
	pop_sz_0 = 40
	fit_fn = fitness_ex1 
	cr_genes = gene_factory_ex1
	cr_indv = indv_factory
	mut_rate = 0.1
	term_cond = {'max_fitness':0, 'iters':50} 
	indv_chars = {}
	for i in range(len(secuencia_bits)):
		aux_dict = {}
		aux_dict['gene_type'] = 'binary'
		aux_dict['fact_range'] = [0,1]
		indv_chars[i] = aux_dict.copy()
	GA = GENALG(pop_sz_0, fit_fn, cr_genes, cr_indv, mut_rate, term_cond, indv_chars)
	slots = 5
	generations, goal_cross, overall_max_fitness, overall_fittest_indv = GA.apply(secuencia_bits,slots)
	print(overall_max_fitness)
	print(overall_fittest_indv)
import numpy as np
from genetic_algorithm import GENALG


def gene_factory_ex2(gene_type, fact_range):
    if fact_range != list('abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ ') or gene_type != str:
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

def fitness_ex2(indv, objective):
    vals = list(indv.values())
    obj = list(objective)
    hits =0
    for i in range(len(vals)):
        if vals[i] == obj[i]:
            hits += 1   
    return hits
	
if __name__ == '__main__':
	# Prueba ejercicio 2
	frase = 'helloworld'
	pop_sz_0 = 40
	fit_fn = fitness_ex2 
	cr_genes = gene_factory_ex2
	cr_indv = indv_factory
	mut_rate = 0.2
	term_cond = {'max_fitness':10, 'iters':70} 
	indv_chars = {}
	char_list = list('abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ ')
	for i in range(len(frase)):
		aux_dict = {}
		aux_dict['gene_type'] = str
		aux_dict['fact_range'] = char_list
		indv_chars[i] = aux_dict.copy()
	GA = GENALG(pop_sz_0, fit_fn, cr_genes, cr_indv, mut_rate, term_cond, indv_chars)
	slots = 5
	generations, goal_cross, overall_max_fitness, overall_fittest_indv = GA.apply(frase,slots)
	print(overall_max_fitness)
	print(overall_fittest_indv)
# coding=utf-8
import numpy as np
from genetic_algorithm_mod import GENALG
import matplotlib.pyplot as plt
from ast import *
from arboles import *
import seaborn as sns


# Función para crear los genes de los individuos del ejercicio 2. Recibe 2 inputs:
# - gene_type: Corresponde al tipo de gen (En este caso es un bit por lo tanto es 'binary' )
# - fact_range: conjunto de valores posibles para un gen (En este caso los valores posibles son 0 o 1)
# Retorna un gen del tipo especificado y dentro del rango especificado.
def gene_factory(AST, indv_chars):
    allowed_functions = indv_chars['allowed_functions']
    allowed_terminals = indv_chars['allowed_terminals']
    prob_terminal = indv_chars['prob_terminal']
    factory = AST(allowed_functions, allowed_terminals, prob_terminal)
    return factory

# Función para crear los individuos. Recibe 2 inputs:
# - Función creadora de genes: descrita arriba.
# - Diccionario caracterizando al individuo: diccionario que para cada gen del individuo contiene la información del
#   tipo de gen y del conjunto de valores posibles para ese gen
# Retorna un individuo adecuado para el problema.
def indv_factory(gene_factory_ex1, indv_chars):
    factory = gene_factory_ex1(AST, indv_chars)
    max_depth = indv_chars['max_depth']
    new_indv = factory(max_depth)
    return new_indv.copy()  # retornamos el individuo creado


# Función de fitness para el ejercicio 1. Recibe a un individuo y un diccionario con la secuencia y un ponderador.
# Retorna la multiplicación del ponderador y el valor absoluto de la diferencia entre el número entero que representa
# la secuencia entregada y el número entero que representa la secuencia del individuo.
def fitness_ex3(indv, objective):
    val = indv.eval()
    t_list=[item.eval() for item in indv.serialize() if type(item)==TerminalNode]
    rep_ls=[]
    for item in t_list:
        if t_list.count(item)>1 and item not in rep_ls:
            rep_ls.append(item)
    pen_ls=[t_list.count(item)-1 for item in rep_ls]
    fitness = objective['ponderador'][0] * abs(objective['secuencia'] - val)+objective['ponderador'][1] * sum(pen_ls)
    return -fitness


if __name__ == '__main__':
    # Ejercicio 2.1.3
    # Seteamos los parametros a ser ocupados por el algoritmo para obtener los gráficos pedidos
    secuencia_bits = 65346
    ponderador = [1 / 100, 700]
    fit_params = {'secuencia': secuencia_bits, 'ponderador': ponderador}
    pop_sz_0 = 50
    fit_fn = fitness_ex3
    cr_genes = gene_factory_ex1
    cr_indv = indv_factory
    mut_rate = 0.2
    term_cond = {'type': 'iterations', 'fitness_th': 0, 'iters': 1000}
    selection_type = 'tournament'
    slots = 5
    elitism_rate = 0.1
    random_state = 42
    indv_chars = {'allowed_functions': [AddNode, SubNode, MultNode], 'allowed_terminals': [25, 7, 8, 100, 4, 2],
                  'prob_terminal': 0.3, 'max_depth': 10}
    GA = GENALG(pop_sz_0, fit_fn, cr_genes, cr_indv, indv_chars, term_cond, mut_rate, elitism_rate)
    generations, goal_cross, overall_max_fitness, overall_fittest_indv = GA.apply(fit_params, selection_type,
                                                                                  random_state, slots)
    print(overall_max_fitness)
    print(overall_fittest_indv)
    # Obtener visualización de Evolución de fitness por generación sin elitismo
    x = list(generations.keys())
    vals = list(generations.values())
    max_fit = [item['max_fitness'] for item in vals]
    mean_fit = [item['mean_fitness'] for item in vals]
    min_fit = [item['min_fitness'] for item in vals]
    fig, ax1 = plt.subplots(figsize=(15, 15))
    ax1.set_xlabel("Generación", fontsize=15)
    ax1.set_ylabel('Fitness (max )')
    ax1.plot(x, max_fit, color='green', linewidth=2, label='max_fit')
    ax1.legend(loc=2, fontsize=15)
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.set_ylabel('Fitness (mean y min)')  # we already handled the x-label with ax1
    ax2.plot(x, mean_fit, color='blue', linewidth=2, label='mean_fit')
    ax2.plot(x, min_fit, color='red', linewidth=2, label='min_fit')
    ax2.legend(fontsize=15)
    plt.title("Evolución de fitness por generación", fontsize=16, fontweight='bold')
    plt.suptitle("Ejercicio 2.1.3", fontsize=20)
    plt.savefig('Images\Fitness_por_Generacion_EX3.png')
    plt.close()
    print('gráfico 3 listo')
# coding=utf-8
import numpy as np
from genetic_algorithm_mod import GENALG
import matplotlib.pyplot as plt
from ast import *
from arboles import *



# Función para crear los genes (nddos) de los individuos. Recibe 2 inputs:
# - ast_: Corresponde a la clase de generadores de árboles aleatorios
# - indv_chars_: Diccionario caracterizando al individuo del problema (funciones, terminales,
#                                                                probabilidad de nodo terminal, máxima profundidad)
# Retorna un generador de árboles aleatorio con las características especificadas.
def gene_factory(ast_, indv_chars_):
    allowed_functions = indv_chars_['allowed_functions']
    allowed_terminals = indv_chars_['allowed_terminals']
    prob_terminal = indv_chars_['prob_terminal']
    factory = ast_(allowed_functions, allowed_terminals, prob_terminal)
    return factory


# Función para crear los individuos. Recibe 2 inputs:
# - gene_factory_: Función creadora de genes, descrita arriba.
# - indv_chars_: Diccionario caracterizando al individuo del problema (funciones, terminales,
# #                                                                probabilidad de nodo terminal, máxima profundidad)
# Retorna un individuo adecuado para el problema.
def indv_factory(gene_factory_, indv_chars_):
    factory = gene_factory_(AST, indv_chars_)
    max_depth = indv_chars_['max_depth']
    new_indv = factory(max_depth)
    return new_indv.copy()  # retornamos el individuo creado


# Función de fitness para el ejercicio 3. Recibe a un individuo y un diccionario con el número y un ponderador.
# Retorna el opuesto de la suma ponderada entre el valor absoluto de la diferencia entre el número a encontrar y el
# número correspondiente a la evaluación del individuo (árbol), y la suma de veces que el árbol viola la
# restricción de unicidad de los terminales.
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
    cr_genes = gene_factory
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
    # Obtener visualización de Evolución de fitness por generación con elitismo v2
    fig, ax1 = plt.subplots(figsize=(15, 15))
    ax1.set_xlabel("Generación", fontsize=15)
    ax1.set_ylabel('Fitness (max)')
    ax1.plot(x, max_fit, color='green', linewidth=2, label='max_fit')
    ax1.legend(loc=2, fontsize=15)
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.set_ylabel('Fitness (mean)')  # we already handled the x-label with ax1
    ax2.plot(x, mean_fit, color='blue', linewidth=2, label='mean_fit')
    ax2.legend(fontsize=15)
    plt.title("Evolución de fitness por generación", fontsize=16, fontweight='bold')
    plt.suptitle("Ejercicio 2.1.3", fontsize=20)
    plt.savefig('Images\Fitness_por_Generacion_EX3_V2.png')
    plt.close()
    print('gráfico 3 V2 listo')
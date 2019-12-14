# coding=utf-8
import numpy as np
from genetic_algorithm_mod import GENALG
import matplotlib.pyplot as plt
from ast import AST
from arboles import *
import seaborn as sns


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


# Función de fitness para el ejercicio 1. Recibe a un individuo y un diccionario con el número a encontrar y
# un ponderador.
# Retorna el opuesto de la multiplicación del ponderador y el valor absoluto de la diferencia entre el número a
# encontrar y el número correspondiente a la evaluación del individuo (árbol).
def fitness_ex1(indv, objective):
    val = indv.eval()
    fitness = objective['ponderador'] * abs(objective['secuencia'] - val)
    return -fitness

if __name__ == '__main__':
    # Obtener visualización de heatmap de configuraciones ejercicio 1
    secuencia_bits = 65346
    ponderador = 1 / 10000
    fit_params = {'secuencia': secuencia_bits, 'ponderador': ponderador}
    fit_fn = fitness_ex1
    cr_genes = gene_factory
    cr_indv = indv_factory
    selection_type = 'tournament'
    slots = 5
    elitism_rate = 0.1
    random_state = 42
    indv_chars = {'allowed_functions': [AddNode, SubNode, MultNode, MaxNode],
                  'allowed_terminals': [25, 7, 8, 100, 4, 2], 'prob_terminal': 0.3, 'max_depth': 10}
    pop_sizes = [50 * i for i in range(1, 21)]
    mut_rates = [i / 10 for i in range(11)]
    term_cond = {'type': 'fitness_th', 'fitness_th': 0, 'iters': 100}
    res = []
    for rt in mut_rates:
        mut_rate = rt
        res_rt = []
        for item in pop_sizes:
            pop_sz_0 = item
            GA = GENALG(pop_sz_0, fit_fn, cr_genes, cr_indv, indv_chars, term_cond, mut_rate, elitism_rate)
            generations, goal_cross, overall_max_fitness, overall_fittest_indv = GA.apply(fit_params, selection_type,
                                                                                          random_state, slots)
            res_rt.append(goal_cross)
        res.append(res_rt[:])
    data = np.array(res)
    sns.set()
    fig = plt.figure(figsize=(15, 10))
    cmap = sns.cm.rocket_r
    ax = sns.heatmap(data, annot=True, fmt="d", linewidths=.5, xticklabels=pop_sizes, yticklabels=mut_rates, cmap=cmap)
    plt.title("Heatmap de configuraciones", fontsize=16, fontweight='bold')
    plt.suptitle("Ejercicio 2.1.1", fontsize=20)
    plt.xlabel("Generación", fontsize=15)
    plt.xlabel("Tamaño de Población", fontsize=15)
    plt.ylabel("Tasa de Mutación", fontsize=15)
    plt.savefig('Images\Heatmap_EX1.png')
    plt.close()
    print('Gráfico 6 listo')
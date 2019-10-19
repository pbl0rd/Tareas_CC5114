import numpy as np
from genetic_algorithm import GENALG
import matplotlib.pyplot as plt
import seaborn as sns


# Función para crear los genes de los individuos del ejercicio 2. Recibe 2 inputs:
# - gene_type: Corresponde al tipo de gen (En este caso es un string str)
# - fact_range: conjunto de valores posibles para un gen
# Retorna un gen del tipo especificado y dentro del rango especificado.
def gene_factory_ex2(gene_type, fact_range):

    # Para este problema todos los genes deben ser del tipo str y corresponder a una letra minúscula,
    # mayúscula o a un espacio
    if fact_range != list('abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ ') or gene_type != str:
        raise ValueError("Parámetros incorrectos")
    else:
        # elegimos un caracter al azar dentro del conjunto de posibilidades fact_range
        gene = np.random.choice(fact_range)
        return gene  # retornamos el gen creado


# Función para crear los individuos. Recibe 2 inputs:
# - Función creadora de genes: descrita arriba.
# - Diccionario caracterizando al individuo: diccionario que para cada gen del individuo contiene la información del
#   tipo de gen y del conjunto de valores posibles para ese gen
# Retorna un individuo adecuado para el problema.
def indv_factory(gene_factory, indv_chars):    
    vals = list(indv_chars.values())  # Generamos lista con las caracteristicas de cada gen del individuo a crear
    num_genes = len(vals)  # Obtenemos numero de genes que tendrá el individuo
    new_indv = {}   # Creamos diccionario vacío para guardar la información de los genes del individuo
    for i in range(num_genes):
        # Creamos el gen de la posición i con las características adecuadas para esa posición.
        new_indv[i] = gene_factory(indv_chars[i]['gene_type'],indv_chars[i]['fact_range'])
    return new_indv  # retornamos el individuo creado


# Función de fitness para el ejercicio 2. Recibe a un individuo y la frase buscada. Retorna el número de coincidencias
# (mismo caracter y misma ubicación) entre el individuo y la frase.
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
    # Seteamos los parametros a ser ocupados por el algoritmo para obtener los gráficos pedidos
    random_state = 42  # Fijamos una semilla para hacer el experimento reproducible
    frase = 'helloworld'
    pop_sz_0 = 50
    fit_fn = fitness_ex2
    cr_genes = gene_factory_ex2
    cr_indv = indv_factory
    mut_rate = 0.2
    term_cond = {'type':'iterations','fitness_th':10, 'iters':100}
    indv_chars = {}
    selection_type='tournament'
    slots = 5
    elitism_rate = 0.0
    char_list = list('abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ ')
    for i in range(len(frase)):
        aux_dict = {}
        aux_dict['gene_type'] = str
        aux_dict['fact_range'] = char_list
        indv_chars[i] = aux_dict.copy()
    GA = GENALG(pop_sz_0, fit_fn, cr_genes, cr_indv, indv_chars,term_cond, mut_rate, elitism_rate)
    generations, goal_cross, overall_max_fitness, overall_fittest_indv = GA.apply(frase,selection_type, random_state, slots)
    print(overall_max_fitness)
    print(overall_fittest_indv)
    # Obtener visualización de Evolución de fitness por generación sin elitismo
    x = list(generations.keys())
    vals = list(generations.values())
    max_fit = [item['max_fitness'] for item in vals]
    mean_fit = [item['mean_fitness'] for item in vals]
    min_fit = [item['min_fitness'] for item in vals]
    fig= plt.figure(figsize=(15,15))
    plt.plot( x,  max_fit, marker='o', markerfacecolor='green', markersize=5, color='olive', linewidth=2,label='max_fit')
    plt.plot( x,  mean_fit, marker='', color='blue', linewidth=2,label='mean_fit')
    plt.plot( x,  min_fit, marker='', color='red', linewidth=2, label='min_fit')
    plt.title("Evolución de fitness por generación", fontsize=16, fontweight='bold')
    plt.suptitle("Encontrar una frase", fontsize=20)
    plt.xlabel("Generación", fontsize=15)
    plt.ylabel("Fitness", fontsize=15)
    plt.legend(fontsize=15)
    plt.savefig('Images\Fitness_por_Generacion_EX2.png')
    plt.close()
    print('Gráfico 1 listo')
    # Obtener visualización de Evolución de fitness por generación con elitismo
    elitism_rate = 0.2  # Fijamos una tasa de elitismo del 20%
    GA = GENALG(pop_sz_0, fit_fn, cr_genes, cr_indv, indv_chars,term_cond, mut_rate, elitism_rate)
    generations, goal_cross, overall_max_fitness, overall_fittest_indv = GA.apply(frase,selection_type, random_state, slots)
    x = list(generations.keys())
    vals = list(generations.values())
    max_fit = [item['max_fitness'] for item in vals]
    mean_fit = [item['mean_fitness'] for item in vals]
    min_fit = [item['min_fitness'] for item in vals]
    fig= plt.figure(figsize=(15,15))
    plt.plot( x,  max_fit, marker='o', markerfacecolor='green', markersize=5, color='olive', linewidth=2,label='max_fit')
    plt.plot( x,  mean_fit, marker='', color='blue', linewidth=2,label='mean_fit')
    plt.plot( x,  min_fit, marker='', color='red', linewidth=2, label='min_fit')
    plt.title("Evolución de fitness por generación", fontsize=16, fontweight='bold')
    plt.suptitle("Encontrar una frase", fontsize=20)
    plt.xlabel("Generación", fontsize=15)
    plt.ylabel("Fitness", fontsize=15)
    plt.legend(fontsize=15)
    plt.savefig('Images\Fitness_por_Generacion_EX2_Elitismo.png')
    plt.close()
    print('Gráfico 2 listo')
    # Obtener visualización de heatmap de configuraciones con elitismo
    term_cond = {'type':'fitness_th','fitness_th':10, 'iters':3000}  # Cambiamos la condición de parada
    pop_sizes = [50*i for i in range(1,21)]
    mut_rates = [i/10 for i in range(11)]
    res=[]
    for rt in mut_rates:
        mut_rate = rt
        res_rt = []
        for item in pop_sizes:
            pop_sz_0 = item
            GA = GENALG(pop_sz_0, fit_fn, cr_genes, cr_indv, indv_chars,term_cond, mut_rate, elitism_rate)
            generations, goal_cross, overall_max_fitness, overall_fittest_indv = GA.apply(frase,selection_type, random_state, slots)
            res_rt.append(goal_cross)
        res.append(res_rt[:])
    data = np.array(res)
    sns.set()
    fig = plt.figure(figsize=(15,10))
    cmap = sns.cm.rocket_r
    ax = sns.heatmap(data, annot=True, fmt="d",linewidths=.5, xticklabels =pop_sizes, yticklabels=mut_rates, cmap=cmap)
    plt.title("Heatmap de configuraciones", fontsize=16, fontweight='bold')
    plt.suptitle("Encontrar una frase", fontsize=20)
    plt.xlabel("Generación", fontsize=15)
    plt.xlabel("Tamaño de Población", fontsize=15)
    plt.ylabel("Tasa de Mutación", fontsize=15)
    plt.savefig('Images\Heatmap_EX2_Elitismo.png')
    plt.close()
    print('Gráfico 3 listo')
    # Obtener visualización de heatmap de configuraciones sin elitismo
    elitism_rate = 0.0
    res = []
    for rt in mut_rates:
        mut_rate = rt
        res_rt = []
        for item in pop_sizes:
            pop_sz_0 = item
            GA = GENALG(pop_sz_0, fit_fn, cr_genes, cr_indv, indv_chars, term_cond, mut_rate, elitism_rate)
            generations, goal_cross, overall_max_fitness, overall_fittest_indv = GA.apply(frase, selection_type,
                                                                                          random_state, slots)
            res_rt.append(goal_cross)
        res.append(res_rt[:])
    data = np.array(res)
    sns.set()
    fig = plt.figure(figsize=(15, 10))
    cmap = sns.cm.rocket_r
    ax = sns.heatmap(data, annot=True, fmt="d", linewidths=.5, xticklabels=pop_sizes, yticklabels=mut_rates, cmap=cmap)
    plt.title("Heatmap de configuraciones", fontsize=16, fontweight='bold')
    plt.suptitle("Encontrar una frase", fontsize=20)
    plt.xlabel("Generación", fontsize=15)
    plt.xlabel("Tamaño de Población", fontsize=15)
    plt.ylabel("Tasa de Mutación", fontsize=15)
    plt.savefig('Images\Heatmap_EX2.png')
    plt.close()
    print('Gráfico 4 listo')
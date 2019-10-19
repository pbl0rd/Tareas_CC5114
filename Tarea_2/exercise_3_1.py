import numpy as np
from genetic_algorithm import GENALG
import matplotlib.pyplot as plt
import seaborn as sns

# Función para crear los genes de los individuos del ejercicio 3. Recibe 2 inputs:
# - gene_type: Corresponde al tipo de gen (En este caso es un entero int)
# - fact_range: conjunto de valores posibles para un gen ( en este caso
# Retorna un gen del tipo especificado y dentro del rango especificado.
def gene_factory_ex3(gene_type, fact_range):
    # Para este problema todos los genes deben ser del tipo int y estar entre 0 y 15
    if fact_range != [0, 15] or gene_type != int:
        raise ValueError("Parámetros incorrectos")
    else:
        # elegimos un entero al azar entre 0 y 15
        gene = np.random.randint(fact_range[0], fact_range[1] + 1)
        return gene


# Función para crear los individuos. Recibe 2 inputs:
# - Función creadora de genes: descrita arriba.
# - Diccionario caracterizando al individuo: diccionario que para cada gen del individuo contiene la información del
#   tipo de gen y del conjunto de valores posibles para ese gen
# Retorna un individuo adecuado para el problema.
def indv_factory(gene_factory, indv_chars):
    vals = list(indv_chars.values())  # Generamos lista con las caracteristicas de cada gen del individuo a crear
    num_genes = len(vals)  # Obtenemos numero de genes que tendrá el individuo
    new_indv = {}  # Creamos diccionario vacío para guardar la información de los genes del individuo
    for i in range(num_genes):
        # Creamos el gen de la posición i con las características adecuadas para esa posición.
        new_indv[i] = gene_factory(indv_chars[i]['gene_type'], indv_chars[i]['fact_range'])
    return new_indv  # retornamos el individuo creado    


# Función de fitness para el ejercicio 3. Recibe a un individuo y un diccionario con los pesos delas cajas, con los
# valores de las cajas, la capacidad de la mochila, un factor de castigo por exceder el peso en un kg y un ponderador.
# Retorna la suma de los valores de las cajas escogidas menos el catigo por el exceso de peso
# todo esto multiplicado por el ponderador
def fitness_ex3(indv, objective):
    vals = list(indv.values())
    pesos = objective['pesos']
    valores = objective['valores']
    fitness = np.dot(vals, valores)
    penalizacion = 0
    peso_total = np.dot(vals, pesos)
    if peso_total > objective['capacidad']:
        penalizacion = objective['castigo'] * (peso_total - objective['capacidad'])
    fitness -= penalizacion
    return objective['ponderador'] * fitness


if __name__ == '__main__':
    # Prueba ejercicio 3 con ejemplo mencionado en readme
    random_state = 42
    pesos = [12, 2, 1, 1, 4]
    valores = [4, 2, 2, 1, 10]
    capacidad = 15
    castigo = 5
    slots = 5
    ponderador = 1 / 100
    selection_type = 'tournament'
    fit_params = {'pesos': pesos, 'valores': valores, 'capacidad': capacidad, 'castigo': castigo,
                  'ponderador': ponderador}
    pop_sz_0 = 50
    fit_fn = fitness_ex3
    cr_genes = gene_factory_ex3
    cr_indv = indv_factory
    mut_rate = 0.2
    elitism_rate = 0.2
    term_cond = {'type': 'iterations', 'fitness_th': 0.36, 'iters': 100}
    indv_chars = {}
    for i in range(len(pesos)):
        aux_dict = {}
        aux_dict['gene_type'] = int
        aux_dict['fact_range'] = [0, 15]
        indv_chars[i] = aux_dict.copy()
    GA = GENALG(pop_sz_0, fit_fn, cr_genes, cr_indv, indv_chars, term_cond, mut_rate, elitism_rate)
    generations, goal_cross, overall_max_fitness, overall_fittest_indv = GA.apply(fit_params, selection_type,
                                                                                  random_state, slots)
    print(overall_max_fitness)
    print(overall_fittest_indv)
    # Obtener visualización de Evolución de fitness por generación
    x = list(generations.keys())
    vals = list(generations.values())
    max_fit = [item['max_fitness'] for item in vals]
    mean_fit = [item['mean_fitness'] for item in vals]
    min_fit = [item['min_fitness'] for item in vals]
    fig = plt.figure(figsize=(15, 15))
    plt.plot(x, max_fit, marker='o', markerfacecolor='green', markersize=5, color='olive', linewidth=2, label='max_fit')
    plt.plot(x, mean_fit, marker='', color='blue', linewidth=2, label='mean_fit')
    plt.plot(x, min_fit, marker='', color='red', linewidth=2, label='min_fit')
    plt.title("Evolución de fitness por generación", fontsize=16, fontweight='bold')
    plt.suptitle("Unbound-Knapsack", fontsize=20)
    plt.xlabel("Generación", fontsize=15)
    plt.ylabel("Fitness", fontsize=15)
    plt.legend(fontsize=15)
    plt.savefig('Images\Fitness_por_Generacion_EX3.png')
    plt.close()
    print('gráfico 1 listo')
    # Obtener visualización de heatmap de configuraciones
    random_state = 42
    pesos = [12, 2, 1, 1, 4]
    valores = [4, 2, 2, 1, 10]
    capacidad = 15
    castigo = 5
    slots = 5
    ponderador = 1 / 100
    selection_type = 'tournament'
    fit_params = {'pesos': pesos, 'valores': valores, 'capacidad': capacidad, 'castigo': castigo,
                  'ponderador': ponderador}
    pop_sizes = [50 * i for i in range(1, 21)]
    mut_rates = [i / 10 for i in range(11)]
    fit_fn = fitness_ex3
    cr_genes = gene_factory_ex3
    cr_indv = indv_factory
    elitism_rate = 0.2
    term_cond = {'type': 'fitness_th', 'fitness_th': 0.36, 'iters': 10000}
    indv_chars = {}
    for i in range(len(pesos)):
        aux_dict = {}
        aux_dict['gene_type'] = int
        aux_dict['fact_range'] = [0, 15]
        indv_chars[i] = aux_dict.copy()
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
    plt.suptitle("Unbound-Knapsack", fontsize=20)
    plt.xlabel("Generación", fontsize=15)
    plt.xlabel("Tamaño de Población", fontsize=15)
    plt.ylabel("Tasa de Mutación", fontsize=15)
    plt.savefig('Images\Heatmap_EX3.png')
    plt.close()
    print('gráfico 2 listo')






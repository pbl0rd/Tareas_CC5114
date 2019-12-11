import numpy as np
from genetic_algorithm import GENALG
import matplotlib.pyplot as plt
import seaborn as sns


# Función para crear los genes de los individuos del ejercicio 1. Recibe 2 inputs:
# - gene_type: Corresponde al tipo de gen (En este caso es un bit por lo tanto es 'binary' )
# - fact_range: conjunto de valores posibles para un gen (En este caso los valores posibles son 0 o 1)
# Retorna un gen del tipo especificado y dentro del rango especificado.
def gene_factory_ex1(gene_type, fact_range):
    if fact_range != [0, 1] or gene_type != 'binary':
        raise ValueError("Parámetros incorrectos")
    else:
        # elegimos un valor al azar dentro del conjunto de posibilidades fact_range ([0,1])
        gene = np.random.choice(fact_range)
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


# Función de fitness para el ejercicio 1. Recibe a un individuo y un diccionario con la secuencia y un ponderador.
# Retorna la multiplicación del ponderador y el valor absoluto de la diferencia entre el número entero que representa
# la secuencia entregada y el número entero que representa la secuencia del individuo.
def fitness_ex1(indv, objective):
    vals = list(indv.values())
    vals_str = ''.join(str(i) for i in vals)
    fitness = objective['ponderador'] * abs(int(objective['secuencia'], 2) - int(vals_str, 2))
    return -fitness


if __name__ == '__main__':
    # Prueba ejercicio 1
    # Seteamos los parametros a ser ocupados por el algoritmo para obtener los gráficos pedidos
    secuencia_bits = '00101010110101'
    ponderador = 1 / (2 ** (len(secuencia_bits) - 4))
    fit_params = {'secuencia': secuencia_bits, 'ponderador': ponderador}
    pop_sz_0 = 50
    fit_fn = fitness_ex1
    cr_genes = gene_factory_ex1
    cr_indv = indv_factory
    mut_rate = 0.1
    term_cond = {'type': 'iterations', 'fitness_th': 0, 'iters': 100}
    selection_type = 'tournament'
    slots = 5
    elitism_rate = 0.0
    random_state = 42
    indv_chars = {}
    for i in range(len(secuencia_bits)):
        aux_dict = {}
        aux_dict['gene_type'] = 'binary'
        aux_dict['fact_range'] = [0, 1]
        indv_chars[i] = aux_dict.copy()
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
    fig = plt.figure(figsize=(15, 15))
    plt.plot(x, max_fit, marker='o', markerfacecolor='green', markersize=5, color='olive', linewidth=2, label='max_fit')
    plt.plot(x, mean_fit, marker='', color='blue', linewidth=2, label='mean_fit')
    plt.plot(x, min_fit, marker='', color='red', linewidth=2, label='min_fit')
    plt.title("Evolución de fitness por generación", fontsize=16, fontweight='bold')
    plt.suptitle("Secuencia de bits", fontsize=20)
    plt.xlabel("Generación", fontsize=15)
    plt.ylabel("Fitness", fontsize=15)
    plt.legend(fontsize=15)
    plt.savefig('Images\Fitness_por_Generacion_EX1.png')
    plt.close()
    print('gráfico 1 listo')

import numpy as np
from neural_network import NeuralNetwork
from neuron_layer import NeuronLayer
from neuron import Neuron
from tanh import Tanh
from sigmoid import Sigmoid
from sklearn.model_selection import train_test_split


# Función que ocuparemos para normalizar el dataset
def normalize_func(x, high=1, low=0):
    col_max = np.max(x,axis=0)
    col_min = np.min(x,axis=0)
    new_x = (x-col_min)/(col_max-col_min)*(high-low)+low
    return new_x


if __name__ == '__main__':
    # cargamos el dataset
    iris = np.loadtxt('seeds_dataset.txt', delimiter=',')
    # separamos el dataset en features  y labels
    features = iris[:, :7]
    # aplicamos 1-hot enconding
    labels = iris[:, 7].astype(int) - 1
    labels_2 = np.eye(max(labels) + 1)[labels]
    # Normalizamos el dataset
    features_2 = normalize_func(features)
    # particionamos el dataset en entrenamiento 80% y test 20%
    data_train, data_test, labels_train, labels_test = train_test_split(features_2, labels_2, test_size=0.20,
                                                                        random_state=42)
    # Fijamos los hiperparámetros
    hlayers = 3  # número de capas ocultas
    neurons_per_layer = [20, 20, 20]  # número de neuronas por capas oculta
    entrada = 7  # número de inputs de la red
    salida = 3  # número de neuronas de la capa de salida
    lr = 0.005  # tasa de aprendizaje de la red
    ac_functions = {0: Sigmoid(), 1: Sigmoid(), 2: Sigmoid(), 3: Sigmoid()}  # funciones de activación de las capas
    np.random.seed(0)  # fijamos una semilla para hacer los resultados reproducibles
    # generamos los pesos y bias iniciales de la red
    weights = {}
    bias = {}
    for i in range(hlayers + 1):
        layer_weights = {}
        layer_bias = {}
        if i == 0:
            for j in range(neurons_per_layer[i]):
                layer_weights[j] = 4 * np.random.rand(entrada) - 2
                layer_bias[j] = 4 * np.random.rand() - 2

        elif i == hlayers:
            for j in range(salida):
                layer_weights[j] = 4 * np.random.rand(neurons_per_layer[i - 1]) - 2
                layer_bias[j] = 4 * np.random.rand() - 2
        else:
            for j in range(neurons_per_layer[i]):
                layer_weights[j] = 4 * np.random.rand(neurons_per_layer[i - 1]) - 2
                layer_bias[j] = 4 * np.random.rand() - 2
        weights[i] = layer_weights.copy()
        bias[i] = layer_bias.copy()
    # inicializamos la red con los parámetros fijados anteriormente
    model = NeuralNetwork(hlayers=hlayers, neurons_per_layer=neurons_per_layer, entrada=entrada, salida=salida,
                          weights=weights, bias=bias,  lrate=lr, ac_functions=ac_functions)
    epochs = 300  # número de épocas
    # entrenamos la red con el dataset de entrenamiento
    preds_per_epoch, error_per_epoch, accuracy_per_epoch = model.train_network(data_train, labels_train, epochs)
    # escribimos los resultados a archivos de texto
    with open('preds_per_epoch.txt', 'w') as f:
        print(preds_per_epoch, file=f)
    with open('error_per_epoch.txt', 'w') as f:
        print(error_per_epoch, file=f)
    with open('accuracy_per_epoch.txt', 'w') as f:
        print(accuracy_per_epoch, file=f)
    final_weights = model.get_weights()
    with open('final_weights.txt', 'w') as f:
        print(final_weights, file=f)
    final_bias = model.get_bias()
    with open('final_bias.txt', 'w') as f:
        print(final_bias, file=f)
    # evaluamos nuestro red con el dataset de testeo
    preds_test, error_test, accuracy_test = model.eval(data_test, labels_test)
    with open('preds_test.txt', 'w') as f:
        print(preds_test, file=f)
    print(error_test)
    print(accuracy_test)

import numpy as np
from neural_network import NeuralNetwork
from neuron_layer import NeuronLayer
from neuron import Neuron
from step import Step
from tanh import Tanh
from sigmoid import Sigmoid
from sklearn.model_selection import train_test_split


def normalize_func(x, high=1, low=0):
    col_max = np.max(x,axis=0)
    col_min = np.min(x,axis=0)
    new_x = (x-col_min)/(col_max-col_min)*(high-low)+low
    return new_x


if __name__ == '__main__':
    iris = np.loadtxt('seeds_dataset.txt', delimiter=',')
    features = iris[:, :7]
    labels = iris[:, 7].astype(int) - 1
    labels_2 = np.eye(max(labels) + 1)[labels]
    features_2 = normalize_func(features)
    data_train, data_test, labels_train, labels_test = train_test_split(features_2, labels_2, test_size=0.20,
                                                                        random_state=42)
    hlayers = 4
    neurons_per_layer = [8, 7, 6, 7]
    entrada = 7
    salida = 3
    lr = 0.03
    ac_functions = {0: Sigmoid(), 1: Sigmoid(), 2: Tanh(), 3: Sigmoid(), 4: Sigmoid()}
    np.random.seed(0)
    weights = {}
    for i in range(hlayers + 1):
        layer_weights = {}
        if i == 0:
            for j in range(neurons_per_layer[i]):
                layer_weights[j] = 4 * np.random.rand(entrada) - 2

        elif i == hlayers:
            for j in range(salida):
                layer_weights[j] = 4 * np.random.rand(neurons_per_layer[i - 1]) - 2
        else:
            for j in range(neurons_per_layer[i]):
                layer_weights[j] = 4 * np.random.rand(neurons_per_layer[i - 1]) - 2
        weights[i] = layer_weights.copy()
    model = NeuralNetwork(hlayers=hlayers, neurons_per_layer=neurons_per_layer, entrada=entrada, salida=salida,
                          weights=weights, lr=lr, ac_functions=ac_functions)
    epochs = 300
    preds_per_epoch, error_per_epoch, accuracy_per_epoch = model.train_network(data_train,labels_train, epochs)
    #with open('preds_per_epoch.txt', 'w') as f:
     #   print(preds_per_epoch, file=f)
    with open('error_per_epoch.txt', 'w') as f:
        print(error_per_epoch, file=f)
    with open('accuracy_per_epoch.txt', 'w') as f:
        print(accuracy_per_epoch, file=f)

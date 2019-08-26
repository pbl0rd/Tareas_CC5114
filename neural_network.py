import numpy as np
from neuron_layer import NeuronLayer
from neuron import Neuron


class NeuralNetwork(object):

    def __init__(self, layers=2, neurons_per_layer=[3, 3], entrada=3, salida=2,
                 weights=None, lr=0.1, ac_functions=[Step, Step]):
        self.__length = neurons
        self.__acfunctions = ac_functions
        self.__lrate = lr
        self.__layers = []
        if weights == None:
            for i in range(neurons):
                self.__neurons.append(Neuron(n_weights=n_weights, ac_function=ac_function, lr=lr))
        else:
            for i in range(neurons):
                self.__neurons.append(Neuron(n_weights=len(wieghts[i]), weights=weights[i],
                                             ac_function=ac_function, lr=lr))


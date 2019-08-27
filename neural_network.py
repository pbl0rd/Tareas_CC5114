import numpy as np
from neuron_layer import NeuronLayer
from step import Step


class NeuralNetwork(object):

    def __init__(self, layers=2, neurons_per_layer=[3, 3], entrada=3, salida=2,
                 weights=None, lr=0.1, ac_functions=[Step(), Step(), Step()]):
        self.__acfunctions = ac_functions
        self.__lrate = lr
        self.__layers = []
        if weights == None:
            for i in range(layers+1):
                if i == 0:
                    self.__layers.append(NeuronLayer(neurons=neurons_per_layer[i], n_weights=entrada,
                                                     ac_functions=ac_functions[i], lr=lr))
                elif i == layers:
                    self.__layers.append(NeuronLayer(neurons=salida, n_weights=neurons_per_layer[i-1],
                                                     ac_functions=ac_functions[i], lr=lr))
                else:
                    self.__layers.append(NeuronLayer(neurons=neurons_per_layer[i], n_weights=neurons_per_layer[i-1],
                                                     ac_function=ac_functions[i], lr=lr))
        else:
            for i in range(layers+1):
                if i == 0:
                    self.__layers.append(NeuronLayer(neurons=neurons_per_layer[i], weights=weights[i],
                                                     ac_functions=ac_functions[i], lr=lr))
                elif i == layers:
                    self.__layers.append(NeuronLayer(neurons=salida,  weights=weights[i],
                                                     ac_functions=ac_functions[i], lr=lr))
                else:
                    self.__layers.append(NeuronLayer(neurons=neurons_per_layer[i],  weights=weights[i],
                                                     ac_function=ac_functions[i], lr=lr))

    def feed(self, x):
        in_aux = x
        layers_out = []
        for i in range(len(self.__layers)):
            res = self.__layers[i].feed(in_aux)[:]
            layers_out.append(res[:])
            in_aux = res[:]
        return res[:], layers_out[:]

    def train(self, x, y):
        res, layers_out = self.feed(x)





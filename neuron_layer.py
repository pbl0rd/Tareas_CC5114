import numpy as np
from neuron import Neuron
from step import Step
from tanh import Tanh
from sigmoid import Sigmoid

# Clase Capa de Red Neuronal
class NeuronLayer(object):

    # Método constructor para la clase Capa de Red Neuronal que recibe un entero con el número de neuronas de la capa,
    # otro entero con el número de pesos que debe tener cada una de las neuronas de la capa. Opcionalmente puede
    # recibir un diccionario con los pesos de cada neurona (lista),  una lista con los pesos (weights) y un float
    # con el sesgo (bias).
    def __init__(self, neurons=1, n_weights=3, weights=None, lr=0.1, ac_function=Step()):
        self.__length = neurons
        self.__acfunction = ac_function
        self.__lrate = lr
        self.__neurons = {}
        if weights is None:
            for i in range(neurons):
                self.__neurons[i] = Neuron(n_weights=n_weights, ac_function=ac_function, lr=lr)
        else:
            for i in range(neurons):
                self.__neurons[i] = Neuron(n_weights=len(weights[i]), weights=weights[i], ac_function=ac_function,
                                           lr=lr)

    def get_lenght(self):
        return self.__length

    def get_lrate(self):
        return self.__lrate

    def get_acfunction(self):
        return self.__acfunction

    def get_neurons(self):
        return self.__neurons.copy()

    def get_weights(self, i=None):
        if i is None:
            weights = {}
            for j in range(self.__length):
                weights[j] = self.__neurons[j].get_weights()
            return weights.copy()
        else:
            weights_i = []
            for j in range(self.__length):
                weights_i.append(self.__neurons[j].get_weights()[i])
            return weights_i[:]

    def get_bias(self):
        bias = {}
        for j in range(self.__length):
            bias[j] = self.__neurons[j].get_bias()
        return bias.copy()

    def set_weights(self, new_weights):
        for j in range(self.__length):
            self.__neurons[j].set_weights(new_weights[j])

    def set_bias(self, new_bias):
        for j in range(self.__length):
            self.__neurons[j].set_bias(new_bias[j])

    def feed(self, x):
        res = []
        for i in range(len(self.__neurons)):
            res.append(self.__neurons[i].feed(x))
        return res[:]





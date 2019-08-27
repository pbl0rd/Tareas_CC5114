import numpy as np
from neuron import Neuron


class NeuronLayer(object):

    def __init__(self, neurons=1, n_weights=3, weights=None, lr=0.1, ac_function=Step()):
        self.__length = neurons
        self.__acfunction = ac_function
        self.__lrate = lr
        self.__neurons = []
        if weights == None:
            for i in range(neurons):
                self.__neurons.append(Neuron(n_weights=n_weights, ac_function=ac_function, lr=lr))
        else:
            for i in range(neurons):
                self.__neurons.append(Neuron(n_weights=len(wieghts[i]), weights=weights[i],
                                             ac_function=ac_function, lr=lr))

    def get_lenght(self):
        return self.__length

    def get_acfunction(self):
        return self.__acfunction

    def feed(self, x):
        res = []
        for i in range(len(self.__neurons)):
            res.append(self.__neurons[i].feed(x))
        return res[:]





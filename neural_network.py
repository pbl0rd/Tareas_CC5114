import numpy as np
from neuron_layer import NeuronLayer
from step import Step


class NeuralNetwork(object):

    def __init__(self, hlayers=2, neurons_per_layer=[3, 3], entrada=3, salida=2,
                 weights=None, lr=0.1, ac_functions={0:Step(), 1:Step(), 2:Step()}):
        self.__acfunctions = ac_functions
        self.__lrate = lr
        self.__hlayers = hlayers
        self.__layers = {}
        if weights is None:
            for i in range(hlayers+1):
                if i == 0:
                    self.__layers[i] = NeuronLayer(neurons=neurons_per_layer[i], n_weights=entrada,
                                                     ac_functions=ac_functions[i], lr=lr)
                elif i == hlayers:
                    self.__layers[i] = NeuronLayer(neurons=salida, n_weights=neurons_per_layer[i-1],
                                                     ac_functions=ac_functions[i], lr=lr)
                else:
                    self.__layers[i] = NeuronLayer(neurons=neurons_per_layer[i], n_weights=neurons_per_layer[i-1],
                                                     ac_function=ac_functions[i], lr=lr)
        else:
            for i in range(hlayers+1):
                if i == 0:
                    self.__layers[i] = NeuronLayer(neurons=neurons_per_layer[i], weights=weights[i],
                                                     ac_functions=ac_functions[i], lr=lr)
                elif i == hlayers:
                    self.__layers[i] = NeuronLayer(neurons=salida,  weights=weights[i],
                                                     ac_functions=ac_functions[i], lr=lr)
                else:
                    self.__layers[i] = NeuronLayer(neurons=neurons_per_layer[i],  weights=weights[i],
                                                     ac_function=ac_functions[i], lr=lr)

    def set_weights(self, new_weights):
        for i in range(self.__hlayers+1):
            self.__layers[i].set_weights(new_weights[i])

    def set_bias(self, new_bias):
        for i in range(self.__hlayers+1):
            self.__layers[i].set_bias(new_bias[i])

    def feed(self, x):
        in_aux = x
        layers_out = {}
        for i in range(self.__hlayers+1):
            res = self.__layers[i].feed(in_aux)[:]
            layers_out[i] = res[:]
            in_aux = res[:]
        return res[:], layers_out.copy()

    def back_prop(self, layers_out, y):
        pos = self.__hlayers # posición empezamos en la última capa
        grads = {} # guardaremos los vectores con los delta en este diccionario
        for i in range(self.__hlayers+1):
            if pos-i == self.__hlayers:
                error = y - layers_out[pos-i]
                delta = np.multiply(error,
                                    self.__layers[pos-i].get_acfunction().derivative(layers_out[pos-i]))
                grads[pos-i] = delta
            else:
                error = [np.dot(self.__layers[pos-i+1].get_weights(j),grads[pos-i+1]) for j in range(self.__layers[pos-i].get_lenght())]
                delta = np.multiply(error, self.__layers[pos-i].get_acfunction().derivative(layers_out[pos-i]))
                grads[pos-i] = delta
        return grads.copy()

    def upd_params(self, x, layers_out, grads):
        new_weights_net = {}
        new_bias_net = {}
        lr = self.__lrate
        for i in range(self.__hlayers+1):
            old_weights = self.__layers[i].get_weights()
            old_bias = self.__layers[i].get_bias()
            new_weights = {}
            new_bias = {}
            for j in range(self.__layers[i].get_lenght()):
                if i == 0:
                    new_weights[j] = old_weights[j] + x[j] * lr * grads[i][j]
                else:
                    new_weights[j] = old_weights[j] + layers_out[i-1][j] * lr * grads[i][j]
                new_bias[j] = old_bias + lr * grads[i][j]
            new_weights_net[i] = new_weights.copy()
            new_bias_net[i] = new_bias.copy()
        return new_weights_net.copy(), new_bias_net.copy()

    def train(self, x, y):
        res, layers_out = self.feed(x)
        grads = self.back_prop(layers_out, y)
        new_weights, new_bias = self.upd_params(x, layers_out, grads)
        self.set_weights(new_weights)
        self.set_bias(new_bias)





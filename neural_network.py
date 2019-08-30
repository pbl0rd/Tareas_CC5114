import numpy as np
from neuron_layer import NeuronLayer
from step import Step
from tanh import Tanh
from sigmoid import Sigmoid

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
                                                     ac_function=ac_functions[i], lr=lr)
                elif i == hlayers:
                    self.__layers[i] = NeuronLayer(neurons=salida, n_weights=neurons_per_layer[i-1],
                                                     ac_function=ac_functions[i], lr=lr)
                else:
                    self.__layers[i] = NeuronLayer(neurons=neurons_per_layer[i], n_weights=neurons_per_layer[i-1],
                                                     ac_function=ac_functions[i], lr=lr)
        else:
            for i in range(hlayers+1):
                if i == 0:
                    self.__layers[i] = NeuronLayer(neurons=neurons_per_layer[i], weights=weights[i],
                                                     ac_function=ac_functions[i], lr=lr)
                elif i == hlayers:
                    self.__layers[i] = NeuronLayer(neurons=salida,  weights=weights[i],
                                                     ac_function=ac_functions[i], lr=lr)
                else:
                    self.__layers[i] = NeuronLayer(neurons=neurons_per_layer[i],  weights=weights[i],
                                                     ac_function=ac_functions[i], lr=lr)

    def set_weights(self, new_weights):
        for i in range(self.__hlayers+1):
            self.__layers[i].set_weights(new_weights[i])

    def set_bias(self, new_bias):
        for i in range(self.__hlayers+1):
            self.__layers[i].set_bias(new_bias[i])

    def get_weights(self):
        weights ={}
        for i in range(self.__hlayers+1):
            weights[i] = self.__layers[i].get_weights()
        return weights.copy()

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
                new_weights_neuron = []
                for k in range(len(self.__layers[i].get_neurons()[j].get_weights())):
                    if i == 0:
                        new_weights_neuron.append(old_weights[j][k] + x[k] * lr * grads[i][j])
                    else:
                        new_weights_neuron.append(old_weights[j][k] + layers_out[i-1][k] * lr * grads[i][j])
                new_weights[j] = np.array(new_weights_neuron).copy()
                new_bias[j] = old_bias[j] + lr * grads[i][j]
            new_weights_net[i] = new_weights.copy()
            new_bias_net[i] = new_bias.copy()
        return new_weights_net.copy(), new_bias_net.copy()

    def train(self, x, y):
        res, layers_out = self.feed(x)
        grads = self.back_prop(layers_out, y)
        new_weights, new_bias = self.upd_params(x, layers_out, grads)
        self.set_weights(new_weights)
        self.set_bias(new_bias)
        ans = np.array(y)
        ans_hat = np.array(res)
        diff =ans-ans_hat
        error = np.dot(diff,diff)/len(diff)
        if error == 0.0:
            acierto = 1
        else:
            acierto = 0
        return res, error, acierto

    def train_w_set(self, x, y):
        preds = []
        epoch_error = 0
        accuracy = 0
        for j in range(len(x)):
            res, error, acierto= self.train(x[j], y[j])
            preds.append(res[:])
            epoch_error += error
            accuracy += acierto
        epoch_error = epoch_error/len(x)
        accuracy = accuracy/len(x)
        return preds[:], epoch_error, accuracy

    def train_network(self, x, y, epochs=100):
        preds_per_epoch = {}
        error_per_epoch = {}
        accuracy_per_epoch = {}
        for i in range(epochs):
            preds, epoch_error, accuracy = self.train_w_set(x, y)
            preds_per_epoch[i] = preds[:]
            error_per_epoch[i] = epoch_error
            accuracy_per_epoch[i] = accuracy
        return preds_per_epoch.copy(), error_per_epoch.copy(), accuracy_per_epoch.copy()

    def eval(self,test_x, test_y):
        preds = []
        error_final = 0
        accuracy = 0
        for i in range(len(test_x)):
            res, layers_out = self.feed(test_x[i])
            preds.append(res)
            ans = np.array(test_y[i])
            ans_hat = np.array(res)
            diff = ans - ans_hat
            error = np.dot(diff, diff) / len(diff)
            if error == 0.0:
                acierto = 1
            else:
                acierto = 0
            error_final += error
            accuracy += acierto
        error_final = error_final/len(test_x)
        accuracy = accuracy/len(test_x)
        return preds[:], error_final, accuracy









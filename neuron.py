import numpy as np
from sigmoid import Sigmoid
from tanh import Tanh
from step import Step

# Clase Neurona
class Neuron(object):
    # Método constructor para la clase Neurona que
    # recibe una lista de floats con los pesos (weights), un float
    # con el sesgo (bias) y .

    def __init__(self, n_weights=3, weights=4*np.random.rand(3)-2,
                 bias=4*np.random.rand()-2, ac_function=Tanh(), lr=0.1):
        if n_weights != len(weights):
            self.__weights = 4*np.random.rand(n_weights)-2
        else:
            self.__weights = weights
        self.__bias = bias
        self.__acfunction = ac_function
        self.__lrate = lr

    # Métodos get para obtener los atributos de la Neurona.

    def get_weights(self):
        return self.__weights

    def get_bias(self):
        return self.__bias

    def get_acfunction(self):
        return self.__acfunction

    def get_lrate(self):
        return self.__lrate

    # Métodos set para fijar nuevos valores para los atributos de
    # la Neurona.

    def set_weights(self, pesos):
        self.__weights = pesos

    def set_bias(self, bias):
        self.__bias = bias

    def set_acfunction(self, ac_function):
        self.__acfunction = ac_function

    def set_lrate(self, l_rate):
        self.__lrate = l_rate

    # Método para alimentar al perceptron con un arreglo de inputs (x)
    # del mismo tamaño que el arreglo (weights) y retornar la respuesta
    # de la Neurona.
    def feed(self, x):
        if len(x) == len(self.__weights):
            val = np.dot(x, self.__weights) + self.__bias
            res = self.__acfunction.apply(val)
            return res
        else:
            raise ValueError("Número de inputs incorrecto")

    def train(self, x, answer):
        old_w = self.get_weights()
        if len(x) == len(old_w):
            res = self.feed(x)
            diff = answer - res
            l_rate = self.get_lrate()
            old_b = self.get_bias()
            if self.__acfunction == Step():
                delta = diff
            else:
                delta = diff * self.__acfunction.derivative(res)
            new_w = []
            for i in range(len(old_w)):
                new_w.append(old_w[i] + l_rate * x[i] * delta)
            self.set_weights(new_w)
            new_b = old_b + l_rate * delta
            self.set_bias(new_b)
        else:
            raise ValueError("Número de inputs incorrecto")


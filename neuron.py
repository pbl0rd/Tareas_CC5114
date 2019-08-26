import numpy as np
import sigmoid

# Clase Neurona
class Neuron(object):
    # Método constructor para la clase Neurona que
    # recibe una lista de floats con los pesos (weights), un float
    # con el sesgo (bias) y .

    def __init__(self, weights, bias):
        self.__weights = weights
        self.__bias = bias
        self.__acfunction =
        self.__lrate = 

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

    # Método para alimentar al perceptron con un arreglo de inputs (x)
    # del mismo tamaño que el arreglo (weights) y retornar la respuesta
    # de la Neurona.
    def feed(self, x):
        if len(x) == len(self.__weights):
            if np.dot(x, self.__weights) + self.__bias <= 0:
                return 0
            else:
                return 1
        else:
            raise ValueError("Número de inputs incorrecto")

    def train(self, input, answer):
        if type(train_set) is list:
            self.set_weights(weights_0)
            self.set_bias(bias_0)
            for item in train_set:
                if len(item) - 1 == len(self.__weights):
                    diff = item[-1] - self.feed(item[:-1])
                    new_w = []
                    for i in range(len(self.__weights)):
                        new_w.append(self._weights[i] + lr * item[i] * diff)
                    self.set_weights(new_w)
                    new_b = self.__bias + lr * diff
                    self.set_bias(new_b)
                else:
                    raise ValueError("Número de inputs incorrecto")
        else:
            raise ValueError("Train_set debe ser una lista de listas de floats")

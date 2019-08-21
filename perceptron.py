import numpy as np

# Clase Perceptrón
class Perceptron(object):

    # Método constructor para la clase perceptrón que
    # recibe una lista con los pesos (weights) y un float
    # con el sesgo (bias).

    def __init__(self, weights, bias):
        self.__weights = weights
        self.__bias = bias

    # Métodos get para obtener los atributos del perceptrón.

    def get_weights(self):
        return self.__weights

    def get_bias(self):
        return self.__bias

    # Métodos set para fijar nuevos valores para los atributos del
    # perceptrón.

    def set_weights(self, pesos):
        self.__weights = pesos

    def set_bias(self, bias):
        self.__bias = bias

    # Método para alimentar al perceptron con un arreglo de inputs (x)
    # del mismo tamaño que el arreglo (weights) y retornar la respuesta
    # del perceptrón.
    def feed(self, x):
        if len(x) == len(self.__weights):
            if np.dot(x, self.__weights) + self.__bias <= 0:
                return 0
            else:
                return 1
        else:
            raise ValueError("Número de inputs incorrecto")

# Subclase del perceptrón que permite implementar la función lógica AND


class PerAnd(Perceptron):

    def __init__(self):
        super(PerAnd, self).__init__([2, 2], -3)

# Subclase del perceptrón que permite implementar la función lógica OR


class PerOr(Perceptron):

    def __init__(self):
        super(PerOr, self).__init__([2, 2], -1)

# Subclase del perceptrón que permite implementar la función lógica NAND


class PerNAnd(Perceptron):

    def __init__(self):
        super(PerNAnd, self).__init__([-2, -2], 3)

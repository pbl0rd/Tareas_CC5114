import numpy as np
from neuron import Neuron
from tanh import Tanh
from sigmoid import Sigmoid


# Clase Capa de Red Neuronal
class NeuronLayer(object):

    # Método constructor para la clase Capa de Neuronas que recibe un entero con el número de neuronas de la capa y
    # otro entero con el número de pesos que debe tener cada una de las neuronas de la capa. Opcionalmente puede
    # recibir un diccionario con los pesos de cada neurona (lista), un diccionario con los sesgos de cada
    # neurona (float), un float con la tasa de aprendizaje lr y la función de activación que comparten las neuronas de
    # la capa (debe ser Sigmoid() o Tanh()).
    def __init__(self, neurons: int, n_weights: int, weights=None, bias=None, lrate=0.1, ac_function=Sigmoid()):
        if type(neurons) != int:
            raise ValueError("El número de neuronas neurons debe ser un número entero positivo")
        elif neurons < 1:
            raise ValueError("El número de neuronas neurons debe ser un número entero positivo")
        else:
            self.__length = neurons
            self.__input_length = n_weights
            self.__acfunction = ac_function
            self.__lrate = lrate
            self.__neurons = {}
            # Dependiendo de los inputs ingresado inicializamos las neuronas de la capa
            if weights is None and bias is None:
                for i in range(neurons):
                    self.__neurons[i] = Neuron(n_weights=n_weights, ac_function=ac_function, lrate=lrate)
            elif bias is None:
                if type(weights) is not dict:
                    raise ValueError("Input weights debe ser un diccionario con las listas de pesos de cada neurona")
                elif len(list(weights.keys())) != neurons:
                    raise ValueError("Número de entradas del diccionario weights debe ser igual al número de neuronas")
                else:
                    for i in range(neurons):
                        self.__neurons[i] = Neuron(n_weights=n_weights, weights=weights[i], ac_function=ac_function,
                                                   lrate=lrate)
            elif weights is None:
                if type(bias) is not dict:
                    raise ValueError("Input bias debe ser un diccionario con los sesgos de cada neurona")
                elif len(list(bias.keys())) != neurons:
                    raise ValueError("Número de entradas del diccionario bias debe ser igual al número de neuronas")
                else:
                    for i in range(neurons):
                        self.__neurons[i] = Neuron(n_weights=n_weights, bias=bias[i], ac_function=ac_function,
                                                   lrate=lrate)
            else:
                if type(weights) is not dict or type(bias) is not dict:
                    raise ValueError(
                        "El input weights y bias deben ser diccionarios con las listas de pesos y bias de cada " +
                        "neurona respectivamente")
                elif len(list(weights.keys())) != neurons or len(list(bias.keys())) != neurons:
                    raise ValueError("El número de entradas de los diccionario weights y bias debe " +
                                     "ser igual al número de neuronas")
                else:
                    for i in range(neurons):
                        self.__neurons[i] = Neuron(n_weights=n_weights, weights=weights[i], bias=bias[i],
                                                   ac_function=ac_function, lrate=lrate)

    # Métodos get para obtener los atributos de la capa.

    # Función para obtener el número de neuronas que tiene la capa
    def get_length(self):
        return self.__length

    # Función para obtener el número inputs que recibe cada neurona de la capa
    def get_input_length(self):
        return self.__input_length

    # Función para obtener la tasa de aprendizaje que comparten las neuronas de la capa
    def get_lrate(self):
        return self.__lrate

    # Función para obtener la función de activación que comparten las neuronas de la capa
    def get_acfunction(self):
        return self.__acfunction

    # Función para obtener un diccionario con las neuronas de la capa
    def get_neurons(self):
        return self.__neurons

    # Función para obtener un diccionario con loss pesos de las neuronas de la capa
    def get_weights(self):
        weights = {}
        for j in range(self.__length):
            weights[j] = self.__neurons[j].get_weights()
        return weights

    # Función para obtener un arreglo con los pesos correspondientes a la posición i de cada neurona de la capa.
    # Recibe un int con la posición requerida
    def get_weights_pos_i(self, i: int):
        weights_i = []
        for j in range(self.__length):
            weights_i.append(self.__neurons[j].get_weight_i(i))
        return np.array(weights_i)

    # Función para obtener un diccionario con los sesgos de las neuronas de la capa
    def get_bias(self):
        bias = {}
        for j in range(self.__length):
            bias[j] = self.__neurons[j].get_bias()
        return bias

    # Métodos set para fijar nuevos valores para los atributos de la capa.

    # Función para modificar los pesos de las neuronas de la capa.
    # Recibe un diccionario con los nuevos arreglos de pesos para las neuronas de la capa
    def set_weights(self, new_weights: dict):
        if type(new_weights) is not dict:
            raise ValueError("El input new_weights debe ser un diccionario con los arreglos de pesos de cada neurona")
        elif len(list(new_weights.keys())) != self.__length:
            raise ValueError("El número de entradas del diccionario new_weights debe ser igual al número de neuronas")
        else:
            for j in range(self.__length):
                self.__neurons[j].set_weights(new_weights[j])

    # Función para modificar los sesgos de las neuronas de la capa.
    # Recibe un diccionario con los nuevos sesgos para las neuronas de la capa
    def set_bias(self, new_bias):
        if type(new_bias) is not dict:
            raise ValueError("El input new_bias debe ser un diccionario con los bias de cada neurona")
        elif len(list(new_bias.keys())) != self.__length:
            raise ValueError("El número de entradas del diccionario new_bias debe ser igual al número de neuronas")
        else:
            for j in range(self.__length):
                self.__neurons[j].set_bias(new_bias[j])

    # Función para alimentar a la capa de neuronas con un arreglo de inputs (x) cuyo tamaño coincide con el número de
    # pesos de cada neurona de la capa. Retorna un arreglo con la respuesta dada por cada neurona de la capa.
    def feed(self, x: np.ndarray):
        res = []
        for i in range(len(self.__neurons)):
            res.append(self.__neurons[i].feed(x))
        return np.array(res)





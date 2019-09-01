import numpy as np
from step import Step
from tanh import Tanh
from sigmoid import Sigmoid


# Clase Neurona
class Neuron(object):
    # Método constructor para la clase Neurona que recibe un entero con el número de pesos/inputs que tendrá
    # la nuerona y retorna una Neurona con ese número de pesos aleatorios (entre [-2,2]) y un bias aleatorio
    # (entre [-2,2]) con función de activación sigmoidea y tasa de aprendizaje igual a 0.1. Opcionalmente, se puede
    # ingresar una lista de floats con los pesos (weights) que queremos que tenga la neurona, un float
    # con el sesgo (bias), el tipo de función de activación que debe tener la neurona (Sigmoid(), Tanh() o Step()) y
    # finalmente un float con la tasa de aprendizaje lr.

    def __init__(self, n_weights: int, weights=None, bias=None, ac_function=Sigmoid(), lr=0.1):
        # Verificamos que los parámetros de entrada del constructor sean los correctos
        if type(n_weights) != int:
            raise ValueError("Input n_weights debe ser un número entero")
        elif weights is not None and type(weights) not in [list, np.ndarray]:
            raise ValueError("Los pesos Weights debe ser una lista de floats")
        elif weights is not None and len(weights) != n_weights:
            raise ValueError("el número n_weights debe coincidir con los pesos entregados")
        elif type(ac_function) != Step and type(ac_function) != Sigmoid and type(ac_function) != Tanh:
            raise ValueError("La función de activación debe ser Step(), Sigmoid() o bien, Tanh()")
        elif type(lr) != float:
            raise ValueError("La tasa de aprendizaje lr debe ser un float")
        elif bias is not None and type(bias) != float:
            raise ValueError("El sesgo bias debe ser un float")
        else:
            if weights is None:  # En caso de no contar con los pesos
                self.__weights = 4*np.random.rand(n_weights)-2
            else:
                for i in range(len(weights)):
                    if type(weights[i]) != float:
                        raise ValueError("cada peso debe ser un float")
                self.__weights=np.array(weights)
            if bias is None: # En caso de no contar con el bias
                4 * np.random.rand() - 2
            else:
                self.__bias = bias
            self.__length = n_weights
            self.__acfunction = ac_function
            self.__lrate = lr

    # Métodos get para obtener los atributos de la Neurona.

    # Función para obtener los pesos de la neurona
    def get_weights(self):
        return self.__weights

    # Función para obtener el número de pesos/inputs de la neurona
    def get_length(self):
        return self.__length

    # Función para obtener el peso i de la neurona
    def get_weight_i(self, i: int):
        if type(i) != int:
            raise ValueError("el input debe ser un número entero")
        elif i >= self.__length or i < -self.__length:
            raise ValueError("La neurona no tiene el peso indicado")
        else:
            return self.__weights[i]

    # Función para obtener el sesgo de la neurona
    def get_bias(self):
        return self.__bias

    # Función para obtener la función de activación de la neurona
    def get_acfunction(self):
        return self.__acfunction

    # Función para obtener la tasa de aprendizaje de la neurona
    def get_lrate(self):
        return self.__lrate

    # Métodos set para fijar nuevos valores para los atributos de la Neurona.

    # Función para modificar los pesos de la neurona, recibe un arreglo numpy con los nuevos pesos
    def set_weights(self, pesos: np.ndarray):
        if type(pesos) not in [list, np.ndarray]:
            raise ValueError("Los pesos Weights debe ser una lista de floats")
        elif len(pesos) != self.__length:
            raise ValueError("Número de pesos incorrecto")
        else:
            for i in range(len(pesos)):
                if type(pesos[i]) != float:
                    raise ValueError("cada peso debe ser un float")
            self.__weights = np.array(pesos)

    # Función para modificar el peso i de la neurona. Recibe un float con el nuevo peso y un entero con la posición i
    def set_weight_i(self, peso: float, i: int):
        if type(peso) != float or type(i) != int:
            raise ValueError("El peso entregado debe ser un float y la posición i debe ser un int")
        elif i >= self.__length or i < -self.__length:
            raise ValueError("La neurona no tiene el peso indicado")
        else:
            self.__weights[i] = peso

    # Función para modificar el sesgo de la neurona. Recibe un float con el nuevo sesgo
    def set_bias(self, bias: float):
        if type(bias) != float:
            raise ValueError("El sesgo bias debe ser un float")
        else:
            self.__bias = bias

    # Función para modificar la función de activación de la neurona. Recibe Step(), Sigmoid() o bien, Tanh() como
    # entrada
    def set_acfunction(self, ac_function):
        if type(ac_function) != Step and type(ac_function) != Sigmoid and type(ac_function) != Tanh:
            raise ValueError("La función de activación debe ser Step(), Sigmoid() o bien, Tanh()")
        else:
            self.__acfunction = ac_function

    # Función para modificar la tasa de aprendizaje de la neurona. Recibe un float con la nueva tasa de aprendizaje
    def set_lrate(self, l_rate: float):
        if type(l_rate) != float:
            raise ValueError("La tasa de aprendizaje lr debe ser un float")
        else:
            self.__lrate = l_rate

    # Método para alimentar a la neurona con un arreglo de inputs (x)
    # del mismo tamaño que el arreglo (weights) y retornar la respuesta
    # de la Neurona.
    def feed(self, x: np.ndarray):
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


import numpy as np


# Clase para la función de activación sigmoide
class Sigmoid(object):

    # Método para aplicar la función
    def apply(x):
        return 1 / (1 + np.exp(-x))

    # Método para aplicar la derivada de la función
    def derivative(x):
        return Sigmoid.apply(x)*(1 - Sigmoid.apply(x))

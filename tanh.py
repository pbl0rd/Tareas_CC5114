import numpy as np


# Clase para la función de activación
# tangente hiperbólica
class Tanh(object):

    # Método para aplicar la función
    def apply(x):
        return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

    # Método para aplicar la derivada de la función
    def derivative(x):
        return 1 - Tanh.apply(x)**2

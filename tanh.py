import numpy as np


# Clase para la función de activación
# tangente hiperbólica
class Tanh(object):

    # Método para aplicar la función
    def apply(self, x):
        x_aux = np.array(x)
        return (np.exp(x_aux) - np.exp(-x_aux)) / (np.exp(x_aux) + np.exp(-x_aux))

    # Método para aplicar la derivada de la función
    def derivative(self, x):
        x_aux = np.array(x)
        return 1 - self.apply(x_aux)**2

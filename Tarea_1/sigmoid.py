import numpy as np


# Clase para la función de activación sigmoide
class Sigmoid(object):

    # Método para aplicar la función
    def apply(self, x):
        if x > 0:
            return 1 / (1 + np.exp(-x))
        else:
            return np.exp(x)/(np.exp(x)+1)

    # Método para aplicar la derivada de la función
    def derivative(self, x):
        x_aux = np.array(x)
        return self.apply(x_aux)*(1 - self.apply(x_aux))

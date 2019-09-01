import numpy as np


# Clase para la función de activación
# tangente hiperbólica
class Tanh(object):

    # Método para aplicar la función
    def apply(self, x):
        if x > 20:
            return (1-np.exp(-2*x)) / (1+np.exp(-2*x))
        elif x < -20:
            return (np.exp(2*x)-1)/(np.exp(2*x)+1)
        else:
            return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

    # Método para aplicar la derivada de la función
    def derivative(self, x):
        return 1 - self.apply(x)**2

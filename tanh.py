import numpy as np


# Clase para la función de activación
# tangente hiperbólica
class Tanh(object):

    # Método para aplicar la función
    def apply(self, x):
        if x > 0:
            return (1-np.exp(-2*x)) / (1+np.exp(-2*x))
        else:
            return (np.exp(2*x)-1)/(np.exp(2*x)+1)

    # Método para aplicar la derivada de la función
    def derivative(self, x):
        x_aux = np.array(x)
        return 1 - self.apply(x_aux)**2

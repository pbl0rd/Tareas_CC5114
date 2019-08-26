import numpy as np


# Clase para la función de activación
# escalón
class Step(object):

    # Método para aplicar la función
    def apply(self, x):
        if x < 0:
            return 0
        else:
            return 1

    # Método para aplicar la derivada de la función
    def derivative(self, x):
        if x == 0:
            raise ValueError("No existe la derivada para esta función en 0")
        else:
            return 0

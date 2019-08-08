from perceptron import PerNAnd

# Clase para implementar un Summing Number Gate


class SummingNumberGate(object):

    # Método cosntrutor de la clase summing number gate que tiene
    # como atributo un objeto del tipo NAND definido en el archivo
    # con la clase perceptrón.

    def __init__(self):
        self.nand = PerNAnd()

    # Método que recibe un arreglo de inputs (x) bidimendional donde cada
    # coordenada corresponde al valor de un bit y retorna el valor de la
    # suma de estos.

    def sum_bit(self, x):
        if len(x) == len(self.nand.get_weights()):
            return self.nand.feed(
                [self.nand.feed([x[0], self.nand.feed(x)]), self.nand.feed([self.nand.feed(x), x[1]])])
        else:
            raise ValueError("Número de inputs incorrecto")

    # Método que recibe un arreglo de inputs (x) bidimendional donde cada
    # coordenada corresponde al valor de un bit y retorna el valor del bit
    # que se acarrea en la suma de estos.

    def carry_bit(self, x):
        if len(x) == len(self.nand.get_weights()):
            return self.nand.feed([self.nand.feed(x), self.nand.feed(x)])
        else:
            raise ValueError("Número de inputs incorrecto")
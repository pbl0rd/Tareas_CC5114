from perceptron import PerNAnd

# Clase para implementar un Summing Number Gate


class SummingNumberGate(object):

    # Método construtor de la clase summing number gate que tiene
    # como atributo un objeto del tipo NAND definido en el archivo
    # con la clase perceptrón.

    def __init__(self):
        self.nand = PerNAnd()

    # Método que recibe un arreglo de inputs (x) bidimendional donde cada
    # coordenada corresponde al valor de un bit y retorna el valor de la
    # suma de estos y el valor del bit que se acarrea en la suma de estos..

    def sum_bits(self, x):
        if len(x) == len(self.nand.get_weights()):
            out_1 = self.nand.feed(x)
            out_2 = self.nand.feed([x[0], out_1])
            out_3 = self.nand.feed([out_1, x[1]])
            sum_bit = self.nand.feed([out_2, out_3])
            carry_bit = self.nand.feed([out_1, out_1])
            return sum_bit, carry_bit
        else:
            raise ValueError("Número de inputs incorrecto")

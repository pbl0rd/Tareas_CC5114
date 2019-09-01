import unittest
from sigmoid import Sigmoid
import numpy as np


class TestSigmoid(unittest.TestCase):

    def test_apply(self):
        a = Sigmoid()
        self.assertEqual(a.apply(1), 1/(1+np.exp(-1)))
        self.assertEqual(a.apply(10000), 1/(1+np.exp(-10000)))
        self.assertEqual(a.apply(-10000), 1 / (1 + np.exp(10000)))

    def test_derivative(self):
        a = Sigmoid()
        self.assertEqual(a.derivative(1), 1/(1+np.exp(-1))*(1-1/(1+np.exp(-1))))
        self.assertEqual(a.derivative(10000), 1 / (1 + np.exp(-10000)) * (1 - 1 / (1 + np.exp(-10000))))
        self.assertEqual(a.derivative(-10000), 1 / (1 + np.exp(10000)) * (1 - 1 / (1 + np.exp(10000))))


if __name__ == '__main__':
    unittest.main()

import unittest
from tanh import Tanh
import numpy as np


class TestTanh(unittest.TestCase):

    def test_apply(self):
        a = Tanh()
        self.assertEqual(a.apply(1), np.tanh(1))
        self.assertEqual(a.apply(10000), np.tanh(10000))
        self.assertEqual(a.apply(-10000), np.tanh(-10000))

    def test_derivative(self):
        a = Tanh()
        self.assertEqual(a.derivative(1), 1-np.tanh(1)**2)
        self.assertEqual(a.derivative(1000), 1 - np.tanh(1000) ** 2)
        self.assertEqual(a.derivative(-1000), 1 - np.tanh(-1000) ** 2)


if __name__ == '__main__':
    unittest.main()

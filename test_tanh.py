import unittest
from tanh import Tanh
import numpy as np


class TestTanh(unittest.TestCase):

    def test_apply(self):
        self.assertEqual(Tanh.apply(1), 0.7615941559557649)

    def test_derivative(self):
        self.assertEqual(Tanh.derivative(1), 0.41997434161402614)


if __name__ == '__main__':
    unittest.main()

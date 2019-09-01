import unittest
from neuron import Neuron
from sigmoid import Sigmoid
from tanh import Tanh
import numpy as np


class TestNeuron(unittest.TestCase):

    def setUp(self):
        self.neuron = Neuron(5, [2.0, 3.0, 5.5, 4.0, 1.1], 2.3)

    def tearDown(self):
        pass

    def test_constructor(self):
        with self.assertRaises(ValueError):
            self.neuron = Neuron('hola', [2.0, 3.0, 5.5, 4.0, 1.1], 2.3)
        with self.assertRaises(ValueError):
            self.neuron = Neuron(-3, [2.0, 3.0, 5.5, 4.0, 1.1], 2.3)
        with self.assertRaises(ValueError):
            self.neuron = Neuron(5.0, [2.0, 3.0, 5.5, 4.0, 1.1], 2.3)
        with self.assertRaises(ValueError):
            self.neuron = Neuron(6, [2.0, 3.0, 5.5, 4.0, 1.1], 2.3)
        with self.assertRaises(ValueError):
            self.neuron = Neuron(5, [2.0, 3, 5.5, 4.0, 1.1], 2.3)
        with self.assertRaises(ValueError):
            self.neuron = Neuron(5, 'hola', 2.3)
        with self.assertRaises(ValueError):
            self.neuron = Neuron(5, [2.0, 3.0, 5.5, 4.0, 1.1], 2)
        with self.assertRaises(ValueError):
            self.neuron = Neuron(5, [2.0, 3.0, 5.5, 4.0, 1.1], 'hola')
        with self.assertRaises(ValueError):
            self.neuron = Neuron(5, [2.0, 3.0, 5.5, 4.0, 1.1], 2.3, 4)
        with self.assertRaises(ValueError):
            self.neuron = Neuron(5, [2.0, 3.0, 5.5, 4.0, 1.1], 2.3, 'hola')
        with self.assertRaises(ValueError):
            self.neuron = Neuron(5, [2.0, 3.0, 5.5, 4.0, 1.1], 2.3, ac_function=np.mean)
        with self.assertRaises(ValueError):
            self.neuron = Neuron(5, [2.0, 3.0, 5.5, 4.0, 1.1], 2.3, lrate=3)
        with self.assertRaises(ValueError):
            self.neuron = Neuron(5, [2.0, 3.0, 5.5, 4.0, 1.1], 2.3, lrate='hola')

    def test_get_weights(self):
        a = [2.0, 3.0, 5.5, 4.0, 1.1]
        for i in range(self.neuron.get_length()):
            self.assertEqual(self.neuron.get_weights()[i], a[i])

    def test_get_length(self):
        self.assertEqual(self.neuron.get_length(), 5)

    def test_get_bias(self):
        self.assertEqual(self.neuron.get_bias(), 2.3)

    def test_get_weight_i(self):
        self.assertEqual(self.neuron.get_weight_i(3), 4.0)
        with self.assertRaises(ValueError):
            self.neuron.get_weight_i(5)
        with self.assertRaises(ValueError):
            self.neuron.get_weight_i(-6)

    def test_get_acfunction(self):
        self.assertIsInstance(self.neuron.get_acfunction(), Sigmoid)

    def test_get_lrate(self):
        self.assertEqual(self.neuron.get_lrate(), 0.1)

    def test_set_weights(self):
        self.neuron.set_weights([0.1, 0.1, 0.1, 0.1, 0.1])
        for i in range(len([0.1, 0.1, 0.1, 0.1, 0.1])):
            self.assertEqual(self.neuron.get_weights()[i], [0.1, 0.1, 0.1, 0.1, 0.1][i])
        with self.assertRaises(ValueError):
            self.neuron.set_weights([0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
        with self.assertRaises(ValueError):
            self.neuron.set_weights([0.1, 0.1, 0.1, 0.1, 'a'])
        with self.assertRaises(ValueError):
            self.neuron.set_weights('hola')
        with self.assertRaises(ValueError):
            self.neuron.set_weights(3)

    def test_set_weight_i(self):
        self.neuron.set_weight_i(0.1, 1)
        self.assertEqual(self.neuron.get_weight_i(1), 0.1)
        with self.assertRaises(ValueError):
            self.neuron.set_weight_i(3, 1)
        with self.assertRaises(ValueError):
            self.neuron.set_weight_i(0.1, 1.0)
        with self.assertRaises(ValueError):
            self.neuron.set_weight_i(0.1, 7)
        with self.assertRaises(ValueError):
            self.neuron.set_weight_i('hola', 1)
        with self.assertRaises(ValueError):
            self.neuron.set_weight_i(0.1, 'hola')

    def test_set_bias(self):
        self.neuron.set_bias(1.8)
        self.assertEqual(self.neuron.get_bias(), 1.8)
        with self.assertRaises(ValueError):
            self.neuron.set_bias([1.0, 5.0])
        with self.assertRaises(ValueError):
            self.neuron.set_bias(4)
        with self.assertRaises(ValueError):
            self.neuron.set_bias('hola')

    def test_set_acfunction(self):
        self.neuron.set_acfunction(Tanh())
        self.assertIsInstance(self.neuron.get_acfunction(), Tanh)
        with self.assertRaises(ValueError):
            self.neuron.set_acfunction('hola')

    def test_set_lrate(self):
        self.neuron.set_lrate(0.3)
        self.assertEqual(self.neuron.get_lrate(), 0.3)
        with self.assertRaises(ValueError):
            self.neuron.set_lrate([1.0, 5.0])
        with self.assertRaises(ValueError):
            self.neuron.set_lrate(4)
        with self.assertRaises(ValueError):
            self.neuron.set_lrate('hola')

    def test_feed(self):
        x = [1.0, 2.0, -3.0, 4.0, -10.0]
        self.assertAlmostEqual(self.neuron.feed(x), 1/(1+np.exp(1.2)))
        with self.assertRaises(ValueError):
            self.neuron.feed([1.0, 3, -3.0, 4.0, -10.0])
        with self.assertRaises(ValueError):
            self.neuron.feed([1.0, 5.0])
        with self.assertRaises(ValueError):
            self.neuron.feed(4)
        with self.assertRaises(ValueError):
            self.neuron.feed('hola')

    def test_train(self):
        with self.assertRaises(ValueError):
            self.neuron.feed([1.0, 3, -3.0, 4.0, -10.0])
        with self.assertRaises(ValueError):
            self.neuron.feed([1.0, 5.0])
        with self.assertRaises(ValueError):
            self.neuron.feed(4)
        with self.assertRaises(ValueError):
            self.neuron.feed('hola')


if __name__ == '__main__':
    unittest.main()

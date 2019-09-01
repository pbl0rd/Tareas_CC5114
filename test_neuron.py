import unittest
from neuron import Neuron
from sigmoid import Sigmoid
from tanh import Tanh


class TestNeuron(unittest.TestCase):

    def setUp(self):
        self.neuron = Neuron(5, [2.0, 3.0, 5.5, 4.0, 1.1], 2.3)

    def tearDown(self):
        pass

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

    def test_set_acfunction(self):
        self.neuron.set_acfunction(Tanh())
        self.assertIsInstance(self.neuron.get_acfunction(), Tanh)
        with self.assertRaises(ValueError):
            self.neuron.set_acfunction('hola')


if __name__ == '__main__':
    unittest.main()

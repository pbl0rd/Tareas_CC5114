import unittest
from neuron_layer import NeuronLayer


class TestNeuronLayer(unittest.TestCase):

    def setUp(self):
        self.neuron_layer = NeuronLayer(5, [2.0, 3.0, 5.5, 4.0, 1.1], 2.3)

    def tearDown(self):
        pass

    def test_constructor(self):
        with self.assertRaises(ValueError):
            self.neuron_layer = NeuronLayer('hola', [2.0, 3.0, 5.5, 4.0, 1.1], 2.3)
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


if __name__ == '__main__':
    unittest.main()

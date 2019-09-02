import unittest
from neuron_layer import NeuronLayer


class TestNeuronLayer(unittest.TestCase):

    def setUp(self):
        self.neuron_layer = NeuronLayer(2, 2, {0: [2.0, 3.0], 1: [1.0, 3.0]}, {0: 2.3, 1: 5.0})

    def tearDown(self):
        pass

    def test_constructor(self):
        with self.assertRaises(ValueError):
            self.neuron_layer = NeuronLayer('hola', 2, {0: [2.0, 3.0], 1: [1.0, 3.0]}, {0: 2.3, 1: 5.0})
        with self.assertRaises(ValueError):
            self.neuron_layer = NeuronLayer(2.0, 2, {0: [2.0, 3.0], 1: [1.0, 3.0]}, {0: 2.3, 1: 5.0})
        with self.assertRaises(ValueError):
            self.neuron_layer = NeuronLayer(2, 2, {0: [2.0, 3.0], 1: [1.0, 3.0], 2: [1.0, 3.0]}, {0: 2.3, 1: 5.0})
        with self.assertRaises(ValueError):
            self.neuron_layer = NeuronLayer(2, 2, 'hola', {0: 2.3, 1: 5.0})
        with self.assertRaises(ValueError):
            self.neuron_layer = NeuronLayer(2, 2, {0: [2.0, 3.0], 1: [1.0, 3.0, 4.0]}, {0: 2.3, 1: 5.0})
        with self.assertRaises(ValueError):
            self.neuron_layer = NeuronLayer(2, 2, {0: [2.0, 3.0], 1: [1.0, 3.0]}, {0: 2.3, 1: 5.0, 2: 1.0})


if __name__ == '__main__':
    unittest.main()

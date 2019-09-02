import unittest
from neural_network import NeuralNetwork


class TestNeuralNetwork(unittest.TestCase):

    def setUp(self):
        self.neural_net = NeuralNetwork(1, [2],
                                        2, 2, {0: {0: [1.2, 3.1], 1: [2.2, 3.0]}, 1: {0: [1.2, 3.1], 1: [2.2, 3.0]}},
                                        {0: {0: 1.0, 1: 3.0}, 1: {0: 3.1, 1: 2.2}})

    def tearDown(self):
        pass

    def test_constructor(self):
        with self.assertRaises(ValueError):
            self.neuron_net = NeuralNetwork(1.0, [2],
                                        2, 2, {0: {0: [1.2, 3.1], 1: [2.2, 3.0]}, 1: {0: [1.2, 3.1], 1: [2.2, 3.0]}},
                                        {0: {0: 1.0, 1: 3.0}, 1: {0: 3.1, 1: 2.2}})
        with self.assertRaises(ValueError):
            self.neuron_net = NeuralNetwork('hola', [2],
                                        2, 2, {0: {0: [1.2, 3.1], 1: [2.2, 3.0]}, 1: {0: [1.2, 3.1], 1: [2.2, 3.0]}},
                                        {0: {0: 1.0, 1: 3.0}, 1: {0: 3.1, 1: 2.2}})
        with self.assertRaises(ValueError):
            self.neuron_net = NeuralNetwork(1, 3.0,
                                        2, 2, {0: {0: [1.2, 3.1], 1: [2.2, 3.0]}, 1: {0: [1.2, 3.1], 1: [2.2, 3.0]}},
                                        {0: {0: 1.0, 1: 3.0}, 1: {0: 3.1, 1: 2.2}})
        with self.assertRaises(ValueError):
            self.neuron_net = NeuralNetwork(1, [2.0],
                                        2, 2, {0: {0: [1.2, 3.1], 1: [2.2, 3.0]}, 1: {0: [1.2, 3.1], 1: [2.2, 3.0]}},
                                        {0: {0: 1.0, 1: 3.0}, 1: {0: 3.1, 1: 2.2}})
        with self.assertRaises(ValueError):
            self.neuron_net = NeuralNetwork(1, 'hola',
                                        2, 2, {0: {0: [1.2, 3.1], 1: [2.2, 3.0]}, 1: {0: [1.2, 3.1], 1: [2.2, 3.0]}},
                                        {0: {0: 1.0, 1: 3.0}, 1: {0: 3.1, 1: 2.2}})
        with self.assertRaises(ValueError):
            self.neuron_net = NeuralNetwork(1, [2],
                                        5, 2, {0: {0: [1.2, 3.1], 1: [2.2, 3.0]}, 1: {0: [1.2, 3.1], 1: [2.2, 3.0]}},
                                        {0: {0: 1.0, 1: 3.0}, 1: {0: 3.1, 1: 2.2}})
        with self.assertRaises(ValueError):
            self.neuron_net = NeuralNetwork(1, [2],
                                        2.0, 2, {0: {0: [1.2, 3.1], 1: [2.2, 3.0]}, 1: {0: [1.2, 3.1], 1: [2.2, 3.0]}},
                                        {0: {0: 1.0, 1: 3.0}, 1: {0: 3.1, 1: 2.2}})
        with self.assertRaises(ValueError):
            self.neuron_net = NeuralNetwork(1, [2],
                                        2, 2.0, {0: {0: [1.2, 3.1], 1: [2.2, 3.0]}, 1: {0: [1.2, 3.1], 1: [2.2, 3.0]}},
                                        {0: {0: 1.0, 1: 3.0}, 1: {0: 3.1, 1: 2.2}})
        with self.assertRaises(ValueError):
            self.neuron_net = NeuralNetwork(1, [2],
                                        2, 2, {0: {0: [1.2, 3.1], 1: [2.2, 3.0], 2: [2.2, 3.0]}, 1: {0: [1.2, 3.1], 1: [2.2, 3.0]}},
                                        {0: {0: 1.0, 1: 3.0}, 1: {0: 3.1, 1: 2.2}})
        with self.assertRaises(ValueError):
            self.neuron_net = NeuralNetwork(1, [2],
                                            2, 2,
                                            'hola',
                                            {0: {0: 1.0, 1: 3.0}, 1: {0: 3.1, 1: 2.2}})
        with self.assertRaises(ValueError):
            self.neuron_net = NeuralNetwork(1, [2],
                                            2, 2,
                                            {0: {0: [1.2, 3.1], 1: [2.2, 3.0]}, 1: {0: [1.2, 3.1], 1: [2.2, 3.0]}},
                                            {0: {0: 1.0, 1: 3.0, 2: 9.0}, 1: {0: 3.1, 1: 2.2}})
        with self.assertRaises(ValueError):
            self.neuron_net = NeuralNetwork(1, [2],
                                            2, 2,
                                            {0: {0: [1.2, 3.1], 1: [2.2, 3.0]}, 1: {0: [1.2, 3.1], 1: [2.2, 3.0]}},
                                            'hola')



if __name__ == '__main__':
    unittest.main()

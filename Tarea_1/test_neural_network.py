import unittest
from neural_network import NeuralNetwork


class TestNeuralNetwork(unittest.TestCase):

    def setUp(self):
        self.neural_net = NeuralNetwork(5, [2.0, 3.0, 5.5, 4.0, 1.1], 2.3)

    def tearDown(self):
        pass

    def test_constructor(self):
        with self.assertRaises(ValueError):
            self.neuron_net = NeuralNetwork(5, [2.0, 3.0, 5.5, 4.0, 1.1], 2.3)

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

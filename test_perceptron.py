import unittest
from perceptron import Perceptron


class TestPerceptron(unittest.TestCase):

    def setUp(self):
        self.per_1 = Perceptron([1, 0], 5)

    def tearDown(self):
        pass

    def test_get_weights(self):
        self.assertEqual(self.per_1.get_weights(), [1, 0])

    def test_get_bias(self):
        self.assertEqual(self.per_1.get_bias(), 5)

    def test_set_weights(self):
        self.per_1.set_weights([-1, 3])
        self.assertEqual(self.per_1.get_weights(), [-1, 3])

    def test_set_bias(self):
        self.per_1.set_bias(-3)
        self.assertEqual(self.per_1.get_bias(), -3)

    def test_feed(self):
        self.assertEqual(self.per_1.feed([-5, 2]), 0)
        with self.assertRaises(ValueError):
            self.per_1.feed([2, 5, 3])


if __name__ == '__main__':
    unittest.main()

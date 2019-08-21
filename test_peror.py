import unittest
from perceptron import PerOr


class TestPerOr(unittest.TestCase):

    def setUp(self):
        self.peror_1 = PerOr()

    def tearDown(self):
        pass

    def test_get_weights(self):
        self.assertEqual(self.peror_1.get_weights(), [2, 2])

    def test_get_bias(self):
        self.assertEqual(self.peror_1.get_bias(), -1)

    def test_set_weights(self):
        self.peror_1.set_weights([-1, 3])
        self.assertEqual(self.peror_1.get_weights(), [-1, 3])

    def test_set_bias(self):
        self.peror_1.set_bias(-3)
        self.assertEqual(self.peror_1.get_bias(), -3)

    def test_feed(self):
        self.assertEqual(self.peror_1.feed([1, 1]), 1)
        self.assertEqual(self.peror_1.feed([1, 0]), 1)
        self.assertEqual(self.peror_1.feed([0, 1]), 1)
        self.assertEqual(self.peror_1.feed([0, 0]), 0)


if __name__ == '__main__':
    unittest.main()

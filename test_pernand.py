import unittest
from perceptron import PerNAnd


class TestPerNAnd(unittest.TestCase):

    def setUp(self):
        self.pernand_1 = PerNAnd()

    def tearDown(self):
        pass

    def test_get_weights(self):
        self.assertEqual(self.pernand_1.get_weights(), [-2, -2])

    def test_get_bias(self):
        self.assertEqual(self.pernand_1.get_bias(), 3)

    def test_set_weights(self):
        self.pernand_1.set_weights([-1, 3])
        self.assertEqual(self.pernand_1.get_weights(), [-1, 3])

    def test_set_bias(self):
        self.pernand_1.set_bias(-3)
        self.assertEqual(self.pernand_1.get_bias(), -3)

    def test_feed(self):
        self.assertEqual(self.pernand_1.feed([1, 1]), 0)
        self.assertEqual(self.pernand_1.feed([1, 0]), 1)
        self.assertEqual(self.pernand_1.feed([0, 1]), 1)
        self.assertEqual(self.pernand_1.feed([0, 0]), 1)


if __name__ == '__main__':
    unittest.main()

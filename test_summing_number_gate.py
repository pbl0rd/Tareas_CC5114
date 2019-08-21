import unittest
from summing_number_gate import SummingNumberGate


class TestSummingNumberGate(unittest.TestCase):

    def setUp(self):
        self.sum_gate_1 = SummingNumberGate()

    def tearDown(self):
        pass

    def test_sum_bits(self):
        self.assertEqual(self.sum_gate_1.sum_bits([1, 1]), (0, 1))
        self.assertEqual(self.sum_gate_1.sum_bits([1, 0]), (1, 0))
        self.assertEqual(self.sum_gate_1.sum_bits([0, 1]), (1, 0))
        self.assertEqual(self.sum_gate_1.sum_bits([0, 0]), (0, 0))


if __name__ == '__main__':
    unittest.main()

import unittest
from step import Step


class TestStep(unittest.TestCase):

    def test_apply(self):
        a = Step()
        self.assertEqual(a.apply(1), 1)
        self.assertEqual(a.apply(-1), 0)

    def test_derivative(self):
        a = Step()
        self.assertEqual(a.derivative(1), 0)
        self.assertEqual(a.derivative(-1), 0)
        with self.assertRaises(ValueError):
            a.derivative(0)


if __name__ == '__main__':
    unittest.main()
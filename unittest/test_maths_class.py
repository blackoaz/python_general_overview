from sum_method import Mathematics
import unittest

class TestMathematics(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(Mathematics().sum(1, 2), 3)
        self.assertNotEqual(Mathematics().sum(1, 2), 4)

    def test_subtract(self):
        self.assertEqual(Mathematics().subtract(2, 1), 1)

    def test_multiply(self):
        self.assertEqual(Mathematics().multiply(2, 3), 6)
    


if __name__ == '__main__':
    unittest.main(verbosity=2)
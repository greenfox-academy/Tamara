import unittest
from fibonacci import fibonacci

class FibonacciTest(unittest.TestCase):
    def test_number_one(self):
        test_number = fibonacci(1)
        self.assertEqual(test_number, 1)

    def test_number_two(self):
        test_number = fibonacci(2)
        self.assertEqual(test_number, 1)

    def test_number_null(self):
        test_number = fibonacci(0)
        self.assertEqual(test_number, 0)
if __name__ == '__main__':
    unittest.main()
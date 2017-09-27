import unittest
from Sum import Summa_number

class SummaTest(unittest.TestCase):
    def test_empty_numbers(self):
        test_number = Summa_number()
        self.assertFalse(test_number.add_number([]))

    def test_one_number(self):
        test_number = Summa_number()
        self.assertEqual(test_number.add_number([6]), 6)        

    def test_add_number(self):
        test_number = Summa_number()
        self.assertEqual(test_number.add_number([1, 3, 6]), 10)
       
    def test_with_null(self):
        test_number = Summa_number()
        self.assertEqual(test_number.add_number([0]), 0)
        

if __name__ == '__main__':
    unittest.main()
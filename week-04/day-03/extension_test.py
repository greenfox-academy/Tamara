import unittest
import extension

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_2_and_3_is_5(self):
        self.assertEqual(extension.add(2, 3), 5)

    def test_add_4_and_1_is_5(self):
        self.assertEqual(extension.add(4, 1), 5)

    def test_add_minus_number(self):
        self.assertEqual(extension.add(-5, 1), -4)

    def test_add_positive_number(self):
        self.assertEqual(extension.add(5, 1), 6)

    def test_max_of_three_first(self):
        self.assertEqual(extension.max_of_three(5, 4, 3), 5)

    def test_max_of_three_third(self):
        self.assertEqual(extension.max_of_three(3, 4, 5), 5)

    def test_max_of_three_second(self):
        self.assertEqual(extension.max_of_three(3, 9, 8), 9)

    def test_median_four(self):
        self.assertEqual(extension.median([7,5,3,5]), 5)

    def test_median_five(self):
        self.assertEqual(extension.median([1,2,3,4,5]), 3)

    def test_median_even(self):
        self.assertEqual(extension.median([7,5,3,5,1,2]), 4)

    def test_is_vovel_a(self):
        self.assertTrue(extension.is_vovel('a'))

    def test_is_vovel_u(self):
        self.assertTrue(extension.is_vovel('u'))

    def test_is_vovel_e(self):
        self.assertTrue(extension.is_vovel('é'))

    def test_translate_bemutatkozik(self):
        self.assertEqual(extension.translate('bemutatkozik'), 'bevemuvutavatkovozivik')

    def test_translate_kolbice(self):
        self.assertEqual(extension.translate('kolbice'), 'kovolbiviceve')

if __name__ == '__main__':
    unittest.main()
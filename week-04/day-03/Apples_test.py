import unittest
from Apples import Apple

class AppleTest(unittest.TestCase):
    def test_get_apple(self):
        test_apple = Apple()
        self.assertEqual(test_apple.get_apple(), "apple")

    def test_apple_instance(self):
        self.assertFalse("melon")


if __name__ == '__main__':
    unittest.main()
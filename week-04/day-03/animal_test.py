import unittest
from animal import Animal


animal = Animal()

class AnimalFeedTest(unittest.TestCase):
    
    def test_eating(self):
        animal.eat()
        self.assertEqual(animal.hunger, 49)

    def test_drink(self):
        animal.drink()
        self.assertEqual(animal.thirst, 49)
    
    def test_play(self):
        animal.play()
        self.assertEqual(animal.hunger, 50)
        self.assertEqual(animal.thirst, 50)

if __name__ == '__main__':
    unittest.main()
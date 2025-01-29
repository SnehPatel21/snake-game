import unittest
from food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food()

    def test_initial_position(self):
        self.assertIsNotNone(self.food.position)

    def test_randomize_position(self):
        initial_position = self.food.position
        self.food.randomize_position()
        self.assertNotEqual(self.food.position, initial_position)

if __name__ == '__main__':
    unittest.main()

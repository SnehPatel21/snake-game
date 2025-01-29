import unittest
from snake import Snake

class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()

    def test_initial_length(self):
        self.assertEqual(len(self.snake.body), 1)

    def test_initial_position(self):
        self.assertEqual(self.snake.body[0], (0, 0))

    def test_move(self):
        self.snake.move()
        self.assertNotEqual(self.snake.body[0], (0, 0))

if __name__ == '__main__':
    unittest.main()

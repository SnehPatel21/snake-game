import unittest
from game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_initial_score(self):
        self.assertEqual(self.game.score, 0)

    def test_game_over(self):
        self.game.snake.body = [(0, 0), (0, 1), (0, 2)]
        self.game.snake.move()
        self.assertTrue(self.game.is_game_over())

if __name__ == '__main__':
    unittest.main()

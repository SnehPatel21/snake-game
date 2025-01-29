class GameState:
    def __init__(self):
        self.is_game_over = False
        self.score = 0

    def reset(self):
        self.is_game_over = False
        self.score = 0

    def game_over(self):
        self.is_game_over = True

    def increase_score(self, points=1):
        self.score += points

    def get_score(self):
        return self.score

    def is_over(self):
        return self.is_game_over

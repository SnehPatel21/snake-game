import pygame

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.high_score = self.load_high_score()
        self.font = pygame.font.Font(None, 36)
    
    def draw(self, screen):
        score_text = self.font.render(f'Score: {self.score} High Score: {self.high_score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
    
    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
    
    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except:
            return 0
    
    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

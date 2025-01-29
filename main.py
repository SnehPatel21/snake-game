import pygame
import random
import time
from scoreboard import Scoreboard

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLOCK_SIZE = 20
GAME_SPEED = 15

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

class Snake:
    def reset(self):
        self.positions = [(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)]
        self.direction = 'RIGHT'
        self.length = 1

    def __init__(self):
        self.reset()

    def move(self):
        current = self.positions[0]
        x, y = current

        if self.direction == 'UP':
            y -= BLOCK_SIZE
        elif self.direction == 'DOWN':
            y += BLOCK_SIZE
        elif self.direction == 'LEFT':
            x -= BLOCK_SIZE
        elif self.direction == 'RIGHT':
            x += BLOCK_SIZE

        self.positions.insert(0, (x, y))
        if len(self.positions) > self.length:
            self.positions.pop()

    def draw(self):
        for position in self.positions:
            rect = pygame.draw.rect(screen, GREEN, (position[0], position[1], BLOCK_SIZE, BLOCK_SIZE))
            # Debug: Print snake position
            print(f"Drawing snake at {position}")

class Food:
    def __init__(self):
        self.position = self.get_random_position()

    def get_random_position(self):
        x = random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
        y = random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
        return (x, y)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

def show_game_over(screen):
    font = pygame.font.Font(None, 74)
    text = font.render('Game Over!', True, WHITE)
    restart_font = pygame.font.Font(None, 36)
    restart_text = restart_font.render('Press SPACE to Restart', True, WHITE)
    
    screen.blit(text, (WINDOW_WIDTH//2 - text.get_width()//2, WINDOW_HEIGHT//2 - 50))
    screen.blit(restart_text, (WINDOW_WIDTH//2 - restart_text.get_width()//2, WINDOW_HEIGHT//2 + 50))
    pygame.display.flip()

def main():
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    game_over = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if not game_over:
                    if event.key == pygame.K_UP and snake.direction != 'DOWN':
                        snake.direction = 'UP'
                    elif event.key == pygame.K_DOWN and snake.direction != 'UP':
                        snake.direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                        snake.direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                        snake.direction = 'RIGHT'
                elif event.key == pygame.K_SPACE:  # Restart game
                    game_over = False
                    snake.reset()
                    scoreboard.reset()
                    food.position = food.get_random_position()

        if not game_over:
            # Move snake
            snake.move()

            # Check collision with food
            if snake.positions[0] == food.position:
                snake.length += 1
                food.position = food.get_random_position()
                scoreboard.increase_score()

            # Check collision with walls
            head_x, head_y = snake.positions[0]
            if (head_x < 0 or head_x >= WINDOW_WIDTH or 
                head_y < 0 or head_y >= WINDOW_HEIGHT):
                game_over = True

            # Check collision with self
            if snake.positions[0] in snake.positions[1:]:
                game_over = True

            # Draw everything
            screen.fill(BLACK)
            snake.draw()
            food.draw()
            scoreboard.draw(screen)
            pygame.display.flip()

        if game_over:
            show_game_over(screen)

        clock.tick(GAME_SPEED)

    pygame.quit()

if __name__ == "__main__":
    main()

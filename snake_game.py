import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Clock to control the frame rate
clock = pygame.time.Clock()

# Snake class
class Snake:
    def __init__(self):
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        self.grow = False

    def update(self):
        head_x, head_y = self.positions[0]
        if self.direction == pygame.K_UP:
            head_y -= CELL_SIZE
        elif self.direction == pygame.K_DOWN:
            head_y += CELL_SIZE
        elif self.direction == pygame.K_LEFT:
            head_x -= CELL_SIZE
        elif self.direction == pygame.K_RIGHT:
            head_x += CELL_SIZE

        new_head = (head_x, head_y)
        self.positions = [new_head] + self.positions[:-1]

        if self.grow:
            self.positions.append(self.positions[-1])
            self.grow = False

        if self.positions[0] == food.position:
            self.grow = True
            food.reposition(self.positions)

    def draw(self, surface):
        for position in self.positions:
            pygame.draw.rect(surface, GREEN, pygame.Rect(position[0], position[1], CELL_SIZE, CELL_SIZE))

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    self.direction = event.key

# Food class
class Food:
    def __init__(self):
        self.position = (random.randint(0, (SCREEN_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                         random.randint(0, (SCREEN_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, pygame.Rect(self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

    def reposition(self, snake_positions):
        while True:
            new_position = (random.randint(0, (SCREEN_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                            random.randint(0, (SCREEN_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
            if new_position not in snake_positions:
                self.position = new_position
                break

# Main game loop
def main():
    global food
    snake = Snake()
    food = Food()

    while True:
        snake.handle_keys()
        snake.update()

        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        pygame.display.update()
        pygame.display.flip()  # Ensure the display is updated

        clock.tick(10)

if __name__ == '__main__':
    main()

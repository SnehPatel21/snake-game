import pygame
import sys

# This file serves as the main entry point for the game. It will initialize the game and start the game loop.

# Initialize the game
def init_game():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Snake Game')
    return screen

# Main game loop
def main():
    screen = init_game()
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip()  # Update the full display surface to the screen
        clock.tick(60)  # Limit the frame rate to 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
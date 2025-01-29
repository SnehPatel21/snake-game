# Snake Game

A classic Snake game implemented in Python using Pygame.

![{4B3208CF-3181-456A-90C8-6E5A40D979C0}](https://github.com/user-attachments/assets/80ba2f90-8527-4d42-9c65-b378f16422fd)


## Features

- Classic snake gameplay
- Score tracking
- Persistent high score
- Smooth controls

## Setup

1. Make sure you have Python installed
2. Install required dependencies:
```bash
pip install -r requirements.txt
```
3. Run the game:
```bash
python main.py
```

## Controls

- Arrow keys to move the snake
- ESC to quit the game

## How to Play

Eat the food to grow and increase your score. Avoid hitting the walls or yourself!

## Project Structure
- `src/`: Contains the source code for the game.
  - `core/`: Core game mechanics and rules.
  - `entities/`: Definitions for game entities like the snake and food.
  - `ui/`: User interface components for rendering and display.
  - `utils/`: Utility functions for input handling and score tracking.
  - `game.py`: Main entry point for the game.

- `tests/`: Contains test files to ensure functionality of game components.

- `docs/`: Documentation related to the project, including setup instructions and gameplay details.

## Installation Instructions

1. Clone the repository:
    ```sh
    git clone https://github.com/SnehPatel21/snake-game.git
    ```
2. Navigate to the project directory:
    ```sh
    cd snake-game
    ```
3. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
5. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Development Setup

1. Follow the installation instructions to set up the environment.
2. Install additional development dependencies:
    ```sh
    pip install -r dev-requirements.txt
    ```
3. Run the tests to ensure everything is working:
    ```sh
    pytest
    ```

## Basic API Documentation

### `main.py`

- `main()`: Starts the game.

### `snake.py`

- `class Snake`: Represents the snake in the game.
    - `move()`: Moves the snake in the current direction.
    - `grow()`: Increases the length of the snake.
    - `check_collision()`: Checks if the snake has collided with itself or the walls.

### `food.py`

- `class Food`: Represents the food in the game.
    - `spawn()`: Places the food at a random location on the screen.

## Running the Project

To run the game, execute the following command:

```sh
python src/game.py
```

## Testing

To run the tests, execute the following command:

```sh
pytest
```

Enjoy playing the Snake game! Feel free to modify and enhance the game as you wish.

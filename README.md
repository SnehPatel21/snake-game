# Snake Game

## Overview
This project is a simple implementation of the classic Snake game. The game is designed to be easy to understand and modify, making it a great starting point for learning game development.

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

## How to Play

1. Run the game:
    ```sh
    python main.py
    ```
2. Use the arrow keys to control the snake.
3. Eat the food to grow longer.
4. Avoid running into the walls or the snake's own body.

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

## Usage
To run the game, execute the following command:

```bash
python src/game.py
```

Enjoy playing the Snake game! Feel free to modify and enhance the game as you wish.
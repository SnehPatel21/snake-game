class Snake:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def move(self):
        # Logic to move the snake in the current direction
        pass

    def change_direction(self, new_direction):
        # Logic to change the direction of the snake
        self.direction = new_direction

class MovementController:
    def __init__(self, snake):
        self.snake = snake
        self.direction = (0, 1)  # Default direction: moving right

    def set_direction(self, new_direction):
        self.direction = new_direction

    def move(self):
        head_x, head_y = self.snake.head
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        self.snake.body.insert(0, new_head)
        self.snake.body.pop()
        self.snake.head = new_head

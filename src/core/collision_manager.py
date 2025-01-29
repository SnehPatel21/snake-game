class CollisionManager:
    def __init__(self, snake, food, boundaries):
        self.snake = snake
        self.food = food
        self.boundaries = boundaries

    def check_collision_with_food(self):
        return self.snake.head == self.food.position

    def check_collision_with_boundaries(self):
        head_x, head_y = self.snake.head
        min_x, min_y, max_x, max_y = self.boundaries
        return not (min_x <= head_x <= max_x and min_y <= head_y <= max_y)

    def check_collision_with_self(self):
        return self.snake.head in self.snake.body[1:]

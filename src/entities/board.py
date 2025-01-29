class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def is_within_bounds(self, position):
        # Logic to check if a position is within the board boundaries
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

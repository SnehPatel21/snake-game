class Food:
    def __init__(self, position):
        self.position = position

    def relocate(self, new_position):
        # Logic to relocate the food to a new position
        self.position = new_position

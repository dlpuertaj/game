

class Character:

    def __init__(self, x, y, width, height):
        self.x_position = x
        self.y_position = y
        self.width = width
        self.height = height

    def get_position(self):
        return self.position
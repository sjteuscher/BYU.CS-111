from Grid import Grid


class Particle:
    def __init__(self, grid, x=0, y=0):
        self.grid = grid
        self.x = x
        self.y = y
        self.grid.set(x, y, self)

    def __str__(self):
        return f'{type(self).__name__}({self.x},{self.y})'

    def physics(self):
        raise NotImplementedError

    def move(self):
        new_positions = self.physics()
        self.grid.set(self.x, self.y, None)
        (self.x, self.y) = new_positions
        self.grid.set(self.x, self.y, self)




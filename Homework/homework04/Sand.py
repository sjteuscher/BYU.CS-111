from Particle import Particle
from Grid import Grid


class Sand(Particle):

    def is_move_ok(self, x, y):
        try:
            if self.y == y - 1 and self.grid.get(x, y) is None:
                return True
            elif (self.grid.get(x, y - 1) is None and self.grid.get(x, y) is None) and (self.x == x - 1 and self.y == y - 1):
                return True
            elif (self.grid.get(x, y-1) is None and self.grid.get(x, y) is None) and (self.x == x - 1 and self.y == y - 1):
                return True
        except IndexError:
            return False
        # if self.grid is None and self.y == y - 1:
        #     return True
        # elif (self.grid.grid[y][x] is None and self.grid.grid[y - 1][x] is None) and (
        #         self.x == x + 1 and self.y == y - 1):
        #     return True
        # elif (self.grid.grid[y][x] is None and self.grid.grid[y - 1][x] is None) and (
        #         self.x == x - 1 and self.y == y - 1):
        #     return True
        # elif not Grid.in_bounds(self.grid.grid, x, y):
        #     return False
        # else:
        #     return False

    def physics(self):
        # if Sand.is_move_ok(self, 0, 0) and self.y == y-1
        if Sand.is_move_ok(self, self.x, self.y + 1):
            test_tuple = (self.x, self.y + 1)
            return test_tuple
        elif Sand.is_move_ok(self, self.x - 1, self.y + 1):
            test_tuple = (self.x - 1, self.y + 1)
            return test_tuple
        elif Sand.is_move_ok(self, self.x + 1, self.y + 1):
            test_tuple = (self.x + 1, self.y + 1)
            return test_tuple
        else:
            return None

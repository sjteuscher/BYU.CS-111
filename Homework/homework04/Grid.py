from copy import deepcopy


class Grid:
    """
    2D grid with (x, y) int indexed internal storage
    Has .width .height size properties
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = []
        for i in range(height):
            self.grid.append([])
            for j in range(width):
                self.grid[i].append(None)

    def __str__(self):
        return f'Grid({self.height}, {self.width}, first = {self.grid[0][0]})'

    def __repr__(self):
        return f'Grid.build({self.grid})'

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.grid == other.grid
        elif isinstance(other, list):
            return self.grid == other
        return False

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def get(self, x, y):
        if not self.in_bounds(x, y):
            raise IndexError
        return self.grid[y][x]

    def set(self, x, y, value):
        if not self.in_bounds(x, y):
            raise IndexError
        self.grid[y][x] = value

    @staticmethod
    def check_list_malformed(lists):
        if not isinstance(lists, list):
            raise ValueError("This is not a list object")
        if not len(lists) > 0:
            raise ValueError("List must have at least one element")
        for lst in lists:
            if not isinstance(lst, list):
                raise ValueError("Each element of lst must be a list object")
            i = 0
            if not len(lists[i]) == len(lst):
                raise ValueError("Each element of lst must have the same length")

    @staticmethod
    def build(lst):
        Grid.check_list_malformed(lst)
        height = len(lst)
        width = len(lst[0])
        grid_object = Grid(width, height)
        grid_object.grid = deepcopy(lst)
        return grid_object

    def copy(self):
        return deepcopy(self)



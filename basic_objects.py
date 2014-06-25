import random


class Map:
    def __init__(self, width, length):
        self.game_map = {}
        self._width = width
        self._length = length

        for y in range(1, length + 1):
            for x in range(1, width + 1):
                self.game_map[(x, y)] = 0

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    def __getitem__(self, position):
        return self.game_map[(position[0], position[1])]

    def __setitem__(self, position, value):
        self.game_map[(position[0], position[1])] = value

    def recursive_division_maze_generation(self, left, right, top, bottom):
        if bottom - top <= 0 or right - left <= 0:
            return

        if (bottom-top) - (right-left) >= 0:
            y = random.randrange(top, bottom + 1)
            while y % 2 != 0:
                y = random.randrange(top, bottom + 1)
            for x in range(left, right + 1):
                self.game_map[(x, y)] = 1
            path = random.randrange(left, right + 1) 
            while path % 2 != 0:
                path = random.randrange(left, right + 1) 
            self.game_map[(path, y)] = 0
            self.recursive_division_maze_generation(left, right, top, y - 1)
            self.recursive_division_maze_generation(left, right, y + 1, bottom)
        else:
            x = random.randrange(left, right + 1)
            while x % 2 == 0:
                x = random.randrange(left, right + 1)
            for y in range(top, bottom + 1):
                self.game_map[(x, y)] = 1
            path = random.randrange(top, bottom + 1) 
            while path % 2 == 0:
                path = random.randrange(top, bottom + 1) 
            self.game_map[(x, path)] = 0
            self.recursive_division_maze_generation(left, x - 1, top, bottom)
            self.recursive_division_maze_generation(x + 1, right, top, bottom)


class MovingObject:
    def __init__(self, maze):
        self._x = 1
        self._y = 1
        maze[1, 1] = 2
        maze[maze.width, maze.length] = 3
        self._maze = maze

    @property
    def maze(self):
        return self._maze

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def move_left(self):
        if self._x != 1 and self._maze[self._x - 1, self._y] != 1:
            self._maze[self._x, self._y] = 0
            self._x -= 1
            self._maze[self._x, self._y] = 2

    def move_right(self):
        not_out_of_range = self._x != self._maze.width
        if not_out_of_range and self._maze[self._x + 1, self._y] != 1:
            self._maze[self._x, self._y] = 0
            self._x += 1
            if self._maze[self._x, self._y] != 3:
                self._maze[self._x, self._y] = 2

    def move_up(self):
        if self._y != 1 and self._maze[self._x, self._y - 1] != 1:
            self._maze[self._x, self._y] = 0
            self._y -= 1
            self._maze[self._x, self._y] = 2

    def move_down(self):
        not_out_of_range = self._y != self._maze.length
        if not_out_of_range and self._maze[self._x, self._y + 1] != 1:
            self._maze[self._x, self._y] = 0
            self._y += 1
            if self._maze[self._x, self._y] != 3:
                self._maze[self._x, self._y] = 2

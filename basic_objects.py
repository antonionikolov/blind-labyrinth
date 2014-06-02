from random import randint


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
        #print(left, " ", right, " ", top, " ", bottom)
        if bottom - top <= 1 or right - left <= 1:
            return

        if (bottom-top) - (right-left) >= 0:
            y = randint(top, bottom)
            for x in range(left + 1, right):
                self.game_map[(x, y)] = 1
            path = randint(left, right)
            self.game_map[(path, y)] = 0
            self.recursive_division_maze_generation(left, right, top, y - 1)
            self.recursive_division_maze_generation(left, right, y + 1, bottom)
        else:
            x = randint(left, right)
            for y in range(top + 1, bottom):
                self.game_map[(x, y)] = 1
            path = randint(top, bottom)
            self.game_map[(x, path)] = 0
            self.recursive_division_maze_generation(left, x - 1, top, bottom)
            self.recursive_division_maze_generation(x + 1, right, top, bottom)


class MovingObject:
    def __init__(self, map):
        self._x = 1
        self._y = 1
        map[1, 1] = 2
        self._map = map

    @property
    def map(self):
        return self._map

    @map.setter
    def map(self, other_map):
        self._map = other_map

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._y = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def move_left(self):
        if self._x != 1 and self._map[self._x - 1, self._y] != 1:
            self._map[self._x, self._y] = 0
            self._x -= 1
            self._map[self._x, self._y] = 2

    def move_right(self):
        if self._x != self._map.width and self._map[self._x + 1, self._y] != 1:
            self._map[self._x, self._y] = 0
            self._x += 1
            self._map[self._x, self._y] = 2

    def move_up(self):
        if self._y != 1 and self._map[self._x, self._y - 1] != 1:
            self._map[self._x, self._y] = 0
            self._y -= 1
            self._map[self._x, self._y] = 2

    def move_down(self):
        if self._y != self._map.length and self._map[self._x, self._y + 1] != 1:
            self._map[self._x, self._y] = 0
            self._y += 1
            self._map[self._x, self._y] = 2
            
#a = Map(10, 10)
#a.recursive_division_maze_generation(1, 10, 1, 10)
#b = MovingObject(a)
#for y in range(1, 10):
#    print("")
#    for x in range (1, 10):
#        print(a[x, y], end=" ")

import unittest
from basic_objects import MovingObject, Map


def breadth_first_search(maze):
    checked = [[False] * (maze.width+1) for _ in range(maze.length + 1)]
    bfs_queue = [(1, 1)]
    checked[1][1] = True

    while bfs_queue:
        current = bfs_queue.pop(0)
        if current[0] == maze.width and current[1] == maze.length:
            return True

        if current[0] != 1:
            if maze[current[0] - 1, current[1]] != 1:
                if not checked[current[0] - 1][current[1]]:
                    bfs_queue.append((current[0] - 1, current[1]))
                    checked[current[0] - 1][current[1]] = True
        if current[0] != maze.width:
            if maze[current[0] + 1, current[1]] != 1:
                if not checked[current[0] + 1][current[1]]:
                    bfs_queue.append((current[0] + 1, current[1]))
                    checked[current[0] + 1][current[1]] = True
        if current[1] != 1:
            if maze[current[0], current[1] - 1] != 1:
                if not checked[current[0]][current[1] - 1]:
                    bfs_queue.append((current[0], current[1] - 1))
                    checked[current[0]][current[1] - 1] = True
        if current[1] != maze.length:
            if maze[current[0], current[1] + 1] != 1:
                if not checked[current[0]][current[1] + 1]:
                    bfs_queue.append((current[0], current[1] + 1))
                    checked[current[0]][current[1] + 1] = True

    return False


class MapTest(unittest.TestCase):
    def test_property(self):
        maze = Map(10, 10)
        self.assertEqual(maze.width, 10)
        self.assertEqual(maze.length, 10)

    def test_set_and_get_item(self):
        maze = Map(10, 10)
        test = all(maze[i, j] == 0 for i in range(1, 11) for j in range(1, 11))
        self.assertEqual(test, True)

        for i in range(11):
            for j in range(11):
                maze[i, j] = 1
        test = all(maze[i, j] == 1 for i in range(1, 11) for j in range(1, 11))
        self.assertEqual(test, True)

    def test_if_the_random_generated_labyrinth_have_a_solution(self):
        for i in range(1, 100):
            maze = Map(i, i)
            maze.recursive_division_maze_generation(1, i, 1, i)
            maze[maze.width, maze.length] = 0
            self.assertEqual(breadth_first_search(maze), True)


class MovingObjectTest(unittest.TestCase):
    def test_property(self):
        moving_thing = MovingObject(Map(20, 20))
        self.assertEqual(type(moving_thing.maze), Map)

        self.assertEqual(moving_thing.x, 1)
        self.assertEqual(moving_thing.y, 1)

        self.assertEqual(moving_thing.maze[20, 20], 3)

    def test_movement(self):
        moving_thing = MovingObject(Map(20, 20))

        moving_thing.move_left()
        self.assertEqual(moving_thing.x, 1)
        self.assertEqual(moving_thing.y, 1)

        moving_thing.move_up()
        self.assertEqual(moving_thing.x, 1)
        self.assertEqual(moving_thing.y, 1)
 
        for i in range(1, 20):
            moving_thing.move_right()
            self.assertEqual(moving_thing.x, i + 1)
            self.assertEqual(moving_thing.y, 1)

        moving_thing.move_right()
        self.assertEqual(moving_thing.x, 20)
        self.assertEqual(moving_thing.y, 1)

        moving_thing.move_up()
        self.assertEqual(moving_thing.x, 20)
        self.assertEqual(moving_thing.y, 1)

        for i in range(1, 20):
            moving_thing.move_down()
            self.assertEqual(moving_thing.x, 20)
            self.assertEqual(moving_thing.y, i + 1)

        moving_thing.move_right()
        self.assertEqual(moving_thing.x, 20)
        self.assertEqual(moving_thing.y, 20)

        moving_thing.move_down()
        self.assertEqual(moving_thing.x, 20)
        self.assertEqual(moving_thing.y, 20)

        for i in reversed(range(1, 20)):
            moving_thing.move_left()
            self.assertEqual(moving_thing.x, i)
            self.assertEqual(moving_thing.y, 20)

        moving_thing.move_left()
        self.assertEqual(moving_thing.x, 1)
        self.assertEqual(moving_thing.y, 20)

        moving_thing.move_down()
        self.assertEqual(moving_thing.x, 1)
        self.assertEqual(moving_thing.y, 20)

        for i in reversed(range(1, 20)):
            moving_thing.move_up()
            self.assertEqual(moving_thing.x, 1)
            self.assertEqual(moving_thing.y, i)


if __name__ == '__main__':
    unittest.main()
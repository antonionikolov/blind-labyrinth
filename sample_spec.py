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

        test = all(maze[i, j] == 0 for i in range(1, 11) for j in range(1, 11))
        self.assertEqual(test, True)

        for i in range(11):
            for j in range(11):
                maze[i, j] = 1
        test = all(maze[i, j] == 1 for i in range(1, 11) for j in range(1, 11))
        self.assertEqual(test, True)

        for i in range(1, 100):
            maze = Map(i, i)
            maze.recursive_division_maze_generation(1, i, 1, i)
            maze[maze.width, maze.length] = 0;
            self.assertEqual(breadth_first_search(maze), True)


if __name__ == '__main__':
    unittest.main()
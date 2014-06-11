import re
from get_character import _Getch, _GetchUnix, _GetchWindows
from basic_objects import MovingObject, Map
import os

print("Enter the width of the labyrinth: ", end="")
width = input()
print("Enter the length of the labyrinth: ", end="")
length = input()
os.system("clear")

maze  = Map(int(width), int(length))
maze.recursive_division_maze_generation(1, int(width), 1, int(length))
object = MovingObject(maze)
command = _Getch()
getch = ""

while getch != 'q' and object.maze[object.x, object.y] != 3:
    for x in range(1, int(width) + 3):
        print("#", end=" ")
    for y in range(1, int(length) + 1):              
        print("")
        print("#", end=" ")
        for x in range(1, int(width) + 1):
            if abs(object.x - x) < 2 and abs(object.y - y) < 2:
                if object.maze[x, y] == 0:
                    print(" ", end=" ")
                elif object.maze[x, y] == 1:
                    print("#", end=" ")
                elif object.maze[x, y] == 2:
                    print("@", end=" ")
                elif object.maze[x, y] == 3:
                    print("X", end=" ")
            elif object.maze[x, y] == 3:
                print("X", end=" ")
            else:
                print(" ", end=" ")
        print("#", end=" ")
    print("")
    for x in range(1, int(width) + 3):
        print("#", end=" ")

    print("\n\nUse 'w', 'a', 's', 'd' to move and 'q' to quit.")
    getch = command()
    if getch == 'w':
        object.move_up()
    elif getch == 's':
        object.move_down()
    elif getch == 'a':
        object.move_left()
    elif getch == 'd':
        object.move_right()

    os.system("clear")

if getch != 'q':
    print("CONGRATULATIONS! YOU WIN!")

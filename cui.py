import re
from get_character import _Getch, _GetchUnix, _GetchWindows
from basic_objects import MovingObject, Map
import os

print("Enter the width of the labyrinth: ", end="")
width = input()
print("Enter the length of the labyrinth: ", end="")
length = input()
os.system("clear")

temp  = Map(int(width), int(length))
temp.recursive_division_maze_generation(1, int(width), 1, int(length))
object = MovingObject(temp)
command = _Getch()
getch = ""

while getch != 'q':
    for y in range(1, int(length) + 1):              
        print("")
        for x in range(1, int(width) + 1):
            print(object.map[x, y], end=" ")

    print("\n")
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

#! python 3

import boards


def find_loc(x1, y1, x2, y2):
    if {'x': x1, 'y': y1} not in boards.listDict or {'x': x2, 'y': y2} not in boards.listDict:
        print(-1)
    elif x1 > x2 or y1 > y2:
        print(-1)
    else:
        print(x2 - x1 + y2 - y1)


coordinates = input()
[x1, y1, x2, y2] = coordinates.split(" ")
find_loc(int(x1), int(y1), int(x2), int(y2))

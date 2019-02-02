#! python3

import boards


def onLine(x1, y1, x2, y2, x, y):
    if {'x':x1,'y':y1} not in boards.listDict or {'x':x2,'y':y2} not in boards.listDict:
        return False

    elif x == x1:
        if y == y1:
            return True
        else:
            return False

    elif x == x2:
        if y == y2:
            return True
        else:
            return False

    else:
        slope1 = abs((y1 - y) / (x1 - x))
        slope2 = abs((y2 - y) / (x2 - x))

        if slope1 == slope2:
            return True
        else:
            return False


def find_total(x1, y1, x2, y2):
    count = 0
    for student in boards.listDict:
        x = student['x']
        y = student['y']
        # print(student.keys())
        # print(student.values())
        if onLine(x1, y1, x2, y2, x, y):
            count = count + 1

    print(count)


coordinates = input()
[x1, y1, x2, y2] = coordinates.split(" ")
# print(boards.listDict)
find_total(int(x1), int(y1), int(x2), int(y2))

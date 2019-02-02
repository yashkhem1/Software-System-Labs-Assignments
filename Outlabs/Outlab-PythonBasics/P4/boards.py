#! python3

listDict = []

file = open('students.txt', 'r')

# f __name__ == "__main__":
counter = 0
for line in file:
    if counter == 0:
        numStudents = int(line)
    elif counter > 0 and counter <= numStudents:
        [x, y] = line.split(" ")
        listDict.append({'x':int(x),'y':int(y)})
    else:
        break

    counter = counter + 1

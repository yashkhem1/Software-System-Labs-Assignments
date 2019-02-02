#! python3

snakesList = []


class snake:
    def __init__(self, name, length, venom):
        self.name = name
        self.length = length
        self.venom = venom


def findByVenom(venom):
    for snake in snakesList:
        if snake.venom == venom:
            print(snake.name)


def findByLength(length):
    for snake in snakesList:
        if snake.length == length:
            print(snake.name)


if __name__ == "__main__":
    counter = 0
    numSnakes = 0
    numQueries = 0
    snakeFile = open('snakes.txt', 'r')
    for line in snakeFile:
        if counter == 0:
            numSnakes = int(line)
        elif (counter > 0) and (counter <= numSnakes):
            [name, length, venom] = line.split(" ")
            Snake = snake(name, int(length), int(venom))
            snakesList.append(Snake)
        elif counter == numSnakes + 1:
            numQueries = int(line)
        elif counter > numSnakes + 1 and counter <= numSnakes + 1 + numQueries:
            [command, number] = line.split(" ")
            if command == 'V':
                findByVenom(int(number))
            else:
                findByLength(int(number))
        else:
            break

        counter = counter + 1

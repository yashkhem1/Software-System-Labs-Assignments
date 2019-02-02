import sys
import random
import pickle
import string


def fill_choice():
    numList = random.sample(range(1, 5000), 100)
    stringList = []
    #''.join(random.choice(string.ascii_uppercase) for i in range(random.randint(1,9)))
    for i in range(100):
        while(True):
            randString = ''.join(random.choice(string.ascii_uppercase) for i in range(random.randint(3, 6)))
            if randString not in stringList:
                stringList.append(randString)
                break

    choiceList = []
    for i in range(100):
        choiceList.append((numList[i], stringList[i]))

    with open('new_int.p', 'wb') as file:
        pickle.dump(choiceList, file)
        # print(len(choiceList))


def ask_choice():
    filename = sys.argv[1]
    try:
        choices = []
        with open(filename, 'rb') as file:
            choices = pickle.load(file)
        while(True):
            num = int(input('Enter Number: '))
            try:
                if num in range(5000, 7001):
                    break
                else:
                    raise ValueError("Enter a number between 5000 and 7000")

            except ValueError as e:
                print(e)

        found = 0

        for i in range(100):
            for j in range(100):
                if i == j:
                    break
                elif choices[i][0] + choices[j][0] == num:
                    found = 1
                    print(choices[i][1] + ' ' + str(choices[i][0]) + ' ' + choices[j][1] + ' ' + str(choices[j][0]))
                    break

            if found == 1:
                break

        if found != 1:
            found2 = 0
            for i in range(100):
                for j in range(100):
                    if i == j:
                        break
                    elif choices[i][0] + choices[j][0] < num:
                        found2 = 1
                        print(choices[i][1] + ' ' + str(choices[i][0]) + ' ' + choices[j][1] + ' ' + str(choices[j][0]))
                        break

                if found2 == 1:
                    break

        print(choices)

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        fill_choice()
    elif len(sys.argv) == 2:
        ask_choice()

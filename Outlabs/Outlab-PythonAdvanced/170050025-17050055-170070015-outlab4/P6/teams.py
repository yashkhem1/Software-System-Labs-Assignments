import random
import json


def makeTeams(teams, players):
    try:
        x = players / teams
        if teams > players:
            raise ValueError("Enter the numbers again")
        if (players % teams) != 0:
            raise ValueError("Enter the value again with teams=" + str(teams)
                             + "and players=" + str(players - 1))

    except TypeError:
        raise TypeError("Format is incorrect")
    except ZeroDivisionError:
        raise ZeroDivisionError("Number of teams cannot be zero")


# counter=0
p = 0


def createDatabase():
    teams = {}
    jersey = list(range(1, 1001))
    random.shuffle(jersey)
    k = 0
    for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']:
        dic = {}
        y = list(range(1, 11))
        random.shuffle(y)
        for j in range(10):
            dic[jersey[10 * k + j]] = y[j]
        teams[i] = dic
        k = k + 1
    t = json.dumps(teams, indent=4)
    w = open("players.json", "w")
    w.write(t)


def getMinLoyal(doosri, apniTeam, playerID):
    prev = 0
    mini = 10000
    naya_player = 0
    for a in p[doosri]:
        b = p[doosri][a]
        mini = min(mini, b)
        if(mini != prev):
            prev = mini
            naya_player = a
    del p[doosri][naya_player]
    p[doosri][playerID] = p[apniTeam][playerID]  # loyalty equated
    del p[apniTeam][playerID]
    p[apniTeam][naya_player] = mini


    #print(doosri," ", naya_player," ", mini)
# dic=[{"a":"b"},{"c":"d"}]
# print(dic[0])
TeamNames = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}


def main():
    counter = 0
    with open("transfer.txt")as f:
        lines = f.readlines()
        for line in lines:
            l = line.split()
            # print(l)
            b = 0
            try:
                if l[0] not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']:
                    raise ValueError("Try another transfer(Wrong team name)")
                for a in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']:
                    if l[1] in p[a].keys():
                        b = a
                if b == 0:
                    raise ValueError("Try another transfer(Wrong player number)")
                if p[b][l[1]] > 7:
                    raise ValueError("Try another transfer(Player too loyal)")
                elif b == l[0]:
                    raise ValueError("Try another transfer(Player already in the team)")
            except ValueError as e:
                print(e)
            else:
                counter += 1
                print("Transfer Complete")
                getMinLoyal(l[0], b, l[1])
    print(counter)


if __name__ == '__main__':
    createDatabase()
    p = open("players.json")
    p = json.load(p)
    main()
    t = json.dumps(p, indent=4)
    w = open("players.json", "w")
    w.write(t)

import json

with open('infinity_stones.json') as f:
    data = json.load(f)
    w = open("infinity_stones.csv", "w")
    w.write("Stone Name ,Stone Color,Containment Unit \n")
    for stones in data["Infinity Stones"]:
        w.write(stones["Stone Name"] + "," + stones["Stone Color"] + "," + stones["Containment Unit"] + "\n")
    w.close()

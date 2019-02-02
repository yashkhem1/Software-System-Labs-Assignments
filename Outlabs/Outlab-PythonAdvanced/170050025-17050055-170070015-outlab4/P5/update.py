import json
with open("infinity_stones.json") as f:
    data = json.load(f)
    w = open("update_stones.json", "w")
    y = []
    for samaan in data["Infinity Stones"]:
        samaan["Containment Unit"] = "Infinity Gauntlet"
        y.append(samaan)  # json.dumps(samaan,indent=4)
        # print(y)

    dic = {"Infinty Stones": y}
    var = json.dumps(dic, indent=4)
    w.write(var)
    w.close()

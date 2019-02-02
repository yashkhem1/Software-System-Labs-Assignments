class Menu():
    def __init__(self, list_of_items):
        self.menuitems = list_of_items

    def __len__(self):
        return(len(self.menuitems))

    def __str__(self):
        ret = ""
        for item in self.menuitems:
            ret += "Item: "
            ret += item.name
            ret += ", Cost: "
            ret += str(item.cost)
            ret += ", Rating: "
            ret += str(item.rating)
            ret += "\n"
        return(ret)

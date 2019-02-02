class MenuItem():
    def __init__(self, name='', cost=0, rating=0):
        self.name = name
        self.cost = cost
        self.rating = '{0:.6f}'.format(rating)

    def __eq__(self, item2):
        return self.name == item2.name and self.cost == item2.cost and self.rating == item2.rating

    def __str__(self):
        return "Item: " + self.name + ", Cost: " + str(self.cost) + ", Rating: " + str(self.rating)

    def __lt__(self, other):
        if self.rating != other.rating:
            return self.rating < other.rating
        else:
            return self.cost < other.cost

    def __hash__(self):
        return hash((self.name, self.cost, self.rating))

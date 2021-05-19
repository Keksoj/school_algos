import math

class Town:
    """
    I can't deal with those dictionaries so I make an equivalent object to
    ( Paris, {'x': 29, 'y': 15, 'r': 4, 'l': {'Mantes-la-Jolie': 59, 'Versailles': 21}})
    """

    def __init__(self, name, x, y, r, l):
        """
        r is the radius of the town, its size
        l is a dictionary of neigboring towns
        """
        self.name = name
        self.x = x
        self.y = y
        self.r = r
        # get only the names from the neigboring towns
        self.neighbors = []
        for name in l.keys():
            self.neighbors.append(name)

    def distance_to(self, other_town):
        """
        returns the distance between self and another instance of Town
        """
        return math.sqrt((self.x - other_town.x)*(self.x - other_town.x) +
                         (self.y - other_town.y)*(self.y - other_town.y))

    def display(self):
        print(self.name,
              "x: ", self.x,
              "yx: ", self.y,
              "neigbors: ", self.neighbors)

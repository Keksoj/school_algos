from Path import Path
from Town import Town


class Graph:
    """
    This class contains a dictionary of towns,
    so as to implement the travelling salesman problem.
    """

    def __init__(self, number_of_towns, verbose):
        """
        Constructs a graph with add many towns to the graph
        args:
            howManyTowns: the number of towns to add
        properties:
            town_dictonary: a dictionary, for instance {'paris', (0,0,false)}
        """
        self.number_of_towns = number_of_towns

        # creates a dictionary of all towns
        town_dictionary = {}
        for _ in range(number_of_towns):
            town = Town()
            town_dictionary[town.name] = town
        self.town_dictionary = town_dictionary

        if verbose:
            self.display_town_dictonary()

    def display_town_dictonary(self):
        print("town_dictonary:")
        for town in self.town_dictionary.values():
            town.display()

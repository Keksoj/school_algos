from Graph import Graph
from time import perf_counter_ns
from Path import Path
from Town import Town
from pprint import pprint
import random
import string
import copy
import time
import csv
import math


class NearestTownGraph(Graph):
    """
    This child class of Graph finds a path by choosing the nearest town as the next
    """

    def __init__(self, number_of_towns, verbose):
        """
        Constructs a graph with add many towns to the graph.
        Additional properties:
            path: the one path being constructed
        """
        super().__init__(number_of_towns, verbose)
        self.name = "nearest_town"
        self.path = Path()

    def solve(self, verbose):
        """
        This procedure calls the hop_from() method recursively
        """
        # we must clear the path from previous iterations
        self.path = Path()

        if verbose:
            print("\n============ NEAREST TOWN ALGORITHM  ============")

        first_town = list(self.town_dictionary.values())[0]
        self.path.append_town(first_town, verbose)
        if verbose:
            print("We start from")
            first_town.display()

        self.hop_from(
            first_town,
            verbose
        )

        if verbose:
            print("\n=============  RESULT ====================")
            print("The path we found (and surely not the shortest):")
            self.path.display()

    def hop_from(self, current_town, verbose):
        """
        This recursive function finds the nearest town to hop to and adds it to
        the path.
        Args:
            current_town: the current visited town
            unexplored_towns: the grah's town dictionary
            verbose: you know what it is
        """
        #  delete the current town from the dictionary
        del self.town_dictionary[current_town.name]

        # find the closest town. Let us assume it is the first in the graph
        next_town = list(self.town_dictionary.values())[0]


        # compare the distance to every town in the graph to find the shortest one
        for town in self.town_dictionary.values():
            if verbose:
                print("We consider as next_town:")
                town.display()
                print("    distant of:", current_town.distance_to(town))
            if current_town.distance_to(town) < current_town.distance_to(next_town):
                next_town = town
        if verbose:
            print("The nearest town is:")
            next_town.display()
            print("dictionary length:", len(self.town_dictionary))

        # add it to the path, delete it from the dictionary
        self.path.append_town(next_town, verbose)

        # if the graph is not depleted, call the function recursively
        if len(self.town_dictionary) != 1:
            self.hop_from(next_town, verbose)

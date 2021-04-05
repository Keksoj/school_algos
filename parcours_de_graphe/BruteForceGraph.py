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


class BruteForceGraph(Graph):
    """
    This child class of Graph is designed to brute force all possible paths
    """

    def __init__(self, number_of_towns, verbose):
        """
        Constructs a graph with add many towns to the graph
        Additional properties
            current_path: the path currently exlpored
            all_paths: a list of possible paths

        """
        super().__init__(number_of_towns, verbose)
        self.current_path = Path()
        self.name = "brute_force"
        self.all_paths = []
        if verbose:
            self.display_town_dictonary()

    def solve(self, verbose):
        """
        This procedures explores all possible paths
            verbose: boolean
        """

        explored_paths = []
        self.explore_all_paths(
            copy.deepcopy(list(self.town_dictionary.values())[0]),
            copy.deepcopy(self.town_dictionary),
            copy.deepcopy(self.current_path),
            explored_paths,
            verbose
        )
        self.all_paths = explored_paths
        if verbose:
            self.display_all_paths()

        print(
            "\nWe have found", len(
                self.all_paths), "possible paths to link the",
            len(self.town_dictionary), "towns.",
        )

        # sort out the shortest path
        # this is ugly because
        #     AttributeError: 'float' object has no attribute 'length'
        shortest_path = self.all_paths[0]
        shortest_path_length = shortest_path.get_length()
        for path in self.all_paths:
            if path.get_length() < shortest_path_length:
                shortest_path = path
                shortest_path_length = shortest_path.get_length()

        print("Here is the shortest path:")
        shortest_path.display()

    def explore_all_paths(
        self,
        town_to_explore,
        current_town_dictionary,
        current_path,
        list_of_explored_paths,
        verbose
    ):
        """
        this recursive function increments its
            exploredPath: the list of towns already explored
        with the 
            town_to_explore: a Town object
        and doesn't forget to remove it from self.town_dictionary
        If there are no towns to explore left, the explored path is added to
            list_of_explored_paths: a list of possible paths
        If there are still towns to explore, the function calls itself 
        several times over on each of the towns that are left to explore
        with the same town index it is about to explore next.
            verbose: boolean. You know the drill
        """
        if verbose:
            print("\n========= NEW RECURSION===========")
            print("we explore this town:")
            print(town_to_explore.display())

        # Remove the town from the unexplored towns
        del current_town_dictionary[town_to_explore.name]
        if verbose:
            print("unexplored towns:")
            for key in current_town_dictionary.keys():
                print("            ", key)

        # append the town to the path
        current_path.append_town(town_to_explore, verbose)
        if verbose:
            print("The current path:")
            current_path.display()
            print(len(current_town_dictionary))
            print("length of the remaining town dictionary:",
                  len(current_town_dictionary))

        # if all towns are unexplored, add the path to the list
        if (len(current_town_dictionary) == 0):
            list_of_explored_paths.append(current_path)
            if verbose:
                print("we are done with this exploration! Path is:")
                current_path.display()
            return

        # If they are still towns to explore,
        if (len(current_town_dictionary) != 0):

            # iterate over the unexplored towns
            for town_key in current_town_dictionary.keys():
                if verbose:
                    print("next town to explore:", town_key)

                # deepcopy the list of unexplored towns and the current path
                town_dictionary_copy = copy.deepcopy(current_town_dictionary)
                current_path_copy = copy.deepcopy(current_path)

                # call the function recursively
                self.explore_all_paths(
                    town_dictionary_copy[town_key],
                    town_dictionary_copy,
                    current_path_copy,
                    list_of_explored_paths,
                    verbose
                )

    def display_all_paths(self):
        print("\n=========== ALL PATHS FOUND =============")
        for i in range(len(self.all_paths)):
            print("\npath_number", i)
            self.all_paths[i].display()

import random
import string
import copy
import time
import csv
import math
from pprint import pprint
from Town import Town
from Path import Path
from time import perf_counter_ns


class Graph:

    def __init__(self, howManyTowns, verbose):
        """
        Constructs a graph with add many towns to the graph
        args:
            howManyTowns: the number of towns to add
        properties:
            town_dictonary: a dictionary, for instance {'paris', (0,0,false)}
            all_paths: a list of possible paths
        """
        self.number_of_towns = howManyTowns
        town_dictionary = {}
        for _ in range(howManyTowns):
            town = Town()
            town_dictionary[town.name] = town
        self.town_dictionary = town_dictionary
        self.all_paths = []
        self.current_path = Path()
        self.current_path.display()
        if verbose:
            self.display_town_dictonary()

    def measure_exploring_time(self, verbose_path_finding, verbose_measuring):
        """
        This procedures analizes how much computing time is needed to explore all paths
        for a graph with n towns
            verbose: boolean
        """

        explored_paths = []
        startTime = perf_counter_ns()

        # get the first town to start with
        first_town = list(self.town_dictionary.values())[0]

        self.explore_all_paths(
            first_town,
            self.town_dictionary,
            self.current_path,
            explored_paths,
            verbose_path_finding
        )
        self.all_paths = explored_paths
        self.display_all_paths()

        elapsedTime = perf_counter_ns() - startTime
        elapsedTimeLog = math.log(elapsedTime)

        print(
            "The graph with", len(self.town_dictionary), "towns.",
            "it took", elapsedTime, "nanoseconds:", elapsedTime/1000000000, "seconds")
        data = [len(self.town_dictionary), elapsedTime, elapsedTimeLog]
        return data

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
        print
        if (len(current_town_dictionary) == 0):
            list_of_explored_paths.append(current_path)
            if verbose:
                print("we are done with this exploration! Path is:")
                current_path.display()
            return

        if (len(current_town_dictionary) != 0):
            # Of all the unexploredGraph,
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

    def display_town_dictonary(self):
        print("town_dictonary:")
        for town in self.town_dictionary.values():
            town.display()

    def display_all_paths(self):
        for i in range(len(self.all_paths) - 1):
            print("\npath_number", i)
            self.all_paths[i].display()
from time import perf_counter_ns
from Path import Path
from Town import Town
import csv
import math


class Graph:
    """
    This class contains a dictionary of towns,
    so as to implement the travelling salesman problem.
    """

    def __init__(self, number_of_towns, verbose):
        """
        Constructs a graph with so many towns to the graph
        args:
            number_of_towns: the number of towns to add
            verbose: talk to me
        properties:
            town_dictonary: a dictionary, for instance {'paris', (0,0,false)}
        """
        # populate the graph with towns
        self.populate(number_of_towns)
        self.name = "Please_give_me_a_name"
        if verbose:
            self.display_town_dictonary()

    def populate(self, number_of_towns):
        # creates a dictionary of all towns
        town_dictionary = {}
        for _ in range(number_of_towns):
            town = Town()
            town_dictionary[town.name] = town
        self.town_dictionary = town_dictionary

    def display_town_dictonary(self):
        print("town_dictonary:")
        for town in self.town_dictionary.values():
            town.display()

    def solve(self, verbose):
        print("Please implement this method for all children of Graph")

    def test(self, graph_name, verbose):
        """
        Use this method on any child instance of Graph. 
        The child instances must implement those methods:
            __init__(self, number_of_towns, verbose)
            solve(self, verbose)
        """

        # open a file and write the header inside
        with open('./benchmark_{0}.csv'.format(self.name), 'w') as file:
            writer = csv.writer(file)
            row = ['number_of_towns', 'elapsed_time', 'elapsed_time_log']
            writer.writerow(row)
            print(row)

            keep_testing = True
            number_of_towns = 3
            while (keep_testing):

                # sets the counter
                startTime = perf_counter_ns()

                # instantiate a graph and solve it for a given number of towns
                self.populate(number_of_towns)
                self.solve(verbose)

                # measure elapsed time
                elapsedTime = perf_counter_ns() - startTime
                elapsedTimeLog = math.log(elapsedTime)

                # write into the file
                data = [number_of_towns, elapsedTime, elapsedTimeLog]
                writer.writerow(data)
                print(data)

                number_of_towns += 1

                # don't go of testing if an iteration takes more than 10 seconds
                if elapsedTime > 10000000000 or number_of_towns > 500:
                    keep_testing = False

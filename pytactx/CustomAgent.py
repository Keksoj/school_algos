from pytactx import Agent
from Town import Town
from Path import Path
import random
import copy


class CustomAgent(Agent):
    """
    My custom class that inherits Agent but has additionnal methods
    """

    def __init__(self, nom="", username="", password="", arene="", server="", prompt=True, verbose=False):
        name = "Emmanuel-"+randomString()
        super().__init__(name, username, password,
                         arene, server, prompt, verbose)
        self.map = {}
        self.current_path = []
        self.path = []

    def display_destinations_towns(self):
        for ville in self.jeu["destinations"].values():
            print(ville)

    def display_destinations(self):
        print(self.jeu["destinations"])

    def go_to(self, town):
        """
        town is a string
        """
        while (self.derniereDestinationAtteinte != town):
            self.deplacerVers(town)
            self.actualiser()

    def extract_map(self):
        """
        self.jeu["destinations"] is a dictionary like:
            Paris: {'x': 29, 'y': 15, 'r': 4, 'l': {
                'Mantes-la-Jolie': 59, 'Versailles': 21}}
            Mantes-la-Jolie: {'x': 20, 'y': 13, 'r': 2, 'l': {'Paris': 59, 'Rouen': 83, 'Evreux': 45}}
            ...
        wich is a bit ugly. Lets convert those values into Town objects
        """
        map = {}
        print(self.jeu["destinations"])
        for town_name, town_properties_dict in self.jeu["destinations"].items():
            town_as_object = Town(
                town_name,
                town_properties_dict["x"],
                town_properties_dict["y"],
                town_properties_dict["r"],
                town_properties_dict["l"],
            )
            map[town_name] = town_as_object
        self.map = map
        print("the map:", self.map)
        print("the map as a list", list(self.map.values()))

    def find_simple_path(self):
        for town_name in self.map.keys():
            self.path.append(town_name)

    def follow_path(self):
        """
        you must have performed some path finding before calling this function
        """

        self.go_to(self.path.pop())
        for town in reversed(self.path):
            self.go_to(town)

    def find_best_path(self):
        """
        not finished yet
        brute_forces the map to find the shortest path
        """
        explored_paths = []
        self.explore_all_paths(
            copy.deepcopy(list(self.map.values())[0]),
            copy.deepcopy(self.map),
            copy.deepcopy(self.current_path),
            explored_paths,
            True
        )
        self.all_paths = explored_paths

        # sort out the shortest path
        # this is ugly because
        #     AttributeError: 'float' object has no attribute 'length'
        shortest_path = self.all_paths[0]
        shortest_path_length = shortest_path.get_length()
        for path in self.all_paths:
            if path.get_length() < shortest_path_length:
                shortest_path = path
                shortest_path_length = shortest_path.get_length()

        print("Here is the shortest path:", shortest_path)
        self.path = shortest_path

    def explore_all_paths(self,
                          town_to_explore, current_town_dictionary,
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
        # Remove the town from the unexplored towns
        del current_town_dictionary[town_to_explore.name]
        # append the town to the path
        current_path.append_town(town_to_explore, verbose)

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
            for town_key in town_to_explore["neighbors"]:
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


def randomString():
    """
    https://www.askpython.com/python/examples/generate-random-strings-in-python
    charNumber: a int
    """
    random_string = ""
    for _ in range(3):
        # Considering only upper and lowercase letters
        random_integer = random.randint(97, 97 + 26 - 1)
        flip_bit = random.randint(0, 1)
        # Convert to lowercase if the flip bit is on
        random_integer = random_integer - 32 if flip_bit == 1 else random_integer
        # Keep appending random characters using chr(x)
        random_string += (chr(random_integer))
    return random_string

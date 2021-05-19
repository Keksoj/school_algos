from pytactx import Agent
from Town import Town
import random


class CustomAgent(Agent):
    """
    My custom class that inherits Agent but has additionnal methods
    """

    def __init__(self, nom="", username="", password="", arene="", server="", prompt=True, verbose=False):
        name = "Emmanuel-"+randomString()
        super().__init__(name, username, password,
                         arene, server, prompt, verbose)
        self.map = {}

    def display_destinations(self):
        for ville in self.jeu["destinations"].values():
            print(ville)

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
            Paris: {'x': 29, 'y': 15, 'r': 4, 'l': {'Mantes-la-Jolie': 59, 'Versailles': 21}}
            Mantes-la-Jolie: {'x': 20, 'y': 13, 'r': 2, 'l': {'Paris': 59, 'Rouen': 83, 'Evreux': 45}}
            ...
        wich is a bit ugly. Lets convert those values into Town objects
        """
        map = {}
        for town_name, town_properties_dict in self.jeu["destinations"].values():
            town_as_object = Town(
                town_name,
                town_properties_dict[x],
                town_properties_dict[y],
                town_properties_dict[r],
                town_properties_dict[l],
            )
            map[town_name] = town_as_object


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

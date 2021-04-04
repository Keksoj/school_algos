import math
import random


class Town:
    def __init__(self):
        """
        Generates a random Town with random properties:
            name: string
            x: int
            y: int
        """
        self.name = randomString(10)
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)

    def distance_to(self, otherTown):
        return math.sqrt(((self.x-otherTown.x)**2)+(self.y-otherTown.y)**2)

    def one_line_display(self):
        print(self.name,
              "x:", self.x,
              "y:", self.y)

    def display(self):
        print("    name:", self.name,
              "    x:", self.x,
              "    y:", self.y)


def randomString(charNumber):
    """
    https://www.askpython.com/python/examples/generate-random-strings-in-python
    charNumber: a int
    """
    random_string = ""
    for _ in range(charNumber):
        # Considering only upper and lowercase letters
        random_integer = random.randint(97, 97 + 26 - 1)
        flip_bit = random.randint(0, 1)
        # Convert to lowercase if the flip bit is on
        random_integer = random_integer - 32 if flip_bit == 1 else random_integer
        # Keep appending random characters using chr(x)
        random_string += (chr(random_integer))
    return random_string

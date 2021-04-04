from Town import Town


class Path:
    def __init__(self):
        """
        args:
            first_town: instance of the Town class
        properties:
            towns: list of Town instances, in the order of the path
            length: total travel distance driven by the salesman
        """
        self.towns = []
        self.length = 0

    def append_town(self, town, verbose):
        # print("Let's append this town:")
        # town.display()
        if (len(self.towns) != 0):
            distance = self.towns[len(self.towns) - 1].distance_to(town)
            self.length += distance
            if verbose:
                print("distance to the town is:", distance)
        self.towns.append(town)

    def display(self):
        # print("I am a path, my towns are:")
        for town in self.towns:
            town.display()
        print("    path length:", self.length)

    def get_length(self):
        """
        This shouldn't be neccessary but writing
            path.length
        in the lib gives the error:
            AttributeError: 'float' object has no attribute 'length'
        """
        return self.length
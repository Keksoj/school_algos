import random, string, copy, time, csv, math
from time import perf_counter_ns

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
 

class Town:
    
    def __init__(self, name, x, y):
        """
        name: string
        x: int
        y: int
        visited: boolean
        """
        self.name = name
        self.x = x
        self.y = y
        
    def distanceTo(self, otherTown):
        return math.sqrt(((self.x-otherTown.x)**2)+(self.y-otherTown.y)**2)
    
    def display(self):
        print(self.name,self.x,self.y)


graph = {}

def populateGraphWithSoManyTowns(graph, howManyTowns):
    """
    add many towns to the graph
    graph: a dictionary, for instance {'paris', (0,0,false)}
    the boolean is wether the town was visited
    howManyTowns: the number of towns to add
    """
    for i in range(howManyTowns):
        townName = randomString(10)
        x = random.randint(0,10)
        y = random.randint(0,10)
        town = Town(townName, x, y)
        graph[town.name] = town
    
    
# populateGraphWithSoManyTowns(graph, 7)

# print(graph)





def exploreTowns(townToExplore, unexploredGraph, exploredPath, allPaths, verbose):
    """
    this recursive function increments its
        exploredPath: the list of towns already explored
    with the 
        townToExplore: a Town object
    and doesn't forget to remove it from the
        graph: a dictionary of Town objects
    If there are no towns to explore left, the explored path is added to
        allPaths: a list of possible paths
    If there are still towns to explore, the function calls itself 
    several times over on each of the towns that are left to explore
    with the same town index it is about to explore next.
        verbose: boolean. You know the drill
    """
    if verbose:
        print("========= NEW RECURSION===========")
        print("we explore this town:", townToExplore)
    
    
    # Remove the town from the unexplored towns
    del unexploredGraph[townToExplore]
    if verbose:
        print("unexplored towns:", unexploredGraph)
    
    # append the townToExplore to the path
    exploredPath.append(townToExplore)
    if verbose:
        print("explored path:", exploredPath)
    #time.sleep(0.5)

    # if no town is unexplored, add the path to the list
    if verbose:
        print(len(unexploredGraph))
    if (len(unexploredGraph) == 0):
        if verbose:
            print("we are done with this exploration! Path is:", exploredPath)
        allPaths.append(exploredPath)
    else:
        # Of all the unexploredGraph,
        for town in unexploredGraph.keys():
            if verbose:
                print("next town to explore:", town)
                                
            # deepcopy the list of unexplored towns (we need it as an argument)
            unexploredGraphCopy = copy.deepcopy(unexploredGraph)
            # deepcopy the path as well
            exploredPathCopy = copy.deepcopy(exploredPath)    
            
            # call the function recursively
            exploreTowns(town, unexploredGraphCopy, exploredPathCopy, allPaths, verbose)

    
#allPaths = []
#exploreTowns(list(graph)[0], graph, [], allPaths)
#for path in allPaths:
#    print(path)
#print("we have a total of", len(allPaths),"paths")

def measureTimeAndLengthForSoManyTowns(number):
    graph = {}
    
    populateGraphWithSoManyTowns(graph, number)
    allPaths = []
    startTime = perf_counter_ns()
    exploreTowns(list(graph)[0], graph, [], allPaths, False)
    elapsedTime = perf_counter_ns() - startTime
    elapsedTimeLog = math.log(elapsedTime)
    print(
        "We made a graph with", number, "towns.",
        "it took", elapsedTime, "nanoseconds:", elapsedTime/1000000000, "seconds")
    data = [number, elapsedTime, elapsedTimeLog]
    return data

header = ['number_of_towns', 'elapsed_time', 'elapsed_time_log']

with open('./times.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for i in range(2,11):
        data = measureTimeAndLengthForSoManyTowns(i)
        writer.writerow(data)


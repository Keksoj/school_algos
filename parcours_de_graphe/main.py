from Graph import Graph
from BruteForceGraph import BruteForceGraph
from NearestTownGraph import NearestTownGraph
import csv

# brute_force_graph = BruteForceGraph(3, True)
# brute_force_graph.test("brut_force", True)

nearest_town_graph = NearestTownGraph(150, False)
# nearest_town_graph.solve(True)
nearest_town_graph.test("nearest_town", False)
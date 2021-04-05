from Graph import Graph
from BruteForceGraph import BruteForceGraph
import csv

# header = ['number_of_towns', 'elapsed_time', 'elapsed_time_log']

# graph = BruteForceGraph(8, True)


# with open('./times.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(header)
#     data = graph.brute_force_resolution(
#         # debug path finding
#         False,
#         # debug time measuring
#         True
#     )
#     writer.writerow(data)

brute_force_graph = BruteForceGraph(3, True)
brute_force_graph.test("brut_force", True)

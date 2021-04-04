from lib import Graph
import csv

header = ['number_of_towns', 'elapsed_time', 'elapsed_time_log']

graph = Graph(8, True)


with open('./times.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    data = graph.brute_force_resolution(
        # debug path finding
        False,
        # debug time measuring
        True
    )
    writer.writerow(data)

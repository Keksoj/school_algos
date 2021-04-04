from lib import Graph
import csv

header = ['number_of_towns', 'elapsed_time', 'elapsed_time_log']

graph = Graph(3, True)


with open('./times.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    data = graph.measure_exploring_time(
        # debug path finding
        True,
        # debug time measuring
        True
    )
    writer.writerow(data)

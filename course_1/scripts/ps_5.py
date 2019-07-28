from IPython import embed
from copy import copy
import numpy


def dijkstra(paths, start):
    """
    Takes as input a list of undirected paths, a 'start' vertex and val for unconnected verteces.
    Returns shortest distance from start to all verteces (does not handle negative edges)
    """
    # Setup - only start explored. Distance of 0.
    len_paths = len(paths)
    unexplored = list(range(len_paths))
    distances = [100000000] * len_paths
    unexplored.pop(start)
    explored = [start]
    distances[start] = 0
    # Crossers = paths between explored and not.
    # Key = destination. Value = distance from start.
    crossers = {path[0]: path[1] for path in paths[start]}

    for _ in range(len_paths - 1):

        # Choose lowest value crosser
        chosen = min(crossers, key=crossers.get)

        # Also find its value

        chosen_val = crossers[chosen]

        # Remove from 'unexplored' and add to 'explored'.
        unexplored.remove(chosen)
        explored.append(chosen)

        # Update distance and remove entry from 'crossers'.
        distances[chosen] = crossers[chosen]
        del crossers[chosen]

        # Look at paths leading from newly included vertex.
        for path in paths[chosen]:

            # If path leads to unexplored other vertex.
            if path[0] in unexplored:

                # Add/update minimum distance for this vertex.
                path_val = chosen_val + path[1]
                if path[0] in crossers:
                    crossers[path[0]] = min(path_val, crossers[path[0]])
                else:
                    crossers[path[0]] = path_val
    return distances


# Data processing
TXT_FILE = open("dijkstraData.txt", "r")
INPUT_STRING = TXT_FILE.read()
ROWS = INPUT_STRING.splitlines()
PATHS = [row.split("\t") for row in ROWS]
PATHS = [[[int(v) for v in path.split(",")] for path in row[1:-1]] for row in PATHS]
PATHS = [[[path[0] - 1, path[1]] for path in vertex] for vertex in PATHS]


# Core algorithm
DISTANCES = dijkstra(paths=PATHS, start=0)

# Answers
for num in [6, 36, 58, 81, 98, 114, 132, 164, 187, 196]:
    print("number {} - distance {}".format(num, DISTANCES[num]))

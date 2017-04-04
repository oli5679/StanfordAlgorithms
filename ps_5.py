from IPython import embed
from copy import copy

def dijkstra(paths,start,unexplored_val):
    """
    Takes as input a list of undirected paths, a 'start' vertex and val for unconnected verteces. 
    Returns shortest distance from start to all verteces (does not neccessarily handle negative edges)
    """
    #setup - only start explored. Distance of 0.
    len_paths = len(paths)
    unexplored = list(range(len_paths))
    distances = [unexplored_val] * len_paths
    unexplored.pop(start)
    explored = [start]
    distances[start] = 0
    #crossers = paths between explored and not. Key = destination. Value = distance from start.
    crossers = {path[0]:path[1] for path in paths[start]}
    for x in range(len_paths -1):
        #Choose lowest value crosser
        chosen = min(crossers, key=crossers.get)
        #Also find its value
        chosen_val = crossers[chosen]
        #Remove from 'unexplored' and add to 'explored'.
        unexplored.remove(chosen)
        explored.append(chosen)
        #Update distance and remove entry from 'crossers'.
        distances[chosen] = crossers[chosen]
        del crossers[chosen]
        #Look at paths leading from newly included vertex.
        for path in paths[chosen]:
            #If path leads to unexplored other vertex.
            if path[0] in unexplored:
                #add/update minimum distance for this vertex.
                path_val = chosen_val + path[1]
                if path[0] in crossers:
                    crossers[path[0]] = min(path_val, crossers[path[0]])
                else:
                    crossers[path[0]] = path_val
    return distances

#data processing
TXT_FILE = open("dijkstraData.txt", "r")
INPUT_STRING = TXT_FILE.read()
ROWS = INPUT_STRING.splitlines()
PATHS = [row.split('\t') for row in ROWS]
PATHS = [[[int(v) for v in path.split(',')] for path in row[1:-1]] for row in PATHS]
PATHS = [[[path[0]-1, path[1]] for path in vertex] for vertex in PATHS]

#core algorithm
DISTANCES = dijkstra(PATHS, 0, 100000)

#answers
print(DISTANCES[6])
print(DISTANCES[36])
print(DISTANCES[58])
print(DISTANCES[81])
print(DISTANCES[98])
print(DISTANCES[114])
print(DISTANCES[132])
print(DISTANCES[164])
print(DISTANCES[187])
print(DISTANCES[196])
embed()

"""
In this programming problem you'll code up Dijkstra's shortest-path algorithm.

Download the following text file (Right click and select "Save As..."): dijkstraData.txt

The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200. Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge. For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. The next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length 8200. The rest of the pairs of this row indicate the other vertices adjacent to vertex 6 and the lengths of the corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex, and to compute the shortest-path distances between 1 and every other vertex of the graph. If there is no path between a vertex  and vertex 1, we'll define the shortest-path distance between 1 and  to be 1000000.

You should report the shortest-path distances to the following ten vertices, in order: 7,37,59,82,99,115,133,165,188,197. Enter the shortest-path distances using the fields below for each of the vertices.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward  time implementation of Dijkstra's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing the heap-based version. Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.

"""

from IPython import embed
from copy import copy
import numpy

INPUT_PATH = "../data/dijkstraData.txt"


class Dijkstra:
    def __init__(self, paths, start):
        self.paths = paths
        self.start = start
        """
        Takes as input a list of undirected paths, a 'start' vertex and val for unconnected verteces.
        Returns shortest distance from start to all verteces (does not handle negative edges)
        """
        # Setup - only start explored. Distance of 0.
        self.len_paths = len(paths)
        self.unexplored = list(range(self.len_paths))
        self.distances = [100000000] * self.len_paths
        self.unexplored.pop(start)
        self.explored = [start]
        self.distances[start] = 0

        # Crossers = paths between explored and not.
        # Key = destination. Value = distance from start.
        self.crossers = {path[0]: path[1] for path in paths[start]}

    def solve(self):
        for _ in range(self.len_paths - 1):
            chosen, chosen_val = self.choose_min_crosser()
            self.update_paths(chosen, chosen_val)

        return self.distances

    def choose_min_crosser(self):
        # Choose lowest value crosser
        chosen = min(self.crossers, key=self.crossers.get)

        # Also find its value
        chosen_val = self.crossers[chosen]

        # Remove from 'unexplored' and add to 'explored'.
        self.unexplored.remove(chosen)
        self.explored.append(chosen)

        # Update distance and remove entry from 'crossers'.
        self.distances[chosen] = self.crossers[chosen]
        del self.crossers[chosen]

        return chosen, chosen_val

    def update_paths(self, chosen, chosen_val):
        # Look at paths leading from newly included vertex.
        for path in self.paths[chosen]:

            # If path leads to unexplored other vertex.
            if path[0] in self.unexplored:

                # Add/update minimum distance for this vertex.
                path_val = chosen_val + path[1]
                if path[0] in self.crossers:
                    self.crossers[path[0]] = min(path_val, self.crossers[path[0]])
                else:
                    self.crossers[path[0]] = path_val


def parse_file(file_path):
    rows = open(file_path, "r").read().splitlines()
    paths = [row.split("\t") for row in rows]
    paths = [[[int(v) for v in path.split(",")] for path in row[1:-1]] for row in paths]
    return [[[path[0] - 1, path[1]] for path in vertex] for vertex in paths]


def main():
    paths = parse_file(INPUT_PATH)
    shortest_path_finder = Dijkstra(paths=paths, start=0)
    shortest_path_finder.solve()

    # Answers
    for num in [6, 36, 58, 81, 98, 114, 132, 164, 187, 196]:
        print(f"number {num+1} - distance {shortest_path_finder.distances[num]}")

    assert shortest_path_finder.distances[6] == 2599

    assert shortest_path_finder.distances[36] == 2610

    assert shortest_path_finder.distances[98] == 2367


if __name__ == "__main__":
    main()

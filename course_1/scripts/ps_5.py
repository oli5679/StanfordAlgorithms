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
                    self.crossers[path[0]] = min(
                        path_val, self.crossers[path[0]])
                else:
                    self.crossers[path[0]] = path_val


def parse_file(file_path):
    rows = open(file_path, "r").read().splitlines()
    paths = [row.split("\t") for row in rows]
    paths = [[[int(v) for v in path.split(",")]
              for path in row[1:-1]] for row in paths]
    return [[[path[0] - 1, path[1]] for path in vertex] for vertex in paths]


def main():
    paths = parse_file(INPUT_PATH)
    shortest_path_finder = Dijkstra(paths=paths, start=0)
    shortest_path_finder.solve()

    # Answers
    for num in [6, 36, 58, 81, 98, 114, 132, 164, 187, 196]:
        print(
            f"number {num+1} - distance {shortest_path_finder.distances[num]}")

    assert shortest_path_finder.distances[6] == 2599

    assert shortest_path_finder.distances[36] == 2610

    assert shortest_path_finder.distances[98] == 2367


if __name__ == "__main__":
    main()

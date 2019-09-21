import pandas as pd
import numpy as np
from tqdm import tqdm

INPUT_GRAPH_PATHS = ["../data/g1.txt", "../data/g2.txt", "../data/g3.txt"]


def parse_input(input_path):
    graph = pd.read_csv(input_path, sep=" ").reset_index()
    graph.columns = ["from", "to", "distance"]
    return graph


class FloydWarshall:
    """
    let dist be a |V| × |V| array of minimum distances initialized to ∞ (infinity)
    for each edge (u,v)
        dist[u][v] ← w(u,v)  // the weight of the edge (u,v)
    for each vertex v
        dist[v][v] ← 0
    for k from 1 to |V|
        for i from 1 to |V|
           for j from 1 to |V|
              if dist[i][j] > dist[i][k] + dist[k][j] 
                 dist[i][j] ← dist[i][k] + dist[k][j]
             end if
    """

    def __init__(self, edges):
        self.edges = edges
        self.vertices = edges["from"].append(edges["to"]).unique()
        self.num_vertices = len(self.vertices)
        self.distance_matrix = np.full((self.num_vertices, self.num_vertices), np.inf)
        np.fill_diagonal(self.distance_matrix, 0)

        for i, e in self.edges.iterrows():
            self.distance_matrix[e["from"] - 1, e["to"] - 1] = e["distance"]

    def solve(self):
        print(f"num vertices { self.num_vertices}")
        for k in tqdm(range(self.num_vertices)):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    if (
                        self.distance_matrix[i, j]
                        > self.distance_matrix[i, k] + self.distance_matrix[k, j]
                    ):
                        self.distance_matrix[i, j] = (
                            self.distance_matrix[i, k] + self.distance_matrix[k, j]
                        )
        # check for negative cost cycle
        if np.diagonal(self.distance_matrix).min() < 0:
            return np.full((self.num_vertices, self.num_vertices), np.inf)
        else:
            return self.distance_matrix


def main():
    min_val = 1e20
    for i, p in enumerate(INPUT_GRAPH_PATHS):
        print(f"graph number {i}")
        g = parse_input(p)
        fw = FloydWarshall(g)
        d = fw.solve().min()
        min_val = min(d, min_val)

    print(f"shortest shortest path {min_val}")


if __name__ == "__main__":
    main()

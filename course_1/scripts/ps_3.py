"""
The file contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1 to 200. The first column in the file represents the vertex label, and the particular row (other entries except the first column) tells all the vertices that the vertex is adjacent to. So for example, the  row looks like : "6	155	56	52	120 ......". This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc

Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above graph to compute the min cut. (HINT: Note that you'll have to figure out an implementation of edge contractions. Initially, you might want to do this naively, creating a new graph from the old every time there's an edge contraction. But you should also think about more efficient implementations.) (WARNING: As per the video lectures, please make sure to run the algorithm many times with different random seeds, and remember the smallest cut that you ever find.) Write your numeric answer in the space provided. So e.g., if your answer is 5, just type 5 in the space provided.
"""

from IPython import embed
import random
import time
import tqdm
from copy import deepcopy
from copy import copy
import math
import utils

INPUT_PATH = "../data/kargerMinCut.txt"


class Graph:
    def __init__(self, vertex_list, edges_list):
        self.vertex_list = vertex_list
        self.edges_list = edges_list


class RandomContraction(Graph):
    def random_cut(self):
        num_edges = len(self.edges_list)
        v0, v1 = self.edges_list.pop(random.randrange(num_edges))
        self.vertex_list.remove(v1)

        for i in range(num_edges - 1):
            if self.edges_list[i][0] == v1:
                self.edges_list[i][0] = v0
            if self.edges_list[i][1] == v1:
                self.edges_list[i][1] = v0

        self.edges_list = [e for e in self.edges_list if e[0] != e[1]]

    def random_contaction(self):
        while len(self.vertex_list) > 2:

            self.random_cut()

        return len(self.edges_list)


def karger_cut(vertex_list, edges_list):
    n = len(vertex_list)
    num_sims = int(math.ceil(n * n * math.log(n)))
    print(f"num sims {num_sims}")
    min_val = len(edges_list)
    for _ in tqdm.tqdm(range(n)):
        contract_sim = RandomContraction(deepcopy(vertex_list), deepcopy(edges_list))
        min_val = min(min_val, contract_sim.random_contaction())

    return min_val


def main():
    vertex_list, edges_list = utils.parse_graph_vertex_file(INPUT_PATH)
    min_cut = karger_cut(vertex_list, edges_list)
    print(f"minimum cut {min_cut}")

    assert min_cut == 17


if __name__ == "__main__":
    main()

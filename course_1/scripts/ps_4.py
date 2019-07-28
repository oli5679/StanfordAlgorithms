"""
The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). So for example, the  row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph.

Enter the sizes of the 5 largest SCCs in the given graph using the fields below, in decreasing order of sizes. So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, enter 500 in the first field, 400 in the second, 300 in the third, and so on. If your algorithm finds less than 5 SCCs, then enter 0 for the remaining fields. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then you enter 400, 300, and 100 in the first, second, and third fields, respectively, and 0 in the remaining 2 fields.

WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may have to manage memory carefully. The best way to do this depends on your programming language and environment, and we strongly suggest that you exchange tips for doing this on the discussion forums.

"""

from IPython import embed
import time
from tqdm import *
import numpy as np
import pandas as pd
import utils
from collections import defaultdict

INPUT_PATH = "../data/SCC.txt"


class Kosaraju:
    def __init__(self, vertex_list, edges_list):
        self.vertex_list = vertex_list
        self.edges_list = edges_list
        self.edges_list_rev = [[e[1], e[0]] for e in edges_list]
        self.finishing_time = 0
        self.finishing_times = [-1 for e in edges_list]
        self.ordering_forewards = vertex_list
        self.leaders = [-1 for e in edges_list]
        self.explored = -1

    def dfs_loop(self, vertex_list, edges_list, ordering):
        ordered_edges = [x for _, x in sorted(zip(ordering, edges_list))]
        self.explored = []
        for e in ordered_edges:
            if e not in self.explored:
                self.leader = -1
                self.finishing_times[e] = self.finishing_time
                self.dfs(vertex_list, edges_list, e)

    def dfs(self, vertex_list, edges_list, i):
        self.explored.append(i)
        if self.leader != -1:
            self.leader = i
        leaders[i] = self.leader


def standard_DFS():
    count = 0
    while len(UNEXPLORED) > 0:
        count += 1
        print(len(UNEXPLORED))
        recursive_search(UNEXPLORED[0])


def recursive_search(vertex):
    print(vertex)
    UNEXPLORED.remove(vertex)
    EXPLORED.append(vertex)
    for edge in VERTEX_LIST[vertex]:
        if EDGES[edge][0] in UNEXPLORED:
            recursive_search(EDGES[edge][0])
        if EDGES[edge][1] in UNEXPLORED:
            recursive_search(EDGES[edge][1])


def reverse_DFS_loop(graph):
    t = 0
    explored = []
    unexplored = graph
    while len(unexplored > 0):
        pass


def forwards_DFS_loop(graph):
    pass


def parse_input_file(file_path):
    split_rows = [row.split(" ") for row in open(file_path, "r").read().splitlines()]
    clean_rows = [
        [int(entry) - 1 for entry in row if entry is not ""] for row in split_rows
    ]
    vertex_dict = {t[0]: t[1:] for t in clean_rows}
    vertex_list = list(vertex_dict.keys())
    edges_list = []
    for key, value in vertex_dict.items():
        for neighbour in value:
            edges_list.append([key, neighbour])

    edges_list = [list(x) for x in set(tuple(x) for x in edges_list)]
    return vertex_list, edges_list


test_vertex = [[1, 0], [2, 1], [0, 2], [0, 3], [3, 4]]

test_edge = [0, 1, 2, 3, 4]


def main():
    vertex_list, edges_list = parse_input_file(INPUT_PATH)
    from IPython import embed

    embed()


if __name__ == "__main__":
    main()

INPUT_STRING = TXT_FILE.read()
ROWS = INPUT_STRING.splitlines()
EDGES = [row.split(" ") for row in ROWS]
EDGES = [[int(v) - 1 for v in row[:-1]] for row in EDGES]
VERTECES = [item for sublist in EDGES for item in sublist]
VERTEX_LIST = [[] for x in range(len(VERTECES))]
for i in range(len(EDGES)):
    EDGE = EDGES[i]
    VERTEX_LIST[EDGE[0]].append(i)
    VERTEX_LIST[EDGE[1]].append(i)
EXPLORED = []
UNEXPLORED = VERTECES
standard_DFS()

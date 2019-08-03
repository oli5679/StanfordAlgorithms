"""
The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). So for example, the  row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph.

Enter the sizes of the 5 largest SCCs in the given graph using the fields below, in decreasing order of sizes. So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, enter 500 in the first field, 400 in the second, 300 in the third, and so on. If your algorithm finds less than 5 SCCs, then enter 0 for the remaining fields. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then you enter 400, 300, and 100 in the first, second, and third fields, respectively, and 0 in the remaining 2 fields.

WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may have to manage memory carefully. The best way to do this depends on your programming language and environment, and we strongly suggest that you exchange tips for doing this on the discussion forums.

"""

from IPython import embed
import time
from tqdm import tqdm
import numpy as np
import pandas as pd
import utils
from collections import defaultdict, Counter

INPUT_PATH = "../data/SCC.txt"


class Kosaraju:
    def __init__(self, edges_list):
        self.edges_list = edges_list

    def _get_vertex_list(self, edges_list, reversed_flag):
        if reversed_flag:
            i_from, i_to = 1, 0
        else:
            i_from, i_to = 0, 1
        vertex_list = defaultdict(list)
        for e in edges_list:
            vertex_list[e[i_from]] = []
            vertex_list[e[i_to]] = []

        for e in edges_list:
            vertex_list[e[i_from]].append(e[i_to])
        return vertex_list

    def dfs(self, vertex_list, ordering=None, scc_flag=False, ranking_flag=False):
        n = len(vertex_list)
        explored = []

        if ranking_flag:
            ranking = n - 1
            rankings = {}
        if scc_flag:
            scc_group = 0
            sccs = defaultdict(list)
        print(f"n = {n}")
        for i in tqdm(reversed(range(n))):
            if ordering:
                node = ordering[i]
            else:
                node = i
            if i not in explored:
                to_explore = [node]
                if scc_flag:
                    scc_group += 1
                while len(to_explore) > 0:
                    current_node = to_explore.pop(0)
                    if scc_flag:
                        sccs[scc_group].append(current_node)
                    explored.append(current_node)
                    not_already_explored = [
                        e for e in vertex_list[current_node] if e not in explored
                    ]
                    to_explore = not_already_explored + to_explore
                    if ranking_flag:
                        rankings[current_node] = ranking
                        ranking -= 1

        return rankings, sccs

    def find_all_sccs(self):
        print("setup (topo)")
        vertex_list_rev = self._get_vertex_list(self.edges_list, reversed_flag=True)

        print("creatings topological ordering")
        topo_ordering, _ = self.dfs(
            vertex_list=vertex_list_rev,
            ordering=None,
            scc_flag=False,
            ranking_flag=True,
        )
        print("setup (sccs)")
        del vertex_list_rev
        vertex_list = self._get_vertex_list(self.edges_list, reversed_flag=False)

        print("finding sccs")
        _, scc = self.dfs(
            vertex_list=vertex_list,
            ordering=topo_ordering,
            scc_flag=True,
            ranking_flag=False,
        )

        self.sccs = scc

    def largest_n_sccs(self, n):
        self.find_all_sccs()
        print("finding largest three")

        sccs_lens = [len(self.sccs[i]) for i in self.sccs.keys()]
        return sorted(sccs_lens, reverse=True)[:n]


def parse_input_file(file_path):
    split_rows = [row.split(" ") for row in open(file_path, "r").read().splitlines()]
    clean_rows = [
        [int(entry) - 1 for entry in row if entry is not ""] for row in split_rows
    ]
    vertex_dict = {t[0]: t[1:] for t in clean_rows}
    edges_list = []
    for key, value in vertex_dict.items():
        for neighbour in value:
            edges_list.append([key, neighbour])

    edges_list = [list(x) for x in set(tuple(x) for x in edges_list)]

    return edges_list


def main():
    print("parsing input data")
    edges_list = parse_input_file(INPUT_PATH)
    print("initialising")
    kos = Kosaraju(edges_list)
    res = kos.largest_n_sccs(5)
    print(f"results {res}")


if __name__ == "__main__":
    main()

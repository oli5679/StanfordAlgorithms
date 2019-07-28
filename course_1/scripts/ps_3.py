from IPython import embed
import random
import time
import tqdm
from copy import deepcopy
from copy import copy
import math

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


def parse_file(input_path):
    rows = open(input_path, "r").read().splitlines()
    split_rows = [row.split("\t") for row in rows]
    clean_rows = [
        [int(entry) for entry in row if entry is not ""] for row in split_rows
    ]

    vertex_dict = {t[0]: t[1:] for t in clean_rows}
    vertex_list = list(vertex_dict.keys())
    edges_list = []
    for key, value in vertex_dict.items():
        for neighbour in value:
            edges_list.append(sorted([key, neighbour]))

    edges_list = [list(x) for x in set(tuple(x) for x in edges_list)]
    return vertex_list, edges_list


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
    vertex_list, edges_list = parse_file(INPUT_PATH)
    min_cut = karger_cut(vertex_list, edges_list)
    print(f"minimum cut {min_cut}")

    assert min_cut == 17


if __name__ == "__main__":
    main()

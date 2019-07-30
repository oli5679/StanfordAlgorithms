#!/usr/bin/python

# The file contains the edges of a directed graph. Vertices are labeled as
# positive integers from 1 to 875714. Every row indicates an edge, the vertex
# label in first column is the tail and the vertex label in second column is
# the head (recall the graph is directed, and the edges are directed from the
# first column vertex to the second column vertex). So for example, the 11th
# row looks liks : "2 47646". This just means that the vertex with label 2 has
# an outgoing edge to the vertex with label 47646

# Your task is to code up the algorithm from the video lectures for computing
# strongly connected components (SCCs), and to run this algorithm on the given
# graph.

# Output Format: You should output the sizes of the 5 largest SCCs in the given
# graph, in decreasing order of sizes, separated by commas (avoid any spaces).
# So if your algorithm computes the sizes of the five largest SCCs to be 500,
# 400, 300, 200 and 100, then your answer should be "500,400,300,200,100". If
# your algorithm finds less than 5 SCCs, then write 0 for the remaining terms.
# Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and
# 100, then your answer should be "400,300,100,0,0".

from collections import defaultdict, Counter
import random
from IPython import embed
from tqdm import tqdm


def parse_file(path):
    return [[int(v) - 1 for v in row.split(" ")[:2]] for row in open(path)]


def adjacency_list(E, undirected=False):
    """
    Given path to a txt file listing edges, 
        (a) Reads file
        (b) Parses string to create list of edges
        (c) Loops through edges and maps to vertices
            - type default dict, but can be treated as list
            - works for both directed and undirected graphs
        
        Returns (E, V)
    """

    V = defaultdict(list)

    for e in E:
        V[e[0]].append(e[1])
        if undirected:
            V[e[1]].append(e[0])

    return V


def dfs_topo(V_rev, n):
    f = n - 1
    f_vals = Counter()
    explored = []
    for i in tqdm(range(n)):
        if i not in explored:
            to_explore = [i]
            while len(to_explore) > 0:
                current_node = to_explore.pop(0)

                explored.append(current_node)
                for e in V_rev[current_node]:
                    if e not in explored:
                        to_explore.insert(0, e)

                f_vals[f] = current_node
                f -= 1

    return f_vals


def dfs_SCC(V, ordering, n):
    group_counter = 0
    groups = defaultdict(list)
    explored = []

    for i in tqdm(reversed(range(n))):
        node = ordering[i]
        if node not in explored:
            to_explore = [node]
            group_counter += 1
            while len(to_explore) > 0:
                current_node = to_explore.pop(0)
                groups[group_counter].append(current_node)
                explored.append(current_node)
                for e in V[current_node]:
                    if e not in explored:
                        to_explore.insert(0, e)

    return groups


def kosaraju(V, E):
    V_rev = defaultdict(list)

    for e in E:
        V_rev[e[1]].append(e[0])

    n = len(set([item for sublist in E for item in sublist]))
    del E

    f = dfs_topo(V_rev, n)

    groups = dfs_SCC(V, f, n)

    return f, groups


E = parse_file("SCC_test_2.txt")

V = adjacency_list(E)

n = len(set([item for sublist in E for item in sublist]))

V_rev = defaultdict(list)

for e in E:
    V_rev[e[1]].append(e[0])

# del E

f = dfs_topo(V_rev, n)

groups = dfs_SCC(V, f, n)

embed()

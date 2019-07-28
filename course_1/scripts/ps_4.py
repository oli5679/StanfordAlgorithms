from IPython import embed
import time
from tqdm import *
import numpy as np
import pandas as pd


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


TXT_FILE = open("SCC.txt", "r")
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

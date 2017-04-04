from IPython import embed
import random
import time
from tqdm import *
from copy import deepcopy

def del_self_loops(edges_list):
    return [edge for edge in edges_list if edge[0] != edge[1]]

def karger_cut(vertex_list, edges_list):
    while len(vertex_list) > 2:
        #print(vertex_dict.keys())
        vertex_list, edges_list = single_contract(vertex_list, edges_list)
        edges_list = del_self_loops(edges_list)
    count = 0
    for value in edges_list:
        if(value[0] != value[1]):
            count += 1
    return count

def single_contract(vertex_list,edges_list):
    edge = [1, 1]
    while edge[0] == edge[1]:
        edge = edges_list.pop(random.randrange(len(edges_list)))
    vertex_list = [vertex for vertex in vertex_list if vertex != edge[1]]

    for o_edge in edges_list:
        if o_edge[0] == edge[1]:
            o_edge[0] = edge[0]
        if o_edge[1] == edge[1]:
            o_edge[1] = edge[0]

    return vertex_list, edges_list

TXT_FILE = open("kargerMinCut.txt", "r")
INPUT_STRING = TXT_FILE.read()
ROWS = INPUT_STRING.splitlines()
VERTEX_LIST = [row.split('\t') for row in ROWS]
VERTEX_LIST = [[int(entry) for entry in row  if entry is not ''] for row in VERTEX_LIST]
VERTEX_DICT = {t[0]:t[1:] for t in VERTEX_LIST}
EDGES_LIST = []
VERTEX_LIST = list(VERTEX_DICT.keys())

for key, value in VERTEX_DICT.items():
    for neighbour in value:
        EDGES_LIST.append(sorted([key,neighbour]))

EDGES_LIST = [list(x) for x in set(tuple(x) for x in EDGES_LIST)]

MIN_VAL = 1000000000000000

for x in tqdm(range(211932)):
    input_vertex = deepcopy(VERTEX_LIST)
    input_edges = deepcopy(EDGES_LIST)
    ans = karger_cut(input_vertex, input_edges)
    if ans < MIN_VAL:
        MIN_VAL = ans
        print(MIN_VAL)

print('done!')
print(MIN_VAL)

from IPython import embed
import random
import time
from tqdm import *


txt_file = open("kargerMinCut.txt", "r")
input_string = txt_file.read()
rows = input_string.splitlines()
vertex_list = [row.split('\t') for row in rows]
vertex_list = [[int(entry) for entry in row  if entry is not ''] for row in vertex_list]
vertex_dict_1 = {t[0]:t[1:] for t in vertex_list}
edges_list_1 = []

for key, value in vertex_dict_1.items():
    for neighbour in value:
        edges_list_1.append(sorted([key,neighbour]))

edges_list_1= [list(x) for x in set(tuple(x) for x in edges_list_1)]

def karger_cut(vertex_dict,edges_list):
    while(len(vertex_dict) > 2):
        #print(vertex_dict.keys())
        vertex_dict,edges_list = single_cut(vertex_dict,edges_list)
    count = 0

    for value in edges_list:
            if(value[0] != value[1]):
                count += 1
    return count

def single_cut(vertex_dict,edges_list):
    edge = [1,1]
    while edge[0] == edge[1]:
        edge = edges_list.pop(random.randrange(len(edges_list)))
    #print(edge)
    vertex_dict[edge[0]]=vertex_dict[edge[0]]+vertex_dict[edge[1]]
    del vertex_dict[edge[1]]
    for key, value in vertex_dict.items():
        for index in value:
            if index == edge[1]:
                index = edge[0]
            if index == key:
                del index
    for o_edge in edges_list:
        if o_edge[0] == edge[1]:
            o_edge[0] = edge[0]
        if o_edge[1] == edge[1]:
            o_edge[1] = edge[0]
        if o_edge[0] == o_edge[1]:
            del o_edge
    return vertex_dict,edges_list

min = 1000000000000000
for x in tqdm(range(100000000)):
    ans = karger_cut(vertex_dict_1,edges_list_1)
    if ans < min:
        min = ans

print('done!')
print(ans)

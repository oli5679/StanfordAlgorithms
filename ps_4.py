from IPython import embed
txt_file = open("SCC.txt", "r")
input_string = txt_file.read()
rows = input_string.splitlines()
edges = [row.split(' ') for row in rows]
edges = [[int(v) for v in row[:-1]] for row in edges]

def reverse_DFS_loop(graph):
    t = 0
    explored = []
    unexplored = graph
    while len(unexplored > 0):
        node = 

def forwards_DFS_loop(graph):
    pass
embed()
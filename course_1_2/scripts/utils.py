def parse_graph_vertex_file(input_path):
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

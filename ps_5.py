from IPython import embed
txt_file = open("dijkstraData.txt", "r")
input_string = txt_file.read()
rows = input_string.splitlines()
#vertex_dict = {int(t[0]):[[int(g) for g in y.split(',')] for y in t[1:].split('\t') if y] for t in rows}
vertex_list = 

explored = [False*200]
distance = [100000000000]*200
paths= ['not found']*200
explored[0] = True
distance[0] = 0
paths[0] = ""


#vertex_list = [x[0] for x in vertex_list ,[y.split(',') for y in x[1] if x[1]] for x[1] in vertex_list]

print(vertex_dict)
embed()


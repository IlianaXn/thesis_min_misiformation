import networkx as nx
import matplotlib.pyplot as plt
from merge import merge

path = 'graphs/test.txt'
with open(path) as file:
    lines = file.readlines()

expertise = {0: 0, 1: 0, 2: 0, 3: 1, 4: 0, 5: 1, 6: 0}

graph = nx.parse_edgelist(lines, nodetype=int, create_using=nx.DiGraph)

graph, _ = merge([0, 1], graph)

data_edges = graph.edges(data=True)

edge_labels = dict([((node1, node2), (data['weight'] * (1 - expertise[node2]),
                                      data['weight'] * max(1 - expertise[node2], expertise[node2])))
                    for node1, node2, data in data_edges])



position = nx.circular_layout(graph)
nx.draw(graph, pos=position, with_labels=True)
nx.draw_networkx_edge_labels(graph, pos=position, edge_labels=edge_labels)
plt.show()
#plt.savefig('test.png')

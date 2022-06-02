import networkx as nx
import numpy as np

path = 'graphs/email-Eu-core.txt'

initial_graph = nx.read_edgelist(path, nodetype=int, create_using=nx.DiGraph)

# initial_graph = nx.read_edgelist(path, nodetype=int)

initial_graph.remove_edges_from(nx.selfloop_edges(initial_graph))

isolated_nodes = list(nx.isolates(initial_graph))
initial_graph.remove_nodes_from(isolated_nodes)

graph = nx.convert_node_labels_to_integers(initial_graph)

edges = graph.edges()

w_edges = [(node1, node2, np.random.uniform()) for (node1, node2) in edges]
# w_edges_rev = [(node2, node1, np.random.uniform()) for (node1, node2) in edges]

new_g = nx.DiGraph()

new_g.add_weighted_edges_from(w_edges)
# new_g.add_weighted_edges_from(w_edges_rev)

nx.write_edgelist(new_g, f'{path[:-4]}_IC.txt')

for node in new_g.nodes():
    no_activation = np.random.uniform()
    incoming = new_g.in_edges(node, data='weight')
    total = no_activation + sum([w for _, _, w in incoming])
    new_weights = []
    for node1, node2, influence in incoming:
        new_influence = influence / total
        new_weights.append((node1, node2, new_influence))
    new_g.add_weighted_edges_from(new_weights)

nx.write_edgelist(new_g, f'{path[:-4]}_LT.txt')
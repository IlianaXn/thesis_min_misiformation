import networkx as nx
import numpy as np

n = [10, 50, 100]

for size in n:
    print(size)

    # produce scale-free graph
    G = nx.scale_free_graph(size)

    # remove self-loops
    G.remove_edges_from(nx.selfloop_edges(G))

    # remove parallel edges
    di_edges = set(G.edges())

    sf = nx.DiGraph()

    sf.add_edges_from(di_edges)

    nx.write_edgelist(sf, f'graphs/SF_{size}.txt')

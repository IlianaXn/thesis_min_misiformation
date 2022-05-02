import networkx as nx
import random

# generate sf networks n=100, 1000, 10000 and d=10, 50, 100
n = [100, 1000, 10000]
d = [10, 50, 99]
p_inf = [0.1, 0.5, 0.9]

for size in n:
    for deg in d:
        sf_edges = list(nx.barabasi_albert_graph(size, deg).edges())

        # Swap the direction of half edges to diffuse degree
        di_edges = [(sf_edges[i][0], sf_edges[i][1], random.choice(p_inf)) if i % 2 == 0 else (
        sf_edges[i][1], sf_edges[i][0], random.choice(p_inf)) for i in
                    range(len(sf_edges))]
        sf = nx.DiGraph()

        sf.add_weighted_edges_from(di_edges)  # Create a directed graph

        nx.write_edgelist(sf, f'graphs/SF_{size}_{deg}.txt')

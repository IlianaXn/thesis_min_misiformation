import networkx as nx
import random

# generate sw networks n=100, 1000, 10000 and d=10, 50, 100
n = [100, 1000, 10000]
d = [10, 50, 99]
p = [0.25, 0.3, 0.4]
p_inf = [0.1, 0.6, 0.9]

for size in n:
    for deg in d:
        for prob in p:
            sw_edges = list(nx.connected_watts_strogatz_graph(size, deg, prob).edges())

            # Swap the direction of half edges to diffuse degree
            di_edges = [(sw_edges[i][0], sw_edges[i][1], random.choice(p_inf)) if i % 2 == 0 else (
                sw_edges[i][1], sw_edges[i][0], random.choice(p_inf)) for i in
                        range(len(sw_edges))]
            sw = nx.DiGraph()

            sw.add_weighted_edges_from(di_edges)  # Create a directed graph

            nx.write_edgelist(sw, f'graphs/SW_{size}_{deg}_{prob}.txt')

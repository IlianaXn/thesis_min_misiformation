import networkx as nx
import random

# generate sw networks n=100, 1000, 10000 and d=10, 50, 100
n = [100, 1000, 10000]
d = [10, 50, 99]
p = [0.25, 0.3, 0.4]

for size in n[2:]:
    for deg in d[2:]:
        for prob in p:
            sw_edges = list(nx.connected_watts_strogatz_graph(size, deg, prob).edges())

            # Swap the direction of half edges to diffuse degree
            di_edges = [(sw_edges[i][0], sw_edges[i][1]) if i % 2 == 0 else (sw_edges[i][1], sw_edges[i][0]) for i in
                        range(len(sw_edges))]
            sw = nx.DiGraph()
            sw.add_edges_from(di_edges)  # Create a directed graph

            # Remove edges that contribute to cycles s.t. we have an DAG
            while not nx.is_directed_acyclic_graph(sw):
                cycle = nx.find_cycle(sw)
                to_remove = random.randrange(len(cycle))
                sw.remove_edge(*cycle[to_remove])
            nx.write_edgelist(sw, f'graphs/SW_{size}_{deg}_{prob}.txt', data=False)

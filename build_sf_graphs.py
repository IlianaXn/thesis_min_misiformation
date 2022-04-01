import networkx as nx
import random

# generate sf networks n=100, 1000, 10000 and d=10, 50, 100
n = [100, 1000, 10000]
d = [10, 50, 99]

for size in n:
    for deg in d:
        sf_edges = list(nx.barabasi_albert_graph(size, deg).edges())

        # Swap the direction of half edges to diffuse degree
        di_edges = [(sf_edges[i][0], sf_edges[i][1]) if i % 2 == 0 else (sf_edges[i][1], sf_edges[i][0]) for i in
                    range(len(sf_edges))]
        sf = nx.DiGraph()
        sf.add_edges_from(di_edges)  # Create a directed graph

        # Remove edges that contribute to cycles s.t. we have an DAG
        while not nx.is_directed_acyclic_graph(sf):
            cycle = nx.find_cycle(sf)
            to_remove = random.randrange(len(cycle))
            sf.remove_edge(*cycle[to_remove])
        nx.write_edgelist(sf, f'graphs/SF_{size}_{deg}.txt', data=False)
import networkx as nx
import numpy as np


# first attempt: take into consideration only spread from seed nodes
def bond_percolation(graph: nx.DiGraph, seed: set, number: int = 1000) -> tuple[list[nx.DiGraph], dict]:
    graphs = []
    edge_appearance = dict()
    edges_weights = nx.get_edge_attributes(graph, 'weight')
    i = 0
    while i < number:
        flag = False
        edges = []
        for edge, inf in edges_weights.items():
            try:
                inf = inf[-1]
            except TypeError:
                pass
            rand_nmb = np.random.uniform()
            if rand_nmb <= inf:
                edges.append(edge)
                if edge[0] in seed and not flag:
                    flag = True
        if flag:
            for edge in edges:
                try:
                    edge_appearance[edge].add(i)
                except KeyError:
                    edge_appearance[edge] = {i}
            g = nx.DiGraph()
            g.add_edges_from(edges)
            graphs.append(g)
            i += 1

    return graphs, edge_appearance

import networkx as nx
import numpy as np


# first attempt: take into consideration only spread from seed nodes
def bond_percolation(seed, edge_labels: dict, info: str, number: int = 100) -> tuple[list[nx.DiGraph], dict]:
    if info == 'truth':
        flag = 1
    else:
        flag = 0
    graphs = []
    edge_appearance = dict()
    for i in range(number):
        edges = []
        for edge, info in edge_labels.items():
            influence = info[flag]
            if np.random.uniform() <= influence:
                edges.append(edge)

                try:
                    edge_appearance[edge].add(i)
                except KeyError:
                    edge_appearance[edge] = {i}

        g = nx.DiGraph()
        g.add_edges_from(edges)
        g.add_node(seed)
        graphs.append(g)

    return graphs, edge_appearance

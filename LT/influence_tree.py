import networkx as nx
import numpy as np


def live_edge(graph: nx.DiGraph, T: int, seeds) -> list[nx.DiGraph]:
    k = 0
    graphs = []
    while k < T:
        edges = []
        flag = False
        for node in graph.nodes():
            incoming = graph.in_edges(node, data='weight')
            for node1, node2, influence in incoming:
                rand = np.random.uniform()
                if influence >= rand:
                    edges.append((node1, node2))
                    if node1 in seeds and not flag:
                        flag = True
                    break
        if flag:
            g = nx.DiGraph()
            g.add_edges_from(edges)
            graphs.append(g)
            k += 1
    return graphs


def induced_trees(root: int, graphs: list[nx.DiGraph]) -> list[nx.DiGraph]:
    trees = []
    for g in graphs:
        if root in g.nodes():
            tree = nx.bfs_tree(g, root)
            trees.append(tree)
    return trees

import networkx as nx
from copy import deepcopy
from deterministic_LT import propagation
import time


def weighted_removal(graph: nx.DiGraph, expertise: dict[int, tuple[float, float]], seeds_truth: set[int], seeds_lie: set[int], k: int):
    start = time.time()

    edges = list(graph.out_edges(seeds_lie, data='weight'))

    # compute truth and lie propagation
    activated_t = propagation(graph, expertise, seeds_truth, 0)
    activated_f = propagation(graph, expertise, seeds_lie, 1)

    initial_good = len(activated_t)
    initial_bad = len(activated_f)
    initial_value = initial_bad
    values = [initial_value]

    # prune graphs
    nodes = set(graph.nodes())
    graph_truth = nx.DiGraph(graph)
    graph_truth.remove_nodes_from(nodes - activated_t)
    in_edges = deepcopy(graph_truth.in_edges(seeds_truth))
    graph_truth.remove_edges_from(in_edges)

    graph_false = nx.DiGraph(graph)
    graph_false.remove_nodes_from(nodes - activated_f)
    in_edges = deepcopy(graph_false.in_edges(seeds_lie))
    graph_false.remove_edges_from(in_edges)

    # sort according to weight
    edges.sort(key=lambda x: x[2], reverse=True)

    if k > len(edges):
        print('new value of k =', len(edges))
        k = len(edges)

    times = k // 50

    removed_edges = []

    for i in range(times + 1):
        start = i * 50

        edges_to_remove = edges[start:start + 50]

        graph.remove_edges_from(edges_to_remove)

        activated_t = propagation(graph, expertise, seeds_truth, 0)
        activated_f = propagation(graph, expertise, seeds_lie, 1)

        removed_edges.extend(edges_to_remove)
        values.append(initial_good - len(activated_t) + len(activated_f))
        if len(activated_f) == 0:
            print(f'We stopped at {k - start - len(edges_to_remove)} remaining edge(s).')
            break


    print('Weighted removal')
    print('I removed:', removed_edges)
    print('Initial value:', initial_value)
    print('Final value:', values[-1])
    dur = time.time() - start
    return values, dur
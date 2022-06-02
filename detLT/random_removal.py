import networkx as nx
from deterministic_LT import propagation
from numpy import random
import time

def random_removal(graph: nx.DiGraph, expertise: dict[int, tuple[float, float]], seeds_truth: set[int], seeds_false: set[int] ,k: int):
    start_t = time.time()
    # compute truth and lie propagation
    activated_t = propagation(graph, expertise, seeds_truth, 0)
    activated_f = propagation(graph, expertise, seeds_false, 1)

    initial_good = len(activated_t)
    initial_bad = len(activated_f)
    initial_value = initial_bad
    values = [initial_value]

    edges = list(graph.out_edges(seeds_false))

    # random permutation of edges
    random.shuffle(edges)

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
        activated_f = propagation(graph, expertise, seeds_false, 1)

        removed_edges.extend(edges_to_remove)
        values.append(initial_good - len(activated_t) + len(activated_f))
        if len(activated_f) == 0:
            print(f'We stopped at {k - start - len(edges_to_remove)} remaining edge(s).')
            break

    print('Random removal')
    print('I removed:', removed_edges)
    print('Initial value:', initial_value)
    print('Final value:', values[- 1])
    dur = time.time() - start_t
    return values, dur
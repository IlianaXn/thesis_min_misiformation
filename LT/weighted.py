import networkx as nx
from numpy import random
from influence_tree import live_edge, induced_trees
import time


def weighted_removal(graph: nx.DiGraph, seeds_truth: set[int], seeds_lie: set[int], k: int):
    start = time.time()

    edges = list(graph.out_edges(seeds_lie, data='weight'))

    # keep only the difference
    common_seeds = seeds_truth.intersection(seeds_lie)
    seeds_truth, seeds_lie = seeds_truth - seeds_lie, seeds_lie - seeds_truth

    # number of samples
    T = 5000
    samples = live_edge(graph, T, seeds_truth | seeds_lie | common_seeds)
    print('telos')

    # trees rooted at seeds
    trees_truth = dict()
    for seed in seeds_truth:
        trees_truth[seed] = induced_trees(seed, samples)

    # trees rooted at seeds
    trees_lie = dict()
    for seed in seeds_lie:
        trees_lie[seed] = induced_trees(seed, samples)

    # trees rooted at common seeds
    trees_common = dict()
    for seed in common_seeds:
        trees_common[seed] = induced_trees(seed, samples)


    current_good_spread = 0
    current_bad_spread = 0

    # initial common spread
    initial_common_spread = 0

    for seed, trees in trees_common.items():
        for t in trees:
            initial_common_spread += len(nx.descendants(t, seed))

    for seed, trees in trees_truth.items():
        for t in trees:
            current_good_spread += len(nx.descendants(t, seed))

    for seed, trees in trees_lie.items():
        for t in trees:
            current_bad_spread += len(nx.descendants(t, seed))

    initial_good_spread = current_good_spread + initial_common_spread
    initial_bad_spread = current_bad_spread + initial_common_spread

    values = [initial_bad_spread]

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

        current_good_spread = current_bad_spread = 0

        for seed, trees in trees_truth.items():
            for t in trees:
                for e in edges_to_remove:
                    try:
                        t.remove_edge(e[0], e[1])
                    except nx.NetworkXError:
                        pass
                current_good_spread += len(nx.descendants(t, seed))

        for seed, trees in trees_lie.items():
            for t in trees:
                for e in edges_to_remove:
                    try:
                        t.remove_edge(e[0], e[1])
                    except nx.NetworkXError:
                        pass
                current_bad_spread += len(nx.descendants(t, seed))

        removed_edges.extend(edges_to_remove)
        values.append(initial_good_spread - current_good_spread + current_bad_spread)
        if current_bad_spread == 0:
            print(f'We stopped at {k - start - len(edges_to_remove)} remaining edge(s).')
            break

    print('Weighted removal')
    print('I removed:', removed_edges)
    print('Initial value:', initial_bad_spread)
    print('Final value:', initial_good_spread - current_good_spread + current_bad_spread)
    dur = time.time() - start
    return values, dur
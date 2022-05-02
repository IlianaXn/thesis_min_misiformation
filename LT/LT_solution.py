import networkx as nx
import numpy as np
from influence_tree import live_edge, induced_trees
from queue import PriorityQueue
import time


def probabilistic_LT(graph: nx.DiGraph, seeds_truth: set[int], seeds_lie: set[int], k: int):
    start = time.time()

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
        trees_truth[seed] = (induced_trees(seed, samples), [])

    # trees rooted at seeds
    trees_lie = dict()
    for seed in seeds_lie:
        trees_lie[seed] = (induced_trees(seed, samples), [])

    # trees rooted at common seeds
    trees_common = dict()
    for seed in common_seeds:
        trees_common[seed] = induced_trees(seed, samples)

    gain_good = dict()
    gain_bad = dict()

    # initialization to 0
    for edge in graph.edges():
        gain_good[edge] = gain_bad[edge] = 0

    for trees, spreads in trees_truth.values():
        for i in range(len(trees)):
            spreads.append(dict())
            for node in trees[i]:
                spreads[i][node] = 0

    for trees, spreads in trees_lie.values():
        for i in range(len(trees)):
            spreads.append(dict())
            for node in trees[i]:
                spreads[i][node] = 0

    # initial common spread
    initial_common_spread = 0

    for seed, trees in trees_common.items():
        for t in trees:
            initial_common_spread += len(nx.descendants(t, seed))

    # compute initial spreads
    for seed, (trees, spreads) in trees_truth.items():
        for i in range(len(trees)):
            h = list(nx.bfs_edges(trees[i], seed))
            for edge in reversed(h):
                spreads[i][edge[0]] += spreads[i][edge[1]] + 1
                gain_good[edge] += spreads[i][edge[1]] + 1

    for seed, (trees, spreads) in trees_lie.items():
        for i in range(len(trees)):
            h = list(nx.bfs_edges(trees[i], seed))
            for edge in reversed(h):
                spreads[i][edge[0]] += spreads[i][edge[1]] + 1
                gain_bad[edge] += spreads[i][edge[1]] + 1

    current_good_spread = 0
    current_bad_spread = 0

    for seed, (_, spreads) in trees_truth.items():
        for s in spreads:
            current_good_spread += s[seed]

    for seed, (_, spreads) in trees_lie.items():
        for s in spreads:
            current_bad_spread += s[seed]

    initial_good_spread = current_good_spread + initial_common_spread
    initial_bad_spread = current_bad_spread + initial_common_spread

    values = [initial_bad_spread]
    edges = set(graph.edges())

    removed_edges = []

    while k:

        # find edge with greatest decrement
        gain, potential_edge = 0, None
        for edge in edges:
            temp = gain_bad[edge] - gain_good[edge]
            if temp > gain:
                gain, potential_edge = temp, edge

        if not gain:
            print(f'We stopped at {k} remaining edge(s).')
            break
        else:
            removed_edges.append(potential_edge)
            k -= 1
            edges.remove(potential_edge)
            current_good_spread -= gain_good[potential_edge]
            current_bad_spread -= gain_bad[potential_edge]

            values.append(initial_good_spread - current_good_spread + current_bad_spread)
            u, v = potential_edge

            for seed, (trees, spreads) in trees_truth.items():
                for i in range(len(trees)):
                    t = trees[i]
                    if potential_edge in trees[i].edges():
                        s = spreads[i]
                        pred = u
                        while pred != seed:
                                s[pred] -= s[v] + 1
                                par = next(t.predecessors(pred))
                                gain_good[(par, pred)] -= s[v] + 1
                                pred = par

                        s[v] = 0
                        h = list(nx.bfs_edges(t, v))
                        for edge in h:
                            gain_good[edge] -= s[edge[1]] + 1
                            s[edge[1]] = 0
                        h.append(potential_edge)
                        t.remove_edges_from(h)

            for seed, (trees, spreads) in trees_lie.items():
                for i in range(len(trees)):
                    t = trees[i]
                    if potential_edge in trees[i].edges():
                        s = spreads[i]
                        pred = u
                        while pred != seed:
                            s[pred] -= s[v] + 1
                            par = next(t.predecessors(pred))
                            gain_bad[(par, pred)] -= s[v] + 1
                            pred = par

                        s[v] = 0
                        h = list(nx.bfs_edges(t, v))
                        for edge in h:
                            gain_bad[edge] -= s[edge[1]] + 1
                            s[edge[1]] = 0
                        h.append(potential_edge)
                        t.remove_edges_from(h)

    print('Greedy solution')
    print('I removed:', removed_edges)
    print('Initial value:', initial_bad_spread)
    print('Final value:', initial_good_spread - current_good_spread + current_bad_spread)
    duration = time.time() - start
    return values, duration
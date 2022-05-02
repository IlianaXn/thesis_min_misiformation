import networkx as nx
from influence_tree import live_edge, induced_trees
import time
from queue import PriorityQueue


def distance_diff(graph: nx.DiGraph, seeds_truth: set[int], seeds_lie: set[int], k: int):
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

    w_edges = graph.edges(data='weight')

    rev_edges = [(u, v, 1 / w) for u, v, w in w_edges]

    graph.add_weighted_edges_from(rev_edges)

    nodes = set(graph.nodes())

    dist_good = []
    for s in seeds_truth:
        dist_good.append(nx.shortest_path_length(graph, s, weight='weight'))

    dist_bad = []
    for s in seeds_lie:
        dist_bad.append(nx.shortest_path_length(graph, s, weight='weight'))

    min_dist_good = dict()
    min_dist_bad = dict()

    for u in nodes:
        min_dist_good[u] = min_dist_bad[u] = len(nodes)

    for u in nodes:
        if u not in seeds_truth:
            for v in dist_good:
                try:
                    dist = v[u]
                except KeyError:
                    continue
                if dist < min_dist_good[u]:
                    min_dist_good[u] = dist

        if u not in seeds_lie:
            for v in dist_bad:
                try:
                    dist = v[u]
                except KeyError:
                    continue
                if dist < min_dist_bad[u]:
                    min_dist_bad[u] = dist

    q = PriorityQueue()
    for u in graph.nodes():
        diff = 0
        if u not in seeds_truth:
            diff -= min_dist_good[u]
        if u not in seeds_lie:
            diff += min_dist_bad[u]

        q.put((diff, u))

    k_edges = []
    diff_next, node_next = - 1, - 1

    flag = True
    out_edges = []

    while k:
        if k > 50:
            t = 50
        else:
            t = k % 50

        edges_to_remove = []
        while t:
            if flag:
                if node_next == - 1:
                    diff, node = q.get()
                else:
                    diff, node = diff_next, node_next
                nodes = [node]
                while True:
                    diff_next, node_next = q.get()
                    if diff_next != diff:
                        break
                    else:
                        nodes.append(node_next)

                out_edges = list(graph.out_edges(nodes, data='weight'))
                out_edges.sort(key=lambda x: x[2])

            if len(out_edges) <= t:
                edges_to_remove.extend(out_edges)
                flag = True
                t -= len(out_edges)
            else:
                edges_to_remove.extend(out_edges[:t])
                flag = False
                t = 0

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

        if k > 50:
            k -= 50
        else:
            k = 0
        k_edges.extend(edges_to_remove)
        values.append(initial_good_spread - current_good_spread + current_bad_spread)

        if current_bad_spread == 0:
            print(f'We stopped at {k} remaining edge(s).')
            break

    print('Distance method')
    print('I removed:', k_edges)
    print('Initial valued:', initial_bad_spread)
    print('Final value:', initial_good_spread - current_good_spread + current_bad_spread)
    dur = time.time() - start
    return values, dur
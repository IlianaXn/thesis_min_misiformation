import networkx as nx
from deterministic_LT import propagation
from copy import deepcopy
from queue import PriorityQueue
import time

def edge_betweenness_diff(graph: nx.DiGraph, expertise: dict[int, tuple[float, float]], seeds_truth: set[int], seeds_false: set[int], k: int):
    start = time.time()

    # compute truth and lie propagation
    activated_t = propagation(graph, expertise, seeds_truth, 0)
    activated_f = propagation(graph, expertise, seeds_false, 1)

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
    in_edges = deepcopy(graph_false.in_edges(seeds_false))
    graph_false.remove_edges_from(in_edges)

    good_edges = set(graph_truth.edges(data='weight'))
    bad_edges = set(graph_false.edges(data='weight'))
    edges = good_edges.union(bad_edges)

    if k > len(edges):
        print('new value of k =', len(edges))
        k = len(edges)

    rev_graph_truth = graph_truth.copy()
    rev_graph_false = graph_false.copy()

    w_edges = graph_truth.edges(data='weight')

    rev_edges = [(u, v, 1 / w) for u, v, w in w_edges]

    rev_graph_truth.add_weighted_edges_from(rev_edges)

    w_edges = graph_false.edges(data='weight')

    rev_edges = [(u, v, 1 / w) for u, v, w in w_edges]

    rev_graph_false.add_weighted_edges_from(rev_edges)

    truth_betw = nx.edge_betweenness_centrality_subset(rev_graph_truth, seeds_truth, set(graph_truth.nodes()) - seeds_truth, weight='weight')
    lie_betw = nx.edge_betweenness_centrality_subset(rev_graph_false, seeds_false, set(graph_false.nodes()) - seeds_false, weight='weight')

    q = PriorityQueue()
    for e in edges:
        try:
            truth = truth_betw[(e[0], e[1])]
        except KeyError:
            truth = 0
        try:
            lie = lie_betw[(e[0], e[1])]
        except KeyError:
            lie = 0
        diff = truth - lie

        q.put((diff, e))

    k_edges = []

    diff_next, edge_next = - 1, None

    flag = True
    out_edges = []
    while k:
        if k >= 50:
            t = 50
        else:
            t = k % 50

        edges_to_remove = []
        while t:
            if flag:
                if edge_next is None:
                    diff, edge = q.get()
                else:
                    diff, edge = diff_next, edge_next
                out_edges = [edge]

                while True:
                    if q.empty():
                        break
                    diff_next, edge_next = q.get()
                    if diff_next != diff:
                        break
                    else:
                        out_edges.append(edge_next)

                out_edges.sort(key=lambda x: x[2], reverse=True)
            if len(out_edges) <= t:
                edges_to_remove.extend(out_edges)
                flag = True
                t -= len(out_edges)
            else:
                edges_to_remove.extend(out_edges[:t])
                out_edges = out_edges[t:]
                flag = False
                t = 0

        if k > 50:
            k -= 50
        else:
            k = 0
        k_edges.extend(edges_to_remove)

        for e in edges_to_remove:
            try:
                graph_truth.remove_edge(e[0], e[1])
            except nx.NetworkXError:
                pass
            try:
                graph_false.remove_edge(e[0], e[1])
            except nx.NetworkXError:
                pass

        activated_t = propagation(graph_truth, expertise, seeds_truth, 0)
        activated_f = propagation(graph_false, expertise, seeds_false, 1)

        # prune graphs
        graph_truth.remove_nodes_from(set(graph_truth.nodes()) - activated_t)
        graph_false.remove_nodes_from(set(graph_false.nodes()) - activated_f)

        values.append(initial_good - len(activated_t) + len(activated_f))

        if len(activated_f) == 0:
            print(f'We stopped at {k} remaining edge(s).')
            break

    print('Betweenness method')
    print('I removed:', k_edges)
    print('Initial value:', initial_value)
    print('Final value:', values[- 1])
    print(len(k_edges))
    print(len(set(k_edges)))
    dur = time.time() - start
    return values, dur

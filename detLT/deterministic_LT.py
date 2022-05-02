import networkx as nx
from collections import deque
from copy import deepcopy
import time


def propagation(graph: nx.DiGraph, expertise: dict[int, tuple[float, float]], seeds: set[int], flag: int, edge: tuple[int, int] = None) -> set[int]:
    newly_activated = seeds.copy()
    activated = seeds.copy()
    sum_i = dict()
    while newly_activated:
        out_edges = graph.out_edges(newly_activated, data='weight')
        newly_activated = set()
        for u, v, influence in out_edges:
            if (u,v) == edge:
                continue
            try:
                sum_i[v] += influence
            except KeyError:
                sum_i[v] = influence
            if v not in activated and sum_i[v] >= expertise[v][flag]:
                newly_activated.add(v)
                activated.add(v)
    return activated


def deterministic_LT(graph: nx.DiGraph, expertise: dict[int, tuple[float, float]], seeds_truth: set[int], seeds_false: set[int], k: int):
    start = time.time()

    # compute truth and lie propagation
    activated_t = propagation(graph, expertise, seeds_truth, 0)
    activated_f = propagation(graph, expertise, seeds_false, 1)

    initial_good = len(activated_t)
    initial_bad = len(activated_f)
    total = initial_value = initial_bad

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

    truth_edges = set(graph_truth.edges())
    false_edges = set(graph_false.edges())

    # edges to examine, the rest is useless
    edges = false_edges

    removed_edges = []
    values = [total]

    while k:
        temp = ((0, 0), total)
        for edge in edges:
            temp_activated_t = len(activated_t)
            if edge in truth_edges:
                temp_activated_t = len(propagation(graph_truth, expertise, seeds_truth, 0, edge))

            temp_activated_f = len(activated_f)
            if edge in false_edges:
                temp_activated_f = len(propagation(graph_false, expertise, seeds_false, 1, edge))
            new_total = initial_good - temp_activated_t + temp_activated_f

            if new_total < temp[1]:
                temp = (edge, new_total)
        if temp[1] == total:
            print(f'We stopped at {k} remaining edge(s).')
            break
        else:
            removed_edges.append(temp[0])
            k -= 1
            total = temp[1]
            values.append(total)
            try:
                graph_truth.remove_edge(*temp[0])
            except nx.NetworkXError:
                pass
            graph_false.remove_edge(*temp[0])

            activated_t = propagation(graph_truth, expertise, seeds_truth, 0)
            activated_f = propagation(graph_false, expertise, seeds_false, 1)


            if total != initial_good - len(activated_t) + len(activated_f):
                print('SKATA')


            # prune graphs
            graph_truth.remove_nodes_from(set(graph_truth.nodes()) - activated_t)
            graph_false.remove_nodes_from(set(graph_false.nodes()) - activated_f)


            truth_edges = set(graph_truth.edges())
            false_edges = set(graph_false.edges())

            # edges to examine, the rest is useless
            edges = false_edges

    print('Greedy solution')
    print('I removed:', removed_edges)
    print('Initial value:', initial_value)
    print('Final value:', total)
    duration = time.time() - start
    return values, duration
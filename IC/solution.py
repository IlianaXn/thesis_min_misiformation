import networkx as nx
from bond_percolation import bond_percolation


def count_desc(graph, seeds):
    sus_set = set()
    for s in seeds:
        try:
            curr = nx.descendants(graph, s)
            sus_set = sus_set.union(curr)
        except:
            pass
    return len(sus_set)


# path = 'graphs/test.txt'
path = 'graphs/SF_10.txt'
with open(path) as file:
    lines = file.readlines()

graph = nx.parse_edgelist(lines, nodetype=int, create_using=nx.DiGraph)
total_nodes = len(graph)

seeds_truth = {0, 1}
seeds_false = {0, 1}

expertise = {}
with open('expertise/values.txt') as file:
    i = 0
    for line in file:
        exp = float(line)
        expertise[i] = exp
        i += 1

# expertise = {0: 0, 1: 0, 2: 0, 3: 1, 4: 0, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0}
data_edges = graph.edges(data=True)

edge_false = [(node1, node2, (data['weight'] * (1 - expertise[node2])))
              for node1, node2, data in data_edges]
edge_truth = [(node1, node2, (data['weight'] * max(1 - expertise[node2], expertise[node2])))
              for node1, node2, data in data_edges]

truth_graph = nx.DiGraph()
truth_graph.add_weighted_edges_from(edge_truth)

false_graph = nx.DiGraph()
false_graph.add_weighted_edges_from(edge_false)

number = 80000
truth_graphs, truth_app = bond_percolation(truth_graph, seeds_truth, number)
false_graphs, false_app = bond_percolation(false_graph, seeds_false, number)

k = 1
edges = set(graph.edges)
removed_edges = []
affected_t = affected_f = set(range(number))
truth_spreads = [count_desc(truth_graphs[i], seeds_truth) for i in range(number)]
false_spreads = [count_desc(false_graphs[i], seeds_false) for i in range(number)]
truth_initial = truth_g = sum(truth_spreads) / number
lie_initial = lie_g = sum(false_spreads) / number

while k:
    if lie_g == 0:
        break

    initial = ((0, 0), 0)
    edge_t = set()
    edge_f = set()
    print('Initial values:', truth_g, lie_g)

    for edge in edges:
        # print('Edge to examine:', edge)

        try:
            truth_e = list(filter(lambda x: x not in truth_app[edge], truth_spreads))
            truth_curr, truth_number = sum(truth_e), len(truth_e)
        except KeyError:
            truth_curr, truth_number = 0, 1

        if not truth_number:
            truth_number = 1  # fix

        try:
            lie_e = list(filter(lambda x: x not in false_app[edge], false_spreads))
            lie_curr, lie_number = sum(lie_e), len(lie_e)
        except KeyError:
            lie_curr, lie_number = 0, 1

        if not lie_number:
            lie_number = 1  # TODO: it is in every graph, maybe do again bond percolation

        gain = lie_g - truth_g - (lie_curr / lie_number - truth_curr / truth_number)

        # print('Edge, gain', edge, gain)
        if gain > initial[1]:
            initial = (edge, gain)

    if initial[0] == (0, 0):
        print('sad, no more')
        break
    else:
        edge = initial[0]
        try:
            affected_t = truth_app[edge]
        except KeyError:
            affected_t = set()
        try:
            affected_f = false_app[edge]
        except KeyError:
            affected_f = set()
        # compute spreads here
        for i in affected_t:
            truth_graphs[i].remove_edge(*edge)
            truth_spreads[i] = count_desc(truth_graphs[i], seeds_truth)
        for i in affected_f:
            false_graphs[i].remove_edge(*edge)
            false_spreads[i] = count_desc(false_graphs[i], seeds_false)

        truth_g = sum(truth_spreads) / number
        lie_g = sum(false_spreads) / number
        edges.remove(edge)
        del truth_app[edge]
        del false_app[edge]
        removed_edges.append(edge)
        k -= 1

print('I removed:', removed_edges)
print('Initial value:', lie_initial)
print('Final value:', truth_initial - truth_g + lie_g)

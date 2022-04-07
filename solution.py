import networkx as nx
from merge import merge
from bond_percolation import bond_percolation
import numpy as np

#path = 'graphs/test.txt'
path = 'graphs/SF_100_10.txt'
with open(path) as file:
    lines = file.readlines()

#expertise = {0: 0, 1: 0, 2: 0, 3: 1, 4: 0, 5: 1, 6: 0}

graph = nx.parse_edgelist(lines, nodetype=int, create_using=nx.DiGraph)
total_nodes = len(graph)

seeds = [0, 1]
graph, prob_edges = merge(seeds, graph)


expertise = dict([(node, np.random.uniform()) for node in range(total_nodes)])

data_edges = graph.edges(data=True)

edge_labels = dict([((node1, node2), (data['weight'] * (1 - expertise[node2]),
                                      data['weight'] * max(1 - expertise[node2], expertise[node2])))
                    for node1, node2, data in data_edges])

number = 10000
truth_graphs, truth_app = bond_percolation(seeds[0], edge_labels, 'truth', 10000)
false_graphs, false_app = bond_percolation(seeds[0], edge_labels, 'lies', 10000)

k = 1
edges = set(edge_labels.keys())
edges_removed = set()
affected_t = affected_f = set(range(number))
truth_spreads = [0] * number
false_spreads = [0] * number

while k:
    truth_spreads = [len(nx.descendants(truth_graphs[i], seeds[0])) if i in affected_t
                     else truth_spreads[i] for i in range(number)]
    false_spreads = [len(nx.descendants(false_graphs[i], seeds[0])) if i in affected_f
                     else false_spreads[i] for i in range(number)]

    truth_g = sum(truth_spreads) / number
    lie_g = sum(false_spreads) / number

    initial = ((0, 0), 0)
    edge_t = set()
    edge_f = set()
    number_t = number
    for edge in edges:
        if edge[0] in seeds and len(prob_edges[edge[1]]) > 1:
            number_t = prob_edges[edge[1]][-1] * number
        for i in range(number_t):
            try:
                if i in truth_app[edge]:
                    truth_graphs[i].remove_edge(*edge)
                    edge_t.add(i)
            except KeyError:
                pass
            try:
                if i in false_app[edge]:
                    false_graphs[i].remove_edge(*edge)
                    edge_f.add(i)
            except KeyError:
                pass

        truth = sum([len(nx.descendants(truth_graphs[i], seeds[0])) if i in edge_t
                         else truth_spreads[i] for i in range(number)])
        lie = sum([len(nx.descendants(false_graphs[i], seeds[0])) if i in edge_f
                         else false_spreads[i] for i in range(number)])

        gain = lie_g - truth_g - (lie / number - truth / number)

        for i in range(number_t):
            try:
                if i in truth_app[edge]:
                    truth_graphs[i].add_edge(*edge)
            except KeyError:
                pass

            try:
                if i in false_app[edge]:
                    false_graphs[i].add_edge(*edge)
            except KeyError:
                pass
        '''
        try:
            number_true = len(truth_app[edge])
            truth = sum(filter(lambda x: x not in truth_app[edge], truth_spreads))
        except KeyError:
            truth, number_true = 0, 1

        try:
            number_false = len(false_app[edge])
            lie = sum(filter(lambda x: x not in false_app[edge], false_spreads))
        except KeyError:
            lie, number_false = 0, 1
        
        gain = lie_g - truth_g - (lie / number_false - truth / number_true)
        '''

        if gain > initial[1]:
            initial = (edge, gain)

    if initial[0] == (0, 0):
        print('sad, no more')
        break
    else:
        edge = initial[0]
        number_t = number
        if edge[0] in seeds and len(prob_edges[edge[1]]) > 1:
            edges_removed.add((edge, prob_edges[edge[1]][-1]))
            number_t = prob_edges[edge[1]][-1] * number
            del prob_edges[edge[1]][-1]
        else:
            edges_removed.add(edge)
            edges.remove(edge)

        for i in range(number_t):
            try:
                if i in truth_app[edge]:
                    truth_graphs[i].remove_edge(*edge)
            except KeyError:
                pass
            try:
                if i in false_app[edge]:
                    false_graphs[i].remove_edge(*edge)
            except KeyError:
                pass

        del truth_app[edge]
        del false_app[edge]
        k -= 1

print(edges_removed)
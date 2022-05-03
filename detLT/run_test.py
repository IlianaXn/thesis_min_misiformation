import networkx as nx
import math
from numpy import random
from deterministic_LT import deterministic_LT
from random_removal import random_removal
from weighted import weighted_removal
from edge_betweenness import edge_betweenness_diff

# path = 'graphs/test.txt'
path = '../create_graphs/graphs/email-Eu-core_LT.txt'
with open(path) as file:
    lines = file.readlines()


graph = nx.parse_edgelist(lines, nodetype=int, create_using=nx.DiGraph)

nodes = set(graph.nodes())
size = math.ceil(0.01 * len(nodes))
# seeds_truth = set(random.choice(len(nodes), size, replace=False).flatten())
seeds_truth = {512, 97, 65, 867, 102, 327, 360, 559, 150, 535, 574}

# seeds_false = set(random.choice(len(nodes), size, replace=False).flatten())
seeds_false = {2, 902, 903, 648, 809, 616, 822, 438, 669, 958, 511}

expertise = {}
with open('../expertise/values.txt') as file:
    i = 0
    for line in file:
        exp = float(line)
        expertise[i] = (min(exp, 1 - exp), exp)
        i += 1
        if i == len(nodes):
            break

edges = len(graph.edges())
k = math.ceil(0.03 * edges)
# k = 5295

print("Seeds truth:", seeds_truth)
print("Seeds false:", seeds_false)
print("k:", k)

print('start')
results, dur = edge_betweenness_diff(graph, expertise, seeds_truth, seeds_false, k)
print(results)
print(dur, 's')
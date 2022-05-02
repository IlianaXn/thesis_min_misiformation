import networkx as nx
import math
from numpy import random
from LT_solution import probabilistic_LT
from random_removal import random_removal
from distance import distance_diff
from weighted import weighted_removal

# path = 'graphs/test.txt'
path = '../create_graphs/graphs/facebook_combined_LT.txt'
with open(path) as file:
    lines = file.readlines()

graph = nx.parse_edgelist(lines, nodetype=int, create_using=nx.DiGraph)

nodes = set(graph.nodes())
size = math.ceil(0.01 * len(nodes))
# seeds_truth = set(random.choice(len(nodes), size, replace=False).flatten())
seeds_truth = {3203, 132, 3468, 2572, 525, 1676, 1040, 1808, 1041, 1558, 1431, 280, 665, 2077, 3103, 32, 2855, 2343, 2218, 4020, 316, 3139, 2121, 74, 3404, 3926, 3160, 347, 3679, 1120, 738, 2658, 3812, 996, 1510, 3682, 3305, 1516, 1012, 3445, 1015}

# seeds_false = set(random.choice(len(nodes), size, replace=False).flatten())
seeds_false = {3201, 1537, 259, 2820, 2182, 3592, 3851, 267, 141, 3863, 537, 2459, 3359, 2594, 3493, 3111, 4008, 433, 2355, 320, 68, 2503, 2888, 1738, 461, 2511, 3539, 3540, 469, 3804, 3420, 1376, 1513, 2923, 3436, 2926, 3951, 2675, 2548, 3452, 3199}

edges = len(graph.edges())
k = math.ceil(0.03 * edges)
# k = 5295

print("Seeds truth:", seeds_truth)
print("Seeds false:", seeds_false)
print("k:", k)

print('start')
# results_trees, dur = probabilistic_LT(graph, seeds_truth, seeds_false, k)
# print(results_trees)
# print(dur, 's')
results_random, dur = distance_diff(graph, seeds_truth, seeds_false, k)
print(results_random)
print(dur, 's')
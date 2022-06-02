import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

fb = nx.read_edgelist("graphs/facebook_combined.txt")
eu = nx.read_edgelist("graphs/email-Eu-core.txt")
wiki = nx.read_edgelist("graphs/Wiki-Vote.txt")

eu.remove_edges_from(nx.selfloop_edges(eu))
isol = list(nx.isolates(eu))
eu.remove_nodes_from(isol)


def find_degree(G):
    return nx.degree_centrality(G)

names = ['email-Eu-core', 'Social circles: Facebook', 'Wikipedia vote']
graphs = [fb, wiki, eu]
degrees = []
for g in graphs:
    n = len(g.nodes())
    degrees.append(list(map(lambda x: x*n, list(find_degree(g).values()))))

fig, axs = plt.subplots(1, 3, figsize=(10, 5))
for i in range(3):
  axs[i % 3].hist(degrees[i])
  axs[i % 3].set_title(names[i])
  axs[i % 3].set_xlabel('Degree')
  axs[i % 3].set_ylabel('#Nodes')

#
fig.tight_layout()
fig.show()
fig.savefig('degree_distr.png')
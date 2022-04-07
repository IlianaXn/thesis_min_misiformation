import networkx as nx


def merge(seeds: list, original: nx.DiGraph) -> tuple[nx.DiGraph, dict[list[float]]]:
    output = nx.DiGraph(original)
    new_node = seeds[0]
    out_edges = output.edges(seeds, data=True)
    probs = dict()
    nums_prob = dict()
    seeds = set(seeds)
    for _, node2, attr in out_edges:
        if node2 not in seeds:
            try:
                probs[node2].append(attr['weight'])
            except KeyError:
                probs[node2] = [attr['weight']]

    for node in probs.keys():
        total = 0
        nums_prob[node] = []
        for prob in probs[node]:
            total = total + (1 - total) * prob
            nums_prob[node].append(prob)
        nums_prob[node].sort()
        probs[node] = total

    edges = []
    for node2, prob in probs.items():
        edges.append((new_node, node2, prob))

    output.remove_nodes_from(seeds)
    output.add_node(new_node)
    output.add_weighted_edges_from(edges)

    return output, nums_prob

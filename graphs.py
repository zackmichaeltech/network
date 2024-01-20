import networkx as nx
import random
import matplotlib.pyplot as plt

def generate_weighted_small_world(n_nodes, k, p, weight_range=(1, 10)):
    """
    Generate a weighted small-world graph.

    :param n_nodes: Number of nodes in the graph.
    :param k: Each node is connected to k nearest neighbors in ring topology.
    :param p: The probability of rewiring each edge.
    :param weight_range: Tuple indicating the range of weights (inclusive).
    :return: A NetworkX graph with weights assigned to edges.
    """
    # Generate a small-world graph
    G = nx.watts_strogatz_graph(n_nodes, k, p)
    
    # Assign random weights
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(*weight_range)
    
    return G



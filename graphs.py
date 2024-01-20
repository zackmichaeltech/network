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
    
    pos = nx.spring_layout(G)  # positions for all nodes

    return G, pos


import networkx as nx
import matplotlib.pyplot as plt

def generate_grid_graph(m, n, weight_range=(1, 10)):
    """
    Generate a city grid graph with weighted edges and enumerated node positions.

    :param m: Number of rows (height of the grid).
    :param n: Number of columns (width of the grid).
    :param weight_range: Tuple indicating the range of weights (inclusive).
    :return: A NetworkX graph representing a city grid and positions for each node.
    """
    # Create an empty graph
    G = nx.Graph()

    # Add nodes and edges to create a grid
    for i in range(m * n):
        G.add_node(i)
        if i % n != 0:  # Add edge to the left node if not on the left edge
            G.add_edge(i, i - 1)
        if i >= n:  # Add edge to the top node if not on the top edge
            G.add_edge(i, i - n)

    # Assign random weights to edges
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(*weight_range)

    # Generate positions for each node in a grid layout
    pos = {i: (i % n, m - 1 - i // n) for i in range(m * n)}

    return G, pos

import networkx as nx
import matplotlib.pyplot as plt
import random

def generate_example_city():
    """
    Generate a city graph with weighted edges, representing important stops (like train stations).
    Nodes are positioned in a way that resembles a natural city layout.
    
    :return: A NetworkX graph representing a city with important stops and positions for each node.
    """
    # Create an empty graph
    G = nx.Graph()

    # Define node labels and positions (x, y coordinates)
    stations = {
        0: {"pos": (1, 1), "label": "Central Station"},
        1: {"pos": (4, 1), "label": "Parkside"},
        2: {"pos": (1, 3), "label": "Downtown"},
        3: {"pos": (3, 4), "label": "Uptown"},
        4: {"pos": (5, 3), "label": "Eastend"},
        5: {"pos": (5, 5), "label": "Industry Zone"},
        6: {"pos": (4, 7), "label": "Hilltop"},
        7: {"pos": (1, 7), "label": "Suburbia"},
        8: {"pos": (2, 5), "label": "Old Town"},
        9: {"pos": (7, 1), "label": "Riverside"},
    }

    # Add nodes to the graph
    for node, attrs in stations.items():
        G.add_node(node, **attrs)

    # Define edges between nodes (u, v) and assign random weights
    edges = [
        (0, 1), (0, 2), (1, 4), (2, 3), (2, 8), 
        (3, 4), (3, 5), (3, 6), (3, 8), (4, 9),
        (5, 6), (7, 8)
    ]

    for (u, v) in edges:
        G.add_edge(u, v, weight=random.randint(1, 10))

    # Extract positions from node attributes for plotting
    pos = nx.get_node_attributes(G, 'pos')

    return G, pos

# Generate the city graph
G, pos = generate_example_city()


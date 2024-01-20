import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.collections import LineCollection
import numpy as np
import graphs

# Create a graph
n_nodes = 10
k = 4  # Number of nearest neighbors
p = 0.5  # Probability of rewiring
G = graphs.generate_weighted_small_world(n_nodes, k, p)

edges = [(1, 2, 1.0), (2, 3, 1.0), (3, 4, 1.0), (1, 4, 4.0), (2, 4, 2.5)]
G.add_weighted_edges_from(edges)

pos = nx.spring_layout(G)  # positions for all nodes

# Dijkstra's algorithm
path = nx.dijkstra_path(G, source=1, target=4)
path_edges = list(zip(path, path[1:]))

# Prepare plot
fig, ax = plt.subplots()
plt.axis('off')

# Draw the base graph (nodes, edges, labels)
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, edgelist=edges, width=6)
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)})

# Create a LineCollection for the path, initially empty
lc = LineCollection([], colors='r', linewidths=6)
ax.add_collection(lc)

# Function to get LineCollection segments for a list of edges
def edge_segments(edges):
    return [np.array([pos[u], pos[v]]) for u, v in edges]

# Animation update function
def update(num):
    if num > 0:
        lc.set_segments(edge_segments(path_edges[:num]))
    return lc,

# Animate
ani = FuncAnimation(fig, update, frames=len(path_edges) + 1, interval=1000, blit=True)

plt.show()

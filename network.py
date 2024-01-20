import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.collections import LineCollection
import numpy as np
import graphs

# Create a graph
n_nodes = 5
# k = 4  # Number of nearest neighbors for small world
# p = 0.5  # Probability of rewiring for small world
# G, pos = graphs.generate_weighted_small_world(n_nodes, k, p)

m_nodes = 5
G, pos = graphs.generate_example_city()

# Dijkstra's algorithm
path = nx.dijkstra_path(G, source=1, target=8)
path_edges = list(zip(path, path[1:]))

# Prepare plot
fig, ax = plt.subplots()
plt.axis('off')

nx.draw(G, pos, with_labels=False, node_size=700, node_color='lightblue')
nx.draw_networkx_labels(G, pos, {i: G.nodes[i]['label'] for i in G.nodes()}, font_size=10)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("City Train Stations")

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

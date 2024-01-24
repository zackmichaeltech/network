# network.py
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.collections import LineCollection
import numpy as np
import graphs

# Create a graph
# G, pos = graphs.generate_weighted_small_world(n_nodes, k, p)
G, pos = graphs.generate_example_city()

# Dijkstra's algorithm
path = nx.dijkstra_path(G, source=1, target=5)
path_edges = list(zip(path, path[1:]))

# Make some visual choices
# Prepare plot with transparent background
fig, ax = plt.subplots()
fig.patch.set_facecolor('w')
ax.patch.set_facecolor('w')
plt.axis('off')

# Set figure size for HD resolution
fig.set_size_inches(1920 / fig.dpi, 1080 / fig.dpi)
# Reduce padding around the graph
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)


# Create a LineCollection for the path, initially empty
lc = LineCollection([], colors='r', linewidths=20)
ax.add_collection(lc)
lc.set_zorder(1)  # Set zorder for the path

# Node colors and sizes
node_color = '#FFA07A'  # Light salmon color for nodes
node_border_color = 'k'  # Black border for nodes
node_size = 5000

# Edge colors and widths
edge_color = '#20B2AA'  # Light Sea Green color for edges
edge_width = 10

# Draw edges with increased thickness
edges_collection = nx.draw_networkx_edges(G, pos, edge_color=edge_color, width=edge_width)
edges_collection.set_zorder(2)  # Set zorder for edges collection

# Draw nodes with a border
nodes = nx.draw_networkx_nodes(G, pos, node_color=node_color, edgecolors=node_border_color, linewidths=1, node_size=node_size)
nodes.set_zorder(3)

# Text box configuration
box = dict(boxstyle='round,pad=0.3', fc='white', ec='k', lw=1)

# Draw node labels with text boxes
labels = nx.draw_networkx_labels(G, pos, {i: G.nodes[i]['label'] for i in G.nodes()}, font_size=30, font_color='k', bbox=box)
for label in labels.values():
    label.set_zorder(4)

# Get edge attributes
edge_weights = nx.get_edge_attributes(G, 'weight')
edge_names = nx.get_edge_attributes(G, 'name')

# Draw edge labels with weights and names and text boxes
for edge, weight in edge_weights.items():
    label = f"{edge_names[edge]} ({weight})"
    pos_mid = ((pos[edge[0]][0] + pos[edge[1]][0]) / 2, (pos[edge[0]][1] + pos[edge[1]][1]) / 2)
    plt.text(pos_mid[0], pos_mid[1], label, horizontalalignment='center', verticalalignment='center', fontsize=24, bbox=box, zorder=5)

plt.title("City Train Stations")

# Save the still figure as a .png
plt.savefig('city_still.png', dpi=100)

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

# Save the animation as a gif
ani.save('city_path_animation.gif', writer=PillowWriter(fps=2), dpi=100, savefig_kwargs={'transparent': True})

# plt.show()

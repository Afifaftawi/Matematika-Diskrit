import networkx as nx
import matplotlib.pyplot as plt

#buat graf kosong
G = nx.Graph()

#tambahkan simpul (nodes) dan sisi (edges)
G.add_edges_from ([('A','B'), ('A','C'), ('B','C'), ('C','D'), ('D','A')])

#gambarkan graf
plt.figure(figsize=(6, 4))
nx.draw (G, with_labels = True, node_color = 'lightblue', edge_color = 'red',node_size = 800)
plt.title ("REPRESENTASI GRAF")
plt.show()

#tampilkan adjacency list
print("adjacency list")
for node in G.adj:
  print (f"{node}: {list(G.adj[node])}")

n = 6
for i in range(1, n):
    if i % 2:
        print(i % 2)



# for i in range(bn):
#     for j in range(bn):
#         if not i == j:
#             if links.count([i, j]):
#                 G.add_edge(i + 1, j + 1, weight = 1)
#             else:
#                 G.add_edge(i + 1, j + 1, weight = )
# for edge in links:
#     G.edges[edge]['weight'] = 1

# print(G.number_of_nodes(), G.number_of_edges(), list(G.nodes), list(G.edges),
#       nx.clustering(G), nx.connected_components(G), sep = "\n")
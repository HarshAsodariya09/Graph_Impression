import pandas as pd
import networkx as nx

# Read the CSV file into a DataFrame
impression = pd.read_csv('impression_2.csv')

# Create an empty graph
G = nx.Graph()

# Add edges between nodes based on connections in the DataFrame
for col in impression.columns[1:]:
    for source, target in zip(impression['Email Address'], impression[col]):
        if pd.notna(target):
            G.add_edge(source, target)

# Calculate betweenness centrality of nodes
betweenness_centrality = nx.betweenness_centrality(G)

# Print the betweenness centrality of each node with a serial number
print("Serial\tNode\tBetweenness Centrality")
for i, (node, centrality) in enumerate(sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True), 1):
    print(f"{i}\t{node}\t{centrality}")
print()
print()
# Calculate clustering coefficient for each node
clustering_coefficients = nx.clustering(G)

# Sort the nodes based on their clustering coefficients in descending order
sorted_nodes = sorted(clustering_coefficients, key=clustering_coefficients.get, reverse=True)

# Print the ranked nodes and their clustering coefficients
print("Rank\tNode\tClustering Coefficient")
for rank, node in enumerate(sorted_nodes, start=1):
    coefficient = clustering_coefficients[node]
    print(f"{rank}\t{node}\t{coefficient}")

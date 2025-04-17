import pandas as pd
import random

# Read the CSV file into a DataFrame
impression = pd.read_csv('impression_2.csv')

# Get unique email addresses from column 'Email Address'
nodes = impression['Email Address'].unique()

# Create a dictionary to store connections
connections = {}

# Iterate over each column (except the first one) to find connections
for col in impression.columns[1:]:
    for source, target in zip(impression['Email Address'], impression[col]):
        if pd.notna(target):
            if source not in connections:
                connections[source] = set()
            connections[source].add(target)

# Perform random walks with teleportation
num_walks = 1000000
visited_nodes = []
for _ in range(num_walks):
    # Choose a random starting node
    current_node = random.choice(nodes)
    visited_nodes.append(current_node)
    while True:
        # Introduce teleportation with probability 0.15
        if random.random() < 0.15:
            # Choose a completely random node
            current_node = random.choice(nodes)
        else:
            # Get connected nodes
            connected_nodes = connections.get(current_node, [])
            if not connected_nodes:
                # If no connected nodes, break the loop
                break
            # Move to a random connected node
            current_node = random.choice(list(connected_nodes))
        visited_nodes.append(current_node)

# Count visits to each node
node_counts = pd.Series(visited_nodes).value_counts()

# Print visited nodes with ranks and counts
print("Rank\tEmail Address\t\tCount")
for rank, (node, count) in enumerate(node_counts.items(), start=1):
    print(f"{rank}\t{node}\t\t{count}")
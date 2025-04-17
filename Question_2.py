#importing the required libraries
import pandas as pd
import networkx as nx
import numpy as np
import random
    

# Read the CSV file into a DataFrame
impression = pd.read_csv('impression_2.csv')

# Create an empty directed graph
G = nx.DiGraph()

# Add edges between nodes based on connections in the DataFrame
for col in impression.columns[1:]: # Iterate over each column (except the first one) to find connections
    for source, target in zip(impression['Email Address'], impression[col]): # Iterate over each row to get source and target nodes
        if pd.notna(target):
            G.add_edge(source, target)
            
rating = nx.pagerank(G) # Calculate PageRank values for each node
ranking = sorted(rating, key=rating.get, reverse=True) # Sort nodes by PageRank value in descending order
print()
print("Top 10 nodes with their PageRank values:- ")
for i in range(1,11): # Print the top 10 nodes with their PageRank values
    name =  ranking[i-1] 
    rate = rating[name]
    print(i,' ',name,'  ',rate)

# Convert the graph to an adjacency matrix
adj_matrix = nx.to_numpy_array(G, nodelist=sorted(G.nodes())) # Convert the graph to an adjacency matrix

'''take random zeros form the adj_matrix and use linear regression to find the missing values , if 
it's greater than 0.5 then replace it with 1 else 0'''

def remove_row_column(matrix, i, j): # Function to remove a row and column from a matrix
    return np.delete(np.delete(matrix, i, 0), j, 1)

def get_row(matrix, i): # Function to get a row from a matrix
    return matrix[i, :]

def get_column(matrix, j): # Function to get a column from a matrix
    return matrix[:, j]

n=len(adj_matrix)
#print(n)
nodes = list(G.nodes()) # Get the list of nodes in the graph

total_edges_added=0 # Initialize the total number of edges added to 0

def main(): # Main function to fill missing values in the adjacency matrix
    global total_edges_added # Declare total_edges_added as a global variable
    for j in range(0,n): #iterating over each element of the matrix by nested loop
        for i in range(0,n):
            if adj_matrix[i][j]==0:
                small_matrix=remove_row_column(adj_matrix,i,j) #removing the row and column of the missing value
                row_mat=np.delete(get_row(adj_matrix,i), j, axis=0) #getting the row of the missing value
                col_mat=np.delete(get_column(adj_matrix,j), i, axis=0) #getting the column of the missing value
                '''now i will make X matrix of coefficient and X^T*small_matrix^T = row_mat^T and then
                get the value of X by lstsq method and getting the value of missing value by multiplying
                X with col_mat if it's greater than 0.5 then replace it with 1 else 0'''
                X = np.linalg.lstsq(small_matrix.T, row_mat.T, rcond=None)[0] # Solve for X using least squares method
                value=np.dot(X.T,col_mat) # Calculate the missing value
                if value>0.5: # If the missing value is greater than 0.5
                    total_edges_added+=1 
                    G.add_edge(nodes[i], nodes[j]) # Add an edge between the nodes
                    adj_matrix[i][j]=1
                else:
                    adj_matrix[i][j]=0

main() # Call the main function to fill missing values in the adjacency matrix
print()
rating = nx.pagerank(G) # Calculate PageRank values for each node
ranking = sorted(rating, key=rating.get, reverse=True) # Sort nodes by PageRank value in descending order
print("Top 10 nodes with their PageRank values after transformation :- ")
print()
for i in range(1,11): # Print the top 10 nodes with their PageRank values
    name =  ranking[i-1]
    rate = rating[name]
    print(i,name, rate)
print()
print()
print("Total edges added:",total_edges_added) # Print the total number of edges added
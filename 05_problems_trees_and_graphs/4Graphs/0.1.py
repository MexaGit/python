from collections import defaultdict

def build_graph(edges):
    # Initialize a default dictionary where each key will have an empty list by default
    graph = defaultdict(list)

    # Iterate over each pair of edges (x, y)
    for x, y in edges:
        graph[x].append(y)  # Add edge from node x to node y
        # graph[y].append(x)  # Uncomment this line if the graph is undirected

    return graph

# Example usage of the build_graph function:
# Given edges representing a directed graph:
# 1 -> 2
# 1 -> 3
# 2 -> 4
# 3 -> 4

edges = [(1, 2), (1, 3), (2, 4), (3, 4)]

graph = build_graph(edges)
print(dict(graph))  # Output: {1: [2, 3], 2: [4], 3: [4]}

# Test case 2 (undirected graph):
# Uncomment the line `graph[y].append(x)` to make it an undirected graph
# Now the graph should represent:
# 1 -- 2
# 1 -- 3
# 2 -- 4
# 3 -- 4

graph_undirected = build_graph(edges)
# print(dict(graph_undirected)) # Output: {1: [2, 3], 2: [4], 3: [4]}

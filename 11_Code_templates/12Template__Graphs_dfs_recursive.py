# DFS (Depth-First Search) recursion
def fn(graph):
    def dfs(node):
        ans = 0  # Initialize answer for this node

        # Explore all neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in seen:  # If the neighbor hasn’t been visited
                seen.add(neighbor)  # Mark the neighbor as visited
                ans += dfs(neighbor)  # Recursively explore the neighbor

        return ans  # Return the result of this DFS call

    seen = {START_NODE}  # Initialize the set of visited nodes with the start node
    return dfs(START_NODE)  # Start the DFS from the starting node

# What Does This Code Do?
# This code explores a graph starting from START_NODE using DFS recursion. The graph can have cycles,
# so we use a seen set to keep track of which nodes have already been visited. The DFS function processes each node,
# explores all its neighbors, and returns the accumulated result (which is stored in ans).

"""
How Does DFS Work in This Code?
Recursive Exploration:
    For each node, the code looks at all its neighbors.
    If a neighbor hasn’t been visited yet (not in seen), we:
        Mark it as visited.
        Recursively call dfs() on that neighbor to explore deeper.
        Accumulate the result in ans.
Return the Accumulated Answer:
    Each dfs() call returns a value, and the results are summed up across all neighbors.
The seen Set:
    Ensures that each node is visited only once (avoiding cycles).
"""
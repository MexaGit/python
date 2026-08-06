from typing import List

class Solution:
    # Depth-First Search (DFS) function
    def dfs(self, adjList: List[List[int]], visited: List[int], src: int) -> None:
        visited[src] = 1  # Mark the current node as visited

        # Visit all the neighbors of the current node
        for neighbor in adjList[src]:
            if visited[neighbor] == 0:  # If neighbor is not visited
                self.dfs(adjList, visited, neighbor)

    # Function to count connected components
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0  # If no nodes, there are no components

        components = 0  # To count the number of connected components
        visited = [0] * n  # To track visited nodes
        adjList = [[] for _ in range(n)]  # Adjacency list to represent the graph

        # Build the adjacency list from edges
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        # Iterate over all nodes
        for i in range(n):
            if visited[i] == 0:  # If the node is not visited
                components += 1  # A new component is found
                self.dfs(adjList, visited, i)  # Perform DFS to visit all nodes in this component

        return components  # Return the total number of connected components

# Example usage:
solution = Solution()

# Test case 1
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(solution.countComponents(n, edges))  # Output: 2
# Explanation: There are two connected components: [0, 1, 2] and [3, 4].

# Test case 2
n = 4
edges = [[0, 1], [2, 3]]
print(solution.countComponents(n, edges))  # Output: 2
# Explanation: There are two connected components: [0, 1] and [2, 3].

# Test case 3
n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
print(solution.countComponents(n, edges))  # Output: 1
# Explanation: All nodes are part of a single connected component.

"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates
that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

#---------------------------------------------------------------------------------------------------#

Approach 1: Depth-First Search (DFS)
Intuition
If you're not familiar with DFS, check out our Explore Card.

In an undirected graph, a connected component is a subgraph in which each pair of vertices is connected via a path.
So essentially, all vertices in a connected component are reachable from one another.

Let's see how we can use DFS to solve the problem. If we run DFS, starting from a particular vertex, it will continue
to visit the vertices depth-wise until there are no more adjacent vertices left to visit. Thus, it will visit
all of the vertices within the connected component that contains the starting vertex. Each time we finish exploring
a connected component, we can find another vertex that has not been visited yet, and start a new DFS from there.
The number of times we start a new DFS will be the number of connected components.

Algorithm

1. Create an adjacency list such that adj[v] contains all the adjacent vertices of vertex v.
2. Initialize a hashmap or array, visited, to track the visited vertices.
3. Define a counter variable and initialize it to zero.
4. Iterate over each vertex in edges, and if the vertex is not already in visited, start a DFS from it. Add every vertex visited during the DFS to visited.
5. Every time a new DFS starts, increment the counter variable by one.
6. At the end, the counter variable will contain the number of connected components in the undirected graph.
"""
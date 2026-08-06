from collections import defaultdict, deque
from typing import List

class Solution:
    # Depth First Search (DFS): Recursive
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = [False] * n

        def dfs(curr_node):
            if curr_node == destination:
                return True
            if not seen[curr_node]:
                seen[curr_node] = True
                for next_node in graph[curr_node]:
                    if dfs(next_node):
                        return True
            return False

        return dfs(source)

# Test cases
# Test case 1
n = 6
edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
source = 0
destination = 5
solution = Solution()
print(solution.validPath(n, edges, source, destination))  # Output: False
# Explanation: There is no path from node 0 to node 5 in the graph.

# Test case 2
n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2
print(solution.validPath(n, edges, source, destination))  # Output: True
# Explanation: There is a path from node 0 to node 2 in the graph.

# Test case 3
n = 1
edges = []
source = 0
destination = 0
print(solution.validPath(n, edges, source, destination))  # Output: True
# Explanation: The source and destination are the same, so the path is trivially valid.

"""
https://leetcode.com/problems/find-if-path-exists-in-graph/description/
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes
a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge,
and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to
destination, or false otherwise.
"""
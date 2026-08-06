from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Initialize an indegree array with 0 for all nodes
        indegree = [0] * n

        # Calculate the indegree of each node
        for _, y in edges:  # We only care about the destination (y) in each edge (x, y)
            indegree[y] += 1

        # Return the list of nodes that have an indegree of 0
        # These nodes are the ones with no incoming edges and thus must be in the smallest set of vertices
        return [node for node in range(n) if indegree[node] == 0]

# Example usage and test cases
# Test case 1
n = 6
edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
# Explanation: Nodes 0 and 3 have no incoming edges. Therefore, these are the nodes to include.
solution = Solution()
print(solution.findSmallestSetOfVertices(n, edges))  # Output: [0, 3]

# Test case 2
n = 5
edges = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
# Explanation: Nodes 0, 2, and 3 have no incoming edges. Therefore, these are the nodes to include.
print(solution.findSmallestSetOfVertices(n, edges))  # Output: [0, 2, 3]

# Test case 3
n = 3
edges = [[0, 1], [0, 2]]
# Explanation: Only node 0 has no incoming edges.
print(solution.findSmallestSetOfVertices(n, edges))  # Output: [0]

"""
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where 
edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique
 solution exists.

Notice that you can return the vertices in any order.

#---------------------------------------------------------------------------------------------#
The problem wants the smallest set of nodes from which all other nodes can be reached. This can be rephrased 
as the smallest set of nodes that cannot be reached from other nodes, because if a node can be reached from another 
node, then we would rather just include the "parent" rather than the "child" in our set.

A node cannot be reached from another node if it has an indegree of 0 (no edges are entering the node). 
Therefore, we can just find the indegree of all nodes and only include the ones with a zero indegree.

Note: if the graph had cycles, we would run into some edge cases. Imagine if the graph was just one cycle (a circle).
Which node do we return? Technically, returning any of them would be correct. Our algorithm, however, 
would return nothing because none of the nodes would have an indegree of 0. Fortunately, the given graph is acyclic,
so we don't have to worry about these cases.

This example doesn't require a DFS, but is a good exercise to better understand the mechanics of graphs. 
These are all the examples we'll be looking at in this article - try the upcoming practice problems on your 
own before moving on to BFS.
"""

from collections import defaultdict
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Set to store the roads with directed edges (x -> y)
        roads = set()

        # Graph to store undirected connections (adjacency list)
        graph = defaultdict(list)

        # Build the graph and roads set
        for x, y in connections:
            graph[x].append(y)  # Add the directed road x -> y
            graph[y].append(x)  # Add the undirected reverse path y -> x for traversal
            roads.add((x, y))  # Track the roads that need to be checked for reordering

        # Depth-First Search (DFS) function to traverse the graph
        def dfs(node):
            ans = 0
            # Traverse through each neighbor of the current node
            for neighbor in graph[node]:
                if neighbor not in seen:
                    # If the road needs reordering, increment the answer
                    if (node, neighbor) in roads:
                        ans += 1
                    seen.add(neighbor)  # Mark the neighbor as visited
                    ans += dfs(neighbor)  # Recursively check for other neighbors

            return ans

        # Set to keep track of visited nodes, starting with node 0
        seen = {0}
        # Perform DFS from node 0 (the capital)
        return dfs(0)

# Example usage and test cases

# Test case 1
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Explanation: We need to reorder roads [1 -> 3] and [4 -> 0].
solution = Solution()
print(solution.minReorder(n, connections))  # Output: 3

# Test case 2
n = 5
connections = [[1, 0], [1, 2], [3, 2], [3, 4]]
# Explanation: We need to reorder road [1 -> 2].
print(solution.minReorder(n, connections))  # Output: 1

"""
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between
two different cities (this network form a tree). Last year, The ministry of transport decided to orient
the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.
This year, there will be a big event in the capital (city 0), and many people want to travel to this city.
Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number
of edges changed.
It's guaranteed that each city can reach city 0 after reorder.

"""
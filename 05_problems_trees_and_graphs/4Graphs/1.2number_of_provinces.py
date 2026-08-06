from collections import defaultdict
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # or implement the DFS iteratively,
        # you can just modify the dfs function while keeping everything else the same
        def dfs(start):
            stack = [start]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)

        # Step 1: Build the graph
        n = len(isConnected)  # Get the number of nodes (cities)
        graph = defaultdict(list)  # Create a default dictionary to store the graph

        # Loop through the matrix to add edges between connected cities
        for i in range(n):
            for j in range(i + 1, n):  # Check only the upper triangle of the matrix (since it's symmetric)
                if isConnected[i][j]:  # If city i and city j are connected
                    graph[i].append(j)  # Add an edge between i and j
                    graph[j].append(i)  # Since it's undirected, add an edge from j to i too

        # Step 2: Initialize a set to keep track of visited nodes and a counter for the number of provinces
        seen = set()  # Keep track of the cities we've visited
        ans = 0  # This will count the number of connected components (provinces)

        # Step 3: Loop through all nodes to perform DFS if they haven't been visited
        for i in range(n):
            if i not in seen:  # If city i has not been visited, it's part of a new province
                # add all nodes of a connected component to the set
                ans += 1  # Increment the number of provinces
                seen.add(i)  # Mark city i as visited
                dfs(i)  # Perform DFS to mark all cities in this province as visited

        return ans  # Return the total number of provinces

# Example usage:
# Test case 1
isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [1, 1, 0]
]
# Explanation: There are two provinces: [0, 1] and [2].
solution = Solution()
print(solution.findCircleNum(isConnected))  # Output: 2

# Test case 2
isConnected = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 1, 1]
]
# Explanation: There is one province, as all cities are connected.
print(solution.findCircleNum(isConnected))  # Output: 1
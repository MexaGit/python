from collections import defaultdict
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Depth-First Search (DFS) function to explore all connected nodes
        def dfs(node):
            for neighbor in graph[node]:
                # Check if the neighbor has already been visited to prevent cycles
                # the next 2 lines are needed to prevent cycles
                if neighbor not in seen:
                    seen.add(neighbor)  # Mark the neighbor as visited
                    dfs(neighbor)  # Recursively visit the neighbor

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
    [0, 0, 1]
]
# Explanation: There are two provinces: [0, 1] and [2].
solution = Solution()
print(solution.findCircleNum(isConnected))  # Output: 2

# Test case 2
isConnected = [
    [1,0,0],
    [0,1,0],
    [0,0,1]
]
# Explanation: There is one province, as all cities are connected.
print(solution.findCircleNum(isConnected))  # Output: 3

"""
https://leetcode.com/problems/number-of-provinces/description/
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b,
and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly
connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

#---------------------------------------------------------------------------------------------#

We are told that there are n cities, with some cities being connected.
We can treat each of the cities as a node, with each city labeled between 0 to n - 1.

The connections (edges) are given to us in the input. Before we start any traversal, we can first build a graph 
so that we can easily access any given node's neighbors. If this is your first time solving graph problems, 
don't worry. This is a standard first step and the code used to do it is very similar across all problems. 
We iterate over all pairs of cities (i, j), and if isConnected[i][j] = 1, we add an undirected edge between i and j.

Next, how do we count the provinces? In a province, you can start at any city and find a path to reach any other city.
 This means that they form a connected component.

With an undirected graph, a traversal on a given node will visit every node in the connected component 
node belongs to. This is a property you can memorize, but it also makes sense if you think about it. 
Remember that in a binary tree, if you did a traversal starting from the root, you would visit every node in the tree.

Knowing that a DFS will visit every node in a connected component, we can use a data structure seen to tell us which 
cities we have already visited. This is another standard idea in all graph problems to avoid visiting a node multiple
times. When we are performing the traversal and are at a given node, we iterate over the neighbors. 
For each neighbor, we first check if neighbor has been visited. If it has, we ignore it. If it hasn't, 
we mark it as visited in seen and then recursively call dfs(neighbor) (just like we did with binary trees).

We iterate over the cities, and if we find a city i is not visited yet, we can perform a DFS starting from i. 
As we know, this traversal will visit every node in the connected component that i belongs 
to (aka, the province that i belongs to). After the traversal, seen will be updated with the entire province. 
We can increment the answer, and we don't need to worry about the province we just visited anymore because 
seen will prevent us from revisiting it.
"""
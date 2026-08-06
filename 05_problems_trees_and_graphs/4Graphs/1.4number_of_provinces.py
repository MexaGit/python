from collections import defaultdict  # This is like having a magical box, default value for non-existent key
from typing import List  # Helps tell Python that we are working with a list of lists (for cities)

class Solution:  # We are creating a "Solution" blueprint where we can store our cool solution logic!
    def findCircleNum(self, isConnected: List[List[int]]) -> int:  # This function solves the problem!
        # Step 1: Build the graph (like drawing cities connected by roads!)
        n = len(isConnected)  # Find how many cities we have in total

        graph = defaultdict(list)  # Prepare a magical dictionary to store our roads

        # Loop through the matrix to add edges (roads) between connected cities
        for i in range(n):  # For every city i...
            for j in range(i + 1, n):  # Check cities ahead of i (so we don’t repeat work)
                # knows whether isConnected[i][j] is 1 or 0 in the matrix.
                # This evaluates truthy = 1 and falsy = 0 values.
                if isConnected[i][j]:  # If there's a road between city i and city j...
                    graph[i].append(j)  # Add j to i's list of connected cities
                    graph[j].append(i)  # Add i to j's list too (because roads go both ways)

        # Step 2: Get ready to explore! We need a "seen" set and an "ans" counter
        seen = set()  # This is our "visited cities" list
        ans = 0  # This will count the number of groups (provinces)

        # Step 3: Time to visit each city to find all the provinces! ensures we don’t miss any provinces.
        for i in range(n):  # Loop through all cities (from 0 to n-1)
            if i not in seen:  # If City i hasn’t been visited yet...
                ans += 1  # We found a new province, so increment the answer

                stack = [i]  # Start with the current city (i) in the stack
                seen.add(i)  # Mark the current city (i) as visited

                while stack:  # Keep exploring as long as there are cities in the stack
                    node = stack.pop()  # Take the last city from the stack (DFS) = 0

                    # node = 0, graph[0] = [1]
                    for neighbor in graph[node]:  # Explore all neighbors of the current city (node)
                        # neighbor = 1, seen = {0}
                        if neighbor not in seen:  # If the neighbor hasn’t been visited...
                            # seen = {0, 1}
                            seen.add(neighbor)  # Mark the neighbor as visited
                            # stack = [1]
                            stack.append(neighbor)  # Add the neighbor to the stack to explore later

        return ans  # Finally, tell how many provinces (groups) we found!

# Final Answer:
# Time complexity: O(n²) = Graph construction: O(n²) + DFS traversal: O(n) = O(n²) + O(n) ≈ O(n²)
# Space complexity: O(n²) = Graph storage: O(n²) + Seen set and stack: O(n) = O(n²) + O(n) ≈ O(n²)

# 🎮 Example playground scenarios:
# Test case 1: Three kids with two separate friend groups.
isConnected = [
    [1, 1, 0],  # Kid 0 is friends with Kid 1, but not Kid 2.
    [1, 1, 0],  # Kid 1 is friends with Kid 0, but not Kid 2.
    [0, 0, 1]   # Kid 2 is only friends with themselves (loner group).
]
solution = Solution()
print(solution.findCircleNum(isConnected))  # Output: 2

# Test case 2: Four kids who are all connected in one big group.
# graph = {
#     0: [3],
#     3: [0, 2],
#     1: [2],
#     2: [1, 3]
# }
isConnected = [
    [1, 0, 0, 1],  # Kid 0 is friends with Kid 3. graph = {0: [3], 3: [0]}
    [0, 1, 1, 0],  # Kid 1 is friends with Kid 2. graph = {0: [3], 3: [0], 1: [2], 2: [1]}
    [0, 1, 1, 1],  # Kid 2 is friends with Kids 1 and 3. graph = {0: [3], 3: [0, 2], 1: [2], 2: [1, 3]}
    [1, 0, 1, 1]   # Kid 3 is friends with Kids 0 and 2 (already reflected in previous steps).
]
print(solution.findCircleNum(isConnected))  # Output: 1

# First Loop (Building the Graph):
# The first loop over i and j constructs the graph using the isConnected matrix.
# This tells us who is connected to whom and makes it easier to explore the provinces.
#
# Second Loop (Finding the Provinces):
# The second loop iterates through each city to make sure that:
#   We explore all cities (nodes).
#   We count each province (group of connected cities) only once.
#   DFS/BFS exploration ensures that all connected cities in the same province are visited.

"""
We use a set for seen because:

Fast lookups (O(1)) ensure the algorithm runs efficiently.
No duplicates: Each city is only visited once.
Order doesn't matter: We only care about whether a city has been visited, not the order of visits.
"""

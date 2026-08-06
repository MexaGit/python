from typing import List  # We are working with lists of things, like groups of kids.

class Solution:
    # This is our explorer (DFS) who will visit all the kids in a group.
    def dfs(self, adjList: List[List[int]], visited: List[int], src: int) -> None:
        visited[src] = 1  # Mark this kid as "visited" so we don’t say hi twice.
        # here is most important line, where will change the visited: [0, 0, 0, 0, 0]
        # one by one example line 81

        # Now, go through each friend of this kid.
        for neighbor in adjList[src]:
            print(adjList[src])
            if visited[neighbor] == 0:  # If we haven’t met this friend yet...
                self.dfs(adjList, visited, neighbor)  # Go visit that friend too!
                # adjList: [[1], [0, 2], [1], [4], [3]]
                # visited: [0, 0, 0, 0, 0] (no one visited yet)
                # src: 0 (starting DFS from Kid 0)

    # This function counts how many friend groups (connected components) exist.
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:  # If there are no kids, there are no groups!
            return 0

        components = 0  # Start with zero groups of friends.
        visited = [0] * n  # Make a list to track which kids we have met.
        adjList = [[] for _ in range(n)]  # Create a list for each kid’s friends.
        # adj_list = []
        # for _ in range(n):
        #     adj_list.append([])  # Appending an empty list in each iteration

        # Let's add the handshakes between kids to their friend lists.
        for edge in edges: # edges = [[0, 1], [1, 2], [3, 4]]
            # adjList[edge[0]].append(edge[1])  # adjList[1].append(2)
            # adjList[edge[1]].append(edge[0])  # adjList[2].append(1)
            # adjList = [[1], [0, 2], [1], [], []]
            # adjList[edge[0]].append(edge[1])  # adjList[3].append(4)
            # adjList[edge[1]].append(edge[0])  # adjList[4].append(3)
            # adjList = [[1], [0, 2], [1], [4], [3]]
            adjList[edge[0]].append(edge[1])  # Kid A shakes hands with Kid B.
            adjList[edge[1]].append(edge[0])  # Kid B shakes hands with Kid A.

        # Now, let's explore the playground and see how many friend groups we have.
        for i in range(n):
            if visited[i] == 0:  # If we haven’t met this kid yet...
                # visited = [0, 0, 0, 0, 0]  # No kid has been visited yet.
                components += 1  # We found a new group of friends!
                print(adjList, visited, i)
                self.dfs(adjList, visited, i)  # Explore the entire group.

        return components  # After exploring, return the total number of groups.

# Example usage:
solution = Solution()

# Test case 1
n = 5
edges = [[0, 1], [1, 2], [3, 4]]  # Handshakes: (0-1), (1-2), and (3-4).
print(solution.countComponents(n, edges))  # Output: 2
# Explanation: There are two friend groups:
# Group 1: [0, 1, 2] (connected by handshakes)
# Group 2: [3, 4] (connected by a handshake)



"""
Possible Real-World Scenarios of the Same Problem:
Social Network Analysis
"You have n people and a list of friendships. Each friendship connects two people. Your task is to find 
how many friend groups exist, where everyone in the group is connected directly or indirectly."

This is the same graph problem:
    People = nodes
    Friendships = edges
    Connected components = number of friend groups
    
DFS Call on Kid 0:
Line 4: visited[0] = 1

Now:
visited = [1, 0, 0, 0, 0]  # Mark Kid 0 as visited.
Line 7: Explore Kid 0’s friends:

for neighbor in adjList[0]:  # neighbor = 1
Line 8: Check if Kid 1 is visited:


if visited[1] == 0:  # True, since visited[1] = 0
Line 9: Call DFS for Kid 1:


self.dfs(adjList, visited, 1)

DFS Call on Kid 1:
Line 4: visited[1] = 1

Now:
visited = [1, 1, 0, 0, 0]  # Mark Kid 1 as visited.
Line 7: Explore Kid 1’s friends:


for neighbor in adjList[1]:  # neighbors = [0, 2]
Line 8: Check if Kid 0 is visited:


if visited[0] == 0:  # False, since visited[0] = 1
Skip Kid 0 because it has already been visited.
Line 8: Check if Kid 2 is visited:


if visited[2] == 0:  # True, since visited[2] = 0
Line 9: Call DFS for Kid 2:


self.dfs(adjList, visited, 2)

DFS Call on Kid 2:
Line 4: visited[2] = 1

Now:
visited = [1, 1, 1, 0, 0]  # Mark Kid 2 as visited.
Line 7: Explore Kid 2’s friends:


for neighbor in adjList[2]:  # neighbor = 1
Line 8: Check if Kid 1 is visited:


if visited[1] == 0:  # False, since visited[1] = 1
Skip Kid 1 because it has already been visited.

then return to line 45
an start again but now with the number 3 for i
"""


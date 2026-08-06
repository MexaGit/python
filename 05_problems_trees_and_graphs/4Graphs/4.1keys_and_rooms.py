from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Depth-First Search (DFS) function
        def dfs(node):
            # Traverse through each key (neighbor) in the current room
            for neighbor in rooms[node]:
                # If the room hasn't been visited yet, mark it as visited and visit it
                if neighbor not in seen:
                    seen.add(neighbor)  # Mark this room as visited
                    dfs(neighbor)  # Recursively visit its connected rooms

        seen = {0}  # Set to store visited rooms, starting with room 0
        dfs(0)  # Start the DFS from room 0

        # After DFS, check if we have visited all the rooms
        return len(seen) == len(rooms)

# Example usage and test cases

# Test case 1
rooms = [[1], [2], [3], []]
# Explanation: You can visit room 0, then use key 1 to enter room 1, use key 2 to enter room 2, and use key 3 to
# enter room 3. Since we were able to visit every room, we return true.
solution = Solution()
print(solution.canVisitAllRooms(rooms))  # Output: True

# Test case 2
rooms = [[1, 3], [3, 0, 1], [2], [0]]
# Explanation: Room 2 cannot be visited because it is not connected to any room that has been unlocked.
print(solution.canVisitAllRooms(rooms))  # Output: False

"""
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit
all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which
room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true
if you can visit all the rooms, or false otherwise.

#------------------------------------------------------------------------------------------------------#
Every room is locked except 0. This indicates that we can start at 0. When we visit a room, we find some keys that 
enable us to visit other rooms. This tells us we can model the problem as a graph. The rooms are nodes and the keys 
are edges.

The input of the graph is the most convenient one - an adjacency list. We don't need to build graph like we did in 
the previous examples because the input already serves that function - if we want to find the neighbors of a given 
node i, we can simply check rooms[i].

The problem is asking if we can visit all rooms. This is equivalent to "starting a DFS from 0, can you visit all 
nodes?".

So we simply start a DFS from 0, and check if we visited all the nodes after the traversal finishes. 
Because we add a node to seen every time we visit it, we can simply compare the size of seen against n 
(which is the length of rooms since the input is an adjacency list).
"""
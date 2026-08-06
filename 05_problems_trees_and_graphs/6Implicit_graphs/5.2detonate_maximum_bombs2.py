from collections import defaultdict
from typing import List

class Solution:
    # Depth-First Search, Recursive
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(bombs)

        # Build the graph
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]

                # Create a path from node i to node j, if bomb i detonates bomb j.
                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    graph[i].append(j)

        # DFS to get the number of nodes reachable from a given node cur
        def dfs(cur, visited):
            visited.add(cur)
            for neib in graph[cur]:
                if neib not in visited:
                    dfs(neib, visited)
            return len(visited)

        answer = 0
        for i in range(n):
            visited = set()
            answer = max(answer, dfs(i, visited))

        return answer

# Test case 1: A simple case with 2 bombs
# Explanation:
# The best bomb to detonate is bomb 0 because:
# - Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
# - Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
# - Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
# Thus all 5 bombs are detonated.
bombs1 = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
# Expected output: 2 (both bombs can detonate each other)
print(Solution().maximumDetonation(bombs1))

# Test case 2: Multiple bombs in range
bombs2 = [[1, 1, 5], [10, 10, 5]]
# Expected output: 3 (all bombs are within range to detonate each other)
print(Solution().maximumDetonation(bombs2))

"""
Overview
We can transform the map of bombs into a graph by representing each bomb i as a node i in the same location. 
The equivalent of bomb 1 detonating bomb 2 is a directed edge from node 1 to node 2.

To determine whether bomb 1 detonates bomb 2, we can compare the Euclidean distance between their centers and the 
radius of bomb 1. If the distance is less than or equal to the radius of bomb 1, then bomb 1 can detonate bomb 2. 
Note that this relationship is not commutative: bomb 1 detonating bomb 2 does not necessarily imply the converse is 
also true.

distance 2 = (x1−x2) +(y1−y2)2

Therefore, the original problem can be transformed into a graph traversal problem where we calculate the total number 
of reachable nodes from each node i.

Starting with building the graph, we need to traverse each pair of two distinct bombs (i, j) to check if bomb i 
detonates bomb j. If so, we create a directed edge from node i to node j. We consider all different pairs of nodes, 
and note that two pairs of the same bombs in different orders are considered to be different. In short, we consider 
both (i, j) and (j, i).

Each of the following methods begins with the building process above.

#----------------------------------------------------------------------------------------#

Approach 1: Depth-First Search, Recursive
Intuition
If you are not familiar with depth-first (DFS) search, please refer to our explore cards Depth-First Search 
Explore Card. We will focus on the usage in this article and not the implementation details.

In DFS, we explore nodes as far as possible along each branch. Upon reaching the end of the current branch, we 
backtrack to the next possible branch and continue exploring. Once we encounter an unvisited node, we take one of its 
neighbor nodes (if it exists) as the next node on this branch. Recursively call the function to the next node and 
solve the subproblem. If we reach the end of this branch, we backtrack to the previous node and visit the next neighbor
node (if it exists), and repeat the process.

We can use a hash set visited to keep track of all the visited nodes. Initially, visited is empty. When we find an 
unvisited neighbor node, we can add it to visited so it won't be visited anymore.
At the end of the DFS, we can return the size of visited as the number of visited nodes (detonated bombs).
We will perform the DFS from each node and update answer as the maximum number of reachable nodes starting from 
each node.

Algorithm
1. Initialize answer as 0.
2. Create hash map graph containing all directed edges corresponding to the detonation relationships between all bombs.
3. Create an empty hash set visited.
4. Define a recursive function dfs(cur) to recursively find all reachable nodes from node cur:
    Add cur to visited.
    Recursively call dfs(neib) on each unvisited neighbor of cur.
5. Repeat from step 3 for each node i and update answer as the maximum size of visited after each DFS.
6. Return answer when all DFS operations are complete.
"""


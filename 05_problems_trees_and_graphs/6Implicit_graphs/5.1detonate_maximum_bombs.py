from collections import defaultdict, deque
from typing import List

class Solution:
    # Breadth-First Search
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(bombs)

        # Build the graph where an edge exists if a bomb can detonate another bomb.
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue  # Skip if comparing the bomb to itself
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]

                # Check if bomb 'i' can detonate bomb 'j' by comparing distances
                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    graph[i].append(j)  # Add edge from bomb i to bomb j

        # BFS to explore all bombs that can be detonated starting from bomb 'i'
        def bfs(i):
            queue = deque([i])
            visited = set([i])
            while queue:
                cur = queue.popleft()
                for neighbor in graph[cur]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return len(visited)  # Return the number of bombs detonated

        answer = 0
        # Check each bomb to find the maximum number of bombs detonated
        for i in range(n):
            answer = max(answer, bfs(i))

        return answer  # Return the maximum number of detonated bombs

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
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is
in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the
X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range.
These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only
one bomb.

#------------------------------------------------------------------------------------------#

Approach 3: Breadth-First Search
Intuition
If you are not familiar with breadth-first search, please refer to our explore cards Breadth-First Search Explore Card.
 We will focus on the usage in this article and not the implementation details.

In BFS, we explore the nodes in the order of their depth. Assuming that the starting node has a depth of 0, we will 
explore all nodes at the present depth (d) before moving on to all nodes at the next depth (d + 1).

Back to this problem, we start with node i with depth = 0, then we mark all its unvisited neighbor nodes with depth = 1
to be visited soon, once we visit a node with depth = 1, we mark all its unvisited neighbor nodes with depth = 2 
as well.

We can use a queue as a container to store all nodes to be visited without mixing the order, and a hash set visited 
to store all visited nodes. When we enqueue a node, we immediately add it to visited, which prevents it from being 
enqueued again by other nodes later.

Once the BFS is complete, the number of visited nodes (denoted bombs) is the size of visited.

We will perform BFS from each node i and update answer as the maximum number of reachable nodes starting from each node.

Algorithm
1. Initialize answer as 0.
2. Create hash map graph containing all directed edges corresponding to the detonation relationships between all bombs.
3. Define a function bfs(i) that finds all the reachable nodes from node i.
    Initialize an empty queue queue and an empty hash set visited.
    Add i to both queue and visited.
    While the queue is not empty, dequeue the first node cur.
    Check if cur has any unvisited neighbor nodes, if so, enqueue them into queue, add them to visited, 
    and repeat the previous step.
    Return the size of visited when the iteration is complete.
4. Call bfs on every node i and update answer as the maximum size of visited after each BFS.
5. Return answer when the all BFS operations are complete.

"""
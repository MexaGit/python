from collections import defaultdict, deque
from typing import List

class Solution:
    # Depth First Search (DFS): Recursive
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # Store all edges according to nodes in 'neighbors'.
        neighbors = defaultdict(list)
        for node_a, node_b in edges:
            neighbors[node_a].append(node_b)
            neighbors[node_b].append(node_a)

        # Mark the nodes in 'restricted' as visited.
        seen = [False] * n
        for node in restricted:
            seen[node] = True

        def dfs(curr_node):
            # Mark 'curr_node' as visited and increment 'ans' by 1.
            nonlocal ans
            ans += 1
            seen[curr_node] = True

            # Go for unvisited neighbors of 'currNode'.
            for next_node in neighbors[curr_node]:
                if not seen[next_node]:
                    dfs(next_node)
        ans = 0
        dfs(0)
        return ans

# Test case: Graph with 7 nodes and some restricted nodes
n = 7
edges = [[0,1], [1,2], [1,3], [3,4], [4,5], [4,6]]
restricted = [4, 5]

# Explanation: Starting from node 0, we can reach nodes [0, 1, 2, 3].
# Nodes 4 and 5 are restricted, so we cannot visit beyond node 3.
# Expected output: 4 (reachable nodes are [0, 1, 2, 3])
solution = Solution()
print(solution.reachableNodes(n, edges, restricted))  # Output: 4

# Test case: All nodes are reachable, no restrictions
n = 5
edges = [[0,1], [1,2], [2,3], [3,4]]
restricted = []

# Explanation: All nodes are connected and reachable. The BFS will visit all nodes.
# Expected output: 5 (reachable nodes are [0, 1, 2, 3, 4])
print(solution.reachableNodes(n, edges, restricted))  # Output: 5

# Test case: Graph with 7 nodes and some restricted nodes
n = 7
edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]]
restricted = [4,2,1]

# Explanation: The diagram above shows the tree.
# Expected output: We have that [0,5,6] are the only nodes that can be reached from node 0 without visiting
# a restricted node.
print(solution.reachableNodes(n, edges, restricted))  # Output: 5

"""
https://leetcode.com/problems/reachable-nodes-with-restrictions/editorial/
There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge
between nodes ai and bi in the tree. You are also given an integer array restricted which represents restricted nodes.

Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.
Note that node 0 will not be a restricted node.

#---------------------------------------------------------------------------------------#
In this problem, we are given an undirected tree where some nodes are restricted.

As shown in the picture below, if we start from node 0, we can reach the following nodes: 0, 1, 2, 3 
(colored in green), which we call reachable. Note that although node 6 is not restricted, it is not reachable 
from 0 because cannot reach it by traversing node 5, since it is a restricted node.

Approach 1: Breadth First Search (BFS)
Intuition
In BFS, we will explore all nodes at the present depth (d) before moving on to the nodes at the next depth (d + 1).
Here is the order in which we visit nodes using BFS, the starting node is colored in red, and the numbers stand 
for the depth of each node. Regardless of the specific structure, we always visit the node of depth = 0, 
then all nodes of depth = 1, all nodes of depth = 2, and so forth.

We visit the starting node first with depth 0, then we mark all its unvisited neighbor nodes with depth 1 to be 
visited soon, once we visit a node with a depth of 1, we mark all its unvisited neighbor nodes with depth 2 as well.
Thus, we can use a queue queue as a container to store all the nodes to be visited without mixing the order. 
Since the operation on the queue is done in First In, First Out (FIFO) order, it allows us to explore all the nodes
 of the current depth, before moving on to nodes of the next depth!

Once we add a node to the queue, we immediately mark it as visited to prevent it from being added to the queue 
again by some other nodes later.

Considering that some of the nodes are restricted, we can mark them as visited at the beginning to avoid adding 
them to the queue. Later in the process, we only consider unvisited nodes, so these restricted nodes will never be taken into account, let alone those that can only be visited by traversing restricted nodes.

If you are not much familiar with BFS traversal, we suggest you read our Leetcode Explore Card and have some 
knowledge of it beforehand.
There are also many other interesting problems that can be solved using BFS. You can practice using BFS approach 
on the following problems! (click to show)

Algorithm
1. Initialize an empty queue queue to store the nodes to be visited, set ans = 0 as the number of reachable nodes.
2. Use one bool array seen to mark all restricted nodes as visited by setting their values to true.
3. Add the starting node 0 to queue and mark it also as visited.
4. If queue has nodes, get the first node curr_node from queue, increment ans by 1. Otherwise, go to step 6.
5. Add unvisited neighbor nodes of curr_node to queue and mark them as visited. Repeat step 4.
6. Once we emptied queue, it means that we have visited all the reachable nodes. Return ans.

Complexity Analysis
Let n be the number of nodes in the given tree.

Time complexity: O(n)
In a typical BFS search, the time complexity is O(V+E) where V is the number of vertices and E is the number of 
edges. In this problem, there are n nodes and n−1 edges.
The time complexity is O(n).

Space complexity: O(n)
Since the number of edges and vertices are of the same order of magnitude, thus we used a hash map neighbors 
rather than an adjacency matrix to store the edges, this will cost O(n) space for O(n) edges.
We use seen, either a hash set or an array to record the visited nodes, this takes O(n) space.
There may be up to n nodes stored in queue which takes O(n) space.
Therefore, the space complexity is O(n).
"""
from collections import defaultdict, deque
from typing import List

class Solution:
    # Breadth First Search (BFS)
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # Step 1: Build the graph using the given edges.
        neighbors = defaultdict(list)
        for node_a, node_b in edges:
            neighbors[node_a].append(node_b)
            neighbors[node_b].append(node_a)

        # Step 2: Mark all restricted nodes as "seen" to prevent visiting them.
        seen = [False] * n
        for node in restricted:
            seen[node] = True

        # Step 3: Start BFS from node 0 (the starting node).
        ans = 0
        queue = deque([0])
        seen[0] = True  # Mark node 0 as visited

        # Step 4: Traverse the graph using BFS
        while queue:
            curr_node = queue.popleft()  # Get the current node to process
            ans += 1  # Count the current node as visited

            # Step 5: Visit all neighbors of the current node
            for next_node in neighbors[curr_node]:
                # If the neighbor has not been seen and is not restricted, visit it
                if not seen[next_node]:
                    seen[next_node] = True
                    queue.append(next_node)

        # Return the total number of reachable nodes
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
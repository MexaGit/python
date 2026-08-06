from collections import defaultdict, deque
from typing import List

class Solution:
    #Breadth First Search (BFS)
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Build the graph from the given list of edges
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)  # Undirected graph, so add both (a->b) and (b->a)
            graph[b].append(a)

        # Array to keep track of visited nodes
        seen = [False] * n
        seen[source] = True  # Mark the source node as visited

        # Use a queue for Breadth-First Search (BFS)
        queue = deque([source])

        # While there are nodes to process in the queue
        while queue:
            curr_node = queue.popleft()

            # If we reach the destination node, return True
            if curr_node == destination:
                return True

            # Check the neighbors of the current node
            for next_node in graph[curr_node]:
                if not seen[next_node]:  # If the neighbor hasn't been visited
                    seen[next_node] = True  # Mark it as visited
                    queue.append(next_node)  # Add it to the queue for further processing

        # If BFS completes without finding the destination, return False
        return False

# Test cases
# Test case 1
n = 6
edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
source = 0
destination = 5
solution = Solution()
print(solution.validPath(n, edges, source, destination))  # Output: False
# Explanation: There is no path from node 0 to node 5 in the graph.

# Test case 2
n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2
print(solution.validPath(n, edges, source, destination))  # Output: True
# Explanation: There is a path from node 0 to node 2 in the graph.

# Test case 3
n = 1
edges = []
source = 0
destination = 0
print(solution.validPath(n, edges, source, destination))  # Output: True
# Explanation: The source and destination are the same, so the path is trivially valid.
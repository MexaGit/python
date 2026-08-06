from collections import defaultdict, deque
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # Constants to represent edge colors
        RED = 0
        BLUE = 1

        # Create a graph using a nested dictionary to hold edges
        graph = defaultdict(lambda: defaultdict(list))

        # Add red edges to the graph
        for x, y in redEdges:
            graph[RED][x].append(y)

        # Add blue edges to the graph
        for x, y in blueEdges:
            graph[BLUE][x].append(y)

        # Initialize the answer array with infinity for each node
        ans = [float("inf")] * n

        # Initialize the queue for BFS, starting from node 0 with both colors
        queue = deque([(0, RED, 0), (0, BLUE, 0)])  # (node, color, steps)

        # Set to keep track of visited nodes with their corresponding edge colors
        seen = {(0, RED), (0, BLUE)}

        # Perform BFS to find the shortest paths
        while queue:
            node, color, steps = queue.popleft()  # Get the current node, its color, and step count

            # Update the answer for the current node with the minimum steps found
            ans[node] = min(ans[node], steps)

            # Get neighbors of the current node for the opposite color
            for neighbor in graph[color][node]:
                if (neighbor, 1 - color) not in seen:  # If this neighbor hasn't been seen with the opposite color
                    seen.add((neighbor, 1 - color))  # Mark it as seen
                    queue.append((neighbor, 1 - color, steps + 1))  # Add it to the queue with incremented steps

        # Return the results, replacing infinities with -1 for unreachable nodes
        return [x if x != float("inf") else -1 for x in ans]


# Example usage
if __name__ == "__main__":
    solution = Solution()

    n = 3
    redEdges = [[0, 1], [1, 2]]
    blueEdges = [[0, 2]]

    # Expected output: [0, 1, 2]
    print(solution.shortestAlternatingPaths(n, redEdges, blueEdges))

    # Test case input
    n = 3
    redEdges = [[0, 1], [1, 2]]
    blueEdges = []

    # Expected output: [0, 1, -1]
    print(solution.shortestAlternatingPaths(n, redEdges, blueEdges))

"""
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. 
Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:
    redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
    blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
    
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such 
that the edge colors alternate along the path, or -1 if such a path does not exist.

In the previous example, we saw how valuable associating additional data with a node could be.

This problem has a simple premise - start at node 0 and find the shortest distance to every other node. On a regular 
graph, we could just associate the steps taken with each node and perform a BFS starting from 0.

However, we have an added constraint - we must alternate between colors. For each state, we can include a variable
color that indicates the color of the next edge we should use. Then when we iterate over the neighbors, we only 
consider edges of color. When we push a neighbor onto the queue, we push the opposite of color with the neighbor 
(push red if color = blue and blue if color = red).

The input gives the graph as an array of edges, thus we need to build our hash map graph. Normally, we want graph[node]
to access all the neighbors of a node. We can add one extra layer so that graph[node][color] gives us all the neighbors
of node accessed through an edge of color.

Now we start a BFS from node 0 considering both colors. That means we start with queue = [(0, 0, 0), (0, 1, 0)]. 
Each element represents (node, color, steps). We saw in an earlier example that the initial queue is the 0 th level 
and can have any number of states. We initialize an answer variable ans that is an array of length n and update it as 
we perform the BFS.

To make the implementation clean, we can use the integers 0 and 1 to represent the colors. It doesn't matter which 
color is 0 and which is 1. When we push a neighbor onto the queue and want to swap the color, we can use the 
trick 1 - color as mentioned above. Remember, because our state is (node, color), we may visit a node twice, 
once for each color. That's why seen is now two-dimensional.
"""

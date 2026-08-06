from collections import defaultdict, deque  # 🎒 defaultdict stores the roads, deque is for the BFS queue
from typing import List  # 📝 Just tells Python that we're working with lists

class Solution:
    # 🛤️ Use Breadth-First Search (BFS) to explore the roads (graph).
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Step 1: 🛠️ Build the road map (graph) from the list of edges
        graph = defaultdict(list)  # 🎒 Use defaultdict to store which houses connect to which
        for a, b in edges:
            graph[a].append(b)  # 🔄 Since it’s an undirected road, add both a->b and b->a
            graph[b].append(a)   # This means you can go back and forth between these houses
            # graph = {
            #     0: [1, 2],
            #     1: [0],
            #     2: [0],
            #     3: [5, 4],
            #     5: [3, 4],
            #     4: [5, 3]
            # }

        # Step 2: 🗒️ Create a list to keep track of visited houses (nodes)
        # seen = [True, False, False, False, False, False]
        seen = [False] * n  # 🏠 Mark all houses as unvisited initially
        seen[source] = True  # ✅ Mark your starting house (source) as visited

        # Step 3: 🚶‍♂️ Use a queue to explore the houses (BFS)
        queue = deque([source])  # 🎒 Start with your house (source) in the queue

        # Step 4: 🔄 Explore houses one by one until you find your friend’s house or run out of roads
        while queue:
            # curr_node = queue.popleft() → curr_node = 0
            # Neighbors of House 0: [1, 2]
            curr_node = queue.popleft()  # 🚪 Visit the house at the front of the queue

            # 🏁 If you reach your friend’s house (destination), mission complete!
            if curr_node == destination:
                return True  # 🎉 Yes, you can reach your friend's house!

            # 🔍 Check all the connected houses (neighbors) from the current house
            for next_node in graph[curr_node]:  # Example: if curr_node = 0, then graph[0] might be [1, 2]
                # 🏠 If you haven’t visited this house before, proceed with the next steps.
                if not seen[next_node]:  # Example: If next_node = 1, check if seen[1] is False
                    seen[next_node] = True  # ✅ Mark this house as visited to avoid revisiting it
                    # Example update: if next_node = 1, then seen[1] becomes True
                    queue.append(next_node)  # 🎒 Add this house to the queue to visit its neighbors later
                    # Example update: if next_node = 1, queue might look like queue = [1, 2] after appending

        # 🛑 If you’ve visited all possible houses and didn’t find your friend’s house, return False
        return False  # 😔 No way to reach the destination!

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

"""
Here’s how we can frame the problem more practically, using Amazon-style logistics or delivery systems:

Scenario: Package Delivery Across Cities 🚚
You are a delivery driver traveling between n cities.
The cities (nodes) are connected by two-way roads (edges).
Each road connects exactly two cities (like a bi-directional edge in a graph).
Your job is to figure out if there is a valid path from your starting city (source) to the destination city.

Explanation:
House 0 connects to houses 1 and 2.
House 3 connects to houses 5 and 4.
House 5 connects to houses 3 and 4.
House 4 connects to houses 5 and 3.


"""

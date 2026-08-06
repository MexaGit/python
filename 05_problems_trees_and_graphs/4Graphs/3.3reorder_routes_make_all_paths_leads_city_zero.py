from collections import defaultdict  # 🎒 A magic backpack to store lists of roads.
from typing import List  # 📝 Just tells Python that we are working with lists.

class Solution:
    # 🛤️ Iterative version: Let's fix the roads!
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = set()  # 🛑 This keeps track of all the **one-way roads**.
        graph = defaultdict(list)  # 🌐 This stores the map of all the **cities** and **roads**.

        # 🔄 Build the **map** and mark all the roads that need to be checked.
        # connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
        for x, y in connections:
            # for x, y in connections:
            #     graph[x].append(y)  # Add y to the list of neighbors for x
            #     graph[y].append(x)  # Add x to the list of neighbors for y
            # roads = {(0, 1), (1, 3), (2, 3), (4, 0), (4, 5)}
            # graph = { 0: [1, 4], 1: [0, 3], 3: [1, 2], 2: [3], 4: [0, 5], 5: [4] }
            graph[x].append(y)  # ➡️ From city x to y.
            graph[y].append(x)  # ➡️ And from city y to x (for travel back).
            roads.add((x, y))  # 🚧 Add the original one-way road (from x to y).

        ans = 0  # 🎯 This keeps track of how many roads we need to **reorder**.
        stack = [0]  # 🎒 Start from **city 0** (the capital) and explore from there.
        seen = {0}  # 👀 Keep track of the **cities we’ve already visited** to avoid going in circles.

        # 🔄 Keep exploring cities until there are no more left in the backpack (stack).
        while stack:
            node = stack.pop()  # 🏙️ Take a city out of the backpack to explore.
            # connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
            # roads = {(0, 1), (1, 3), (2, 3), (4, 0), (4, 5)}
            # graph = { 0: [1, 4], 1: [0, 3], 3: [1, 2], 2: [3], 4: [0, 5], 5: [4] }
            # 🔍 Check all the neighbors (connected cities) of the current city.
            for neighbor in graph[node]: # Neighbors of 0: [1, 4] (from graph[0]) first iteration
                # 🛑 If we haven’t visited this neighboring city yet...
                if neighbor not in seen: # if 1 not in seen:  # True, since seen = {0}
                    # 🚦 Check if the road goes **from the current city to the neighbor**.
                    if (node, neighbor) in roads: # if (0, 1) in roads:  # True, road goes in wrong direction
                        ans += 1  # 🔧 If yes, we need to **fix this road**.

                    # ✅ Mark the neighbor as visited and add it to the stack.
                    # first iteration seen = {0, 1} all the way {0, 1, 2, 3, 4, 5}
                    seen.add(neighbor)  # 👀 We’ve now seen this city.66
                    # stack = [1]
                    stack.append(neighbor)  # 🎒 Add it to the backpack to explore it later.

        # 🎉 Return the total number of roads that need to be fixed.
        return ans

# [0 → 1], [1 → 3], [2 → 3], [4 → 0], [4 → 5]
# graph = {
#   0: [1, 4],  # City 0 is connected to cities 1 and 4
#   1: [0, 3],  # City 1 is connected to cities 0 and 3
#   3: [1, 2],  # City 3 is connected to cities 1 and 2
#   2: [3],     # City 2 is connected to city 3
#   4: [0, 5],  # City 4 is connected to cities 0 and 5
#   5: [4]      # City 5 is connected to city 4
# }
# 2 → 3 → 1 → 0 =  3: [1, 2] one already reversed, so 2 can use that path to city 0

# Example usage and test cases
# Test case 1
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Explanation: We need to reorder roads [1 -> 3] and [4 -> 0].
solution = Solution()
print(solution.minReorder(n, connections))  # Output: 3

# Test case 2
n = 5
connections = [[1, 0], [1, 2], [3, 2], [3, 4]]
# Explanation: We need to reorder road [1 -> 2].
print(solution.minReorder(n, connections))  # Output: 1

"""
Possible Real-World Scenario
In a real-world situation, this might be framed like:

Scenario: Logistics Network Redesign 🚛

"You are working for a transportation company that has built a network of narrow one-way roads connecting various 
distribution centers (cities). Some of these roads are not facing the correct direction, and with an upcoming event 
in the main hub (city 0), all distribution centers need to be able to send goods to this hub. Your task is to 
determine the minimum number of road directions that need to be reversed so that every distribution center can 
reach the main hub."

This framing makes it feel like a logistics problem rather than a traditional graph problem.
"""
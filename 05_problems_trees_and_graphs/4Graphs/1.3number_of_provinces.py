from collections import defaultdict  # 🎒 A backpack to store friendships (connections)
from typing import List  # 📝 Just tells Python that we are working with a list

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # 🔄 Step 1: Define an "explore group" function using DFS and a stack.
        def dfs(start):
            stack = [start]  # 🎒 Start with the current kid on the stack.
            # 🔄 Keep going until there are no more kids left to explore.
            while stack:
                node = stack.pop()  # 🎯 Take one kid off the stack to explore.
                # 🔍 Check all of this kid’s friends.
                for neighbor in graph[node]:
                    if neighbor not in seen:  # 🤔 If we haven’t met this friend before:
                        seen.add(neighbor)  # 📝 Mark this friend as visited.
                        stack.append(neighbor)  # 🎒 Add them to the stack for later exploration.

        # 🗺️ Step 2: Build the "friendship web" (graph) from the chart.
        n = len(isConnected)  # 🎒 Total number of kids (or cities).
        graph = defaultdict(list)  # 🛠️ Create an empty web to store friendships.

        # 🔄 Loop through the matrix to record friendships (upper half only).
        for i in range(n):
            for j in range(i + 1, n):  # ➡️ Only look at one half to avoid duplicates.
                if isConnected[i][j]:  # 👫 If Kid i and Kid j are friends:
                    graph[i].append(j)  # 📋 Add j to i's friend list.
                    graph[j].append(i)  # 📋 Add i to j's friend list (friendship is mutual).

        # 🎯 Step 3: Set up a notebook to track visited kids and count groups.
        seen = set()  # 📝 Store visited kids here to avoid meeting them twice.
        ans = 0  # 🧮 This will count the number of friend groups.

        # 🔄 Step 4: Go through all the kids to explore their friend groups.
        for i in range(n):  # 🎒 Loop through each kid from 0 to n-1.
            if i not in seen:  # 🤔 If we haven’t visited this kid yet:
                ans += 1  # 🎉 Found a new friend group! Increase the count.
                seen.add(i)  # 📝 Mark this kid as visited.
                dfs(i)  # 🔍 Use DFS to explore all their friends.

        # 🏁 Step 5: Return the total number of friend groups.
        return ans  # 🎯 This is the answer: the total number of friend groups.

# 🎮 Example playground scenarios:

# Example usage:
# Test case 1
isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
# Explanation: There are two provinces: [0, 1] and [2].
solution = Solution()
print(solution.findCircleNum(isConnected))  # Output: 2

# Test case 2
isConnected = [
    [1,0,0],
    [0,1,0],
    [0,0,1]
]
# Explanation: There is one province, as all cities are connected.
print(solution.findCircleNum(isConnected))  # Output: 3



"""
Scenario:
"There are n cities. Some pairs of cities are directly connected by a highway, while others are not. If there’s a 
highway between City A and City B, and one between City B and City C, then City A is indirectly connected to City C. 
This makes them part of the same region (or province). A province is defined as a group of cities that are either 
directly or indirectly connected through highways, with no connections to cities outside the group.

You are given an n x n matrix called isConnected, where isConnected[i][j] = 1 means there’s a highway between city i 
and city j. Your task is to return the total number of provinces (disconnected groups of cities)."

Why This is a Disguised Graph Problem
The problem asks you to identify all the connected components in a graph (cities connected directly or indirectly).
You can solve it using DFS or BFS to explore all connected cities starting from each unvisited city.

Takeaways for Interviews
Recognizing Patterns: Problems involving groups, connections, or clusters are often graph problems in disguise.
Appropriate Tools: Knowing DFS, BFS, and Union-Find helps a lot, as these are common tools for connected components.
Business Context: Expect problems to be framed in real-world terms (like cities, flights, products, warehouses), 
especially at companies like Amazon that handle logistics.
"""


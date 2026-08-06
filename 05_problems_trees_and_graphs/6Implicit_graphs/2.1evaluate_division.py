from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Function to answer a query by finding the ratio between the start and end variables
        def answer_query(start, end):
            # If the start variable is not in the graph, return -1 (indicating no information)
            if start not in graph:
                return -1

            # Set to keep track of visited nodes (variables)
            seen = {start}
            # Stack for DFS traversal, initialized with the start variable and a ratio of 1
            stack = [(start, 1)]

            # Perform DFS to explore all possible paths
            while stack:
                node, ratio = stack.pop()
                # If we reach the end variable, return the current ratio
                if node == end:
                    return ratio

                # Explore neighbors (connected variables) of the current node
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append((neighbor, ratio * graph[node][neighbor]))

            # If no path was found, return -1
            return -1

        # Build the graph using the equations and values
        graph = defaultdict(dict)
        for i in range(len(equations)):
            # each equation we have:
            numerator, denominator = equations[i]
            val = values[i] # find the associated value
            graph[numerator][denominator] = val # create an edge, the edge has a weight of value
            graph[denominator][numerator] = 1 / val # go the other way around

        # Process each query and calculate the result
        ans = []
        for numerator, denominator in queries:
            ans.append(answer_query(numerator, denominator))

        return ans

# Test case 1
# Explanation:
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# note: x is undefined => -1.0
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
solution = Solution()
print(solution.calcEquation(equations, values, queries))
# Output: [6.0, 0.5, -1.0, 1.0, -1.0]

# Test case 2
equations = [["x", "y"], ["y", "z"]]
values = [4.0, 2.0]
queries = [["x", "z"], ["z", "x"], ["x", "x"], ["z", "z"], ["w", "x"]]
print(solution.calcEquation(equations, values, queries))
# Output: [8.0, 0.125, 1.0, 1.0, -1.0]

"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi]
and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer
for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and
that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for
them.
"""
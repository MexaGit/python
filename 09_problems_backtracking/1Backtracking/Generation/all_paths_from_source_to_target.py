from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # The target node is the last node in the graph
        target = len(graph) - 1
        results = []

        # Backtracking function to explore all paths
        def backtrack(curr_node, path):
            # If the current node is the target, append the current path to results
            if curr_node == target:
                results.append(list(path))
                return
            # Explore all neighbors of the current node
            for next_node in graph[curr_node]:
                path.append(next_node)
                backtrack(next_node, path)  # Recursively explore the next node
                path.pop()  # Backtrack by removing the last added node

        # Start the backtracking from the source node (0) with an initial path
        path = [0]
        backtrack(0, path)

        return results

# Test Case 1:
# Input: graph = [[1,2],[3],[3],[]]
# Output: All paths from node 0 to node 3
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
print(Solution().allPathsSourceTarget([[1, 2], [3], [3], []]))
# Expected output: [[0, 1, 3], [0, 2, 3]]

# Test Case 2:
# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: All paths from node 0 to node 4
print(Solution().allPathsSourceTarget([[4,3,1], [3,2,4], [3], [4], []]))
# Expected output: [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 4]]

# Test Case 3:
# Input: graph = [[1],[]]
# Output: All paths from node 0 to node 1
print(Solution().allPathsSourceTarget([[1], []]))
# Expected output: [[0, 1]]


"""
https://leetcode.com/problems/all-paths-from-source-to-target/description/
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node
n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed
edge from node i to node graph[i][j]).

#----------------------------------------------------------------------------------------#

Overview
If a hint is ever given on the problem description, that would be backtracking.

Indeed, since the problem concerns about the path exploration in a graph data structure, it is a perfect scenario to
apply the backtracking algorithm.

As a reminder, backtracking is a general algorithm that incrementally builds candidates to the solutions, and abandons
a candidate ("backtrack") as soon as it determines that the candidate cannot possibly lead to a valid solution.

For more details about how to implement a backtracking algorithm, one can refer to our Explore card.

In this solution, we start from an approach using backtracking and discuss another alternative approach for this problem.

Approach 1: Backtracking
Overview

Intuition
    Specifically, for this problem, we could assume ourselves as an agent in a game, we can explore the graph one
    step at a time.

At any given node, we try out each neighbor node recursively until we reach the target or there is no more node to hop
on. By trying out, we mark the choice before moving on, and later on we reverse the choice (i.e. backtrack) and start
another exploration.

To better demonstrate the above idea, we illustrate how an agent would explore the graph with the backtracking strategy,
in the following image where we mark the order that each edge is visited.

Algorithm
The above idea might remind one of the Depth-First Search (DFS) traversal algorithm.
Indeed, often the backtracking algorithm assumes the form of DFS, but with the additional step of backtracking.

And for the DFS traversal, we often adopt the recursion as its main form of implementation.
With recursion, we could implement a backtracking algorithm in a rather intuitive and concise way. We break it down
into the following steps:

    Essentially, we want to implement a recursive function called backtrack(currNode, path) which continues the
    exploration, given the current node and the path traversed so far.

        Within the recursive function, we first define its base case, i.e. the moment we should terminate the recursion.
        Obviously, we should stop the exploration when we encounter our target node. So the condition of the base case
        is currNode == target.

        As the body of our recursive function, we should enumerate through all the neighbor nodes of the current node.

        For each iteration, we first mark the choice by appending the neighbor node to the path. Then we recursively
        invoke our backtrack() function to explore deeper. At the end of the iteration, we should reverse the choice
        by popping out the neighbor node from the path, so that we could start all over for the next neighbor node.

    Once we define our backtrack() function, it suffices to add the initial node (i.e. node with index 0) to the path, to
    kick off our backtracking exploration.
"""
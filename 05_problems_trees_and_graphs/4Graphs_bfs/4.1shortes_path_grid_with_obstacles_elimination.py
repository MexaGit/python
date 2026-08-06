from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # Helper function to check if a position is within the grid boundaries
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        m = len(grid)  # Number of rows in the grid
        n = len(grid[0])  # Number of columns in the grid
        # Initialize the queue for BFS with starting point (0, 0) and k obstacles to remove
        queue = deque([(0, 0, k, 0)])  # (row, col, remaining removals, steps)
        seen = {(0, 0, k)}  # Set to keep track of visited positions with remaining removals
        # Possible directions to move: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            row, col, remain, steps = queue.popleft()  # Dequeue the front element
            # Check if we have reached the bottom-right corner
            if row == m - 1 and col == n - 1:
                return steps  # Return the number of steps taken to reach the target

            # Explore all possible directions
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx  # Calculate the next position
                if valid(next_row, next_col):  # Check if the next position is valid
                    # if is not an obstacle
                    if grid[next_row][next_col] == 0:
                        # If the cell is empty (0), we can move there without using a removal
                        if (next_row, next_col, remain) not in seen: # if is not in our set
                            # add to our set
                            seen.add((next_row, next_col, remain))  # Mark this position as seen
                            queue.append((next_row, next_col, remain, steps + 1))  # Enqueue the position
                    # If the cell is an obstacle (1), we can move there if we have removals left
                    elif remain and (next_row, next_col, remain - 1) not in seen:
                        seen.add((next_row, next_col, remain - 1))  # Use a removal and mark as seen
                        queue.append((next_row, next_col, remain - 1, steps + 1))  # Enqueue the position

        return -1  # If the target cannot be reached, return -1

# Example usage of the shortestPath function
if __name__ == "__main__":
    solution = Solution()

    # Test case input
    grid = [[0, 0, 0],
            [1, 1, 0],
            [0, 0, 0],
            [0, 1, 1],
            [0, 0, 0]]
    k = 1

    # Expected output: 6
    result = solution.shortestPath(grid, k)
    print(f"Shortest path length: {result}")  # Should print 6

"""
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). 
You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1)
given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

This problem has two main differences. First, we can't move diagonally (this is trivial to handle, we just modify 
directions to not include diagonal deltas). Second, we are allowed to move to squares with 1, but only up to k.

Recall that when we were looking at binary trees, we occasionally passed arguments to our dfs function other than node.
This was how we associated crucial information with each node. For example, when we looked at Path Sum, we passed an 
argument curr that represented the sum of the path we have taken so far.

In the first and third examples in this article, we associated the current level (as an integer steps) with each node.

This idea of associating additional information with nodes is a very common and useful one. In this problem, we are 
allowed to remove up to k obstacles on a given path. We can use a variable remain to represent how many removals we 
have remaining on the current path. Initially, we start in the top left with remain = k. For every (node, remain) pair,
we consider the neighbors like usual. If a neighbor is 0, then we just move to it without modifying remain. 
If a neighbor is 1, we can move to it, but we use up one of our removals, so we pass remain - 1 with the neighbor. 
Of course, we can only do this if remain > 0.

We've been using seen to avoid visiting the same node twice. In reality, seen actually prevents us from visiting 
the same state twice. It's just that we've only looked at problems where the node entirely describes the state. 
We need to store (node, remain) in seen instead of just node.
"""

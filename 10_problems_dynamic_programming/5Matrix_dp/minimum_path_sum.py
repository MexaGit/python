from typing import List
from functools import cache

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache  # Using memoization to store previously computed results
        def dp(row, col):
            # Base case: Starting at the top-left corner, return the value in grid[0][0]
            if row + col == 0:
                return grid[row][col]

            ans = float("inf")  # Initialize answer to a large value to find minimum

            # If we're not in the first row, we can move from the cell above
            if row > 0:
                ans = min(ans, dp(row - 1, col))

            # If we're not in the first column, we can move from the cell to the left
            if col > 0:
                ans = min(ans, dp(row, col - 1))

            # Add the current grid value to the minimum path sum obtained from previous cells
            return grid[row][col] + ans

        # Get the dimensions of the grid
        m = len(grid)
        n = len(grid[0])

        # Start from the bottom-right corner and return the minimum path sum
        return dp(m - 1, n - 1)


# Test case 1: 3x3 grid
grid1 = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
# The minimum path sum is 7: 1→3→1→1→1.
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
print(Solution().minPathSum(grid1))  # Output: 7

# Test case 2: 2x2 grid
grid2 = [
    [1, 2],
    [1, 1]
]
# The minimum path sum is 3: 1→2→1.
print(Solution().minPathSum(grid2))  # Output: 3


"""
https://leetcode.com/problems/minimum-path-sum/description/
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the
sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

#------------------------------------------------------------------------------------------------#

Summary
We have to find the minimum sum of numbers over a path from the top left to the bottom right of the given matrix .

"""
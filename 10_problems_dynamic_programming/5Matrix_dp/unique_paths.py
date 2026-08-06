from functools import  cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache  # Using memoization to avoid recomputation
        def dp(row, col):
            # Base case: when both row and col are 0, we've reached the top-left corner,
            # so there's exactly one way to stay here.
            if row + col == 0:
                return 1

            ways = 0
            # If we're not in the first row, check the cell above (row - 1, col)
            if row > 0:
                ways += dp(row - 1, col)
            # If we're not in the first column, check the cell to the left (row, col - 1)
            if col > 0:
                ways += dp(row, col - 1)

            # Return the total number of ways to reach the current cell (row, col)
            return ways

        # Start from the bottom-right corner (m-1, n-1) and calculate the paths.
        return dp(m - 1, n - 1)


# Test case 1: 3x2 grid
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
print(Solution().uniquePaths(3, 2))  # Output: 3

# Test case 2: 7x3 grid
# There are 28 unique paths from the top-left to the bottom-right.
print(Solution().uniquePaths(3, 7))  # Output: 28

"""
https://leetcode.com/problems/unique-paths/description/
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or
right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the
bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

#--------------------------------------------------------------------------------------------------#

Overview
Since robot can move either down or right, there is only one path
to reach the cells in the first row: right->right->...->right.

The same is valid for the first column, though the path here is down->down->...->down.

What about the "inner" cells (m, n)? To such cell one could move
either from the cell on the left (m, n - 1), or from the cell above
(m - 1, n). That means that the total number of paths to move into (m, n) cell
is uniquePaths(m - 1, n) + uniquePaths(m, n - 1).

Now, one could transform these ideas into 3-liner recursive solution:
This solution is not fast enough to pass all the testcases, though it
could be used as a starting point for the DP solution.

Approach 1: Dynamic Programming
One could rewrite recursive approach into dynamic programming one.

Algorithm
    Initiate 2D array d[m][n] = number of paths. To start, put number of paths
    equal to 1 for the first row and the first column.
    For the simplicity, one could initiate the whole 2D array by ones.
    Iterate over all "inner" cells: d[col][row] = d[col - 1][row] + d[col][row - 1].
    Return d[m - 1][n - 1].
"""
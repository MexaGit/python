from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [float("inf")] * n
        dp[0] = 0

        for row in range(m):
            next_row = [0] * n
            for col in range(n):
                next_row[col] = dp[col]
                if col > 0:
                    next_row[col] = min(next_row[col], next_row[col - 1])

                next_row[col] += grid[row][col]

            dp = next_row

        return dp[n - 1]

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
from typing import List

class Solution:
    # Bottom-up
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for row in range(m):
            for col in range(n):
                if row + col == 0:
                    continue

                ans = float("inf")
                if row > 0:
                    ans = min(ans, dp[row - 1][col])
                if col > 0:
                    ans = min(ans, dp[row][col - 1])

                dp[row][col] = grid[row][col] + ans

        return dp[m - 1][n - 1]
    
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

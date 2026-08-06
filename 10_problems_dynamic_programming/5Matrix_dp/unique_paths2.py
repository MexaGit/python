class Solution:
    # Bottom-up:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for row in range(m):
            for col in range(n):
                if row > 0:
                    dp[row][col] += dp[row - 1][col]
                if col > 0:
                    dp[row][col] += dp[row][col - 1]

        return dp[m - 1][n - 1]

# Test case 1: 3x2 grid
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
print(Solution().uniquePaths(3, 2))  # Output: 3

# Test case 2: 7x3 grid
# There are 28 unique paths from the top-left to the bottom-right.
print(Solution().uniquePaths(3, 7))  # Output: 28
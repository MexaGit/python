class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * n
        dp[0] = 1

        for _ in range(m):
            next_row = [0] * n
            for col in range(n):
                next_row[col] += dp[col]
                if col > 0:
                    next_row[col] += next_row[col - 1]

            dp = next_row

        return dp[n - 1]

# Test case 1: 3x2 grid
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
print(Solution().uniquePaths(3, 2))  # Output: 3

# Test case 2: 7x3 grid
# There are 28 unique paths from the top-left to the bottom-right.
print(Solution().uniquePaths(3, 7))  # Output: 28
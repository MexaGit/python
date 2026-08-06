from typing import List

class Solution:
    #  Bottom-Up Dynamic Programming (Tabulation)
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # Initialize the dp array with an extra row of zeros at the bottom
        dp = [[0] * n for _ in range(n + 1)]

        # Fill the dp table from the bottom row to the top
        for row in range(n - 1, -1, -1):
            for col in range(n):
                if col == 0:
                    dp[row][col] = min(dp[row + 1][col], dp[row + 1][col + 1]) + matrix[row][col]
                elif col == n - 1:
                    dp[row][col] = min(dp[row + 1][col], dp[row + 1][col - 1]) + matrix[row][col]
                else:
                    dp[row][col] = min(dp[row + 1][col], dp[row + 1][col + 1], dp[row + 1][col - 1]) + matrix[row][col]

        # The result is the minimum value in the top row
        return min(dp[0])

# Test Case 1
matrix1 = [
    [2, 1, 3],
    [6, 5, 4],
    [7, 8, 9]
]
# Expected Output: 13 (Path: 1 -> 4 -> 8)
print(Solution().minFallingPathSum(matrix1))  # Output: 13

# Test Case 2
matrix2 = [
    [-19, 57],
    [-40, -5]
]
# Expected Output: -59 (Path: -19 -> -40)
print(Solution().minFallingPathSum(matrix2))  # Output: -59
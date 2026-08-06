from typing import List

class Solution:
    # Space Optimized, Bottom-Up Dynamic Programming
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [0] * (n + 1)  # Initialize the DP array

        # Traverse the rows of the matrix from bottom to top
        for row in range(n - 1, -1, -1):
            currentRow = [0] * (n + 1)  # Temporary array to store the current row DP values
            for col in range(n):
                if col == 0:
                    currentRow[col] = min(dp[col], dp[col + 1]) + matrix[row][col]
                elif col == n - 1:
                    currentRow[col] = min(dp[col], dp[col - 1]) + matrix[row][col]
                else:
                    currentRow[col] = min(dp[col], min(dp[col + 1], dp[col - 1])) + matrix[row][col]

            # Update dp with the current row results
            dp = currentRow

        # Find the minimum falling path sum from the top row
        return min(dp[:n])

# Test Case 1
matrix1 = [
    [2, 1, 3],
    [6, 5, 4],
    [7, 8, 9]
]
# Expected Output: 13 (Path: 1 -> 4 -> 8)
# Explanation: There are two falling paths with a minimum sum as shown.
print(Solution().minFallingPathSum(matrix1))  # Output: 13

# Test Case 2
matrix2 = [
    [-19, 57],
    [-40, -5]
]
# Expected Output: -59 (Path: -19 -> -40)
# Explanation: The falling path with a minimum sum is shown.
print(Solution().minFallingPathSum(matrix2))  # Output: -59
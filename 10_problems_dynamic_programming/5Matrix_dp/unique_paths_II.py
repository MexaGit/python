from typing import List

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If the starting cell has an obstacle, return 0 as no paths can start here
        if obstacleGrid[0][0] == 1:
            return 0

        # Initialize the starting point with 1 way to reach it
        obstacleGrid[0][0] = 1

        # Fill the first column. If there's an obstacle, set the value to 0.
        for i in range(1, m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1)

        # Fill the first row. If there's an obstacle, set the value to 0.
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1)

        # For each remaining cell, if there's no obstacle, set its value to the sum
        # of the values from the cell above it and the cell to the left.
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                else:
                    obstacleGrid[i][j] = 0

        # Return the value at the bottom-right corner, which is the total number of paths.
        return obstacleGrid[m - 1][n - 1]

# Test Case 1: 3x3 grid with obstacles
grid1 = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
# There are two possible paths avoiding the obstacle at (1,1).
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
print(Solution().uniquePathsWithObstacles(grid1))  # Output: 2

# Test Case 2: 2x2 grid with an obstacle in the starting position
grid2 = [
    [1, 0],
    [0, 0]
]
# Since the starting position is blocked, no paths are possible.
print(Solution().uniquePathsWithObstacles(grid2))  # Output: 0


"""
https://leetcode.com/problems/unique-paths-ii/description/
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or
right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square
that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to 2 * 109.

#-------------------------------------------------------------------------------------------#

Approach 1: Dynamic Programming
Intuition

The robot can only move either down or right.
Hence any cell in the first row can only be reached from the cell left to it.

And, any cell in the first column can only be reached from the cell above it.

For any other cell in the grid, we can reach it either from the cell to left of it or the cell above it.
If any cell has an obstacle, we won't let that cell contribute to any path.
We will be iterating the array from left-to-right and top-to-bottom. Thus, before reaching any cell we would have the
number of ways of reaching the predecessor cells. This is what makes it a Dynamic Programming problem. We will be using
the obstacleGrid array as the DP array thus not utilizing any additional space.

Note: As per the question, cell with an obstacle has a value 1. We would use this value to make sure if a cell needs to
be included in the path or not. After that we can use the same cell to store the number of ways to reach that cell.

Algorithm
1. If the first cell i.e. obstacleGrid[0,0] contains 1, this means there is an obstacle in the first cell. Hence the robot
won't be able to make any move and we would return the number of ways as 0.
2. Otherwise, if obstacleGrid[0,0] has a 0 originally we set it to 1 and move ahead.
3. Iterate the first row. If a cell originally contains a 1, this means the current cell has an obstacle and shouldn't
contribute to any path. Hence, set the value of that cell to 0. Otherwise, set it to the value of previous cell i.e.
obstacleGrid[i,j] = obstacleGrid[i,j-1]
4. Iterate the first column. If a cell originally contains a 1, this means the current cell has an obstacle and
shouldn't contribute to any path. Hence, set the value of that cell to 0. Otherwise, set it to the value of previous
cell i.e. obstacleGrid[i,j] = obstacleGrid[i-1,j]
5. Now, iterate through the array starting from cell obstacleGrid[1,1]. If a cell originally doesn't contain any
obstacle then the number of ways of reaching that cell would be the sum of number of ways of reaching the cell above it
and number of ways of reaching the cell to the left of it.
 obstacleGrid[i,j] = obstacleGrid[i-1,j] + obstacleGrid[i,j-1]
6. If a cell contains an obstacle set it to 0 and continue. This is done to make sure it doesn't contribute to any
other path.
"""
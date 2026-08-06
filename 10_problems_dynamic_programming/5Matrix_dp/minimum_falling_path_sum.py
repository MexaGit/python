from typing import List

class Solution:
    # Top Down Dynamic Programming
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        memo = [[None] * n for _ in range(n)]  # Create a memoization table

        # Helper function to calculate minimum falling path sum from any cell (row, col)
        def findMinFallingPathSum(row, col):
            # Base case: if column is out of bounds, return a large value
            if col < 0 or col >= n:
                return float('inf')
            # Base case: if we're on the last row, return the value at the current cell
            if row == n - 1:
                return matrix[row][col]
            # Return the precomputed value if it's already calculated
            if memo[row][col] is not None:
                return memo[row][col]

            # Recursive calls to calculate the minimum path sum from the next row
            left = findMinFallingPathSum(row + 1, col - 1)  # Move diagonally left
            middle = findMinFallingPathSum(row + 1, col)  # Move straight down
            right = findMinFallingPathSum(row + 1, col + 1)  # Move diagonally right

            # Calculate the minimum falling path sum from this cell
            memo[row][col] = min(left, middle, right) + matrix[row][col]
            return memo[row][col]

        # Calculate the minimum falling path sum starting from any cell in the top row
        min_falling_sum = float('inf')
        for start_col in range(n):
            min_falling_sum = min(min_falling_sum, findMinFallingPathSum(0, start_col))

        return min_falling_sum

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

"""
https://leetcode.com/problems/minimum-falling-path-sum/description/
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly
below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1),
(row + 1, col), or (row + 1, col + 1).

#----------------------------------------------------------------------------------------------#

Overview
Given a 2D matrix(row, col), we have to find the sum of the minimum falling path in a matrix.
To begin with, let's try to understand, what is a falling path?
To put it in simple words, it is a path that satisfies the following criteria,

A falling path is a path that begins at any cell in the first row of the matrix and ends at any cell in the last row
of the matrix.
From a certain cell (row, col) in the falling path, we can only move to 3 possible cells, (row + 1, col) ,
(row + 1, col + 1), (row + 1, col - 1).

As the name suggests, the falling path sum is the sum of values of all the cells in the chosen path. Our goal is to
find the minimum sum from all possible paths. Let's consider different approaches that can be used to solve this
problem. We will begin with the brute force approach and optimize it using dynamic programming.

Approach 2: Top Down Dynamic Programming
Intuition

The brute force approach is exhaustive. To come up with the optimized solution for the problem, let's take a deeper
look at the following recursion tree,

In the above recursion tree, we can identify the repetitive sub-paths (circled in the same color). For example,
findMinPathSum(1, 0) is calculated twice, findMinPathSum(1, 1) is calculated three times, and so on.

Repeated calculation of the same subproblems is the root cause of the exponential time complexity in the previous
approach. Although, what if our algorithm could remember the result for a subproblem when it is computed the first
time and reuses the stored result every other time?

Pretend you are on a treasure hunt. On reaching point A, you travel to the destination and don't find anything there.
You go back to some other path which again takes you to point A. You wouldn't explore the same path from point A again.
You would say, "I have been here before; I know where this path goes."

How can we make our algorithm think the same way? We can do so by marking every path we have visited so that if we
reach the same path again, we know the result!!

In Dynamic Programming, when a recursive problem solves the same subproblem multiple times, it has the Overlapping
Subproblem property. Such problems can be optimized using a dynamic programming technique called Memoization.

As in the previous approach, each call to findMinFallingPathSum will return the minimum falling path sum between the
current cell and the bottom of the matrix. However, in this approach, we will store the result of each call in the new
parameter memo, and when we revisit this cell in a subsequent call, we will be able to reuse the stored result.

Algorithm
1. In order to record the results of computation for every cell, maintain a 2-dimensional matrix named memo where the
value of memo[row][col] would give the minimum falling path starting from the cell (row, col).
2. Implement a Depth First Search algorithm, by defining a recursive function, findMinFallingPathSum(row, col), that
recursively explores all the paths from the current cell (defined by parameters row and col).
Define Base Case:
In any recursive function, we must define the terminating condition i.e the base case. When the terminating condition
is satisfied, we will exit the recursive search process. The base cases are as follows,
The row or col values are not within the matrix boundaries.
We have reached the last row. In this case, we will return the value of the current cell and not make any other
recursive calls.
Recursively explore all paths: If the base case is not satisfied, it means that we have not reached the end of our
current path, and we must try all options to extend our path and find the one with the minimum sum:
minimumPath = Minimum(findMinFallingPathSum(row + 1, col + 1),
                      findMinFallingPathSum(row + 1, col),
                      findMinFallingPathSum(row + 1, col - 1))
3. To avoid repetitive computation of the results as in the brute force approach, we make use of stored results as
follows,
    Before recursively computing the result for the current cell, check if the memo has the result for the current cell.
    If so, return the result, otherwise, proceed with the recursive call to compute the result.
    After computing the result, store the result in the memo[row][col].
4. Iteratively find the minimum falling path for all possible starting cells i.e cells in 0th row and columns ranging from
0 to matrix.length−1. Track the minimum value in the variable minFallingSum and return the result.
"""
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the number of rows (m) and columns (n)
        m, n = len(matrix), len(matrix[0])
        # Initialize two pointers: left at the beginning and right at the end of the matrix (flattened)
        left, right = 0, m * n - 1

        # Perform binary search in the flattened 2D matrix
        while left <= right:
            # Find the middle point in the flattened matrix
            mid = (left + right) // 2
            row = mid // n  # Convert the 1D mid index to 2D row index
            col = mid % n  # Convert the 1D mid index to 2D column index
            num = matrix[row][col]  # Get the value at the 2D index

            # If we find the target, return True
            if num == target:
                return True

            # If the target is larger, adjust the left pointer
            if num < target:
                left = mid + 1
            else:
                # If the target is smaller, adjust the right pointer
                right = mid - 1

        # If we exit the loop without finding the target, return False
        return False


# Example test case
# Input: matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 3
# Output: True (3 is in the matrix)
solution = Solution()
# Expected output: True
print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))

"""
https://leetcode.com/problems/search-a-2d-matrix/description/
You are given an m x n integer matrix 'matrix' with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time}

#-------------------------------------------------------------------------------#
We need to reduce this problem to the previous example so we can apply the same binary search algorithm.

Let's say that there are n columns. Each row has n elements. The first n indices belong to row 0. The next n indices
belong to row 1, and so on.

If an element is in row, then there are row * n elements above it in the grid. Given an index i, we can find the row
it belongs to by dividing by n. For example, in the image, index 9 belongs to row 2. There are four elements per row
and we have 9 / 4 = 2. This makes sense as there are eight elements above row 2, so indices 8, 9, 10, 11 all belong
to row 2.

To find the column given an index i, we just take i % n. Index 0 belongs to the 0th column, and then every n indices
we are back in the 0th column. Index 1 belongs to the 1st column, and then every n indices we are back in the 1st
column. Because each column is spaced by n indices, the modulus operator gives us the column.

Once we can convert an index i to a (row, col), we can treat the matrix as a normal array and perform a binary search
over it, like we did in the previous example.

Approach 1: Binary Search
Intuition

One could notice that the input matrix m x n could be considered as a sorted array of length m x n.

Sorted array is a perfect candidate for the binary search because the element index in this virtual array 
(for sure we're not going to construct it for real) could be easily transformed into the row and column in the initial 
matrix

row = idx // n and col = idx % n.

Algorithm
The algorithm is a standard binary search :
    Initialise left and right indexes left = 0 and right = m x n - 1.
    While left <= right :
        Pick up the index in the middle of the virtual array as a pivot index: pivot_idx = (left + right) / 2.
        The index corresponds to row = pivot_idx // n and col = pivot_idx % n in the initial matrix, and hence one 
        could get the pivot_element. This element splits the virtual array into two parts.
        Compare pivot_element and target to identify in which part one has to look for target.
"""
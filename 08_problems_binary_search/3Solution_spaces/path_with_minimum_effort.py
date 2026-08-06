from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Helper function to check if the path is valid with the current effort
        def valid(row, col):
            # Ensure the next position is within bounds
            return 0 <= row < m and 0 <= col < n

        # Check if it's possible to reach the bottom-right corner with a given 'effort'
        def check(effort):
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, down, left, up
            seen = {(0, 0)}  # Keep track of visited cells
            stack = [(0, 0)]  # Start from the top-left corner (0, 0)

            while stack:
                row, col = stack.pop()
                # If we reached the bottom-right corner, return True
                if (row, col) == (m - 1, n - 1):
                    return True

                # Explore all four possible directions
                for dx, dy in directions:
                    next_row, next_col = row + dy, col + dx
                    # Check if the next cell is within bounds and not seen yet
                    if valid(next_row, next_col) and (next_row, next_col) not in seen:
                        # Check if the difference in heights is within the allowed effort
                        if abs(heights[next_row][next_col] - heights[row][col]) <= effort:
                            seen.add((next_row, next_col))  # Mark as visited
                            stack.append((next_row, next_col))  # Add to the stack for further exploration

            return False  # If we exhaust all possibilities without reaching the end, return False

        # Dimensions of the height matrix
        m = len(heights)
        n = len(heights[0])

        # Binary search range for the minimum effort
        left = 0
        right = max(max(row) for row in heights)  # Max height difference possible

        # Binary search to find the minimum effort
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1  # Try smaller efforts
            else:
                left = mid + 1  # Try larger efforts

        return left  # 'left' now holds the minimum effort

# Example Test Case 1:
# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The path with the minimum effort is (1 → 2 → 2 → 2 → 5), with an effort of 2.
print(Solution().minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))  # Expected output: 2

# Example Test Case 2:
# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The path with the minimum effort is (1 → 2 → 3 → 4 → 5), with an effort of 1.
print(Solution().minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))  # Expected output: 1

"""
https://leetcode.com/problems/path-with-minimum-effort/description/
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where
heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you
hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right,
and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

"""
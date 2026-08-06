from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Function to check if a cell is valid and part of an island ("1")
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == "1"

        # DFS function being implemented iteratively:
        def dfs(start_row, start_col):
            stack = [(start_row, start_col)]
            while stack:
                row, col = stack.pop()
                for dx, dy in directions:
                    next_row, next_col = row + dy, col + dx
                    if valid(next_row, next_col) and (next_row, next_col) not in seen:
                        seen.add((next_row, next_col))
                        stack.append((next_row, next_col))

        # Define directions for moving in the grid (right, down, left, up)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Set to keep track of visited cells
        seen = set()

        # Variable to store the number of islands
        ans = 0

        # Dimensions of the grid
        m = len(grid)  # Number of rows
        n = len(grid[0])  # Number of columns

        # Loop through each cell in the grid
        for row in range(m):
            for col in range(n):
                # If the cell contains a "1" (land) and hasn't been visited yet
                if grid[row][col] == "1" and (row, col) not in seen:
                    ans += 1  # Increment the island count
                    seen.add((row, col))  # Mark the starting cell of the island as visited
                    dfs(row, col)  # Perform DFS to explore the entire island

        return ans  # Return the total number of islands

# Example usage and test cases
# Test case 1
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
# Explanation: There is one large island.
solution = Solution()
print(solution.numIslands(grid))  # Output: 1

# Test case 2
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
# Explanation: There are three separate islands.
print(solution.numIslands(grid))  # Output: 3

# Test case 2
grid = [
    ["1", "1", "0", "0", "0", "1"],
    ["0", "1", "0", "0", "0", "0"],
    ["0", "1", "1", "0", "1", "1"],
    ["0", "0", "0", "0", "0", "1"],
    ["1", "1", "1", "1", "0", "1"],
    ["1", "1", "1", "1", "0", "1"]
]
# Explanation: There are three separate islands.
print(solution.numIslands(grid))  # Output: 4
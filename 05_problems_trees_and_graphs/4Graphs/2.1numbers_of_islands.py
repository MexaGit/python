from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Function to check if a cell is valid and part of an island ("1")
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == "1"

        # Depth-First Search (DFS) function to visit all cells in the current island
        def dfs(row, col):
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                # Continue DFS if the next cell is valid and has not been visited
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))  # Mark cell as visited
                    dfs(next_row, next_col)  # Recursively visit the next cell

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

"""
https://leetcode.com/problems/number-of-islands/description/
Given an m x n 2D binary grid 'grid' which represents a map of '1's (land) and '0's (water), return the number
of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

#------------------------------------------------------------------------------------#
A matrix is a very common form of graph. We treat each land cell as a node, and the edges are determined 
by the problem description.

It says that an island is formed by connecting adjacent land cells horizontally or vertically. Therefore, 
two land cells share an edge if they are adjacent. For a node at (row, col), the neighbors are at (row - 1, col), 
(row, col - 1), (row + 1, col), (row, col + 1) (if in bounds).

In an island, you can start at any land cell and reach any other land cell. We just saw this exact same idea 
in the previous problem - an island is like a province.

We have identified that this is the same problem - find the number of islands = find the number of connected 
components. The only thing that has changed is the format in which the input provides us with the graph.

In the code, we have a few tools to help us implement the algorithm. First, we declare an array 
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] which holds the coordinate deltas to move in the four directions. 
This makes the code cleaner when iterating over the neighbors. Next, we use a helper function valid that checks 
if a square is in bounds and an island. While these tools aren't necessary, they make the code cleaner 
and more modular.

Some code differences: we only care about squares whose value is "1" (land). We can define a helper function valid 
that first checks if a given (row, col) is in bounds, and then checks if it is land. We can also declare an array 
directions that makes iterating over the 4 neighbors cleaner (this is a very common practice).

Note: we can avoid using the set here by modifying the input. The point of the set is to avoid visiting 
the same square multiple times. We only visit squares with values "1", so instead of putting a square in a set,
we could just change that square's value to "0". However, some interviewers may not want you to modify the input 
(especially if it is something passed by reference like an array).S
"""
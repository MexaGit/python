class Solution(object):
    #Depth-First Search (Recursive) [Accepted]
    def maxAreaOfIsland(self, grid):
        # Set to keep track of visited cells
        seen = set()

        # Helper function to calculate the area of an island
        def area(r, c):
            # Base case: Check if the current cell is out of bounds or already seen, or is water (grid[r][c] == 0)
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in seen and grid[r][c]):
                return 0

            # Mark the current cell as seen (visited)
            seen.add((r, c))

            # Return the current cell (1) plus recursively explore the neighboring cells in all four directions
            return (1 + area(r + 1, c) + area(r - 1, c) + area(r, c - 1) + area(r, c + 1))

        # Compute the maximum area of all islands by applying the area function on every cell
        return max(area(r, c) for r in range(len(grid)) for c in range(len(grid[0])))



solution = Solution()

# Test case 1: Grid with islands
grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]

# The largest island has an area of 6.
print(solution.maxAreaOfIsland(grid))  # Expected output: 6

# Test case 2: Grid with islands
grid = [
    [0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
]

# In this case, the largest island has an area of 5.
print(solution.maxAreaOfIsland(grid))  # Output: 5

# Test case 3: Grid with one large island
grid = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

# The entire grid is one island, so the output should be 9 (3x3 grid).
print(solution.maxAreaOfIsland(grid))  # Output: 9

"""
https://leetcode.com/problems/max-area-of-island/description/
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally
(horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

#-------------------------------------------------------------------------------------------#
Depth-First Search (Recursive) [Accepted]
Intuition and Algorithm

We want to know the area of each connected shape in the grid, then take the maximum of these.
If we are on a land square and explore every square connected to it 4-directionally (and recursively squares connected
to those squares, and so on), then the total number of squares explored will be the area of that connected shape.

To ensure we don't count squares in a shape more than once, let's use seen to keep track of squares we haven't
visited before. It will also prevent us from counting the same shape more than once.
"""
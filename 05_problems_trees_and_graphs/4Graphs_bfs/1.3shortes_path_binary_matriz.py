from collections import deque  # Importing a cool backpack (queue) to help explore places
from typing import List  # Just for helping us write nice code with list grids


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Step 1: If the start (0, 0) is blocked, there's no way to go! Return -1.
        if grid[0][0] == 1:
            return -1

        # Step 2: Helper function to check if the next step is valid (inside maze + not blocked)
        def valid(row, col):
            return 0 <= row < n and 0 <= col < n and grid[row][col] == 0

        # Initialize size of the grid (how big the maze is)
        n = len(grid)

        # Step 3: Start your journey with (0, 0) as the first spot.
        seen = {(0, 0)}  # This set remembers all the places you’ve been.
        queue = deque([(0, 0, 1)])  # (row, col, steps): track where you are + steps taken.

        # Step 4: All 8 possible ways you can move (including diagonals).
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # top-left,    top,      top-right
            (0, -1),            (0, 1),  # left,   you are here!  right
            (1, -1),  (1, 0),   (1, 1)   # bottom-left, bottom,   bottom-right
        ]

        # Step 5: Start the adventure (BFS)!
        while queue:
            row, col, steps = queue.popleft()  # Take the first spot from your backpack.
            # Step 6: If you reached the goal (bottom-right corner), return the steps it took!
            if (row, col) == (n - 1, n - 1):
                return steps
            # Step 7: Explore all 8 directions from your current position.
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx  # Figure out your next step
                # If the new spot is valid and not visited yet:
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))  # Mark it as visited.
                    queue.append((next_row, next_col, steps + 1))  # Add to backpack with +1 step.

        # Step 8: If there's no way to reach the goal, return -1.
        return -1

# Test case: Basic grid where a path exists
grid = [
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 0]
]

# Explanation: A path exists from (0,0) to (2,2) with 3 steps.
# Path: (0,0) -> (1,1) -> (2,2)
# Expected output: 3
solution = Solution()
print(solution.shortestPathBinaryMatrix(grid))  # Output: 3

# Test case 2: Path exists with 4 steps
grid = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0]
]

# Explanation: The path from (0,0) to (2,2) is possible with 4 steps.
# Path: (0,0) -> (0,1) -> (1,2) -> (2,2)
# Expected output: 4
solution = Solution()
print(solution.shortestPathBinaryMatrix(grid))  # Output: 4

# Test case 3: Start is blocked
grid = [
    [1, 0, 0],
    [1, 1, 0],
    [1, 1, 0]
]

# Explanation: The starting point (0,0) is blocked, so no path can exist.
# Expected output: -1
print(solution.shortestPathBinaryMatrix(grid))  # Output: -1

"""
Key Points to Remember:
BFS (Breadth-First Search): This is like exploring layer by layer, step by step. You explore all spots nearby before going deeper.
Queue (backpack): Helps you keep track of the places to explore.
Visited cells (seen): So you don’t get lost or keep checking the same spot.
Valid helper function: Makes sure every step is inside the maze and open (0).
8 Directions: You can move in more than just straight lines!

Directions in a Matrix:
Top-Left (-1, -1)	Top (-1, 0)	    Top-Right (-1, 1)
Left (0, -1)	    Center (0, 0)	Right (0, 1)
Bottom-Left (1, -1)	Bottom (1, 0)	Bottom-Right (1, 1)

Difference Between Coordinates vs. Directions:
Coordinates: (n - 1, n - 1) means the absolute position of the bottom-right corner in an n × n grid.
Directions: (1, 1) means “move one step down and one step right” from your current position.

Visualizing Directions in a Grid:
Let’s say you're standing at (2, 2) in a 5 × 5 grid:
(0, 0)  (0, 1)  (0, 2)  (0, 3)  (0, 4)
(1, 0)  (1, 1)  (1, 2)  (1, 3)  (1, 4)
(2, 0)  (2, 1)  (2, 2)  (2, 3)  (2, 4)
(3, 0)  (3, 1)  (3, 2)  (3, 3)  (3, 4)
(4, 0)  (4, 1)  (4, 2)  (4, 3)  (4, 4)
If you want to move bottom-right from (2, 2), you’d add (1, 1) to your current position.

So:
Current Position: (2, 2)
Move Bottom-Right: (2 + 1, 2 + 1) = (3, 3)
This shows that (1, 1) is a direction, not a fixed coordinate. 
It means: "Take one step down and one step right from wherever you are."
"""
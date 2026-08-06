from collections import deque  # Import a queue, which helps us explore step-by-step
from typing import List  # Import List to use type hints for better code readability

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # A small helper function to check if a cell (row, col) is safe to explore
        def valid(row, col):
            # The cell must be inside the matrix AND must contain a 1 (since we need to update 1s)
            return 0 <= row < m and 0 <= col < n and mat[row][col] == 1

        # Get the number of rows and columns in the matrix
        m = len(mat)  # m is the number of rows (how tall the grid is)
        n = len(mat[0])  # n is the number of columns (how wide the grid is)
        # m = len(mat) counts how many rows there are (how tall the grid is).
        # n = len(mat[0]) counts how many columns are in the first row (how wide the grid is).

        # Create a queue to store the cells we need to explore next
        queue = deque()  # Imagine a line of people waiting their turn to explore the grid
        seen = set()  # A set to keep track of which cells we’ve already visited

        # Step 1: Start by adding all the '0' cells to the queue
        for row in range(m):  # Go through each row in the matrix
            for col in range(n):  # Go through each column in that row
                if mat[row][col] == 0:  # If the cell contains a 0
                    seen.add((row, col))  # Mark this cell as visited
                    queue.append((row, col, 1))  # Add it to the queue with step count 1

        # Step 2: Define the 4 possible directions to move in the grid
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        # Step 3: Start the BFS (explore cells step-by-step from all 0s)
        while queue:  # While there are still cells to explore in the queue
            row, col, steps = queue.popleft()  # Get the next cell from the queue

            # Step 4: Explore all 4 directions from the current cell
            for dx, dy in directions:  # For each direction (Right, Down, Left, Up)
                                   # up + down, left + right
                next_row, next_col = row + dy, col + dx  # Calculate the new position

                # Check if the new cell is valid and hasn't been visited yet
                if (next_row, next_col) not in seen and valid(next_row, next_col):
                    seen.add((next_row, next_col))  # Mark it as visited
                    queue.append((next_row, next_col, steps + 1))  # Add it to the queue
                    mat[next_row][next_col] = steps  # Update the cell with the step count

        # Step 5: After exploring everything, return the updated matrix
        return mat

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example input matrix
    mat = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 1]
    ]

    # Output: [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    print(solution.updateMatrix(mat))

"""
Pseudocode (How It Works)
Step 1: First, find all the 0s in the grid and add them to a queue. We treat 0s as the starting points (like treasures).
Step 2: Use a queue to explore nearby cells in all 4 directions (up, down, left, right).
Step 3: Keep counting how many steps it takes from a 0 to reach the 1s.
Step 4: If we reach a 1, we update it with the number of steps taken.
Step 5: Keep doing this until we explore all cells connected to 0s.
"""
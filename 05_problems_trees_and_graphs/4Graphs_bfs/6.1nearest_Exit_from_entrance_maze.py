from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Get the number of rows and columns in the maze
        rows, cols = len(maze), len(maze[0])
        # Possible directions to move: right, left, down, up
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        # Mark the entrance as visited because we are not considering it an exit
        start_row, start_col = entrance
        maze[start_row][start_col] = "+"

        # Start BFS (breadth-first search) from the entrance
        queue = deque()
        queue.append([start_row, start_col, 0])  # (row, col, distance)

        while queue:
            curr_row, curr_col, curr_distance = queue.popleft()  # Get the front of the queue

            # Check all four directions (right, left, down, up)
            for d in dirs:
                next_row, next_col  = curr_row + d[0], curr_col + d[1]

                # If the neighboring cell is inside the maze and is an empty cell (".")
                if 0 <= next_row < rows and 0 <= next_col < cols and maze[next_row][next_col] == ".":

                    # If this empty cell is on the boundary, it's an exit, return the distance
                    if next_row == 0 or next_row == rows - 1 or next_col == 0 or next_col == cols - 1:
                        return curr_distance + 1

                    # Mark the cell as visited and add it to the queue
                    maze[next_row][next_col] = "+"
                    queue.append([next_row, next_col, curr_distance + 1])

        # If no exit is found after exploring the entire maze, return -1
        return -1


# Example usage of the nearestExit function
if __name__ == "__main__":
    solution = Solution()

    # Test case input
    maze = [["+", "+", ".", "+"],
            [".", ".", ".", "+"],
            ["+", "+", "+", "."]]
    entrance = [1, 2]

    # Expected output: 1 (since the nearest exit is directly to the left of the entrance)
    # Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
    # Initially, you are at the entrance cell [1,2].
    # - You can reach [1,0] by moving 2 steps left.
    # - You can reach [0,2] by moving 1 step up.
    # It is impossible to reach [2,3] from the entrance.
    # Thus, the nearest exit is [0,2], which is 1 step away.
    result = solution.nearestExit(maze, entrance)
    print(f"Nearest exit distance: {result}")  # Should print 1

    # Test case input
    maze = [["+","+","+"],
            [".",".","."],
            ["+","+","+"]]
    entrance = [1,0]
    result1 = solution.nearestExit(maze, entrance)
    print(f"Nearest exit distance: {result1}")  # Should print 2


"""
https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+').
You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column
of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot
step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell
that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

#----------------------------------------------------------------------------------------------------#

Approach 1: Breadth First Search (BFS)
Intuition
This problem is about finding the shortest path in a matrix, thus Breadth First Search (BFS) is a promising method.
    Why BFS over Depth First Search (DFS) for this problem?

The reason is that DFS is not guaranteed to find the shortest path, as it will explore the matrix as much as possible
before moving on to another branch. As shown in the picture below, we may explore the matrix along the green or orange
paths first, but these are not the shortest path.

In BFS, however, we explore cells by the order of their distance from the starting position, so whenever we reach an
exit cell, we are guaranteed that it is the closest exit!

In BFS, we explore cells in the order of their distance from the starting position. We will first visit the cell with
a distance of 0, then move on to all the cells with a distance of 1, then move on to all the cells with a distance of 2,
and so forth.

We use a queue as the container to store all the cells to be visited. Since the operation on a queue is done in
First In, First Out (FIFO) order, it allows us to explore all the cells with distance d which we previously stored,
before moving on to cells with larger distance d + 1!
    How do we prevent revisiting the same cells?

Upon finding an unvisited neighbor cell, we mark it as visited before adding it to the queue, and we skip these visited
cells during further searches. Thus, each empty cell will be added to the queue at most once.
(Since the input matrix maze use different characters to separate empty cells (.) and walls (+), we can take advantage
of this by marking cells to be visited as +.)

Algorithm
1. Initialize an empty queue queue to store all the nodes to be visited.
2. Add entrance and its distance 0 to queue and mark entrance as visited.
3. While we don't reach an exit and queue still has cells, pop the first cell from queue.
Suppose its distance from entrance is curr_distance. We check its neighboring cells in all four directions,
if it has an unvisited neighbor cell:
    If this neighbor cell is an exit, return its distance from the starting position, curr_distance + 1,
    as the nearest distance.
    Otherwise, we mark it as visited, and add it to queue along with its distance curr_distance + 1.
4. If we finish the iteration and no exit is found, return -1.
"""
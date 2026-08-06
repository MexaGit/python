from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)  # Get the size of the board (n x n)

        # Create a flattened version of the board, with positions mapped to cells
        cells = [None] * (n ** 2 + 1)  # We use 1-based indexing, so we add 1 extra element
        label = 1  # This is the flattened board position we will fill
        columns = list(range(0, n))  # List of column indices, left to right initially

        # Traverse the board row by row, in a zigzag manner (left to right, then right to left)
        for row in range(n - 1, -1, -1):  # Start from the bottom row to the top
            for column in columns:
                cells[label] = (row, column)  # Map the flattened board position to (row, column)
                label += 1
            columns.reverse()  # Alternate direction for the next row (zigzag pattern)

        # Distance array, initialized to -1. dist[i] will hold the minimum number of moves to reach cell i.
        dist = [-1] * (n * n + 1)
        dist[1] = 0  # Starting at cell 1, so it takes 0 moves to reach there

        # BFS queue initialized with the start position (cell 1)
        q = deque([1])

        # Perform BFS to calculate the minimum number of moves to reach each cell
        while q:
            curr = q.popleft()  # Get the current cell we are at

            # Check the next 6 possible cells we could move to (as per the dice roll)
            for next in range(curr + 1, min(curr + 6, n ** 2) + 1):
                row, column = cells[next]  # Find the board position (row, column) for cell 'next'

                # Determine where we would land if there is a snake/ladder, or just move to 'next'
                destination = board[row][column] if board[row][column] != -1 else next

                # If this destination cell hasn't been visited yet, mark its distance and add it to the queue
                if dist[destination] == -1:
                    dist[destination] = dist[curr] + 1  # Increment the number of moves
                    q.append(destination)  # Add the new destination to the queue

        # Return the number of moves to reach the last cell (n*n), or -1 if it's unreachable
        return dist[n * n]

# Test case setup
# Explanation:
# In the beginning, you start at square 1 (at row 5, column 0).
# You decide to move to square 2 and must take the ladder to square 15.
# You then decide to move to square 17 and must take the snake to square 13.
# You then decide to move to square 14 and must take the ladder to square 35.
# You then decide to move to square 36, ending the game.
# This is the lowest possible number of moves to reach the last square, so return 4.
board = [[-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 35, -1, -1, 13, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 15, -1, -1, -1, -1]]

# Expected output: 4
expected_output = 4

# Solution instance
solution = Solution()

# Running the test
output = solution.snakesAndLadders(board)
print(f"Output: {output}, Expected: {expected_output}")

"""
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting
from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:
    Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
        This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations,
        regardless of the size of the board.
    If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
    The game ends when you reach the square n2.

A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or
ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start
of another snake or ladder, you do not follow the subsequent snake or ladder.
    For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow
    the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.

#----------------------------------------------------------------------------------------------------------#
Approach 1: Breadth-first search
Intuition
Breadth-first search is an algorithm for finding the shortest path in unweighted graphs (directed or undirected).

This algorithm uses a queue. If this data structure is new to you, we encourage you to visit the queue and stack
explore card. The explore card will help you understand the data structure and practice using it before proceeding.

The queue data structure has two primary operations:
    enqueue: add an element to the end of the queue.
    dequeue: remove the first element in the queue.
C++, Java, Python and other programming languages have built-in queue implementations.

The breadth-first search operates as follows. It maintains a queue of vertices (nodes). It starts with only the
starting vertex (cell 1 in this problem). Then it processes the vertices one by one in the queue. Let's say we are
processing some vertex. There are (possibly zero) outgoing edges from this vertex. If these edges lead to unvisited
vertices, push these vertices to the queue. The algorithm terminates when it has visited all vertices.

Algorithm
1. Find the cell (row,column) associated with each label from 1 to n2. Start from the bottom left cell and traverse the
board alternately left to right and right to left. One can do this by maintaining the order of columns and reversing it
after each row.

2. Maintain a queue of cells and an array to store distances to all cells from the first one. By distance to the cell,
we mean the least number of moves required to reach it. The distance from the first cell to itself is 0.
Mark all other cells as initially unreachable from the first one (we denote the distance to such cells with −1).
Push the first cell to the queue.

3. While the queue is not empty:
Pop a cell from the queue. Let's say its label is curr. For each square next with a label in the range curr+1 to
min(curr+6,n2) (as described by the problem), if next has a snake or a ladder, set destination to the destination of
that snake or ladder. Otherwise, set destination to next.

If dist[destination] is −1 (i.e. the destination has not been visited yet) set dist[destination] to dist[curr]+1
(the number of moves to get to the current cell, plus one more move to get to destination) and push destination on to
the queue.

Return the distance to cell n2. If it is unreachable, the result will be −1.
"""
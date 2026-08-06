from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Function to check if a given row and column index is valid within the board boundaries.
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        # Backtracking function to explore the board for the target word.
        def backtrack(row, col, i, seen):
            # If we have matched all characters of the word, return True.
            if i == len(word):
                return True

            # Explore all four possible directions (right, down, left, up).
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx  # Calculate next cell coordinates

                # Check if the next cell is within bounds and not already seen.
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    # If the character in the next cell matches the current character in the word.
                    if board[next_row][next_col] == word[i]:
                        seen.add((next_row, next_col))  # Mark the cell as seen

                        # Recur for the next character in the word.
                        if backtrack(next_row, next_col, i + 1, seen):
                            return True  # If we found the word, return True

                        # Backtrack: unmark the cell as we explore other paths.
                        seen.remove((next_row, next_col))

            return False  # If no valid path found for this character, return False

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up directions
        m = len(board)  # Number of rows in the board
        n = len(board[0])  # Number of columns in the board

        # Start searching for the word from each cell in the board.
        for row in range(m):
            for col in range(n):
                # If the first character of the word matches the current cell,
                # we start the backtracking from here.
                if board[row][col] == word[0] and backtrack(row, col, 1, {(row, col)}):
                    return True  # If we found the word, return True

        return False  # If no valid path found for the word, return False

# Test Case 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Expected Output: True
print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))

# Test Case 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Expected Output: True
print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))

# Test Case 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Expected Output: False
print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))

# Test Case 4:
# Input: board = [["A"]], word = "A"
# Expected Output: True
print(Solution().exist([["A"]], "A"))

# Test Case 5:
# Input: board = [["A"]], word = "B"
# Expected Output: False
print(Solution().exist([["A"]], "B"))

"""
https://leetcode.com/problems/word-search/description/
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.

#------------------------------------------------------------------------------------------------#

Approach 1: Backtracking
Intuition
This problem is yet another 2D grid traversal problem, which is similar with another problem called 489. Robot Room
Cleaner. https://leetcode.com/problems/robot-room-cleaner/editorial/

Many people in the discussion forum claimed that the solution is of DFS (Depth-First Search). Although it is true that
we would explore the 2D grid with the DFS strategy for this problem, it does not capture the entire nature of the solution.

We argue that a more accurate term to summarize the solution would be backtracking, which is a methodology where we
mark the current path of exploration, if the path does not lead to a solution, we then revert the change
(i.e. backtracking) and try another path.

As the general idea for the solution, we would walk around the 2D grid, and at each step, we mark our choice before
jumping into the next step. And at the end of each step, we would also revert our mark so that we will have a clean
slate to try another direction. In addition, the exploration is done via the DFS strategy, where we go as far as
possible before we try the next direction.


Algorithm
There is a certain code pattern for all the algorithms of backtracking. For example, one can find one template in our
Explore card of Recursion II. https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2793/

The skeleton of the algorithm is a loop that iterates through each cell in the grid. For each cell, we invoke the
backtracking function (i.e. backtrack()) to check if we would obtain a solution, starting from this very cell.

For the backtracking function backtrack(row, col, suffix), as a DFS algorithm, it is often implemented as a recursive
function. The function can be broke down into the following four steps:

Step 1). At the beginning, first we check if we reach the bottom case of the recursion, where the word to be matched
is empty, i.e. we have already found the match for each prefix of the word.

Step 2). We then check if the current state is invalid, either the position of the cell is out of the boundary of the
board or the letter in the current cell does not match with the first letter of the word.

Step 3). If the current step is valid, we then start the exploration of backtracking with the strategy of DFS. First,
we mark the current cell as visited, e.g. any non-alphabetic letter will do. Then we iterate through the four possible
directions, namely up, right, down and left. The order of the directions can be altered, to one's preference.

Step 4). At the end of the exploration, we revert the cell back to its original state. Finally we return the result of
the exploration.

We demonstrate how it works with an example in the following animation.
"""
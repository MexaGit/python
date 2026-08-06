from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 🚦 Function to check if the land is valid (so we don't explore off the map!)
        def valid(row, col):
            # ✔️ It's valid if it's within the grid and the spot is "1" (land)
            return 0 <= row < m and 0 <= col < n and grid[row][col] == "1"

        # 🛟 Use a stack to explore all the connected land pieces (like an island adventure!)
        def dfs(start_row, start_col):
            stack = [(start_row, start_col)]  # 🎒 Start with this land piece in your backpack
            while stack:  # 🚶 Keep going while there’s land left to explore
                row, col = stack.pop()  # 🎯 Grab the last land piece we added
                # 🧭 Explore all four directions (right, down, left, up)
                for dx, dy in directions:
                    next_row = row + dy  # 🛤️ Move to a new row
                    next_col = col + dx  # ➡️ Move to a new column

                    # 🔍 Check if the next spot is land and we haven’t visited it yet
                    if valid(next_row, next_col) and (next_row, next_col) not in seen:
                        seen.add((next_row, next_col))  # 📝 Mark it as visited (no coming back!)
                        stack.append((next_row, next_col))  # 🎒 Add it to the stack to explore next

        # 🗺️ Directions to move: (right, down, left, up)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # 📖 Create a book to track all the land pieces we've visited
        seen = set()

        # 🏝️ A counter to keep track of how many islands we find
        ans = 0

        # 🌐 Find the size of the grid (number of rows and columns)
        m = len(grid)  # Rows (horizontal)
        n = len(grid[0])  # Columns (vertical)

        # 🔄 Go over every spot in the grid, looking for new islands
        for row in range(m):  # Check each row (top to bottom)
            for col in range(n):  # Check each column (left to right)
                # 🏝️ If we find a piece of unvisited land ("1"):
                if (row, col) not in seen and grid[row][col] == "1":
                    ans += 1  # 🎉 We found a new island! Add 1 to our island counter.
                    seen.add((row, col))  # 📝 Mark the land as visited
                    dfs(row, col)  # 🛶 Explore the rest of the island

        return ans  # 🏁 Return the total number of islands we found!

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
class Solution(object):
    # Depth-First Search (Iterative) [Accepted]
    def maxAreaOfIsland(self, grid):
        seen = set()
        ans = 0
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                    and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans

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

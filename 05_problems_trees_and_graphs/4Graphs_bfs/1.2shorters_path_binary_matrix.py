from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        # Determine the maximum valid row and column indices.
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1

        # Define all 8 possible movement directions: diagonal, horizontal, and vertical.
        # directions = [(0, 1), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1), (0, -1), (-1, 0)]
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # top-left, top, top-right
            (0, -1),           (0, 1),   # left, right
            (1, -1),  (1, 0),  (1, 1)    # bottom-left, bottom, bottom-right
        ]

        # Helper function to find valid neighbors of a cell at (row, col).
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference

                # Ensure the new row and column are within bounds and the cell is not blocked.
                if not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:  # Blocked cells are ignored.
                    continue
                yield (new_row, new_col)

        # Check that the first and last cells are open.
        # Edge case: If the start (0, 0) or end (max_row, max_col) is blocked, return -1.
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1

        # Set up the BFS.
        # Initialize BFS with the start position (0, 0).
        queue = deque()
        queue.append((0, 0))  # Start from the top-left corner (0, 0).
        grid[0][0] = 1  # Mark the start position as visited and set its distance to 1.

        # Carry out the BFS.
        # Perform BFS to explore the grid.
        while queue:
            row, col = queue.popleft()  # Get the current cell's position.
            distance = grid[row][col]  # Current distance from the start.

            # If we have reached the bottom-right corner (max_row, max_col), return the distance.
            if (row, col) == (max_row, max_col):
                return distance

            # Explore all valid neighboring cells.
            for neighbour_row, neighbour_col in get_neighbours(row, col):
                # Mark the neighbor as visited by updating its distance.
                grid[neighbour_row][neighbour_col] = distance + 1
                # Add the neighbor to the queue for further exploration.
                queue.append((neighbour_row, neighbour_col))

        # # There was no path.
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
# Path: (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2)
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
https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
Algorithm

Now that we've determined that this is a BFS problem, we need to fill in a few more details and figure out how it 
will all go together. Recall that BFS is implemented using a queue.

A queue is what we refer to as a First-In-First-Out (FIFO) data structure, comparable to people queuing to go on a 
theme park ride. People enter the queue at the back and leave from the front. BFS works by putting the start node 
on the queue, and then while the queue is non-empty, it takes a node off the front of the queue and puts that node's
 neighbors on the back of the queue. In this way, the graph is progressively explored, starting with the nodes 
 nearest to the start node and ending with the nodes farthest away.

We commonly refer to putting a node on the queue as enqueuing and taking a node off the queue as dequeuing. 
We'll use this terminology for the remainder of the article.

Applying BFS to this problem, we'll use the queue to keep track of cells that we have numbered but haven't yet 
numbered the * neighbors* of. While usually for BFS, we'd need a "visited" set to avoid infinite looping around 
cycles, we won't need one for this approach because we're going to overwrite the input, and so only unvisited 
cells will have a 0 in them.

Here's the pseudocode for setting up the BFS. We identify cells with a (row, col) pair. The top-left cell is at 
row = 0 and col = 0 so is identified with the pair (0, 0).

queue = a new queue
enqueue cell (0, 0)
set grid[0][0] to 1

We enqueue the top-left cell as it's the first cell we'll be exploring. We also need to set its distance to be 1 
in the grid (note that this will not cause confusion with the 1's that were used to represent blocked cells).

Now that we've done the initialization, it's time to design the main BFS loop (again, this is fairly standard 
template stuff).

While there are cells left on the queue, we should dequeue a cell, look up its distance (that has already been 
 into the input grid), and explore its neighbors. Exploring the cell's neighbors involves identifying all open 
 cells adjacent to the current cell that still have a 0 in them. For each of these cells, we write the number 
 distance + 1 into them. Finally, we need to enqueue the neighbor so that when we're ready, we can explore its 
 neighbors too.

Here is some pseudocode.

while queue is not empty:

    cell = dequeue a cell
    look up distance at grid[cell row][cell col]

    for each open neighbour:
        if this neighbour is the bottom right cell (target):
            return distance + 1
        set grid[neighbour row][neighbour col] = distance + 1
        enqueue neighbour
return -1

A few points to note:
We return -1 if the loop terminates without returning, as this means we ran out of cells to explore before reaching
the bottom-right cell.

The reason we can simply do distance = grid[cell row][cell col] is because cells are only enqueued once a number 
has been written into them.

We should only write numbers into cells that currently have a 0 in them. If, for example, a cell already had a 2 
in it and you then change that to a 4, it would no longer have the number that represents the shortest distance 
from the top left to itself.

It would be okay to do the check for the bottom-right cell in the outer loop. We would need to return distance 
instead of distance + 1.

The final thing we need to consider is how to get all the neighbors of a cell. In traditional graph representations,
this would be the equivalent of examining all the edges of a given node. For grids, we identify each neighbor 
by its row and column offset from the given cell.

Offsets of a cell's neighbors.

The most common pattern is to put these "offsets" into a list as follows.

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
We can then iterate over this list and use each offset to calculate a neighbor row and column. We need to be careful, 
though; while most cells have 8 neighbors, corner cells only have 3 neighbors, and edges cells have 5 neighbors. 
To handle this, we start by checking that the neighbors row and column actually are within the dimensions of the grid. 
If they are within the grid, we also check that the cell currently contains a 0 (in other words, it hasn't yet been 
numbered and is open). If the cell contains a 0, then we add it to a list of all the neighbors to be returned.

Here is the pseudocode that puts all of this together. This function is reusable for many grid problems (usually 
without the 4 diagonal directions). You should be very familiar with this algorithm and be able to implement it in 
your programming language of choice very quickly.

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

define function get_neighbors(row, col):
neighbors = a container to put the neighbors of (row, col) in
    for each (row_direction, col_direction) pair in directions:
        neighbor_row = row + row_direction
        neighbor_col = col + col_direction
        if (neighbor_row, neighbor_col) is NOT over the edge of the grid AND is 0:
            add (neighbor_row, neighbor_col) to neighbors
    return neighbors
    
Note that it is very important to check that the neighbor row and column are within the grid before checking the number
in it. In most languages, getting this wrong will cause a crash. In Python, it will cause weird bugs due to Python's 
handling of negative indices.

Some people prefer to put the logic for get_neighbors(...) directly into the BFS loop to avoid the need for a separate 
function. It's a matter of personal preference as to which way is best. I prefer to keep it separate because it keeps 
the main BFS loop simpler and cleaner. Additionally, the logic for identifying neighbors is a separate concern to that 
of carrying out a BFS with them.

Complexity Analysis
Let N be the number of cells in the grid.

Time complexity : O(N).
Each cell was guaranteed to be enqueued at most once. This is because a condition for a cell to be enqueued was that 
it had a zero in the grid, and when enqueuing, we also permanently changed the cell's grid value to be non-zero.

The outer loop ran as long as there were still cells in the queue, dequeuing one each time. Therefore, it ran at
most N times, giving a time complexity of O(N).

The inner loop iterated over the unvisited neighbors of the cell that was dequeued by the outer loop. There were at 
most 8 neighbors. Identifying the unvisited neighbors is an O(1) operation because we treat the 8 as a constant.
Therefore, we have a time complexity of O(N).

Space complexity : O(N).
The only additional space we used was the queue. We determined above that at most, we enqueued N cells. Therefore, 
an upper bound on the worst-case space complexity is O(N).

Given that BFS will have nodes of at most two unique distances on the queue at any one time, it would be reasonable 
to wonder if the worst-case space complexity is actually lower. But actually, it turns out that there are cases with 
massive grids where the number of cells at a single distance is proportional to N. So even with cells of a single 
distance on the queue, in the worst case, the space needed is O(N).
"""
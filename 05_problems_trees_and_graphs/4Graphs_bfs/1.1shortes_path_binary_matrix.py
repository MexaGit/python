from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Step 1: If the starting point (0, 0) is blocked, return -1
        if grid[0][0] == 1:
            return -1

        # Step 2: A helper function to check if a cell is valid for traversal
        def valid(row, col):
            return 0 <= row < n and 0 <= col < n and grid[row][col] == 0

        # Initialize the size of the grid (assuming a square grid)
        n = len(grid)

        # Step 3: Initialize the BFS queue with the starting point and the number of steps
        seen = {(0, 0)}  # To mark visited cells
        queue = deque([(0, 0, 1)])  # Queue holds (row, col, steps) to track position and distance

        # Step 4: Directions to explore: all 8 possible movements in a grid (including diagonals)
        directions = [(0, 1), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1), (0, -1), (-1, 0)]

        # Step 5: Perform BFS
        while queue:
            row, col, steps = queue.popleft()  # Dequeue current position
            # Step 6: If we have reached the bottom-right corner, return the number of steps
            if (row, col) == (n - 1, n - 1):
                return steps

            # Step 7: Explore all 8 possible directions from the current position
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                # If the next position is valid and hasn't been visited
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))  # Mark the position as visited
                    queue.append((next_row, next_col, steps + 1))  # Enqueue the new position with incremented steps

        # Step 8: If no path exists, return -1
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
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell
(i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share
an edge or a corner).
The length of a clear path is the number of visited cells of this path.

#---------------------------------------------------------------------------------------#
If an interviewer asks you this question in an interview, then their goal is probably to determine that:

You can recognize that this is a typical shortest path problem that can be solved with a Breadth-first search (BFS).
You can correctly implement a BFS to solve it.
For bonus points, you know that the solution could be optimized using the A* algorithm.
For this article, I'm going to assume that you already know the fundamentals of BFS and are at the stage of 
figuring out how to apply it to a wide range of problems, such as this one. If you aren't yet at this stage, 
then I recommend checking out our relevant Explore Card content on BFS before coming back to this problem.
https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1376/

We'll look at two BFS implementations in this article; one that overwrites the input and another that does not. 
We'll also take a look at how this problem could be solved using A*.

As long as you communicate clearly with your interviewer about what you're doing, making the input more "friendly" 
towards your eyes and brain can be one of the most effective problem-solving techniques when you're stuck. 
Most problems that involve grids of 0's and 1's become a lot easier when drawn like this.

Now that our example is ready to go, have a go at finding the shortest distance to get from the top-left to the 
bottom-right cell.

Finding the shortest path between two nodes in a graph is almost always done using BFS, and all programmers 
should know this. BFS is one of the fundamental algorithms that you are expected to be confident coding before 
a tech interview. So, if you're finding this question challenging, then you're doing the right thing by working 
on it now.

Now that we've determined that this is a BFS problem, we need to fill in a few more details and figure out how it 
will all go together. Recall that BFS is implemented using a queue.

A queue is what we refer to as a First-In-First-Out (FIFO) data structure, comparable to people queuing to go on a 
theme park ride. People enter the queue at the back and leave from the front. BFS works by putting the start node 
on the queue, and then while the queue is non-empty, it takes a node off the front of the queue and puts that node's
 neighbors on the back of the queue. In this way, the graph is progressively explored, starting with the nodes 
 nearest to the start node and ending with the nodes farthest away.

We commonly refer to putting a node on the queue as enqueuing and taking a node off the queue as dequeuing. We'll 
use this terminology for the remainder of the article.

Applying BFS to this problem, we'll use the queue to keep track of cells that we have numbered but haven't yet 
numbered the * neighbors* of. While usually for BFS, we'd need a "visited" set to avoid infinite looping around 
cycles, we won't need one for this approach because we're going to overwrite the input, and so only unvisited 
cells will have a 0 in them.

#---------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------#

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
handling of negative indices.6
"""
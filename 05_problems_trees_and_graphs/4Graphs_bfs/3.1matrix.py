from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Function to check if the cell (row, col) is valid for processing.
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and mat[row][col] == 1

        # Get the dimensions of the matrix
        m = len(mat)  # Number of rows
        n = len(mat[0])  # Number of columns

        # Queue to perform BFS and set to keep track of seen cells
        queue = deque()
        seen = set()

        # Initialize the queue with all the cells that contain 0
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:  # If the cell contains 0
                    queue.append((row, col, 1))  # Append (row, col, steps) to queue
                    seen.add((row, col))  # Mark this cell as seen

        # Directions for moving in the 4 possible directions (right, down, left, up)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Perform BFS to calculate the distances
        while queue:
            row, col, steps = queue.popleft()  # Get the next cell from the queue

            # Explore all 4 possible directions from the current cell
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx  # Calculate the next cell's coordinates

                # If the next cell is valid and hasn't been seen yet
                if (next_row, next_col) not in seen and valid(next_row, next_col):
                    seen.add((next_row, next_col))  # Mark the next cell as seen
                    # Increment stpes by one when we pass it to next level
                    queue.append((next_row, next_col, steps + 1))  # Add it to the queue
                    mat[next_row][next_col] = steps  # Update the distance in the matrix, the answer

        return mat  # Return the updated matrix


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
Given an m x n binary (every element is 0 or 1) matrix mat, find the distance of the nearest 0 for each cell.
The distance between adjacent cells (horizontally or vertically) is 1.

For example, given mat = [[0,0,0],[0,1,0],[1,1,1]], return [[0,0,0],[0,1,0],[1,2,1]].

We have another matrix graph. We are already familiar with traversing these with the help of tools like valid and
directions.

An important observation to make: there is no difference between starting at a 1 and looking for a 0, or starting from
a 0 and looking for a 1.

Let's say you are focusing on a 1 at square x. We do a BFS and find the nearest 0 is at a square y.

Now, let's try starting a BFS from every 0 looking for x. After performing many BFS, you find that the one that
produced a minimum distance was y.

This leads us to our solution. In all the BFS examples we have looked at so far in the course, we initialize the
queue with only one node - the node we start our BFS from. This single node represented the 0th level - the nodes
that have a distance of 0 from the source. There is nothing stopping us from having multiple nodes in the 0th level.

We said that with BFS, every time we visit a node, we do so in the fewest steps possible from the source.
The "source" is actually the 0th level - not a single node. It's just that so far, we have only looked at problems
where the 0th level had only one node.

In this problem, we can have the "source" be any node with a value of 0. We do this by initializing queue with
all 0 nodes. Again, we should associate the steps taken so far (the level) with each node. By the definition of BFS,
every time we visit a node, we will have done so in the fewest steps possible from a 0, which is exactly what the
problem is asking for. By using seen, we will not override any shortest distances we have already found.

#--------------------------------------------------------------------------------------------------#

Approach 1: Breadth-First Search (BFS)
Intuition

The first thing you should think about when it comes to shortest path problems on graphs is BFS. If you're not familiar 
with BFS, we suggest you read the relevant LeetCode Explore Card.
First of all, any cell with value 0 does not need to be changed. For a given cell with value 1, we need to find the 
nearest 0. We could perform a BFS starting from the cell and terminate once we find any 0, as this 0 would be the 
closest one. By repeating this for every cell with value 1, we would solve the problem.

The issue with this is that the constraints state that the matrix could have up to 10,000 cells. Think about a matrix 
where the entire matrix is 1 except for one of the corners. We would need to perform O(size) BFS, with each BFS costing 
up to O(size). In the worst-case scenario, the number of operations we would need is on the order of 100,000,000, which 
would fail the time limit. We need to think of a more efficient way to perform the BFS.

What if we started the BFS from 0 instead of 1? Let's say that we started a BFS from a 1 and found that the 
nearest 0 was x steps away. Now, let's start a BFS from that 0 until we reach the original 1. We will again find 
that the BFS takes x steps. Basically, it doesn't matter if we start from the 0 or 1, both will result in the same 
distance.

If we start BFS from 1, we can only find the shortest distance for that 1. If we start BFS from 0, we could find the 
shortest distance for many 1 at a time. So which 0 should we start from? The answer is all of them!

Let's think about how BFS works. From a source node, we first visit all nodes at a distance of 1. Next, we visit all 
nodes at a distance of 2, then 3, and so on. We can say a node at a distance of x from the source belongs to "level x".
 So the source is at level 0, the neighbors of the source are at level 1, the neighbors of those nodes are at level 2, 
 and so on.

We are used to starting BFS from only one source node, i.e. level 0 only has one node. But there is nothing stopping 
us from having multiple nodes in level 0. If we start with multiple nodes in level 0, then the nodes in level 1 will 
be all the neighbors of the nodes in level 0. The nodes in level 2 will be all the neighbors of the nodes in level 1, 
and so on - the logic is identical. The following animation illustrates this idea (cells are labeled by their level):

As you can see, we don't need to visit any node more than once, which drastically improves our time complexity.

Algorithm

1. Create a copy of mat, we'll call it matrix.
2. Use a data structure seen to mark nodes we have already visited and a queue for the BFS.
3. Put all nodes with 0 into the queue. We will also track the level/number of steps with each queue entry. Mark these nodes in seen as well.
4. Perform the BFS:
    While queue is not empty, get the current row, col, steps from the queue.
    Iterate over the 4 directions. For each nextRow, nextCol, check if it is in bounds and not already visited in seen.
    If so, set matrix[nextRow][nextCol] = steps + 1 and push nextRow, nextCol, steps + 1 onto the queue. 
    Also mark nextRow, nextCol in seen.
5. Return matrix.

Complexity Analysis
Given m as the number of rows and n as the number of columns,

Time complexity: O(m⋅n)
The BFS never visits a node more than once due to seen. Each node has at most 4 neighbors, so the work done at each 
node is O(1). This gives us a time complexity of O(m⋅n), the number of nodes.

Space complexity: O(m⋅n)
Note: some people may choose to modify the input mat instead of creating a copy matrix and using seen.
It is generally not considered good practice to modify the input, especially if it's an array as they are passed by 
reference. Even then, you would only be saving on auxiliary space - if you modify the input as part of your algorithm, 
you still need to count it towards the space complexity.

We could also elect to not count matrix as part of the space complexity as it serves only as the output and the output 
does not count towards the space complexity if it is not used in any logic during the algorithm.

There is a lot of nuance when it comes to these decisions and you should always clarify your decisions with the 
interviewer.

In our implementation, seen and queue uses O(m⋅n) space regardless of interpretation, so that is our space complexity.
"""
from collections import deque
from typing import List, Optional

# Binary tree node class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # If root is empty, return an empty list
        if not root:
            return []

        ans = []  # To store the largest value at each level
        queue = deque([root])  # Use deque for level-order traversal (BFS)

        # Loop through all levels of the binary tree
        while queue:
            current_length = len(queue)  # Number of nodes in the current level
            curr_max = float("-inf")  # This will store the largest value for the current level

            # Process all nodes at the current level
            for _ in range(current_length):
                node = queue.popleft()  # Pop the current node
                # Update the current max for the level
                curr_max = max(curr_max, node.val)
                # Add the left child of the current node to the queue if it exists
                if node.left:
                    queue.append(node.left)
                # Add the right child of the current node to the queue if it exists
                if node.right:
                    queue.append(node.right)
            # After processing all nodes at the current level, append the max value to the result
            ans.append(curr_max)
        # Return the list of largest values, which represent the largest values at each level
        return ans

# Example of how the solution works:
# Given binary tree [1, 3, 2, 5, 3, null, 9]:
#
#        1
#      /   \
#     3     2
#    / \     \
#   5   3     9
#
# The largest values in each row are [1, 3, 9].

# Test case 1
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)
solution = Solution()
print(solution.largestValues(root))  # Output: [1, 3, 9]

# Test case 2 (tree with only one node)
root = TreeNode(1)
solution = Solution()
print(solution.largestValues(root))  # Output: [1]

# Test case 3 (tree with all negative values)
root = TreeNode(-1)
root.left = TreeNode(-2)
root.right = TreeNode(-3)
root.left.left = TreeNode(-4)
root.left.right = TreeNode(-5)
solution = Solution()
print(solution.largestValues(root))  # Output: [-1, -2, -4]

"""
https://leetcode.com/problems/find-largest-value-in-each-tree-row/editorial/
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Intuition

If you are not familiar with BFS traversal, we suggest you read our relevant LeetCode Explore Card.
BFS is perfect when we are dealing specifically with rows/levels of a binary tree. With BFS, we handle one row of
the tree at a time.
Here, we need to find the maximum value in each row. We can simply perform a BFS and for each row, keep track
of the maximum value we have seen so far. We will initialize an integer currMax to a small value like negative infinity. Then we go through the row and try to update currMax when we see larger values. After handling the row, we add currMax to our answer.

Algorithm
1.- If the root is null (empty) tree, just return an empty list.
2.- Initialize the answer list ans and a queue with the root to perform BFS.
3.- Perform BFS - while the queue is not empty:
    Initialize currMax to a small value and save the length of the queue in currentLength.
    Iterate currentLength times:
        Remove a node from the queue.
        Update currMax with node.val if it is larger.
        For each child of node, if it is not null, push it to the queue.
    Add currMax to ans.
4.- Return ans.


"""
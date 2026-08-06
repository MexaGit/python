from collections import deque
from typing import List, Optional

# Binary tree node class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # If root is empty, return an empty list
        if not root:
            return []

        ans = []  # To store the rightmost node at each level
        queue = deque([root])  # Use deque for level-order traversal (BFS)

        # Loop through all levels of the binary tree
        while queue:
            current_length = len(queue)  # Number of nodes in the current level

            # The rightmost node of the current level is the last node in the queue
            # Level 2: Queue contains [2, 3].
            # queue[-1] → Node with value 3 (rightmost of this level).
            # Level 3: Queue contains [5, 4].
            # queue[-1] → Node with value 4 (rightmost of this level).
            ans.append(queue[-1].val) # this is the rightmost node for the current level

            # Process all nodes at the current level
            for _ in range(current_length):
                node = queue.popleft()  # Pop the current node

                # Add the left child of the current node to the queue if it exists
                if node.left:
                    queue.append(node.left)

                # Add the right child of the current node to the queue if it exists
                if node.right:
                    queue.append(node.right)

        # Return the list of rightmost nodes, which forms the right side view of the tree
        return ans


# Example of how the solution works:
# Given binary tree [1, 2, 3, null, 5, null, 4]:
#
#        1
#      /   \
#     2     3
#      \     \
#       5     4
#
# The right-side view is [1, 3, 4] because these are the nodes visible from the right.

# Test case 1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
solution = Solution()
print(solution.rightSideView(root))  # Output: [1, 3, 4]

# Test case 2 (tree with only one node)
root = TreeNode(1)
solution = Solution()
print(solution.rightSideView(root))  # Output: [1]

"""
https://leetcode.com/problems/binary-tree-right-side-view/editorial/
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes
 you can see ordered from top to bottom.
 
 Binary Tree Traversals
|
|-- Depth First (DFS)
|   |
|   |-- Preorder
|   |   |-- Iterative with stack
|   |   |-- Recursive
|   |   |-- Morris
|   |
|   |-- Inorder
|   |   |-- Iterative with stack
|   |   |-- Recursive
|   |   |-- Morris
|   |
|   |-- Postorder
|       |-- Iterative with stack
|       |-- Recursive
|       |-- Morris
|
|-- Breadth First (BFS)
    |
    |-- Iterative with queue

"""
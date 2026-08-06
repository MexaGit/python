from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []  # If the tree is empty, return an empty list

        result = []  # Store the final zigzag order of levels
        queue = deque([root])  # Initialize the queue with the root node
        is_order_left = True  # A flag to alternate between left-to-right and right-to-left

        # Perform BFS, level by level
        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            level = deque()  # Use a deque to build the current level

            for _ in range(level_size):
                node = queue.popleft()  # Pop the current node from the queue

                # Append the node's value to the level list based on the zigzag order
                if is_order_left:
                    level.append(node.val)  # Left to right
                else:
                    level.appendleft(node.val)  # Right to left

                # Add the child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Add the current level to the result list
            result.append(list(level))
            # Toggle the order for the next level
            is_order_left = not is_order_left

        return result  # Return the final zigzag order

# Example of how the solution works:
# Given binary tree [3, 9, 20, null, null, 15, 7]:
#
#        3
#      /   \
#     9     20
#          /  \
#         15   7
#
# The zigzag level order is [[3], [20, 9], [15, 7]].

# Test case 1
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.zigzagLevelOrder(root))  # Output: [[3], [20, 9], [15, 7]]

# Test case 2 (tree with only one node)
root = TreeNode(1)
solution = Solution()
print(solution.zigzagLevelOrder(root))  # Output: [[1]]

# Test case 3 (empty tree)
root = None
solution = Solution()
print(solution.zigzagLevelOrder(root))  # Output: []

# Test case 4 (full binary tree)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.zigzagLevelOrder(root))  # Output: [[1], [3, 2], [4, 5, 6, 7]]

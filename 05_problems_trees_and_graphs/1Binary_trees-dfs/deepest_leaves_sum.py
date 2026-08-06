# Binary tree node class
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_depth = -1  # To track the deepest level found
        deepest_sum = 0  # To accumulate the sum of the deepest leaves
        stack = [(root, 0)]  # Stack to store nodes along with their depth

        while stack:
            node, depth = stack.pop()

            # If it's a leaf node
            if not node.left and not node.right:
                if depth > max_depth:
                    max_depth = depth  # Found a new maximum depth
                    deepest_sum = node.val  # Reset the sum to the current node's value
                elif depth == max_depth:
                    deepest_sum += node.val  # Add to the current deepest sum

            # Add child nodes to the stack
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return deepest_sum

# Example of how the solution works:
# Given binary tree [1, 2, 3, 4, 5, null, 6, 7, null, null, null, null, 8]:
#
#        1
#      /   \
#     2     3
#    / \     \
#   4   5     6
#  /           \
# 7             8
#
# The deepest leaves are 7 and 8, and their sum is 15.

# Test case 1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)
root.right.right.right = TreeNode(8)

solution = Solution()
print(solution.deepestLeavesSum(root))  # Output: 15

# Test case 2 (tree with only one node)
root = TreeNode(1)
solution = Solution()
print(solution.deepestLeavesSum(root))  # Output: 1

# Test case 3 (tree with a single deepest leaf)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

solution = Solution()
print(solution.deepestLeavesSum(root))  # Output: 9 (4 + 5)

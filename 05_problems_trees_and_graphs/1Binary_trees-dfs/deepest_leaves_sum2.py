# Definition for a binary tree node.
from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # Helper function to find the maximum depth of the tree
        def find_max_depth(node):
            if not node:
                return 0
            return 1 + max(find_max_depth(node.left), find_max_depth(node.right))

        # Recursive function to sum the leaves at the target depth
        def sum_deepest_leaves(node, depth, target_depth):
            if not node:
                return 0
            if depth == target_depth and not node.left and not node.right:
                return node.val
            return (sum_deepest_leaves(node.left, depth + 1, target_depth) +
                    sum_deepest_leaves(node.right, depth + 1, target_depth))

        # Step 1: Find the maximum depth of the tree
        max_depth = find_max_depth(root)

        # Step 2: Sum the leaves at the deepest level
        return sum_deepest_leaves(root, 1, max_depth)


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

from collections import deque
from typing import Optional

# Binary tree node class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Iterative DFS Preorder Traversal.
    class Solution:
        def deepestLeavesSum(self, root: TreeNode) -> int:
            deepest_sum = depth = 0
            stack = [(root, 0)]

            while stack:
                node, curr_depth = stack.pop()
                if node.left is None and node.right is None:
                    # if this leaf is the deepest one seen so far
                    if depth < curr_depth:
                        deepest_sum = node.val  # start new sum
                        depth = curr_depth  # note new depth
                    # if there were already leaves at this depth
                    elif depth == curr_depth:
                        deepest_sum += node.val  # update existing sum

                else:
                    if node.right:
                        stack.append((node.right, curr_depth + 1))
                    if node.left:
                        stack.append((node.left, curr_depth + 1))

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

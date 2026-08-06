from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr):
            if not node:
                return False

            # if both children are null, then the node is a leaf
            if node.left is None and node.right is None:
                return (curr + node.val) == targetSum

            curr += node.val
            left = dfs(node.left, curr)
            right = dfs(node.right, curr)
            return left or right
            # if left:
            #     return left
            # else:
            #     return right

        return dfs(root, 0)

# Example binary tree:
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  / \
# 7   2
node5 = TreeNode(5)
node4 = TreeNode(4)
node8 = TreeNode(8)
node11 = TreeNode(11)
node13 = TreeNode(13)
node4_2 = TreeNode(4)
node7 = TreeNode(7)
node2 = TreeNode(2)

# Link nodes together
node5.left = node4
node5.right = node8
node4.left = node11
node8.left = node13
node8.right = node4_2
node11.left = node7
node11.right = node2

# Create an instance of Solution and test hasPathSum
solution = Solution()
target_sum = 22
result = solution.hasPathSum(node5, target_sum)
print(result)  # Expected output: True
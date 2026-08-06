from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right

# Example binary trees
# Tree 1:
#       1
#      / \
#     2   3
p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(3)
p1.left = p2
p1.right = p3

# Tree 2:
#       1
#      / \
#     2   3
q1 = TreeNode(1)
q2 = TreeNode(2)
q3 = TreeNode(3)
q1.left = q2
q1.right = q3

# Create an instance of Solution and test isSameTree
solution = Solution()
result = solution.isSameTree(p1, q1)
print(result)  # Expected output: True

# Example for different trees
# Tree 3:
#       1
#      / \
#     2   1
r1 = TreeNode(1)
r2 = TreeNode(2)
r3 = TreeNode(1)
r1.left = r2
r1.right = r3

# Test with different tree (Tree 1 and Tree 3)
result_different = solution.isSameTree(p1, r1)
print(result_different)  # Expected output: False
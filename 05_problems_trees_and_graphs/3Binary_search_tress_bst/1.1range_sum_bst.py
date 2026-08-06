from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # If the current node is None, return 0
        if not root:
            return 0

        ans = 0  # Initialize sum of values within range

        # Check if the current node's value is within the specified range
        if low <= root.val <= high:
            ans += root.val  # Add to the sum if within range

        # If the current node's value is greater than low, check left subtree
        if low < root.val:
            ans += self.rangeSumBST(root.left, low, high)

        # If the current node's value is less than high, check right subtree
        if root.val < high:
            ans += self.rangeSumBST(root.right, low, high)

        return ans  # Return the total sum

# Example of how the solution works:
# Given binary tree [10, 5, 15, 3, 7, null, 18] and range [7, 15]:
#
#        10
#       /  \
#      5   15
#     / \    \
#    3   7   18
#
# The sum of values within the range [7, 15] is 32 (7 + 10 + 15).

# Test case 1
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

solution = Solution()
print(solution.rangeSumBST(root, 7, 15))  # Output: 32

# Test case 2 (empty tree)
root = None
print(solution.rangeSumBST(root, 5, 10))  # Output: 0

# Test case 3 (all nodes are within the range)
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

print(solution.rangeSumBST(root, 1, 20))  # Output: 30 (10 + 5 + 15)

# Test case 4 (no nodes are within the range)
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

print(solution.rangeSumBST(root, 20, 30))  # Output: 0

"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes 
with a value in the inclusive range [low, high].
"""

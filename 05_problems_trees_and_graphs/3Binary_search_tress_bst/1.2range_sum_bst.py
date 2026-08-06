from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        # 1. Start with a total sum = 0
        ans = 0
        # 2. Put the root node in the backpack (stack)
        stack = [root]

        # 3. While there are still nodes in the backpack:
        while stack:
            # 4. Take out one node from the backpack
            node = stack.pop()

            # 5. If the node’s value is between low and high:
            if low <= node.val <= high:
                # 6. Add the node’s value to the total sum
                ans += node.val
            # 7. If the node has a left child and its value might be useful (low < current value):
            if node.left and low < node.val:
                # 8. Put the left child in the backpack
                stack.append(node.left)
            # 9. If the node has a right child and it might help (current value < high):
            if node.right and node.val < high:
                # 10. Put the right child in the backpack
                stack.append(node.right)
        # 11. When the backpack is empty, return the total sum
        return ans

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

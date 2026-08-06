#  Recursive Inorder + Linear search, O(N) time
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(r: TreeNode):
            # return inorder(r.left) + [r.val] + inorder(r.right) if r else []
            if r:
                # Traverse the left subtree, add the current node's value, and then traverse the right subtree
                return inorder(r.left) + [r.val] + inorder(r.right)
            else:
                # If the node is None, return an empty list
                return []

        return min(inorder(root), key=lambda x: abs(target - x))

# Example of how the solution works:
# Given the following binary search tree:
#
#       4
#      / \
#     2   5
#    / \
#   1   3
#
# Let's find the closest value to target = 3.7.
# The closest value to 3.7 is 4.

# Test case 1
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

solution = Solution()
print(solution.closestValue(root, 3.7))  # Output: 4

# Test case 2 (target is less than the smallest value)
print(solution.closestValue(root, 0.5))  # Output: 1

# Test case 3 (target is greater than the largest value)
print(solution.closestValue(root, 6.0))  # Output: 5

# Test case 4 (target is exactly equal to a node's value)
print(solution.closestValue(root, 3.0))  # Output: 3

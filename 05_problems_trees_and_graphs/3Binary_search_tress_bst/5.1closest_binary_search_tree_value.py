# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Binary Search, O(H) time
    def closestValue(self, root: TreeNode, target: float) -> int:
        # Initialize the closest value as the value of the root node
        closest = root.val

        # Traverse the tree while there are nodes to visit
        while root:
            # Update the closest value based on the current node's value
            closest = min(root.val, closest, key=lambda x: (abs(target - x), x))
            # Move to the left or right child depending on the target value
            root = root.left if target < root.val else root.right

        # Return the closest value found
        return closest

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

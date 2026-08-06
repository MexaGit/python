# 🌲 Definition of a treasure chest (node) in the magic tree.
class TreeNode:
    def __init__(self, x: int):
        self.val = x  # 🏺 Store the treasure value in the chest.
        self.left = None  # ➡️ Path to the smaller treasures (left side).
        self.right = None  # ➡️ Path to the larger treasures (right side).

class Solution:
    # 🔍 Function to find the treasure closest to the target value.
    def closestValue(self, root: TreeNode, target: float) -> int:
        # 🎯 Start by assuming the closest treasure is in the root chest.
        closest = root.val
        # 🔄 Keep exploring the tree as long as there are more chests to check.
        while root:
            # 🔍 Compare the current treasure with the closest found so far.
            # 🛠️ Use a fancy trick to choose the closest:
            #    Compare absolute differences to the target value.
            # closest = min(2, 4, key=lambda x: (abs(3.7 - 4), 4)  # => (0.3, 4)
            closest = min(closest, root.val, key=lambda x: (abs(target - x), x))
            # closest = min(2, 4, key=lambda x: (abs(3.7 - 2), 2)  # => (1.7, 2)

            # 🚶‍♂️ If the target value is smaller, move to the left (smaller treasures).
            if target < root.val:
                root = root.left
            # 🚶‍♂️ If the target value is bigger, move to the right (bigger treasures).
            else:
                root = root.right

        # 🎉 When you can’t explore further, return the closest treasure you found!
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


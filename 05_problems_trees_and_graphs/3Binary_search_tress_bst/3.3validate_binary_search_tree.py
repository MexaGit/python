from typing import Optional

# 🌲 Definition of a treasure chest (node) in the tree.
class TreeNode:
    def __init__(self, x: int):
        self.val = x  # 🏺 Store the treasure inside this chest.
        self.left = None  # ➡️ A path to the smaller treasures (left side).
        self.right = None  # ➡️ A path to the bigger treasures (right side).

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 🏡 If there’s no tree (empty root), return False. No tree to explore!
        if not root:
            return False

        # 🎒 Start by putting the root node in the backpack (stack).
        # 📏 Each node carries a valid treasure range (small, large).
        stack = [(root, float("-inf"), float("inf"))]  # 🌐 Start with no limits (-inf to inf).

        # 🔄 Keep checking until the backpack (stack) is empty:
        while stack:
            # 🎯 Grab a node from the backpack to inspect.
            node, small, large = stack.pop()

            # 🚨 Check if the treasure in this node is between the allowed range.
            if not (small < node.val < large):
                return False  # ❌ If not, the treasure tree is not valid.
            # 🛤️ If the node has a **left child** (smaller treasure):
            # Add it to the backpack with the updated range (must be less than the current node).
            if node.left:
                stack.append((node.left, small, node.val))
            # 🛤️ If the node has a **right child** (bigger treasure):
            # Add it to the backpack with an updated range (must be larger than the current node).
            if node.right:
                stack.append((node.right, node.val, large))
        # 🎉 If we checked all nodes and everything follows the rules, it’s a valid tree!
        return True


# Example of how the solution works:
# Given binary tree [2, 1, 3]:
#
#        2
#       / \
#      1   3
#
# This is a valid BST.

# Test case 1: Valid BST
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

solution = Solution()
print(solution.isValidBST(root1))  # Output: True

# Test case 2: Invalid BST
root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)

print(solution.isValidBST(root2))  # Output: False

# Test case 3: Single node (valid BST)
root3 = TreeNode(1)

print(solution.isValidBST(root3))  # Output: True

# Test case 4: Empty tree (valid BST)
print(solution.isValidBST(None))  # Output: True

# Test case 5: More complex invalid BST
root4 = TreeNode(10)
root4.left = TreeNode(5)
root4.right = TreeNode(15)
root4.right.left = TreeNode(6)  # This makes the tree invalid

print(solution.isValidBST(root4))  # Output: False

"""
Scenario: Inventory System Check 📦
Problem Statement:

"You’re working on a warehouse management system that stores product data in a hierarchical catalog. Each product 
category is arranged such that:

Subcategories on the left contain lower-value items (or earlier serial numbers).
Subcategories on the right contain higher-value items (or later serial numbers).
The entire product catalog must follow these rules to ensure correct data entry. Your task is to write a program to 
verify whether the catalog follows this structure correctly."
"""
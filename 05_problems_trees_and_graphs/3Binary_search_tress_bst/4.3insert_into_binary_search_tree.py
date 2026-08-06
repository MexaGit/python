from typing import Optional, List

# 🌲 Definition of a treasure node (TreeNode).
class TreeNode:
    def __init__(self, x: int):
        self.val = x  # 🏺 Store the treasure (value) inside the chest (node).
        self.left = None  # ➡️ A path to smaller treasures (left branch).
        self.right = None  # ➡️ A path to bigger treasures (right branch).

class Solution:
    # 🌳 This function helps us insert a new treasure into the right spot in the tree.
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root  # 🌟 Start at the root of the treasure tree.

        # 🔄 Keep moving down the tree until we find the right spot.
        while node:
            # 🛤️ If the new treasure is bigger, go to the right branch.
            if val > node.val:
                # 🌱 If there’s no right child, plant the new treasure here.
                if not node.right:
                    # Is there already a treasure in the right room? if not
                    node.right = TreeNode(val)  # 🌳 Add the new treasure (node).
                    return root  # 🎉 Done! Return the root of the updated tree.
                else:
                    node = node.right  # 🚶‍♂️ Keep walking down the right branch.

            # 🛤️ If the new treasure is smaller, go to the left branch.
            else:
                # 🌱 If there’s no left child, plant the new treasure here.
                if not node.left:
                    node.left = TreeNode(val)  # 🌳 Add the new treasure (node).
                    return root  # 🎉 Done! Return the root of the updated tree.
                else:
                    node = node.left  # 🚶‍♂️ Keep walking down the left branch.

        # 🌲 If the tree is empty, create a new tree with the treasure as the root.
        return TreeNode(val)

# Example of how the solution works:
# Starting with the following BST:
#        4
#       / \
#      2   7
#     / \
#    1   3
#
# Inserting the value 5 should result in:
#        4
#       / \
#      2   7
#     / \  /
#    1   3 5

# Test case 1: Insert into existing BST
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(7)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)

solution = Solution()
new_root1 = solution.insertIntoBST(root1, 5)

# Function to do an inorder traversal of the BST and return values as a list
def inorder_traversal(node: Optional[TreeNode]) -> List[int]:
    if not node:
        return []
    return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

print(inorder_traversal(new_root1))  # Output: [1, 2, 3, 4, 5, 7]

# Test case 2: Insert into an empty BST
new_root2 = solution.insertIntoBST(None, 10)
print(inorder_traversal(new_root2))  # Output: [10]

# Test case 3: Insert a value less than existing values
new_root3 = solution.insertIntoBST(root1, 0)
print(inorder_traversal(new_root3))  # Output: [0, 1, 2, 3, 4, 5, 7]

# Test case 4: Insert a value greater than existing values
new_root4 = solution.insertIntoBST(root1, 8)
print(inorder_traversal(new_root4))  # Output: [1, 2, 3, 4, 7, 8]

"""
Possible Real-World Scenario for a BST Insertion Problem
Scenario: Product Catalog Management 📦
Problem Statement:

"You are building an inventory system for an e-commerce platform like Amazon. The products in each category are 
arranged in a sorted catalog, with smaller product IDs (or names) placed before larger ones. Each product is connected 
to its subcategories (in a tree structure).

When a new product arrives, it needs to be inserted into the correct place to maintain the sorted order. 
Your task is to insert this new product into the correct place in the catalog and return the updated catalog structure.
It’s guaranteed that the new product does not already exist in the catalog."
"""
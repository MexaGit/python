from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # recursion:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> TreeNode:
        # If the tree is empty, create a new node with the given value
        if not root:
            return TreeNode(val)

        # If the value to insert is greater than the current node's value,
        # insert it into the right subtree
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            # If the value to insert is less than or equal to the current node's value,
            # insert it into the left subtree
            root.left = self.insertIntoBST(root.left, val)

        # Return the unchanged root node
        return root

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
You are given the root node of a binary search tree (BST) and a value to insert into the tree. 
Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the 
original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion.
You can return any of them.

The recursion implementation is very straightforward :
    If root is null - return TreeNode(val).
    If val > root.val - go to insert into the right subtree.
    If val < root.val - go to insert into the left subtree.
    Return root.
"""

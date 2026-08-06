from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # iteration
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while node:
            # insert into the right subtree
            if val > node.val:
                # insert right now
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            # insert into the left subtree
            else:
                # insert right now
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
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
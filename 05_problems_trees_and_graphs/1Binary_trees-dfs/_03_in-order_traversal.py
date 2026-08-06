# Binary tree node class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_dfs(node):
    if not node:
        return

    inorder_dfs(node.left) # first the left of each node and leaf 1,2,4
    print(node.val)
    inorder_dfs(node.right) #
    return

# Example binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5
#      /  \
#     6    7
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

# Construct the tree
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node5.left = node6
node5.right = node7

# Test the inorder_dfs function
inorder_dfs(node1)

"""
1. In-order Traversal (Left, Root, Right):
Order: Visit the left subtree, 
then the root node, 
then the right subtree.
This traversal of a Binary Search Tree (BST) gives nodes in non-decreasing order.

For inorder traversal, we first recursively call the left child, then perform logic (print in this case) 
on the current node, and then recursively call the right child. This means no logic will be done until 
we reach a node without a left child since calling on the left child takes priority over performing logic.

Running the above code on the example tree, we would see the nodes printed in this order: 3, 1, 4, 6, 0, 2, 5.
Notice that for any given node, its value is not printed until all values in the left subtree are printed, 
and values in its right subtree are not printed until after that.
"""
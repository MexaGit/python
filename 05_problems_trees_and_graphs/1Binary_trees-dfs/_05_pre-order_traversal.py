# Binary tree node class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_dfs(node):
    if not node:
        return

    print(node.val)
    preorder_dfs(node.left)
    preorder_dfs(node.right)
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
preorder_dfs(node1)

"""
2. Pre-order Traversal (Root, Left, Right):
Order: Visit the root node first, 
then the left subtree, 
and finally the right subtree.

Pre-order traversal is often used for copying or serializing the tree.

In preorder traversal, logic is done on the current node before moving to the children. 
Let's say that we wanted to just print the value of each node in the tree to the console. 
In that case, at any given node, we would print the current node's value, then recursively call the left child, 
then recursively call the right child.
Running the above code on the example tree, we would see the nodes printed in this order: 0, 1, 3, 4, 6, 2, 5.

Because the logic (printing) is done immediately at the start of each function call, preorder handles nodes 
in the same order that the function calls happen.
"""
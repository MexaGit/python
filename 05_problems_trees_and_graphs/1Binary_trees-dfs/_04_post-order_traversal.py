# Binary tree node class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorder_dfs(node):
    if not node:
        return

    postorder_dfs(node.left)
    postorder_dfs(node.right)
    print(node.val)
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
postorder_dfs(node1)

"""
Post-order Traversal (Left, Right, Root):
Order: Visit the left subtree, 
then the right subtree, 
and finally the root node.
Post-order is useful for deleting or freeing the tree (used in garbage collection).

The name of each traversal is describing when the current node's logic is performed.

Pre -> before children
In -> in the middle of children
Post -> after children

In postorder traversal, we recursively call on the children first and then perform logic on the current node.
This means no logic will be done until we reach a leaf node since calling on the children takes priority over 
performing logic. In a postorder traversal, the root is the last node where logic is done.

Running the above code on the example tree, we would see the nodes printed in this order: 3, 6, 4, 1, 5, 2, 0.
Notice that for any given node, no values in its right subtree are printed until all values in its left subtree 
are printed, and its own value is not printed until after that.
"""

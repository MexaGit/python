class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

"""
The following code builds a tree that looks like:
    0
  /   \
 1     2
"""

root = TreeNode(0)
one = TreeNode(1)
two = TreeNode(2)

root.left = one
root.right = two

print(root.left.val)
print(root.right.val)
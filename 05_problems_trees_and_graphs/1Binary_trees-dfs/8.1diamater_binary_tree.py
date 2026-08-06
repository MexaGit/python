# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0

        # Helper function to find the longest path
        def longest_path(node):
            nonlocal diameter
            if not node:
                return 0
            # Recursively calculate the longest path for left and right children
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            # Update the diameter at the current node
            diameter = max(diameter, left_path + right_path)

            # Return the longest path considering this node and its parent
            return max(left_path, right_path) + 1

        longest_path(root)
        return diameter

# Example binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

# Create the nodes
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

# Construct the tree
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

# Create an instance of Solution and test diameterOfBinaryTree
solution = Solution()
diameter = solution.diameterOfBinaryTree(node1)
print(diameter)  # Expected output: 3



"""
Let's try to be more specific about how to apply DFS to this question. To count the lengths of each node's
left and right branches, we can implement a recursion function longestPath which takes a TreeNode as input
and returns the longest path from it to the leaf node. It will recursively visit children nodes and retrieve
the longest paths from them to the leaf first, and then add 1 to the longer one before returning it as
the longest path.

In the midst of DFS, we also need to take the following two cases into account:
    1.- the current node's both left and right branches might be a part of the longest path;
    2.- one of the current node's left/right branches might be a part of the longest path.

Figure 1. Two cases of the longest path.
You will see we are going to address them by 1) applying DFS to recursively find the longest branches starting
with the node's left and right children; 2) initializing a global variable diameter to keep track of the longest
path and updating it at each node with the sum of the node's left and right branches; 3) returning the length
of the longest branch between a node's left and right branches.

Algorithm
Initalize an integer variable diameter to keep track of the longest path we find from the DFS.
Implement a recursive function longestPath which takes a TreeNode as input. It should recursively explore the entire tree rooted at the given node. Once it's finished, it should return the longest path out of its left and right branches:
    if node is None, we have reached the end of the tree, hence we should return 0;
    we want to recursively explore node's children, so we call longestPath again with node's left and right children.
    In return, we get the longest path of its left and right children leftPath and rightPath;
    if leftPath plus rightPath is longer than the current longest diameter found, then we need to update diameter;
    finally, we return the longer one of leftPath and rightPath. Remember to add 1 as the edge connecting it with
    parent.
Call longestPath with root.

"""
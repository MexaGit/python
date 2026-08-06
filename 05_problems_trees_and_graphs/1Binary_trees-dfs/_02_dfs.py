# Binary tree node class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node):
    if node is None:
        # Base case: if the current node is None, return (we've reached the end of a path)
        return
    # So process left first, to the end, then return one back
    # go to node.right, check if his has node.left if not
    # return one back and so on
    # Process left subtree first
    dfs(node.left)  # First recursive check: if node.left is None, hit the base case and return immediately
    # Process right subtree after the left on
    print(node.val)
    dfs(node.right)  # Third check: if node.right is None, hit the base case and return immediately
    # Return control to the previous recursive call (go one level up in the recursion tree)
    return f"{node.left}, {node.right}"

# def dfs1(node):
#     if node is None:
#         return "None"
#
#     # Recursively call dfs on the left and right children and return their values
#     left_str = dfs1(node.left)
#     right_str = dfs1(node.right)
#
#     # Return a string representation of the current node and its children
#     return f"{node.val}: ({left_str}, {right_str})"

# Example binary tree:
#       0
#      / \
#     1   2
#    /  \   \
#   3    4   5
#  /    /  \
# 6    7    8
# Test with the following structure:
# Creating the tree structure
node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
# Connecting nodes to build the tree
# Step-by-Step Breakdown:
# Start at the root (node0), but before processing 0, go to node.left.
# Now at node1, again go to node.left (node3).
# At node3, go further to node.left (node6), which has no left child. So you print 6.
# Return back to node3 and process it by printing 3.
# There is no right child for node3, so return back to node1.
# Process node1 by printing 1, then move to node1.right (node4).
# At node4, go to node.left (node7), which has no left child, so print 7.
# Return to node4 and print 4, then move to node4.right (node8).
# Print 8, then return to node1, then node0.
# Now process node0 by printing 0, and then move to node0.right (node2).
# node2 has no left child, so print 2, then move to node2.right (node5).
# Print 5.
node0.left = node1
node0.right = node2
node1.left = node3
node1.right = node4
node2.right = node5
node3.left = node6
node4.left = node7
node4.right = node8


# Test the dfs function
dfs(node0)
#print(dfs1(node1))
# Expected output: (no return value, the function just performs DFS traversal)
# The order of traversal should be: 2, 3

"""
https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/707/traversals-trees-graphs/4686/
In a Depth-First Search (DFS) on Binary Trees , we prioritize depth by traversing as far down the tree as possible in 
one direction (until reaching a leaf node) before considering the other direction. For example, let's say we choose 
left as our priority direction. We move exclusively with node.left until the left subtree has been fully explored. 
Then, we explore the right subtree.

There are three main types of DFS traversal in binary trees: In-order, Pre-order, and Post-order.

The good news is that the structure for performing a DFS is very similar across all problems. It goes as follows:
Handle the base case(s). Usually, an empty tree (node = null) is a base case.
Do some logic for the current node
Recursively call on the current node's children
Return the answer
"""
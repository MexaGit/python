from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function to validate the BST property using DFS
        def dfs(node, small, large):
            # An empty node is a valid BST
            if not node:
                return True

            # The current node's value must be within the valid range
            if not (small < node.val < large):
                return False

            # Recursively check left and right subtrees with updated ranges
            left = dfs(node.left, small, node.val)  # Left subtree must be less than the current node
            right = dfs(node.right, node.val, large)  # Right subtree must be greater than the current node

            # The tree is a BST if both left and right subtrees are also valid BSTs
            return left and right

        # Start the DFS with the entire range of values
        return dfs(root, float("-inf"), float("inf"))


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
wGiven the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

#----------------------------------------------------------------------------------------#

Using recursion, we can construct a function dfs that takes a node and returns true if the tree rooted at node 
is a BST. First, what arguments do we need to pass (other than the node)? In a BST, the root node can be any value
because it is not the child of any node, but every node in the left subtree should be less than it, and every node
in the right subtree should be greater than it. To enforce this, we can use two integer arguments small and large,
and make sure small < node.val < large holds.

If we are defining (small, large) as the interval for allowed values, how do we update them to maintain the BST 
property? At each node, the left subtree nodes should be less than node.val, so we can update large = node.val. 
The right subtree nodes should be greater than node.val, so we can update small = node.val. For the root node, 
we can initialize small = -infinity and large = infinity - the root can be any value since it has no parent.

Remember the definition of a BST: "In a BST, at any given node, let's say your data is val. All data in the left 
subtree is less than val, and all data in the right subtree is greater than val". Because of the "at any given node", 
this means that in a BST, all subtrees are also BSTs. Therefore, given an input node, we need to make sure that 
node.left and node.right are also BSTs.

What is the base case? An empty tree (no nodes) is technically a BST. Therefore, we can return true when the current
node is null.

#----------------------------------------------------------------------------------------#

If a tree rooted at node is a binary search tree, then node.left and node.right must also be binary search trees. 
Because the function isValidBST we are implementing determines if a tree is a binary search tree, we have a 
recursive way to look at the problem.
isValidBST(node.left) && isValidBST(node.right) must be true, and also the current node's value must not violate 
the BST property.

To determine if a node's value is violating the BST property, we can use two arguments small and large. 
These represent the (exclusive) range (small, large) in which a node's value should fall under. If a node's value 
is not in this range, then it is violating the BST property and we can return false.

The root node can have any value, so we initialize small = -infinity and large = infinity.
Every node in the root's left subtree must be less than root.val, so when we call on the left subtree, we can pass
large = root.val.

Every node in the root's right subtree must be greater than root.val, so when we call on the right subtree, we can 
pass small = root.val.
By updating small and large in this manner, we ensure that the constraint that determines if a node's value is 
acceptable is always accurate, as recursion will keep a copy of small and large for each node.

As a base case, when we encounter an empty tree, we return true. Again, think about the case where the input tree 
is a single node. Any node on its own is by definition a binary search tree, so we would need both 
isValidBST(root.left) and isValidBST(root.right) to return true, so we need the empty tree to return true.
"""
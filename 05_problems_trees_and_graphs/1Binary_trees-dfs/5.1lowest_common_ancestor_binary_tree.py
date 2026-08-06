from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[
        TreeNode]:
        if not root:
            return None

        # First case: if the current node is p or q
        if root == p or root == q:
            return root

        # Recursively find LCA in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # Second case: if both left and right are not null, root is the LCA
        if left and right:
            return root

        # Third case: return the non-null child (left or right)
        return left if left else right

    # Here iteratively solve:
    # https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/editorial/

# Example binary tree:
#       3
#      / \
#     5   1
#    / \ / \
#   6  2 0  8
#     / \
#    7   4

# Create the nodes
node3 = TreeNode(3)
node5 = TreeNode(5)
node1 = TreeNode(1)
node6 = TreeNode(6)
node2 = TreeNode(2)
node0 = TreeNode(0)
node8 = TreeNode(8)
node7 = TreeNode(7)
node4 = TreeNode(4)

# Construct the tree
node3.left = node5
node3.right = node1
node5.left = node6
node5.right = node2
node1.left = node0
node1.right = node8
node2.left = node7
node2.right = node4

# Create an instance of Solution and test lowestCommonAncestor
solution = Solution()
lca = solution.lowestCommonAncestor(node3, node5, node1)
print(lca.val)  # Expected output: 3 (the root node)

# Test with different nodes
lca_different = solution.lowestCommonAncestor(node3, node5, node4)
print(lca_different.val)  # Expected output: 5 (the ancestor of node 5 and node 4)

"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
# Example binary tree:
#       3
#      / \
#     5   1
#    / \ / \
#   6  2 0  8
#     / \
#    7   4

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3

Explanation: The LCA of nodes 5 and 1 is 3.

#--------------------------------------------------------------------------------#
This problem is a classic one and a bit trickier than the ones we have already looked at. 
Again, we want our recursive function to return the answer to the question. What is the base case? 
If we have an empty tree, then no LCA exists - return null.

Otherwise, how can we tell if a node is the LCA? Let's say that we are at the root, then there are 3 possibilities.
1.- The root node is p or q. The answer cannot be below the root node, because then it would be missing the root 
(which is either p or q) as a descendant.
2.- One of p or q is in the left subtree, and the other one is in the right subtree. The root must be the answer 
because it is the connection point between the two subtrees, and thus the lowest node to have both p and q as 
descendants.
3.- Both p and q are in one of the subtrees. In that case, the root is not the answer because we could look inside 
the subtree and find a "lower" node.

Remember: because of the recursive nature of trees, we can translate the cases into an algorithm. We just need 
to figure out how to find the answer if it is the first or third case.

In the first case, if we see that the current node is either p or q, we don't need to worry about the subtrees 
at all, because we know the answer cannot be in them. Therefore, we can return something (non-null) right away. 
In the base case, we return null. Therefore, a call to a subtree returns a non-null value only if one of p or q 
is in that subtree. We should return null for a subtree that contains neither p nor q.

Then, the second case is implied if both calls to the left and right subtrees return something non-null, 
and the third case is implied if only one of the calls returns something.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # Define the depth-first search (dfs) function
        def dfs(root: TreeNode) -> int:
            if root is None:
                return 0

            # If only one child is non-null, go into that recursion
            if root.left is None:
                return dfs(root.right) + 1
            elif root.right is None:
                return dfs(root.left) + 1

            # Both children are non-null, so call dfs for both children
            return min(dfs(root.left), dfs(root.right)) + 1

        return dfs(root)
    #Breadth-First Search (BFS)
    """
    Algorithm
    Return 0 if the root is NULL.
    Initialize the queue q with the root node and depth to 1.
    Do the following while the queue isn't empty:
    i. Iterate over all the nodes that are currently in the queue.
    ii. Skip the node if it's null; otherwise, if it's a leaf node, then return depth.
    iii. For each node, add the left and right child to the queue.
    iv. Increment the depth once the level is fully iterated.
    Ideally, our code shouldn't reach here, so return any value once the queue is empty.
    """

# Example binary tree:
#       3
#      / \
#     9  20
#       /  \
#      15   7

# Create the nodes
node3 = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)

# Construct the tree
node3.left = node9
node3.right = node20
node20.left = node15
node20.right = node7

# Create an instance of Solution and test minDepth
solution = Solution()
min_depth = solution.minDepth(node3)
print(min_depth)  # Expected output: 2

"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/editorial/
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

#-------------------------------------------------------------------------#

We are given a binary tree; we must return the minimum number of nodes between the root and any leaf node, 
including both. Let's try to break this problem into subproblems; we need to return the answer from the root 
of the current tree; what if we know the answer considering the left and right child of the root node? If 
the minimum depth for the root node's left child is x and the minimum depth for the root node's right child is y, 
then the minimum depth for the whole tree with the root node will be 1 + min(x, y). The additional +1 
is for the current root node.

This way, we can divide the current problem into subproblems and then solve them using recursion. 
The base condition of this recursion would be when the node is NULL, in which case we should return 0. 
One tricky thing that we need to consider is when one of the children is NULL and the other one isn't. 
We shouldn't move forward with recursion on the NULL child; if we do, we would return 0 due to the base 
condition and the count of nodes from the leaf node on the other side would be discarded as we are taking 
the minimum of the two. In case both children are NULL, it's fine to go into recursion as both would return 0, 
and the minimum of the two won't cause an issue.

If we observe closely, we are first traversing to the deepest node and then backtracking to the parent node 
to find the minimum depth for it; hence, this process is actually Depth-First Search (DFS).

Algorithm:
We will use the dfs method with root as an argument.
The base condition of the recursion would be for the NULL node, in which case we should return 0.
If the left child of root is NULL, then we should return 1 + minimum depth for the right child of the root node, 
which is 1 + dfs(root.right).
If the right child of root is NULL, then we should return 1 + minimum depth for the left child of the root node, 
which is 1 + dfs(root.left).
If both child are non-null, then return 1 + min(dfs(root.left), dfs(root.right)).
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
# Here's the iterative approach
# (remember that iterative is much less common and should only be used if an interviewer asks for it):
    def hasPathSum1(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # stack = [(node, curr)]
        # stack = [(TreeNode(4), 5), (TreeNode(8), 5)]
        # stack = [(TreeNode(4), 5), (TreeNode(9), 13), (TreeNode(13), 13)]
        # stack = [(TreeNode(4), 5), (TreeNode(9), 13)]
        # stack = [(TreeNode(4), 5)]
        # stack = [(TreeNode(11), 9), (TreeNode(2), 9)]
        # stack = [(TreeNode(11), 9)]
        # stack = [(TreeNode(7), 20), (TreeNode(2), 20)]
        stack = [(root, 0)]
        while stack:
            # print_stack(stack)
            # you're unpacking the tuple, meaning you're assigning:
            node, curr = stack.pop()

            # if both children are null, then the node is a leaf
            if node.left is None and node.right is None:
                # node.val: This is the value of the current node being processed in the loop.
                # curr: This is the sum of the values of all nodes along the path leading up to (but not including)
                # the current node. This value is passed along through the recursive/iterative traversal as the
                # algorithm goes deeper into the tree.
                # if (20 + 2) == 22: checks whether the sum of the current path (including the current node)
                if (curr + node.val) == targetSum:
                    return True

            # is key to updating the cumulative sum as you traverse down the binary tree.
            curr += node.val # curr = 5 + 8 = 13
            if node.left:
                stack.append((node.left, curr))  # stack.append((4, 5))
            if node.right:
                stack.append((node.right, curr))  # stack.append((8, 5))

        return False

# Example binary tree:
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  / \
# 7   2
node5 = TreeNode(5)
node4 = TreeNode(4)
node8 = TreeNode(8)
node11 = TreeNode(11)
node13 = TreeNode(13)
node4_2 = TreeNode(4)
node7 = TreeNode(7)
node2 = TreeNode(2)

# Link nodes together
node5.left = node4
node5.right = node8
node4.left = node11
node8.left = node13
node8.right = node4_2
node11.left = node7
node11.right = node2

# Create an instance of Solution and test hasPathSum
solution = Solution()
target_sum = 22
result = solution.hasPathSum1(node5, target_sum)
print(result)  # Expected output: True

"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf
path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Example 1:
      5
      / \
     4   8
    /   / \
   11  13  4
  / \
 7   2

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

Explanation: The root-to-leaf path with the target sum is shown.

First, what information do we need at each function call? We need the current node, but do we need anything else?
If we also keep an integer curr that represents the current sum of the nodes from the root to the current node,
we can check this value against targetSum when we find a leaf. Thus, let's have a helper function dfs(node, curr)
that returns true if there is a path starting at node and ending at a leaf with a sum equal to targetSum,
if we already have curr contributed towards the sum.

What are the base cases? First of all, if we have an empty tree, we can't have a path as there are no nodes,
so return false. If we are at a leaf node (which we can check by seeing if both children are null),
then return (curr + node.val) == targetSum.

Otherwise, if we are not at a leaf, we could either continue down the left path or the right path.
We only need one path to equal targetSum, so return true if either works. Don't forget to add the current node's
value to curr

#-------------------------------------------------------------------#

When we encounter a leaf, we need to know the sum of the values from the root to this leaf. 
We use an additional argument curr in our DFS function to keep track of this path sum.

At any given node, we make the following observation: all possible paths that start at the root and move through
a child of node must pass through node.

Therefore, the first thing we do after checking the base cases is perform curr += node.val. 
Because every call has its own version of curr and we perform this addition at every node, it will always be accurate.

This allows us to easily check for the condition described in the problem. When we encounter a leaf node 
(which we can check for by seeing if both children are null), we check if (curr + node.val) == targetSum. 
If so, we return true.

Calling dfs(node.left, curr) returns a boolean indicating if there exists a path starting from node.left 
and ending at a leaf with a sum of targetSum, starting with curr. Simply put, it tells us if an answer 
can be found by using the left subtree. The same logic applies to dfs(node.right, curr).

Because the problem is asking if any path exists, we return true from a call if either child's call returns true
(we use OR ||).

As we are using ||, any return true will eventually propagate up to the root. If the base case described earlier 
(being at a leaf and (curr + node.val) == targetSum) is satisfied, it will return true and cause the original call 
(to the root) to return true as well.
"""
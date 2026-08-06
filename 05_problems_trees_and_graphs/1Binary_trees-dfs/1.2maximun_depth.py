from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # the depth of the current node itself also needs to be considered.
        # Since the current node adds one additional level to the depth of the tree,
        # you need to add 1 to account for this node.
        return max(left, right) + 1

# Time complexity: O(n)
# - Each node in the tree is visited exactly once, hence the time complexity is proportional to the number of
# nodes in the tree (n).

# Space complexity: O(h) h = height
# - The space complexity is determined by the depth of the recursion stack.
# - In the worst case (for an unbalanced tree), the recursion depth will be equal to the height of the tree (h).
# - In the best case (for a balanced tree), the height will be log(n), making the space complexity O(log n).

# Example binary tree:
#       3
#      / \
#     9   20
#         / \
#        15  7
node3 = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)

# Link nodes together
node3.left = node9
node3.right = node20
node20.left = node15
node20.right = node7

# Create an instance of Solution and test maxDepth
solution = Solution()
depth = solution.maxDepth(node3)
print(depth)  # Expected output: 3 = 3 -> 20 -> 7

"""
Let's start with a recursive approach. When thinking about designing recursive functions,
a good starting point is always the base case. What is the depth of an empty tree (zero nodes, root is null)?
The depth is 0.

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the
farthest leaf node.

       3
      / \
     9   20
         / \
        15  7

A really important concept regarding recursion is that each function call stores its own variables. 
Because we are calling the function for each node, that means every node has its own unique values of left and right
(in the video, we are representing this with the L and R at each node). When we get to the node labeled 6, 
there are actually 4 different values of left simultaneously.

In the solution above, we are doing a postorder traversal because the logic for the current node 
(basically just the return statement) happens after the calls. All three types of DFS can be implemented iteratively,
but postorder and inorder are more complicated to implement than preorder (which is very easy). 
As we mentioned earlier, for most problems, the type of DFS doesn't matter, so we'll take a look at 
a preorder DFS implemented iteratively.
"""


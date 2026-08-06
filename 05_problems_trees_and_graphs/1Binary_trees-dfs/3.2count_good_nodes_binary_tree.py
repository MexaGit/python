# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Here's the iterative approach:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, float("-inf"))]
        ans = 0

        while stack:
            node, max_so_far = stack.pop()
            if node.val >= max_so_far:
                ans += 1

            if node.left:
                stack.append((node.left, max(max_so_far, node.val)))
            if node.right:
                stack.append((node.right, max(max_so_far, node.val)))

        return ans

# Example binary tree:
#       3
#      / \
#     1   4
#    / \   \
#   3   1   5

node3 = TreeNode(3)
node1_left = TreeNode(1)
node4 = TreeNode(4)
node3_left = TreeNode(3)
node1_right = TreeNode(1)
node5 = TreeNode(5)

# Link nodes together
node3.left = node1_left
node3.right = node4
node1_left.left = node3_left
node1_left.right = node1_right
node4.right = node5

# Create an instance of Solution and test goodNodes
solution = Solution()
result = solution.goodNodes(node3)
print(result)  # Expected output: 4

"""
https://leetcode.com/problems/count-good-nodes-in-binary-tree/
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes
with a value greater than X.
Return the number of good nodes in the binary tree.

Example 1:
       3
      / \
     1   4
    / \   \
   3   1   5

Input: root = [3,1,4,3,null,1,5]
Output: 4

Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

#--------------------------------------------------------------------------------------#

In the previous example, we used an argument curr to indicate the current path sum. We saw that every function call
had its own version of curr.

In this problem, we need to know the maximum value seen so far on the current path. We can use an argument maxSoFar
to indicate this.

Recall the observation we made in the previous example: all possible paths that start at the root and move through
a child of node must pass through node.

This observation implies that for any given node, paths starting at the root and ending in the subtree of node must
include node. Therefore we should update maxSoFar with node.val before calling on the children. By performing
this update, we ensure that maxSoFar is accurate at every node.

We have dfs(node, maxSoFar) return the number of good nodes in the subtree rooted at node, with maxSoFar being
the greatest value seen so far. The number of good nodes is the number of good nodes in the left subtree plus
the number of good nodes in the right subtree. We can find these easily by calling dfs on node.left and node.right.
Additionally, if the current node is a good node, we count it as well. We can check this by checking node.val
against maxSoFar.
"""
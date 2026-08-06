# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        # Record the maximum difference
        self.result = 0

        # Helper function to traverse the tree
        def helper(node, cur_max, cur_min):
            if not node:
                return
            # Update the maximum difference
            self.result = max(self.result, abs(cur_max - node.val),
                              abs(cur_min - node.val))
            # Update the current max and min
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            # Recursive call for left and right children
            helper(node.left, cur_max, cur_min)
            helper(node.right, cur_max, cur_min)

        helper(root, root.val, root.val)
        return self.result

# Example binary tree:
#       8
#      / \
#     3   10
#    / \    \
#   1   6    14
#      / \   /
#     4   7 13

# Create the nodes
node8 = TreeNode(8)
node3 = TreeNode(3)
node10 = TreeNode(10)
node1 = TreeNode(1)
node6 = TreeNode(6)
node14 = TreeNode(14)
node4 = TreeNode(4)
node7 = TreeNode(7)
node13 = TreeNode(13)

# Construct the tree
node8.left = node3
node8.right = node10
node3.left = node1
node3.right = node6
node6.left = node4
node6.right = node7
node10.right = node14
node14.left = node13

# Create an instance of Solution and test maxAncestorDiff
solution = Solution()
max_diff = solution.maxAncestorDiff(node8)
print(max_diff)  # Expected output: 7 (Difference between 8 and 1)


"""
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/editorial/
Since the problem asks us for the Maximum Difference, maybe we do not need to compare all ancestors for a given node
and we only need to compare the ancestors with the Maximum value and the Minimum value.
Therefore, for a given node, we only need the maximum value and the minimum value from the root to this node.
To achieve this, we can define a function helper to start recursion, which receives a node and two integers, 
the maximum and minimum value of its ancestors, as input.

In the function helper, we need to update the maximum difference, the current maximum value, and the current 
minimum value.

Algorithm
Step 1: Initialize a variable result to record the required maximum difference.
Step 2: Define a function helper, which takes three arguments as input.
    The first argument is the current node, and the second and third arguments are the maximum and minimum 
    values along the root to the current node, respectively.
    In the function helper, update result and call helper on the left and right subtrees.
Step 3: Run helper on the root. It will automatically do recursion on every node.
Step 4: Finally, return result.
"""
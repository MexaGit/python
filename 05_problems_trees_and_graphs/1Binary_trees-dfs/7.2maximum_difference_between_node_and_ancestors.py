# This class defines what each person (node) in the family tree looks like.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # The person's age.
        self.left = left  # Reference to the left child (if any).
        self.right = right  # Reference to the right child (if any).

# This class contains the function to find the biggest age difference.
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        # If the tree is empty, return 0 since there's no one to compare.
        if not root:
            return 0

        # We’ll store the maximum difference in result as we explore the tree.
        result = 0

        # Helper function to explore the family tree.
        def helper(node, cur_max, cur_min):
            # If the current node doesn't exist, just return.
            nonlocal result

            if not node:
                return

            # Calculate the difference between the current node's age
            # and the max or min age we’ve seen so far on this path.
            result = max(result, abs(cur_max - node.val),  # Difference with max age.
                              abs(cur_min - node.val))  # Difference with min age.

            # Update the max and min age along the path as we explore further.
            cur_max = max(cur_max, node.val)  # The new max age seen so far.
            cur_min = min(cur_min, node.val)  # The new min age seen so far.

            # Now explore the left side of the family.
            helper(node.left, cur_max, cur_min)

            # Then explore the right side of the family.
            helper(node.right, cur_max, cur_min)

        # Start the exploration from the root with its value as the initial max and min.
        helper(root, root.val, root.val)

        # Return the biggest age difference we found.
        return result

# Scenario 3: Tracking Latency in Distributed Systems
# Problem Statement:
# Amazon’s distributed computing system is modeled as a tree, where each node represents a server, and the root node
# is the main server. Each server reports its current latency (node value).
#
# Your task is to find the largest latency difference between any server and one of its ancestors in the system,
# which helps identify network issues.
#
# Task:
# Write a function to return the maximum difference in latency between any server and one of its ancestor servers.

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
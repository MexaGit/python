from typing import Optional  # Just tells Python that some values might be 'None'

# TreeNode class defines what a node in our tree looks like
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode'=None, right=None):
        # Each node has a value and links to left and right child nodes
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If there's no tree at all (root is None), the depth is zero.
        if not root:
            return 0

        # Use a **stack** to explore the tree node by node (like exploring a maze).
        # The stack holds pairs (node, depth), where 'node' is the current spot in the maze,
        # and 'depth' is how far you've gone.
        stack = [(root, 1)]  # Start with the root node at depth 1 (the top of the tree)

        ans = 0  # This will store the deepest depth we can find.

        # Keep exploring until there are no more nodes to visit (stack is empty).
        while stack:
            # Take the top item from the stack (Last In, First Out — LIFO).
            node, depth = stack.pop()

            # Compare the current depth with the max depth found so far and update it.
            ans = max(ans, depth)

            # If the node has a **left child**, explore it by adding it to the stack.
            # Add 1 to the depth because it's one level deeper in the tree.
            if node.left:
                stack.append((node.left, depth + 1))

            # If the node has a **right child**, do the same thing (add it to the stack).
            # The right child is also one level deeper.
            if node.right:
                stack.append((node.right, depth + 1))

        # After exploring all nodes, 'ans' will contain the deepest depth of the tree.
        return ans

# Scenario 2: Customer Support Escalation Levels
# Problem Statement:
# Amazon’s customer support system is structured hierarchically, where each support agent or team reports to a higher
# level agent/team. The root of the tree represents the entry-level support team. Each path from the entry team to the
# farthest specialized team shows how deep an escalation can go.
#
# Your task is to find the maximum escalation depth in the customer support hierarchy.
#
# Task:
# Write a function that returns the maximum depth of the escalation path, which is the longest path from the
# entry-level support to the most specialized support agent.
from typing import Optional


# A class to define what a node in a binary tree looks like.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # The value stored in this node
        self.left = left  # Link to the left child (if any)
        self.right = right  # Link to the right child (if any)


class Solution:
    # This function checks if there is a path in the tree that adds up to the targetSum.
    def hasPathSum1(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # If the tree is empty (no nodes at all), return False.
        if not root:
            return False

        # The stack will store pairs (node, current_sum).
        # "node" is the node we are visiting, and "current_sum" is the sum of the path so far.
        stack = [(root, 0)]  # Start with the root node and a sum of 0.

        # Keep exploring the tree until there are no more nodes left in the stack.
        while stack:
            # Take the top (most recent) node from the stack.
            node, curr = stack.pop()

            # If this is a leaf node (no left or right child), check if the sum matches targetSum.
            if node.left is None and node.right is None:
                # If the sum including this node equals the targetSum, we found the path!
                if (curr + node.val) == targetSum:
                    return True  # We found a path! No need to search further.

            # Add the current node’s value to the path sum.
            curr += node.val

            # If the node has a left child, add it to the stack for future exploration.
            if node.left:
                stack.append((node.left, curr))  # Explore the left child next.

            # If the node has a right child, add it to the stack too.
            if node.right:
                stack.append((node.right, curr))  # Explore the right child next.

        # If we finished exploring and didn't find a path, return False.
        return False

# Scenario 2: Budget Planning for Product Promotion
# Problem Statement:
# Amazon is planning product promotions in different regions. Each node in the tree represents a regional branch where
# a certain amount of budget is allocated. A path from the headquarters (root) to a local branch (leaf) represents how
# the budget flows through the organization.
#
# Your task is to determine if there is a budget allocation path from headquarters to a local branch where the total
# budget equals a specific target amount.
#
# Task:
# Write a function that returns True if such a path exists, where the total budget equals the target amount.
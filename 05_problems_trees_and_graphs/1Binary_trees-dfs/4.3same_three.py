# This class defines what a node in a binary tree looks like.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Value stored in this node
        self.left = left  # Left child node (if any)
        self.right = right  # Right child node (if any)

class Solution:
    # This function checks if two trees, 'p' and 'q', are exactly the same.
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Use a stack (like a backpack) to explore both trees step by step.
        # Start with both root nodes in the stack.
        stack = [(p, q)]

        # Keep going until there’s nothing left in the stack.
        while stack:
            # Take out the top pair of nodes from the stack (LIFO: Last In, First Out).
            p, q = stack.pop()

            # If both nodes are empty (None), they match at this spot, so we move on.
            if p == None and q == None:
                continue  # Move to the next pair in the stack.

            # If one node is empty but the other isn't, the trees are different.
            if p == None or q == None:
                return False  # Trees aren't the same.

            # If the values of the nodes are not the same, the trees are different.
            if p.val != q.val:
                return False  # Trees aren't the same.

            # If we’re still here, it means both nodes have the same value. Now, we need to
            # explore their children. Add the left children of both nodes to the stack.
            stack.append((p.left, q.left))

            # Do the same for the right children of both nodes.
            stack.append((p.right, q.right))

        # If we’ve checked all nodes and found no differences, the trees are the same!
        return True

# Scenario 2: Synchronizing Product Catalogs
# Problem Statement:
# Amazon's product catalog is maintained in a tree-like structure, where each category (like "Electronics" or "Books")
# is a node, and individual products or subcategories are children of those nodes.
#
# Two versions of the product catalog exist: one on the primary server and one on the backup server. Your task is to
# write a function that checks if both catalogs are identical. The catalogs are the same if:
#
# The structure (categories and subcategories) is identical.
# The product data at each node matches exactly.
# Task:
# Write a function to compare the two product catalogs and return True if they are the same, or False if they are
# different.
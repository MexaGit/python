from collections import deque  # Use a deque (a special kind of list) to help explore nodes in order.

# This class defines what a node in the tree looks like.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # The value of the current node.
        self.left = left  # Left child of the node (could be None).
        self.right = right  # Right child of the node (could be None).


# This class contains the function that finds the minimum depth of the tree.
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # If the tree is empty (no root), return depth 0 right away.
        if not root:
            return 0

        # Create a deque (backpack) to explore nodes level by level (like in a game).
        queue = deque([root])  # Start with the root node in the queue.
        depth = 1  # Start at depth 1 since we're starting at the root.

        # Keep exploring while there are still nodes left in the queue.
        while queue:
            current_length = len(queue)  # How many nodes are at this level (in the current queue).

            # Explore all the nodes on this level.
            for _ in range(current_length):
                node = queue.popleft()  # Take the first node from the queue (FIFO - First In, First Out).

                # If this node doesn't exist, skip it and move to the next.
                #       1
                #      / \
                #     2   3
                #    / \
                #  None  4
                if not node:
                    continue

                # If the node has **no children** (it's a leaf), return the current depth.
                if not node.left and not node.right:
                    return depth  # We found the shortest path to a leaf!

                # If this node has a **left child**, add it to the queue to explore later.
                queue.append(node.left)
                # If this node has a **right child**, add it to the queue too.
                queue.append(node.right)

            # After finishing the current level, increase the depth by 1.
            depth += 1

        # If somehow we don't find a leaf (which shouldn't happen), return -1.
        return -1

# Scenario 4: Product Category Navigation
# Problem Statement:
# Amazon's product categories are organized in a hierarchical tree. The root is the top-level category
# (like "Electronics"), and the leaf nodes represent the most specific categories (like "Smartphones under $300").
#
# To improve user experience, you need to determine the minimum number of category levels a customer has to navigate
# through to reach the most specific product category.
#
# Task:
# Write a function to find the minimum depth of the category tree to reach any leaf category.
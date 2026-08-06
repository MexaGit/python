# This class describes what each person (node) looks like in the family tree.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # The person's ID (or name) in the family.
        self.left = left  # Reference to the left child (left branch of family).
        self.right = right  # Reference to the right child (right branch of family).

class Solution:
    # Function to find the Lowest Common Ancestor (LCA) of two people in the family tree.
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Imagine we're exploring the family tree using a backpack (stack).
        # The backpack will help us store people we want to explore next.
        stack = [root]  # Start at the root of the family tree (the oldest ancestor).

        # This dictionary keeps track of **who each person's parent is**.
        # Think of it like: "Who's your parent?" "Oh, it's this person!"
        parent = {root: None}  # At the start, the oldest ancestor has no parent.

        # Explore the family tree until we find both P and Q in the parent dictionary.
        while p not in parent or q not in parent:
            # Take out the top person from the backpack (LIFO: Last In, First Out).
            node = stack.pop()

            # If this person has a **left child**, add the child to the backpack
            # and record the parent-child relationship in the parent dictionary.
            if node.left:
                parent[node.left] = node  # Example: parent[5] = 3
                stack.append(node.left)  # Add the left child to the backpack.

            # If this person has a **right child**, do the same thing.
            if node.right:
                parent[node.right] = node  # Example: parent[1] = 3
                stack.append(node.right)  # Add the right child to the backpack.

        # Now we need to **collect all ancestors of P**.
        ancestors = set()  # This will store the ancestors of P.

        # Start at P and move upwards, adding each person to the ancestors set.
        while p:
            ancestors.add(p)  # Add P to the set of ancestors.
            p = parent[p]  # Move P to its parent.

            # Example: If P is 5, add 5 to ancestors, then move to 3 (its parent).
            # Now ancestors = {5, 3}.

        # Now let's find the **first ancestor of Q** that is also in P's ancestors.
        while q not in ancestors:
            q = parent[q]  # Move Q upwards to its parent.

            # Example: If Q is 1, check if 1 is in ancestors. No.
            # Move Q to its parent, which is 3. Now q = 3.
            # Since 3 is in the ancestors set, 3 is the LCA!

        # Return the common ancestor where both P and Q meet (LCA).
        return q  # This is the lowest common ancestor!

# Scenario 3: Route Planner – Common Meeting Point for Delivery Routes
# Problem Statement:
# Amazon drivers follow a tree-like structure for delivery routes, starting from a main hub (root). Each intersection
# (node) has branches leading to different parts of the city. Given two intersections, P and Q, you need to find the
# earliest intersection on the path from the hub that leads to both P and Q.
#
# Task:
# Write a function that takes the root of the delivery route tree and two intersections, P and Q. The function should
# return the common meeting point (lowest intersection) where both routes split.
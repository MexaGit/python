from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Iterative in-order traversal version to get the minimum difference.
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 1. Define a helper function for iterative in-order traversal.
        def iterative_inorder(root):
            # 2. Initialize a backpack (stack) to explore nodes,
            #    and an empty list to store values in order.
            stack = []
            values = []
            # 3. Start with the root node as the current node.
            # Why Not Just Use stack = [root]?
            # The short answer: In-order traversal requires visiting nodes in a specific order (left, node, right).
            # Simply initializing the stack with [root] will not properly explore the left nodes first.
            curr = root

            # 4. While there are nodes in the stack or the current node exists:
            while stack or curr:
                # 5. If the current node exists, keep adding left children
                #    to the stack (backpack) to explore them later.
                if curr:
                    stack.append(curr)
                    curr = curr.left  # Go left.
                # 6. If no more left children, take the last node from the stack.
                else:
                    curr = stack.pop()  # Take out a node to process.
                    values.append(curr.val)  # Add its value to the list.

                    # 7. Now explore the right child of the current node.
                    curr = curr.right  # Go right.

            # 8. Return the collected values in sorted order.
            return values

        # 9. Collect all node values in order using the iterative traversal.
        values = iterative_inorder(root)
        # 10. Initialize the answer as infinity (a very large number).
        ans = float("inf")
        # 11. Loop through the list of values and find the smallest difference
        #     between consecutive elements.
        for i in range(1, len(values)):
            ans = min(ans, values[i] - values[i - 1])
        # 12. Return the smallest difference found.
        return ans


# Example of how the solution works:
# Given binary tree [4, 2, 6, 1, 3]:
#
#        4
#       / \
#      2   6
#     / \
#    1   3
#
# The minimum absolute difference is 1 (between nodes 2 and 3).

# Test case 1
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

solution = Solution()
print(solution.getMinimumDifference(root))  # Output: 1

# Test case 2 (unbalanced tree)
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

print(solution.getMinimumDifference(root))  # Output: 1 (between 3 and 4)

"""

Why Do We Need Both stack and curr in the Condition?
The stack stores nodes we need to come back to later (for backtracking).
The curr pointer keeps track of the current node we are exploring as we move down the tree.
The loop continues until:

The stack is empty (meaning there are no more nodes left to explore).
curr becomes None (meaning we’ve reached the end of a path and need to backtrack).
If both the stack is empty and curr is None, we are done, and the loop stops.

How It Works in Practice
Imagine we are processing this binary tree:

markdown
Copiar código
      4
     / \
    2   6
   / \
  1   3
Start at the root (curr = 4).

stack is empty.
We push 4 onto the stack and move left to 2 (curr = 2).
Now at node 2, we push it onto the stack and move left to 1 (curr = 1).

At node 1, we push it onto the stack.

It has no left child (curr = None), so now we pop from the stack to process node 1.
Back at node 1:

We add its value to the list.
Now, move to the right child, which is None (curr = None).
Because curr = None, the next step is to pop the next node from the stack (node 2).

What This Means in Simple Terms
As long as there are nodes left to process (in the stack or in the current path), the loop keeps running.
The current node exists means that we haven’t reached the end of the current path yet (i.e., curr is not None).
"""

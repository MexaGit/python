from typing import Optional

# Definition for a binary tree node - DFS iteratively
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            # If the tree is empty (root is None), the depth is 0.
            return 0

        # We use a stack to simulate the recursion in an iterative DFS - Deep search first.
        # The stack holds tuples of (node, depth) where 'node' is the current TreeNode,
        # and 'depth' is the depth of that node in the tree.
        # stack = is a tuple [()] immutable, a list [[]] are mutable
        stack = [(root, 1)]  # (3,1) Start with the root node at depth 1 because we are measuring edges
        # rathe tan nodes as the depth
        ans = 0  # This will keep track of the maximum depth found.

        # Continue the loop until the stack is empty (i.e., all nodes have been processed)
        while stack:
            # Pop a node and its depth from the stack.
            # 'pop()' takes the last element from the stack (LIFO - Last In, First Out).
            # depth: This is just a number you are adding yourself to keep track of how deep you are in the tree.
            # The depth isn't automatically stored inside the TreeNode object; instead, you track it manually by
            # passing it through the stack - depth + 1
            node, depth = stack.pop()

            # Update the maximum depth found so far.
            ans = max(ans, depth)

            # If there is a left child, push it onto the stack with an increased depth.
            if node.left:
                # The left child is at depth 'depth + 1' because it's one level deeper.
                stack.append((node.left, depth + 1))

            # If there is a right child, push it onto the stack with an increased depth.
            if node.right:
                # Similarly, the right child is also one level deeper.
                stack.append((node.right, depth + 1))

        # Once the stack is empty, we have visited all nodes and found the maximum depth.
        return ans



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
print(depth)  # Expected output: 3

"""
This iterative implementation may be more intuitive if you are not used to recursion.
We are simply associating each node with its depth. For a given node with a depth of depth, the depth of the children
will be depth + 1.

The format for performing the traversal with the stack is something that can be easily re-used between problems. 
We make use of a stack and use a while loop until the stack is empty. In each iteration of the while loop, we handle
a single node - this is equivalent to a given function call in the recursive implementation. All the logic that 
is done in the function should be done in the while loop, including handling the children, which is done by pushing 
to the stack.

Important note regarding iterative implementations: in the code, we are adding node.left before node.right. 
Popping from a stack removes the most recently added element, thus we are actually visiting the right subtree 
first in the above code. In the recursive implementations, we visit the left subtree first. 
This difference is irrelevant in this problem because the only thing that matters is that we visit all nodes, 
regardless of order. However, it is still good to understand that when working iteratively, 
the visit order is opposite the insertion order.
"""

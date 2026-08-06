from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 1. Define a helper function called dfs (Depth-First Search).
        #    This function will help us explore the tree in the "in-order" way.
        def dfs(node):
            # 2. If the node is None, return (we reached a leaf).
            if not node:
                return

            # 3. First, explore the left child (small values).
            dfs(node.left)
            # 4. Add the current node’s value to the values list.
            values.append(node.val)
            # 5. Then, explore the right child (big values).
            dfs(node.right)

        # 6. Create an empty list to store all the node values in sorted order.
        values = []

        # 7. Start the in-order traversal of the tree from the root.
        dfs(root)

        # 8. Initialize the answer as infinity (a very large number).
        ans = float("inf")

        # 9. Loop through the list of values and calculate the difference
        #    between consecutive elements. Keep track of the smallest difference.
        for i in range(1, len(values)):
            print(values)
            ans = min(ans, values[i] - values[i - 1])

        # 10. Return the smallest difference found.
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
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any 
two different nodes in the tree.

Difference Between Traversal Orders
Pre-order Traversal:
Visit the current node first, then the left subtree, and finally the right subtree.
Order: Node → Left → Right

In-order Traversal:
Visit the left subtree first, then the current node, and finally the right subtree.
Order: Left → Node → Right
This is what your code is performing.

Post-order Traversal:
Visit the left subtree, then the right subtree, and finally the current node.
Order: Left → Right → Node

What is Tree Traversal?
In computer science, traversal refers to the process of visiting every node in a tree data structure exactly once 
in a specific order. When traversing a binary tree, there are different ways to explore the nodes, such as in-order, 
pre-order, and post-order.

Why In-order Traversal Works in Your Code
In your original problem, you are calculating the minimum difference between consecutive values in a 
Binary Search Tree (BST). Since in-order traversal lists the nodes in sorted order, it ensures that the consecutive 
values in the list reflect the closest nodes in value.
"""

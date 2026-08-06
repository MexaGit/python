from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # 1. If the tree is empty (no treasures to collect), return 0.
        if not root:
            return 0

        # 2. Start with an empty treasure bag (total sum = 0).
        ans = 0
        # 3. Put the first treasure (root node) into your backpack (stack).
        stack = [root]  # This is the starting point of your adventure.

        # 4. Keep going until your backpack is empty (no more nodes to explore).
        while stack:
            # 5. Take a treasure (node) out of the backpack to inspect it.
            node = stack.pop()  # Take out the last thing you put in (LIFO order).

            # 6. If the treasure’s value is within the range (between low and high):
            if low <= node.val <= high:
                # 7. Add the value of this treasure to your total sum.
                ans += node.val  # Put this treasure in your bag!

            # 8. If there’s a **left path** and it might have useful treasures (smaller values):
            if node.left and low < node.val:
                # 9. Put the left child (next node) into your backpack for later exploration.
                stack.append(node.left)  # Keep looking left!

            # 10. If there’s a **right path** and it might have useful treasures (bigger values):
            if node.right and node.val < high:
                # 11. Put the right child (next node) into your backpack for later exploration.
                stack.append(node.right)  # Keep looking right!

        # 12. When your backpack is empty and you've collected all treasures, return the total sum.
        return ans  # Give the final treasure count!

# Example of how the solution works:
# Given binary tree [10, 5, 15, 3, 7, null, 18] and range [7, 15]:
#
#        10
#       /  \
#      5   15
#     / \    \
#    3   7   18
#
# The sum of values within the range [7, 15] is 32 (7 + 10 + 15).

# Test case 1
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

solution = Solution()
print(solution.rangeSumBST(root, 7, 15))  # Output: 32

# Test case 2 (empty tree)
root = None
print(solution.rangeSumBST(root, 5, 10))  # Output: 0

# Test case 3 (all nodes are within the range)
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

print(solution.rangeSumBST(root, 1, 20))  # Output: 30 (10 + 5 + 15)

# Test case 4 (no nodes are within the range)
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

print(solution.rangeSumBST(root, 20, 30))  # Output: 0

"""
Scenario:
You’re working on an e-commerce platform that records the prices of items in a hierarchical data structure. 
Each node in the structure stores:

The price of an item (node value),
Connections to less expensive items (left child) and more expensive items (right child).
Your task is to optimize pricing analytics. Given a minimum price and a maximum price, you need to calculate 
the total value of all items priced between the two values, inclusive.

Write a function that takes:

The root of the price tree,
A low price,
A high price, And returns the total sum of all item prices in the given range.
"""
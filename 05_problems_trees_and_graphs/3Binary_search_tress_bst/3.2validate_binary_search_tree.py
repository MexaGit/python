from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        # 1. Start by putting the root node in the backpack (stack).
        #    Each node carries a range it must stay within.
        #    The root starts with the smallest possible value (-inf) and the largest possible value (inf).
        stack = [(root, float("-inf"), float("inf"))]

        # 2. While there are still nodes in the backpack:
        while stack:
            # 3. Take out one node from the backpack.
            node, small, large = stack.pop()
            # 4. If the node’s value is not between the valid range (small < node.val < large), return False.
            if not (small < node.val < large):
                return False  # This means the tree is not a valid BST.
            # 5. If the node has a left child:
            #    Add the left child to the backpack with an updated range.
            #    The left child must be smaller than the current node’s value.
            if node.left:
                stack.append((node.left, small, node.val))
            # 6. If the node has a right child:
            #    Add the right child to the backpack with an updated range.
            #    The right child must be larger than the current node’s value.
            if node.right:
                stack.append((node.right, node.val, large))

        # 7. If you’ve checked all nodes and found no problems, return True.
        return True

# Example of how the solution works:
# Given binary tree [2, 1, 3]:
#
#        2
#       / \
#      1   3
#
# This is a valid BST.

# Test case 1: Valid BST
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

solution = Solution()
print(solution.isValidBST(root1))  # Output: True

# Test case 2: Invalid BST
root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)

print(solution.isValidBST(root2))  # Output: False

# Test case 3: Single node (valid BST)
root3 = TreeNode(1)

print(solution.isValidBST(root3))  # Output: True

# Test case 4: Empty tree (valid BST)
print(solution.isValidBST(None))  # Output: True

# Test case 5: More complex invalid BST
root4 = TreeNode(10)
root4.left = TreeNode(5)
root4.right = TreeNode(15)
root4.right.left = TreeNode(6)  # This makes the tree invalid

print(solution.isValidBST(root4))  # Output: False


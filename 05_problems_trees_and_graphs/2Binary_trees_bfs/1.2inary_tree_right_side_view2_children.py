from collections import deque  # A deque (like a queue) to help explore levels one by one.
from typing import List, Optional  # Optional type for the root node.

# This class describes a node in the binary tree.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # The value of the current node (house number).
        self.left = left  # Left child (left neighbor's house).
        self.right = right  # Right child (right neighbor's house).

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 1. If the tree (neighborhood) is empty, return an empty list. No houses to see!
        if not root:
            return []

        # 2. Prepare a list to store the rightmost nodes (houses you see from the right side).
        ans = []  # This will hold the rightmost nodes from each level.

        # 3. Use a queue to explore the tree level by level (like visiting each row of houses).
        queue = deque([root])  # Start with the root node (first house on the first row).

        # 4. Keep going until we've visited all the levels in the tree (all rows of houses).
        while queue:
            current_length = len(queue)  # How many nodes (houses) are on this level?

            # 5. Add the rightmost node's value (the last house on this row) to the answer list.
            # Think: "This is the tallest house I can see on this row."
            ans.append(queue[-1].val)  # Add the value of the rightmost node.

            # 6. Now, visit all the houses on the current row (all nodes at this level).
            for _ in range(current_length):
                # Remove the house (node) from the front of the queue.
                node = queue.popleft()

                # 7. If the current house (node) has a left neighbor (left child),
                # add it to the queue for the next level.
                if node.left:
                    queue.append(node.left)

                # 8. If the current house (node) has a right neighbor (right child),
                # add it to the queue for the next level.
                if node.right:
                    queue.append(node.right)

        # 9. When we've visited all the rows, return the rightmost nodes (tallest houses you saw!).
        return ans


# Example of how the solution works:
# Given binary tree [1, 2, 3, null, 5, null, 4]:
#
#        1
#      /   \
#     2     3
#      \     \
#       5     4
#
# The right-side view is [1, 3, 4] because these are the nodes visible from the right.

# Test case 1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
solution = Solution()
print(solution.rightSideView(root))  # Output: [1, 3, 4]

# Test case 2 (tree with only one node)
root = TreeNode(1)
solution = Solution()
print(solution.rightSideView(root))  # Output: [1]

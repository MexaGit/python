from collections import deque  # We need a deque, like a bucket to hold nodes (boxes) while exploring.
from typing import List, Optional  # Helps us define the types of input and output.

# A TreeNode is like a box on a floor, holding a treasure (value) and possibly two smaller boxes inside
# (left and right).
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # This is the treasure in the box.
        self.left = left  # This is a smaller box on the left (if it exists).
        self.right = right  # This is a smaller box on the right (if it exists).

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # 1. If the treehouse is empty (no floors or boxes), you can't find any treasures.
        if not root:
            return []  # Return an empty list since there are no treasures.

        # 2. Prepare a "Treasure List" to keep track of the biggest treasures from each floor.
        ans = []  # This will store the biggest treasures from each level.
        # 3. Use a "bucket" (deque) to collect boxes to explore, starting with the first box on the first floor.
        queue = deque([root])

        # 4. Keep exploring floors until there are no more boxes to check.
        while queue:
            # 5. Check how many boxes (nodes) are on the current floor.
            current_length = len(queue)
            # 6. Start with the smallest possible treasure for comparison.
            curr_max = float("-inf")  # We will update this with the biggest treasure we find.

            # 7. Look inside every box on this floor (process all nodes at the current level).
            for _ in range(current_length):
                # 8. Take the first box from the bucket to open it.
                node = queue.popleft()
                # 9. Is this box's treasure the biggest one we've found on this floor?
                curr_max = max(curr_max, node.val)  # If yes, update curr_max with this treasure.
                # 10. If the box has a smaller box on the left, add it to the bucket for the next floor.
                if node.left:
                    queue.append(node.left)
                # 11. If the box has a smaller box on the right, add it to the bucket for the next floor.
                if node.right:
                    queue.append(node.right)

            # 12. After checking all the boxes on this floor, write down the biggest treasure on your list.
            ans.append(curr_max)
        # 13. When all floors are done, return your "Treasure List" of the biggest treasures from each floor.
        return ans

# Example of how the solution works:
# Given binary tree [1, 3, 2, 5, 3, null, 9]:
#
#        1
#      /   \
#     3     2
#    / \     \
#   5   3     9
#
# The largest values in each row are [1, 3, 9].

# Test case 1
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)
solution = Solution()
print(solution.largestValues(root))  # Output: [1, 3, 9]

# Test case 2 (tree with only one node)
root = TreeNode(1)
solution = Solution()
print(solution.largestValues(root))  # Output: [1]

# Test case 3 (tree with all negative values)
root = TreeNode(-1)
root.left = TreeNode(-2)
root.right = TreeNode(-3)
root.left.left = TreeNode(-4)
root.left.right = TreeNode(-5)
solution = Solution()
print(solution.largestValues(root))  # Output: [-1, -2, -4]

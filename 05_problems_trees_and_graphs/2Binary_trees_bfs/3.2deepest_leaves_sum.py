from collections import deque
from typing import Optional

# Binary tree node class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Iterative BFS Traversal.
    def deepestLeavesSum(self, root: TreeNode) -> int:
        deepest_sum = depth = 0
        queue = deque([(root, 0), ])

        while queue:
            node, curr_depth = queue.popleft()
            if node.left is None and node.right is None:
                # if this leaf is the deepest one seen so far
                if depth < curr_depth:
                    deepest_sum = node.val  # start new sum
                    depth = curr_depth  # note new depth
                # if there were already leaves at this depth
                elif depth == curr_depth:
                    deepest_sum += node.val  # update existing sum
            else:
                if node.left:
                    queue.append((node.left, curr_depth + 1))
                if node.right:
                    queue.append((node.right, curr_depth + 1))

        return deepest_sum
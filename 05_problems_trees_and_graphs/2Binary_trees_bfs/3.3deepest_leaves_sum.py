from collections import deque  # We need a deque to hold boxes as we explore each floor.
from typing import Optional  # Helps us define the type of the input (TreeNode).

# A TreeNode is a box that holds some treasure (value) and might contain two smaller boxes (left and right).
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # The treasure value inside the box.
        self.left = left  # Smaller box on the left (if any).
        self.right = right  # Smaller box on the right (if any).

class Solution:
    # We want to find the sum of treasures at the deepest floor in the treehouse!
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # 1. Prepare to keep track of the deepest floor and the total treasure sum for that floor.
        deepest_sum = 0  # This holds the sum of treasures at the deepest floor.
        depth = 0  # This keeps track of the deepest floor we've seen so far.

        # 2. Use a queue to explore the treehouse level by level (like exploring each floor).
        # Start with the first box (root) on floor 0.
        queue = deque([(root, 0)])  # Each item in the queue is (box, floor level).

        # 3. Keep exploring until there are no more boxes to check.
        while queue:
            # 4. Take the first box from the queue to open it.
            node, curr_depth = queue.popleft()

            # 5. If this is a **leaf box** (no smaller boxes inside), check its floor level.
            if node.left is None and node.right is None:
                # 6. If this leaf is on a deeper floor than any we've seen, start a new treasure sum.
                if depth < curr_depth:
                    deepest_sum = node.val  # Start a new sum with this leaf's treasure.
                    depth = curr_depth  # Record the new deepest floor level.

                # 7. If this leaf is on the same deepest floor, add its treasure to the sum.
                elif depth == curr_depth:
                    deepest_sum += node.val  # Add to the existing treasure sum.

            # 8. If the box has smaller boxes inside, add them to the queue for the next floor.
            else:
                if node.left:
                    queue.append((node.left, curr_depth + 1))  # Add left box.
                if node.right:
                    queue.append((node.right, curr_depth + 1))  # Add right box.

        # 9. When all floors are explored, return the total treasure sum from the deepest floor.
        return deepest_sum

# Scenario 2: Customer Support Escalation
# Problem Statement:
# In Amazon’s customer support system, each level of the hierarchy involves agents resolving issues or escalating
# them to more specialized agents at the next level. The deepest level contains highly specialized agents who resolve
# the most complex issues. Each agent (node) resolves a certain number of tickets (value). Your task is to calculate
# the total number of tickets resolved at the deepest level of support.
#
# Task:
# Write a function to return the sum of tickets resolved by the agents at the deepest level of the support hierarchy.
from collections import deque  # We need a special bucket (deque) to hold rooms as we explore.
from typing import List, Optional  # Helps us specify input/output types.

# A TreeNode is a room that contains a treasure (value).
class TreeNode:
    def __init__(self, x: int):
        self.val = x  # The treasure in the room (node).
        self.left = None  # A smaller room to the left (if any).
        self.right = None  # A smaller room to the right (if any).

class Solution:
    # We need to explore the treehouse floor by floor, but in a zigzag pattern.
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []  # If there are no rooms (empty tree), return an empty list.

        result = []  # This will store the treasures from all the floors.
        queue = deque([root])  # Start with the first room (the root) in our bucket.
        is_order_left = True  # Flag to switch between left-to-right and right-to-left order.

        # Explore the treehouse floor by floor.
        while queue:
            level_size = len(queue)  # How many rooms (nodes) are on this floor?
            level = deque()  # Prepare a new bucket for this floor’s treasures.

            # Visit each room on the current floor.
            for _ in range(level_size):
                node = queue.popleft()  # Take a room from the front of the queue.

                # If we are exploring left-to-right, add the treasure to the right end.
                if is_order_left:
                    level.append(node.val)  # Add the treasure normally (left to right).
                # If we are exploring right-to-left, add the treasure to the left end.
                else:
                    level.appendleft(node.val)  # Add the treasure to the left side.

                # Add the smaller rooms (children) to the queue for the next floor.
                if node.left:
                    queue.append(node.left)  # Add the left child room.
                if node.right:
                    queue.append(node.right)  # Add the right child room.

            # After visiting all rooms on this floor, store the treasures in the result list.
            result.append(list(level))  # Convert the bucket (deque) to a normal list.

            # Switch the order for the next floor (toggle between left-to-right and right-to-left).
            # What Does is_order_left = not is_order_left Do?
            # This line is used to toggle the value of is_order_left. Toggling means that it flips between
            # True and False each time you call it.
            # If is_order_left is True, it becomes False.
            # If is_order_left is False, it becomes True.
            # This is a handy way to switch between two states without needing an if-else statement.
            is_order_left = not is_order_left
            # This ensures that the order switches for the next level. So:
            # First level: Left-to-right → is_order_left = True.
            # Second level: Right-to-left → is_order_left = False.
            # Third level: Left-to-right → is_order_left = True.
            # And so on...
            # if is_order_left:
            #     is_order_left = False
            # else:
            #     is_order_left = True

        return result  # When all floors are explored, return the list of treasures.

#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
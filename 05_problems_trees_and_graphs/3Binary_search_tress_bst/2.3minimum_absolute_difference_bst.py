from typing import Optional, List

# 🧱 This is the blueprint for each "room" (or node) in our treasure map.
class TreeNode:
    def __init__(self, x: int):
        self.val = x  # 🎯 Each node has a treasure (a number) stored inside.
        self.left = None  # 🚪 Left door leading to another smaller treasure room.
        self.right = None  # 🚪 Right door leading to a bigger treasure room.

class Solution:
    # 🚀 We are on a mission to find the smallest difference between treasures (numbers)!
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 🔄 This is our helper function to explore the treasure map **iteratively**.
        def iterative_inorder(root):
            # 🎒 Stack = A backpack to hold rooms we still need to explore.
            # 🗒️ Values = A notebook to write down treasures in order.
            stack = [] # LIFO
            values = []
            # 🎯 Start from the first room (root of the map).
            curr = root

            # 🔄 While there are still unexplored rooms (nodes) or stuff in our backpack:
            while stack or curr: # curr will continue is not None, there is still a node to explore
                # 🚶‍♂️ If there is a current room, keep moving left (to smaller treasures).
                if curr:
                    stack.append(curr)  # 🎒 Store the room for later.
                    curr = curr.left  # ➡️ Go to the left room.
                # 🛑 If no more left rooms to explore:
                else:
                    curr = stack.pop()  # 🎒 Take a room out from the backpack to explore.
                    values.append(curr.val)  # 📝 Write down the treasure in our notebook.

                    # ➡️ Now, let’s check the right room for any bigger treasure.
                    curr = curr.right

            # 🗒️ Return the list of all treasures we collected, nicely sorted.
            return values

        # 🗒️ Use the helper function to collect all treasures in order.
        values = iterative_inorder(root)
        # 🔢 Set the smallest difference to infinity (just a really big number for now).
        ans = float("inf")

        # 🔄 Now, compare all neighboring treasures in the list to find the smallest gap.
        for i in range(1, len(values)):
            # 📉 Keep updating the smallest difference if we find a smaller gap.
            ans = min(ans, values[i] - values[i - 1])
        # 🎯 Return the smallest difference we found!
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
"You are given a system that stores product serial numbers in a tree-like structure. Each serial number is unique, 
and the system ensures that:

Smaller serial numbers always appear on the left branch of each node.
Larger serial numbers always appear on the right branch of each node.
Each product has at most two child products.
Your task is to find the smallest absolute difference between the serial numbers of any two products in the system.

Input:
root = [4, 2, 6, 1, 3]

Output:
1
"""
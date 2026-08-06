from collections import deque
from typing import List

# TreeNode class definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = None  # We'll be assigning this in the dfs function

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Step 1: DFS to assign parent references for each node
        # Now we have a undirected <--> graph
        def dfs(node, parent):
            if not node:
                return

            # Add a parent reference to the current node
            node.parent = parent

            # Recursively assign parents for the left and right children
            dfs(node.left, node)
            dfs(node.right, node)

        # Perform DFS starting from the root to assign parent pointers
        dfs(root, None)

        # Step 2: Use BFS to find all nodes at distance k
        queue = deque([target])  # Initialize the queue with the target node
        seen = {target}  # Set to keep track of visited nodes (start with target) to avoid infinite cycles
        distance = 0  # Track current distance from the target node

        # BFS loop: expand nodes level by level until distance k is reached
        while queue and distance < k:
            current_length = len(queue)  # Number of nodes at the current distance level

            # Process each node at the current distance level
            for _ in range(current_length):
                node = queue.popleft()  # Get the next node in the queue

                # Check all possible neighbors: left child, right child, and parent
                for neighbor in [node.left, node.right, node.parent]:
                    # for each of the neighbor, the neighbor is not null and not yet been seen
                    if neighbor and neighbor not in seen:  # If the neighbor is valid and not yet visited
                        seen.add(neighbor)  # Mark the neighbor as visited
                        queue.append(neighbor)  # Add the neighbor to the queue for the next level

            distance += 1  # Increment the distance after processing the current level

        # Step 3: After reaching the distance k, collect the remaining nodes in the queue
        return [node.val for node in queue]  # Return the values of nodes at distance k

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
# Building the tree structure
#         3
#       /   \
#      5     1
#     / \   / \
#    6   2 0   8
#       / \
#      7   4
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

solution = Solution()
target = root.left  # Node with value 5
k = 2

# Output: [7, 4, 1]
print(solution.distanceK(root, target, k))

"""
Given the root of a binary tree, the value of a target node target, and an integer k,
return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.


"""
# A class that defines what each node in the tree looks like.
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        self.val = val  # Value of the node
        self.left = left  # Left child (if any)
        self.right = right  # Right child (if any)


class Solution:
    # Function to count how many "good" nodes are in the tree.
    def goodNodes(self, root: TreeNode) -> int:
        # If the tree is empty, return 0 (no good nodes).
        if not root:
            return 0

        # Use a stack to explore the tree iteratively.
        # Each item in the stack holds (node, max_so_far).
        # 'max_so_far' keeps track of the largest value we've seen on the path so far.
        stack = [(root, float("-inf"))]  # Start with root and smallest possible value.

        ans = 0  # This will store the total count of good nodes.

        # Keep exploring nodes until the stack is empty.
        while stack:
            # Pop the last node and its max value from the stack (LIFO - Last In, First Out).
            node, max_so_far = stack.pop()

            # If the node's value is greater than or equal to the max value so far, it's a good node.
            if node.val >= max_so_far:
                ans += 1  # Increment the count of good nodes.

            # If the node has a left child, add it to the stack with the new max value.
            if node.left:
                stack.append((node.left, max(max_so_far, node.val)))

            # If the node has a right child, do the same.
            if node.right:
                stack.append((node.right, max(max_so_far, node.val)))

        # After visiting all nodes, return the total count of good nodes.
        return ans

# Scenario 1: Inventory System Monitoring
# Problem Statement:
#
# A company has a hierarchical product inventory system represented as a tree.
# Each node in the tree corresponds to a warehouse or distribution center, and the value stored in the node represents
# the inventory level at that location.
#
# A location (node) is considered "good" if, from the main hub (root) to that location, no other location has a higher
# inventory level. The company wants to count the number of good locations to ensure adequate inventory is maintained
# along the supply chain.
#
# Task:
# Write a function to return the total number of "good" locations in the supply chain.

# Scenario 2: Network Latency Monitoring
# Problem Statement:
#
# Imagine you are managing a network of connected servers represented by a binary tree. Each server (node) stores a
# value indicating the latency (in milliseconds) it is currently experiencing.
#
# A server is considered "good" if no other server along the path from the root (main data center) to that server
# has a higher latency than it. Your task is to find the number of good servers in the network to identify regions
# with acceptable latency levels.
#
# Task:
# Write a function to return the total number of "good" servers in the network.
# BFS (Breadth-First Search)
from collections import deque  # Import deque to use as a queue

def fn(root):
    queue = deque([root])  # Start with the root node in the queue
    ans = 0  # Placeholder for the result (depends on problem logic)

    while queue:  # As long as there are nodes to explore
        current_length = len(queue)  # How many nodes are at the current level

        # Do some logic for the current level (e.g., sum the values, count nodes, etc.)

        for _ in range(current_length):  # Process all nodes at the current level
            node = queue.popleft()  # Take the first node from the queue

            # Do some logic with the current node (e.g., print, sum values)
            if node.left:
                queue.append(node.left)  # Add the left child to the queue
            if node.right:
                queue.append(node.right)  # Add the right child to the queue

    return ans  # Return the result (depends on the problem)

# What Is This Code Doing?
# This code uses a queue to explore all nodes in a tree, one level at a time.
# It’s like playing a game where you explore the first floor of a building before moving to the second floor,
# then the third, and so on. 🏢
#
# Here’s what’s happening:
#   We start at the root node and add it to the queue.
#   For each level, we process all nodes at that level before moving to the next level.
#   The queue keeps track of all the nodes to explore at each step.
#   This level-order traversal is called Breadth-First Search (BFS).

"""
How Does the BFS Code Work?

Queue Initialization:
Start with the root node in the queue.

While Loop:
As long as there are nodes to explore, keep looping.

Process Current Level:
For each level, count the number of nodes at that level.
Process all nodes at the current level by taking them out of the queue.

Add Children to the Queue:
If the current node has left or right children, add them to the queue for the next level.
"""
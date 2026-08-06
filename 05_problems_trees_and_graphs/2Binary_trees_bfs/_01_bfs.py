from collections import deque

def print_all_nodes(root):
    # Initialize a deque with the root node to start the level-order traversal (BFS)
    queue = deque([root])

    # Continue the process as long as there are nodes in the queue
    while queue:
        # Count the number of nodes at the current level
        nodes_in_current_level = len(queue)
        # do some logic here for the current level (if needed, like printing or processing the level)

        # Loop over all nodes at the current level
        for _ in range(nodes_in_current_level):
            # Pop the leftmost node from the queue (current node to process)
            node = queue.popleft()

            # Process the current node (printing its value)
            print(node.val)

            # Append the left child to the queue if it exists
            if node.left:
                queue.append(node.left)

            # Append the right child to the queue if it exists
            if node.right:
                queue.append(node.right)

# The deque here allows for efficient popping from the left (O(1)) and appending to the right (O(1)).

"""
At the start of each iteration inside the while loop (where the comment "do some logic here for the current level" is),
the queue contains exactly all the nodes for the current level. In the beginning, that's just the root.

We then use a for loop to iterate over the current level. We store the number of nodes in the current level 
nodesInCurrentLevel before iterating to make sure the for loop doesn't iterate over any other nodes. The for loop 
visits each node in the current level and puts all the children (the next level's nodes) in the queue.

Because we are removing from the left and adding on the right (opposite ends), after the for loop finishes, the queue 
will hold all the nodes in the next level. We move to the next while loop iteration and the process repeats.
"""



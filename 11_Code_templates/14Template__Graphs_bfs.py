#  BFS (Breadth-First Search)
from collections import deque

def fn(graph):
    queue = deque([START_NODE])  # Start with the initial node in the queue
    seen = {START_NODE}  # Keep track of visited nodes to avoid cycles
    ans = 0  # Placeholder for the answer (depends on the logic needed)

    while queue:  # While there are still nodes to explore
        node = queue.popleft()  # Take the first node from the queue

        # Do some logic with the current node
        # Example: ans += 1  # Count the node (if counting nodes is the logic)

        # Explore all neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in seen:  # If the neighbor hasn’t been visited
                seen.add(neighbor)  # Mark it as visited
                queue.append(neighbor)  # Add it to the queue for future exploration

    return ans  # Return the final answer


# How This BFS Works:
# Initialize the Queue and seen Set:
#   The queue starts with the START_NODE.
#   The seen set keeps track of all visited nodes to avoid visiting the same node multiple times.
# While Loop:
#   As long as there are nodes in the queue, we keep exploring.
#   We remove the first node from the queue (FIFO: First In, First Out).
# Explore Neighbors:
#   For every neighbor of the current node:
#       If the neighbor hasn’t been visited before, we:
#           Mark it as visited.
#           Add it to the queue to explore later.
# Return the Result:
#   The ans variable accumulates some result (like a count or sum) based on the problem logic.
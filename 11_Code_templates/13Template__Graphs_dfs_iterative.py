# DFS (Depth-First Search) iterative
def fn(graph):
    stack = [START_NODE]  # Initialize the stack with the starting node
    seen = {START_NODE}  # Keep track of visited nodes to avoid cycles
    ans = 0  # Placeholder for the result (depends on the problem logic)

    while stack:  # Keep going until there are no more nodes to explore
        node = stack.pop()  # Take the top node from the stack

        # Do some logic with the current node
        # Example: ans += 1  # Counting nodes (if this is the logic)

        # Explore all neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in seen:  # If we haven't visited this neighbor yet
                seen.add(neighbor)  # Mark it as visited
                stack.append(neighbor)  # Add it to the stack for future exploration

    return ans  # Return the final answer (depends on the problem)


# How Does This Code Work?
# Initialize the Stack and seen Set:
#   The stack is initialized with the START_NODE.
#   The seen set keeps track of the nodes we’ve visited so far to avoid visiting the same node multiple times
#   (and avoid cycles).
# DFS Loop Using a Stack:
#   While the stack is not empty, we:
#       Pop a node from the top of the stack.
#       Do some logic with that node (like counting it or processing it).
#       Add unvisited neighbors to the stack.
# The Stack Controls the Order of Exploration:
#   DFS explores nodes as deep as possible before backtracking.
#   We add neighbors to the stack to continue exploring deeper down the path.
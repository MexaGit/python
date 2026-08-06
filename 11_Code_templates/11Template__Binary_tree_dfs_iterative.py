# DFS (Depth-First Search) iterative
def dfs(root):
    stack = [root]  # Start with the root node in the stack
    ans = 0  # Placeholder to store the result (e.g., sum, count, etc.)

    while stack:  # Keep going as long as there are nodes to explore
        node = stack.pop()  # Take the top node from the stack

        # Do some logic with the current node
        # Example: ans += node.val  # Add the node's value to ans (if summing values)

        # Add the left and right children to the stack (if they exist)
        if node.left:
            stack.append(node.left)  # Add left child
        if node.right:
            stack.append(node.right)  # Add right child

    return ans  # Return the final answer (depends on what the logic is doing)

# Key Differences:
# Aspect	            DFS (Stack)	                            BFS (Queue)
# Data Structure	    Stack (stack = [root])	                Queue (queue = deque([root]))
# Order	                LIFO (Last In, First Out)	            FIFO (First In, First Out)
# Use Case	            Depth-First Search (DFS)	            Breadth-First Search (BFS)
# Explores	            One path deeply before backtracking	    All nodes at the current level first
# Memory Usage	        Can go deep, consuming stack memory	    Uses more memory for wide trees

"""
Core Difference between Stack and Queue:

Stack: LIFO (Last In, First Out) – The last element added is the first one to be removed.   
    Think of a stack of plates: You add plates to the top, and you take the top plate off first.
    Used for Depth-First Search (DFS).
Queue: FIFO (First In, First Out) – The first element added is the first one to be removed.
    Think of a line (queue) of people: The first person in line is served first.
    Used for Breadth-First Search (BFS).

Conclusion:
stack = [root] is used for DFS, exploring deep paths.
queue = deque([root]) is used for BFS, exploring nodes level by level.
"""
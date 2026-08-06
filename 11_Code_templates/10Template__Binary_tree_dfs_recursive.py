# DFS (Depth-First Search) recursive
def dfs(root):
    if not root:  # If the current node is None, stop the recursion.
        return

    ans = 0  # Placeholder for the result (usually used for counting or accumulating values)

    # Do some logic here (depends on what you're solving)

    dfs(root.left)  # Visit the left subtree
    dfs(root.right)  # Visit the right subtree

    return ans  # Return the result (if needed)

# How DFS Works in Trees:
# DFS (Depth-First Search) is an exploration method that:
#   Goes as deep as possible along one path before backtracking.
#   In a binary tree, it explores:
#       Left child (if it exists)
#       Right child (if it exists)
# Recursion is used to keep track of which node you're currently on. Once the function hits a None node
# (a leaf's child), it backtracks to the previous node and continues exploring.
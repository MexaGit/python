# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Stack for tree traversal
        # I will start exploring this tree from the root
        stack = [root]
        # Dictionary for parent pointers
        # is the setup for keeping track of each node’s parent so that later on,
        # you can trace back from a node to its ancestors.
        parent = {root: None}

        # Example setup: if the tree is like this:
        #       3
        #      / \
        #     5   1
        #    / \ / \
        #   6  2 0  8
        #     / \
        #    7   4
        # For p = 5 and q = 1, the root is 3, so we start with stack = [3]
        # and parent = {3: None}

        # If p and q are both located early in the tree traversal (e.g., if they are close to the root),
        # the loop might not traverse the entire tree.
        # Step 3: Traverse the tree until we find both p and q
        while p not in parent or q not in parent:
            # Step 3.1: Pop a node from the stack (DFS)
            node = stack.pop()

            # Step 3.2: If the current node has a left child, add it to the stack
            # and record its parent in the parent dictionary.
            if node.left:
                parent[node.left] = node  # Save parent of node.left eg: parent = {5: 3}
                stack.append(node.left)  # Add left child to stack for future exploration eg: # Now stack = [5]

            # Step 3.3: Similarly, if the current node has a right child, add it to the stack
            # and record its parent in the parent dictionary.
            if node.right:
                parent[node.right] = node  # Save parent of node.right eg: parent = {1: 3}
                stack.append(node.right)  # Add right child to stack for future exploration  # Now stack = [5, 1]

            # Example for first iterations:
            # - Start with stack = [3], parent = {3: None}
            # - Pop node 3, add children 5 and 1 to stack
            #   Now stack = [5, 1], parent = {3: None, 5: 3, 1: 3}
            # - Continue the process until both p (5) and q (1) are in `parent`
        # Print parent dictionary
        for key, value in parent.items():
            print(f"{key.val}: {value.val if value else None}", end=", ")

        # Step 4: Create a set to track all ancestors of p
        ancestors = set()

        # Step 5: Traverse from node p upwards to the root, using the parent pointers.
        # Add all ancestors of p to the set.
        while p:
            ancestors.add(p)  # Add p to the set of ancestors
            p = parent[p]  # Move p to its parent

        # Example:
        # - If p is 5, we first add 5 to the ancestors set, then move to 3 (its parent).
        # - Now ancestors = {5, 3}

        # Step 6: Now find the first ancestor of q that is also an ancestor of p.
        # This is the Lowest Common Ancestor (LCA).
        while q not in ancestors:
            q = parent[q]  # Move q to its parent until q is in p's ancestor set

        # Example:
        # - If q is 1, we check: is 1 in ancestors? No.
        # - Move q to its parent, which is 3. Now q = 3.
        # - 3 is in ancestors, so 3 is the LCA.

        return q  # Return the lowest common ancestor (LCA)

# Example binary tree:
#       3
#      / \
#     5   1
#    / \ / \
#   6  2 0  8
#     / \
#    7   4

# Create the nodes
node3 = TreeNode(3)
node5 = TreeNode(5)
node1 = TreeNode(1)
node6 = TreeNode(6)
node2 = TreeNode(2)
node0 = TreeNode(0)
node8 = TreeNode(8)
node7 = TreeNode(7)
node4 = TreeNode(4)

# Construct the tree
node3.left = node5
node3.right = node1
node5.left = node6
node5.right = node2
node1.left = node0
node1.right = node8
node2.left = node7
node2.right = node4

# Create an instance of Solution and test lowestCommonAncestor
solution = Solution()
lca = solution.lowestCommonAncestor(node3, node5, node1)
print(lca.val)  # Expected output: 3 (the root node)

# Test with different nodes
lca_different = solution.lowestCommonAncestor(node3, node5, node4)
print(lca_different.val)  # Expected output: 5 (the ancestor of node 5 and node 4)

"""
Finding LCA of p = 5 and q = 1:
Initial setup:

stack = [3] (start with the root)
parent = {3: None}
Traverse the tree:

Pop node 3, add its children 5 and 1 to the stack:

stack = [5, 1]
parent = {3: None, 5: 3, 1: 3}
Pop node 1, add its children 0 and 8 to the stack:

stack = [5, 0, 8]
parent = {3: None, 5: 3, 1: 3, 0: 1, 8: 1}
Pop node 5, add its children 6 and 2 to the stack:

stack = [0, 8, 6, 2]
parent = {3: None, 5: 3, 1: 3, 0: 1, 8: 1, 6: 5, 2: 5}
Now both p = 5 and q = 1 are in the parent dictionary, so we can stop traversing.

Find ancestors of p (5):

Start with p = 5, add 5 to the set of ancestors.
Move to the parent of 5, which is 3. Add 3 to the ancestors.
Now, ancestors = {5, 3}.
Find LCA by tracing q (1):

Start with q = 1. Check if 1 is in ancestors. It is not.
Move to the parent of 1, which is 3. Check if 3 is in ancestors. It is.
The LCA is 3.

Summary:
The stack is used to traverse the tree using DFS.
The parent dictionary records the parent of each node to help trace ancestors.
The algorithm traces from both p and q upwards to find the lowest common ancestor.
"""
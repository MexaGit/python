class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, False)]  # (node, visited)
        heights = {}  # Store heights of nodes
        diameter = 0

        # Iterative DFS using a stack
        while stack:
            node, visited = stack.pop()

            if node is None:
                continue

            if visited:
                # If we revisit a node, calculate its height and update the diameter
                left_height = heights.get(node.left, 0)
                right_height = heights.get(node.right, 0)

                # Update the diameter using the sum of left and right heights
                diameter = max(diameter, left_height + right_height)

                # Store the height of the current node
                heights[node] = max(left_height, right_height) + 1
            else:
                # First time visiting this node - push it back as "visited"
                stack.append((node, True))

                # Add children to the stack for processing
                stack.append((node.right, False))
                stack.append((node.left, False))

        return diameter


# Example binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

# Create the nodes
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

# Construct the tree
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

# Create an instance of Solution and test diameterOfBinaryTree
solution = Solution()
diameter = solution.diameterOfBinaryTree(node1)
print(diameter)  # Expected output: 3

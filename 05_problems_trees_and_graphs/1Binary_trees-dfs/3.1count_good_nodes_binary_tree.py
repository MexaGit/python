# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0

            # Count good nodes
            ans = 0
            if node.val >= max_so_far:
                ans += 1  # Current node is good

            # Update max_so_far for children
            max_so_far = max(max_so_far, node.val)
            ans += dfs(node.left, max_so_far)  # Count good nodes in left subtree
            ans += dfs(node.right, max_so_far)  # Count good nodes in right subtree

            return ans

        return dfs(root, float("-inf"))

# Example binary tree:
#       3
#      / \
#     1   4
#    / \   \
#   3   1   5

node3 = TreeNode(3)
node1_left = TreeNode(1)
node4 = TreeNode(4)
node3_left = TreeNode(3)
node1_right = TreeNode(1)
node5 = TreeNode(5)

# Link nodes together
node3.left = node1_left
node3.right = node4
node1_left.left = node3_left
node1_left.right = node1_right
node4.right = node5

# Create an instance of Solution and test goodNodes
solution = Solution()
result = solution.goodNodes(node3)
print(result)  # Expected output: 4

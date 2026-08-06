from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = deque([root])
        depth = 1

        while q:
            qSize = len(q)
            for _ in range(qSize):
                node = q.popleft()
                # Since we added nodes without checking null, we need to skip them here.
                if not node:
                    continue
                # The first leaf would be at minimum depth, hence return it.
                if not node.left and not node.right:
                    return depth
                q.append(node.left)
                q.append(node.right)
            depth += 1
        return -1

# Example binary tree:
#       3
#      / \
#     9  20
#       /  \
#      15   7

# Create the nodes
node3 = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)

# Construct the tree
node3.left = node9
node3.right = node20
node20.left = node15
node20.right = node7

# Create an instance of Solution and test minDepth
solution = Solution()
min_depth = solution.minDepth(node3)
print(min_depth)  # Expected output: 2
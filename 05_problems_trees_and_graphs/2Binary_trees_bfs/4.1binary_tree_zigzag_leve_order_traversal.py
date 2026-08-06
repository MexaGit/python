from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        results = []

        def dfs(node: TreeNode, level: int) -> None:
            if level >= len(results):
                results.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    results[level].append(node.val)
                else:
                    results[level].appendleft(node.val)

            for next_node in [node.left, node.right]:
                if next_node is not None:
                    dfs(next_node, level + 1)

        # normal level order traversal with DFS
        dfs(root, 0)

        return results


# Example of how the solution works:
# Given binary tree [3, 9, 20, null, null, 15, 7]:
#
#        3
#      /   \
#     9     20
#          /  \
#         15   7
#
# The zigzag level order is [[3], [20, 9], [15, 7]].

# Test case 1
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.zigzagLevelOrder(root))  # Output: [[3], [20, 9], [15, 7]]

# Test case 2 (tree with only one node)
root = TreeNode(1)
solution = Solution()
print(solution.zigzagLevelOrder(root))  # Output: [[1]]

# Test case 3 (empty tree)
root = None
solution = Solution()
print(solution.zigzagLevelOrder(root))  # Output: []

# Test case 4 (full binary tree)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.zigzagLevelOrder(root))  # Output: [[1], [3, 2], [4, 5, 6, 7]]

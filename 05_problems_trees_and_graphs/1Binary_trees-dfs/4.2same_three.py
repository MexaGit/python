# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Here's an iterative approach. Notice that we are using the exact same code to check the cases.
    # Instead of returning true during the traversal, we return false if any condition is broken, and then
    # return true at the end if we managed to get through the trees without returning false.
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        while stack:
            p, q = stack.pop()

            if p == None and q == None:
                continue

            if p == None or q == None:
                return False

            if p.val != q.val:
                return False

            stack.append((p.left, q.left))
            stack.append((p.right, q.right))

        return True

# Example binary trees
# Tree 1:
#       1
#      / \
#     2   3
p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(3)
p1.left = p2
p1.right = p3

# Tree 2:
#       1
#      / \
#     2   3
q1 = TreeNode(1)
q2 = TreeNode(2)
q3 = TreeNode(3)
q1.left = q2
q1.right = q3

# Create an instance of Solution and test isSameTree
solution = Solution()
result = solution.isSameTree(p1, q1)
print(result)  # Expected output: True

# Example for different trees
# Tree 3:
#       1
#      / \
#     2   1
r1 = TreeNode(1)
r2 = TreeNode(2)
r3 = TreeNode(1)
r1.left = r2
r1.right = r3

# Test with different tree (Tree 1 and Tree 3)
result_different = solution.isSameTree(p1, r1)
print(result_different)  # Expected output: False

"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
#       1           1
#      / \         / \
#     2   3       2   3

Input: p = [1,2,3], q = [1,2,3]
Output: true

#-------------------------------------------------------------------------------#

This problem really demonstrates the recursive nature of binary trees.
If p and q are the same tree, then the following is true:

p.val = q.val
p.left and q.left are the same tree
p.right and q.right are the same tree

The main idea is that if any two trees are the same, then their subtrees must also be the same. 
This gives us a recursive definition of the problem. Because the function we are trying to implement is supposed
to tell us if two trees are the same, we can use the function itself to answer conditions 2 and 3.

The following condition can be used to check if p and q are the same tree:
p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right)

Now, we need base cases so that the recursion eventually terminates. If p and q are both null, then we can return 
true, because they are technically both the same (empty) tree. If either p or q is null but not the other, 
we should return false, as they are clearly not the same tree.

A good way to think about base cases is to think about a tree with only one node. Let's say that p and q are both 
one-node trees with the same value. The first boolean check p.val == q.val passes, so now we check the subtrees. 
Because the nodes don't have children, then both calls to the left and right subtrees will trigger the base case 
and return true.

This is the beauty of recursion - if you're at the root, the left and right subtrees could have thousands of nodes. 
The process of actually going through the trees will have many cascading calls, but you don't need to worry about 
it - you know that simply making the call will give you the answer you need.
"""
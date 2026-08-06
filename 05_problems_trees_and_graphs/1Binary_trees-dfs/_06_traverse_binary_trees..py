# Create a simple linked list: 1 -> 2 -> 3
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_sum(head):
    ans = 0
    while head:
        ans += head.val
        head = head.next

    return ans

# Create linked list nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# Link the nodes together
node1.next = node2
node2.next = node3

# Test the function
print(get_sum(node1))  # Expected output: 6 (1 + 2 + 3)

"""
Traversing a binary tree follows the same idea. We start at the root and traverse by using the child pointers .left
and .right. When traversing linked lists, we usually do it iteratively. With binary trees, we usually do it 
recursively.

There are two main types of tree traversals. The first is called depth-first search (DFS). 
For binary trees specifically, there are 3 ways to perform DFS - preorder, inorder, and postorder 
(don't worry though, the type you choose rarely matters). The other main type of traversal is called 
breadth-first search (BFS). 
"""

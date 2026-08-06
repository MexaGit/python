class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# We call the start of a linked list the head and the end of a linked list the tail.
# Let prev_node be the node at position i - 1
# add an element to a linked list so that it becomes the element at position i
def add_node(prev_node, node_to_add):
    node_to_add.next = prev_node.next
    prev_node.next = node_to_add

# Let prev_node be the node at position i - 1
# delete the element at position
def delete_node(prev_node):
    prev_node.next = prev_node.next.next

"""
This means you can only move forward in the list when iterating. 
The pointer used to reference the next node is usually called next.

prevNode.next is the node being deleted. prevNode.next.next is the node after that which should be kept. 
We change the next pointer of prevNode to point at that node instead of the one being deleted.
Because the node being deleted could only have been reached from prevNode and we have now severed that connection, 
it is no longer part of the list.
"""
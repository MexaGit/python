# Class representing a node in a doubly linked list
class ListNode:
    def __init__(self, val):
        self.val = val  # Value stored in the node
        self.next = None  # Pointer to the next node in the list
        self.prev = None  # Pointer to the previous node in the list

# Function to add a new node at a specific position in the list
# node: the node at position i (the position where the new node will be inserted before)
# node_to_add: the new node to be inserted into the list
def add_node(node, node_to_add):
    prev_node = node.prev  # Get the node that comes before 'node'
    node_to_add.next = node  # Link the new node to the current 'node' as its next node
    node_to_add.prev = prev_node  # Link the new node to 'prev_node' as its previous node
    prev_node.next = node_to_add  # Link 'prev_node' to the new node
    node.prev = node_to_add  # Update the previous pointer of 'node' to point to the new node

    # Time Complexity (Big O): O(1) for inserting the node since it involves
    # a constant number of pointer updates regardless of the list size.

# Function to delete a node from the list
# node: the node at position i (the node to be deleted)
def delete_node(node):
    prev_node = node.prev  # Get the node that comes before the node to be deleted
    next_node = node.next  # Get the node that comes after the node to be deleted
    prev_node.next = next_node  # Link 'prev_node' to 'next_node' (bypassing the node being deleted)
    next_node.prev = prev_node  # Link 'next_node' back to 'prev_node' (bypassing the node being deleted)

    # Time Complexity (Big O): O(1) for deleting the node since it involves
    # a constant number of pointer updates regardless of the list size.

# Test case 1: Adding a node to a doubly linked list
# Creating initial nodes
node1 = ListNode(1)  # head of the list
node2 = ListNode(2)  # second node
node3 = ListNode(3)  # third node

# Linking initial nodes together (node1 <-> node2 <-> node3)
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

# Adding a new node between node1 and node2
node_to_add = ListNode(1.5)
add_node(node2, node_to_add)

# Expected structure: node1 <-> node_to_add (1.5) <-> node2 <-> node3
assert node1.next == node_to_add  # node1's next should now point to node_to_add
assert node_to_add.prev == node1  # node_to_add's previous should point to node1
assert node_to_add.next == node2  # node_to_add's next should point to node2
assert node2.prev == node_to_add  # node2's previous should point to node_to_add

# Test case 2: Deleting a node from the doubly linked list
delete_node(node_to_add)

# Expected structure after deletion: node1 <-> node2 <-> node3 (node_to_add removed)
assert node1.next == node2  # node1's next should point back to node2 after deletion
assert node2.prev == node1  # node2's previous should point back to node1 after deletion

print("All test cases passed!")



"""
A doubly linked list is like a singly linked list, but each node also contains a pointer to the previous node. 
This pointer is usually called prev, and it allows iteration in both directions.
"""
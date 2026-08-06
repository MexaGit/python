class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Linked lists with sentinel nodes
# We call the start of a linked list the head and the end of a linked list the tail.
def add_to_end(node_to_add):
    node_to_add.next = tail
    node_to_add.prev = tail.prev
    tail.prev.next = node_to_add
    tail.prev = node_to_add


def remove_from_end():
    if head.next == tail:
        return

    node_to_remove = tail.prev
    node_to_remove.prev.next = tail
    tail.prev = node_to_remove.prev


def add_to_start(node_to_add):
    node_to_add.prev = head
    node_to_add.next = head.next
    head.next.prev = node_to_add
    head.next = node_to_add


def remove_from_start():
    if head.next == tail:
        return

    node_to_remove = head.next
    node_to_remove.next.prev = head
    head.next = node_to_remove.next


head = ListNode(None)
tail = ListNode(None)
head.next = tail
tail.prev = head

"""
Sentinel nodes sit at the start and end of linked lists and are used to make operations and the code needed 
to execute those operations cleaner. The idea is that, even when there are no nodes in a linked list, 
you still keep pointers to a head and tail. The real head of the linked list is head.next and the real tail is 
tail.prev. The sentinel nodes themselves are not part of our linked list.

The sentinel nodes also allow us to easily add and remove from the front or back of the linked list. 
"""
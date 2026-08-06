class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Reverse the linked list function
def reverse_list(head):
    prev = None # null
    curr = head # 0
    while curr:
        """
        When we are at a node curr, we need to set its next pointer to the node we were at previously.
        Use a prev pointer to track the previous node.
        The prev pointer needs to also update every iteration.
        After updating curr.next, set prev = curr in preparation for the next node.
        If we set curr.next = prev, then we lose the reference to the original curr.next.
        Use nextNode to keep a reference to the original curr.next.
        """
        next_node = curr.next  # first, make sure we don't lose the next node - 1
        curr.next = prev       # reverse the direction of the pointer
        prev = curr            # set the current node to prev for the next node
        curr = next_node       # move on
    return prev

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else " -> None\n")
        current = current.next

# Create the linked list 0 -> 1 -> 2 -> 3 -> 4 -> None
head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)

# Print the original linked list
print("Original linked list:")
print_linked_list(head)

# Reverse the linked list using reverse_list function
reversed_head = reverse_list(head)

# Print the reversed linked list 4 -> 3 -> 2 -> 1 -> 0 -> None
print("Reversed linked list:")
print_linked_list(reversed_head)

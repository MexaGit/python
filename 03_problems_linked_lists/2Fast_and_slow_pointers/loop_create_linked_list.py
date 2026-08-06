class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])  # Initialize the head with the first value
    current = head
    for val in values[1:]:
        current.next = ListNode(val)  # Create the next node
        current = current.next  # Move to the next node
    return head

def print_linked_list(head, max_nodes=100):
    """
    Traverses and prints the linked list.
    To prevent infinite loops in case of cycles, limits traversal to `max_nodes` nodes.
    """
    current = head
    count = 0
    while current and count < max_nodes:
        print(current.val, end=" -> " if current.next else " -> None\n")
        current = current.next
        count += 1
    if count == max_nodes:
        print("... (possible cycle detected)")


# Example: Creating a linked list 1 -> 2 -> 3 -> 4 -> 5 using a list of values
values = [1, 2, 3, 4, 5]
head = create_linked_list(values)

# Traverse and print the linked list to verify
print("Traversing the linked list:")
print_linked_list(head)


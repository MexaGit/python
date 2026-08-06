class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Define the function to find the k-th node from the end
def find_node(head, k):
    slow = head
    fast = head
    # Move the fast pointer k steps ahead
    for _ in range(k):
        fast = fast.next

    # Move both slow and fast until fast reaches the end
    while fast:
        slow = slow.next
        fast = fast.next

    return slow

# Create nodes for the linked list
head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)
fifth = ListNode(5)

# Link the nodes together to form the list: 1 -> 2 -> 3 -> 4 -> 5
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

# Call the function to find the 2nd node from the end
k = 2
node = find_node(head, k)
print(f"The {k}-th node from the end is: {node.val}")  # Output: 4

"""
head -> 1 -> 2 -> 3 -> 4 -> 5 -> None
                      ↑
              (slow points here after traversal)
"""

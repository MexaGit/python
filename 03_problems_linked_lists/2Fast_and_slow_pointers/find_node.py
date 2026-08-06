class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_node(head, k):
    slow = head
    fast = head
    for _ in range(k):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Call the function to find the 2nd node from the end
print(find_node(head, 2).val)  # Output: 4


"""
Example 3: Given the head of a linked list and an integer k, return the kth node from the end.
For example, given the linked list that represents 1 -> 2 -> 3 -> 4 -> 5 and k = 2, 
return the node with value 4, as it is the 2nd node from the end.
"""
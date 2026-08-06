class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next # one step at a time
        fast = fast.next.next # two steps at a time

    return slow.val

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Call the function
print(get_middle(head))  # Output: 3

"""
Remember that slow and fast are completely independent of each other.
The most elegant solution comes from using the fast and slow pointer technique. 
If we have one pointer moving twice as fast as the other, then by the time it reaches the end, 
the slow pointer will be halfway through since it is moving at half the speed.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_middle(head):
    length = 0
    dummy = head
    while dummy:
        length += 1
        dummy = dummy.next

    for _ in range(length // 2):
        head = head.next

    return head.val

# Create a linked list: 10 -> 20 -> 30 -> 40 -> 50
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)
head.next.next.next.next = ListNode(50)

# Call the function
print(get_middle(head))  # Output: 30

"""
This is basically "cheating", and would never pass as an acceptable solution in an interview.
You may have realized that the difficulty in this problem comes from the fact that we don't know
how long the linked list is. One thing we could do is iterate through the linked list once with
a dummy pointer to find the length, then iterate from the head again once we know the length to
find the middle.
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

#In the code, we are creating three nodes, one for each number, then setting the next pointers accordingly.
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
one.next = two
two.next = three
head = one

print(head.val)
print(head.next.val)
print(head.next.next.val)
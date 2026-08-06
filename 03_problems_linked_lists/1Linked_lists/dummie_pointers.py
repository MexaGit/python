def get_sum(head):
    ans = 0
    dummy = head
    # Using the dummy pointer allows us to traverse the linked list without losing a reference to the head.
    while dummy:
        ans += dummy.val
        dummy = dummy.next

    # same as before, but we still have a pointer at the head
    return ans
def get_sum(head):
    if not head:
        return 0
    # Traversal can also be done recursively:
    return head.val + get_sum(head.next)
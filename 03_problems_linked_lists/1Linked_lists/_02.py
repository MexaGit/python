def get_sum(head):
    ans = 0
    #  Traversal: Iterating forward through a linked list can be done with a simple loop.
    while head:
        ans += head.val
        head = head.next

    return ans

"""
Chaining .next

If you have multiple .next, for example head.next.next, everything before the final .next refers to one node. 
For example, given a linked list 1 -> 2 -> 3, if you have head pointing at the first node, and you do 
head.next.next, you are actually referring to 2.next, because head.next is the 2. We'll soon see that this 
is a very useful technique.

The final node's next pointer is null. Therefore, after doing head = head.next at the final node, 
head becomes null and the while loop ends.
"""
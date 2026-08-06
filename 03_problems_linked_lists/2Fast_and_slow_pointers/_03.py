from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        # fast ensures that the pointer hasn't gone beyond the list's end.
        # fast.next ensures that there is a next node available for fast to move forward to.
        # fast and fast.next checks if the pointer is not None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next

        return False

# Create a linked list: 3 -> 2 -> 0 -> -4 (with a cycle back to node 2)
head = ListNode(3)
second = ListNode(2)
third = ListNode(0)
fourth = ListNode(-4)

head.next = second
second.next = third
third.next = fourth
fourth.next = second  # Cycle here

# Call the function
solution = Solution()
print(solution.hasCycle(head))  # Output: True

"""
3 -> 2 -> 0 -> -4
     ↑         |
     |_________|
"""

# Create a linked list: 1 -> 2 -> 3 -> 4 (no cycle) = 1 -> 2 -> 3 -> 4 -> None
head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)

head.next = second
second.next = third
third.next = fourth

# Call the function
print(solution.hasCycle(head))  # Output: False


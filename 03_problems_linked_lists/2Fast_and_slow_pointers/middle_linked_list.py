from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Move fast one step ahead: this one return one before
        # fast = fast.next

        # Traverse the list with fast moving 2 steps and slow moving 1 step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Return the middle node (slow pointer)
        return slow

# Example: Creating a linked list 1 -> 2 -> 3 -> 4 -> 5
# using next.next.next can work for very small linked lists
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Call the middleNode function
solution = Solution()
middle_node = solution.middleNode(head)

# Print the value of the middle node
print(f"The middle node's value is: {middle_node.val}")  # Output: 3
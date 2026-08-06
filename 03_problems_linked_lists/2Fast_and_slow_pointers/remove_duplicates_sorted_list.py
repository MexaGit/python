class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current is not None and current.next is not None:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


# Example: Creating a linked list 1 -> 2 -> 3 -> 4 -> 5
# using next.next.next can work for very small linked lists
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else " -> None\n")
        current = current.next

# Print the original linked list
print("Original linked list:")
print_linked_list(head)

# Remove duplicates using the deleteDuplicates function
solution = Solution()
new_head = solution.deleteDuplicates(head)

# Print the linked list after removing duplicates
print("Linked list after removing duplicates:")
print_linked_list(new_head)
# Define the ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def pairSum(self, head):
        current = head
        values = []

        while current:
            values.append(current.val)
            current = current.next

        i = 0
        j = len(values) - 1
        maximumSum = 0
        while (i < j):
            maximumSum = max(maximumSum, values[i] + values[j])
            i += 1
            j -= 1

        return maximumSum

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Create the linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

# Print the original linked list
print("Original linked list:")
print_linked_list(head)

# Create the Solution object and use pairSum function
solution = Solution()
maximum_twin_sum = solution.pairSum(head)

# Print the result of the maximum twin sum
print("Maximum twin sum:", maximum_twin_sum)

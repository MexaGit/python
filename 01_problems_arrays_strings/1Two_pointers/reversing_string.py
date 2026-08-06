from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0  # Initialize the left pointer at the start of the list
        right = len(s) - 1  # Initialize the right pointer at the end of the list

        # Continue swapping until the two pointers meet
        while left < right:
            # Swap the elements at the left and right pointers
            s[left], s[right] = s[right], s[left]
            # Move the pointers towards the center
            left += 1  # Move left pointer to the right
            right -= 1  # Move right pointer to the left

# Example usage
solution = Solution()
s = ["h", "e", "l", "l", "o"]
solution.reverseString(s)
print(s)  # Output: ["o", "l", "l", "e", "h"]

"""
Time Complexity:

The function performs a single pass through half of the list, making the time complexity O(n), where n is the length 
of the string.

Space Complexity:

Since the operation is done in place and does not require additional storage that scales with the input size, the space
 complexity is O(1).
"""





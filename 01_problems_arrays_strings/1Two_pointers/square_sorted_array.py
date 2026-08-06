from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)  # Get the length of the input list
        result = [0] * n  # Initialize a result list with zeros of the same length as nums
        print(result)
        left = 0  # Left pointer starts at the beginning of the list
        right = n - 1  # Right pointer starts at the end of the list

        # Traverse the result list in reverse order to fill it with squares
        # first value = n -1 = 4 in this case 10,
        # second value = -1 is where the loop stops, but it stops before reaching -1,
        # meaning the loop stops at index 0.
        # third value = -1 as the step size means the loop moves backwards through the list.
        #          start: 4, end: 0, step: 4-0
        for i in range(n - 1, -1, -1):
            # Compare the absolute values of the elements at the left and right pointers
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]  # Get the square of the element from the right
                right -= 1  # Move the right pointer to the left
            else:
                square = nums[left]  # Get the square of the element from the left
                left += 1  # Move the left pointer to the right

            result[i] = square * square  # Square the value and store it in the result

        return result  # Return the sorted squares list

# Example usage
solution = Solution()
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
print(solution.sortedSquares([-4, -1, 0, 3, 10]))  # Output: [0, 1, 9, 16, 100]
print(solution.sortedSquares([-7, -3, 2, 3, 11]))  # Output: [4, 9, 9, 49, 121]

"""
https://leetcode.com/problems/squares-of-a-sorted-array/
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in 
non-decreasing order.

Time Complexity:
The time complexity is O(n) because we make a single pass through the input list and perform constant-time operations 
for each element.

Space Complexity:
The space complexity is O(n) due to the additional result list used to store the squared values.
"""
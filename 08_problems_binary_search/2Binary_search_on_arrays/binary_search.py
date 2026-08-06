from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize the two pointers: left at the beginning, right at the end of the list
        left = 0
        right = len(nums) - 1

        # Use a binary search approach, iterating while the left pointer is less than or equal to the right
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            num = nums[mid]
            # If the number at mid is the target, return its index
            if num == target:
                return mid
            # If the target is smaller than the number at mid, move the right pointer to mid - 1
            if num > target:
                right = mid - 1
            else:
                # If the target is larger, move the left pointer to mid + 1
                left = mid + 1

        # If the target is not found, return -1
        return -1

# Example test case
# Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
# Output: 4 (The target 9 is at index 4)
# Explanation: 9 exists in nums and its index is 4
solution = Solution()
print(solution.search([-1, 0, 3, 5, 9, 12], 9))  # Expected output: 4


"""
https://leetcode.com/problems/binary-search/description/
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search
target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List
# Given an array of integers nums and an integer k, return the number of contiguous sub-arrays
# where the product of all the elements in the subarray is strictly less than k.
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # If k is less than or equal to 1, there can't be any valid subarrays
        if k <= 1:
            return 0

        ans = left = 0  # Initialize answer and left pointer
        curr = 1  # Current product of the window

        # Iterate through the array with the right pointer
        for right in range(len(nums)):
            curr *= nums[right]  # Multiply the current number to the product

            # While the product is greater than or equal to k, shrink the window from the left
            while curr >= k:
                curr //= nums[left]  # Divide the product by the leftmost number
                left += 1  # Move the left pointer to the right

            # Print each valid subarray ending at 'right'
            for i in range(left, right + 1):
                print(f"Valid subarray: {nums[i:right + 1]}")

            # The number of valid subarrays ending at 'right' is (right - left + 1)
            ans += right - left + 1

        return ans  # Return the total count of valid subarrays

# Example usage
solution = Solution() # Summary of Valid Subarrays: [10], [5], [10, 5], [2], [5, 2], [6], [2, 6], [5, 2, 6] = 8
print(solution.numSubarrayProductLessThanK([10, 5, 2, 6], 100))  # Output: 8
print(solution.numSubarrayProductLessThanK([1, 2, 3], 0))        # Output: 0
print(solution.numSubarrayProductLessThanK([1, 2, 3], 6))        # Output: 4
# [1], [2], [1, 2], [3]

"""
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product
of all the elements in the subarray is strictly less than k.

Example 1:
Input: nums = [10,5,2,6], k = 100
Output: 8

Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:
Input: nums = [1,2,3], k = 0
Output: 0

Time Complexity: O(n), where n is the length of the input list nums. Each element is processed at most twice 
(once by the right pointer and once by the left pointer).

Space Complexity: O(1) since no additional space is used that scales with the input size.
"""
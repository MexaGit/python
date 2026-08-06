from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0  # Initialize the left pointer of the sliding window
        ans = float('-inf')  # Start with the lowest possible value for comparison

        curr = 0  # Initialize the sum of the current window

        # Iterate over the array using the right pointer
        for right in range(len(nums)):
            curr += nums[right]  # Add the current element to the window sum

            # If we have reached the size of the window 'k'
            if right >= k - 1:
                # Update the maximum average found
                ans = max(ans, curr / k)

                # Remove the leftmost element from the window
                curr -= nums[left]
                left += 1  # Move the left pointer to the right

        return ans  # Return the maximum average found

# Example usage
solution = Solution()
print(solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # Output: 12.75
print(solution.findMaxAverage([5, 5, 5, 5], 1))             # Output: 5.0
print(solution.findMaxAverage([1, 2, 3, 4, 5], 2))          # Output: 4.0
print(solution.findMaxAverage([3,2,4,1,5], 2))          # Output: 3.0

"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 = minus power of 5 = 0.00001 will be accepted.

Time Complexity: O(n), where n is the length of the input list nums. Each element is processed once in the loop.
Space Complexity: O(1) since no additional space is used that scales with the input size.
"""
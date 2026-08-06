from typing import List
from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Use the @cache decorator to memoize the dp function results.
        # dp(i) returns the length of the Longest Increasing Subsequence (LIS) ending at index i.
        @cache
        def dp(i):
            # Base case: The LIS at any single index is at least 1 (the element itself).
            ans = 1

            # Recurrence relation: Look at all the previous elements (from 0 to i-1),
            # and check if nums[i] can extend any of the LIS that ends at nums[j].
            for j in range(i):
                # nums[i] must be greater than nums[j] to continue an increasing subsequence.
                if nums[i] > nums[j]:
                    # Update the current LIS length based on the maximum LIS length found so far.
                    ans = max(ans, dp(j) + 1)

            return ans

        # Find the maximum LIS across all indices.
        return max(dp(i) for i in range(len(nums)))


# Test cases
sol = Solution()

# Test case 1: The longest increasing subsequence is [2, 3, 7, 101].
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4

# Test case 2: The longest increasing subsequence is [0, 1, 2, 3].
print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))  # Output: 4

"""
https://leetcode.com/problems/longest-increasing-subsequence/description/
Given an integer array nums, return the length of the longest strictly increasing
subsequence
.
"""
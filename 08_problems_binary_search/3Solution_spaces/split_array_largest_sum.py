from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        # Function to determine how many subarrays are required
        # if the maximum sum allowed is 'max_sum_allowed'.
        def min_subarrays_required(max_sum_allowed: int) -> int:
            current_sum = 0
            splits_required = 0

            # Iterate through the elements of the array
            for element in nums:
                # If adding the current element does not exceed 'max_sum_allowed'
                if current_sum + element <= max_sum_allowed:
                    current_sum += element
                else:
                    # Otherwise, increment the number of splits and start a new subarray
                    current_sum = element
                    splits_required += 1

            # Add one to account for the final subarray
            return splits_required + 1

        # The smallest possible sum is the largest element in nums
        # The largest possible sum is the sum of all elements in nums
        left = max(nums)
        right = sum(nums)

        # Perform binary search to minimize the maximum sum in subarrays
        while left <= right:
            # Calculate the mid point
            max_sum_allowed = (left + right) // 2

            # Determine the minimum number of subarrays needed
            if min_subarrays_required(max_sum_allowed) <= m:
                right = max_sum_allowed - 1
                minimum_largest_split_sum = max_sum_allowed
            else:
                # Move to the right side if we need more subarrays
                left = max_sum_allowed + 1

        return minimum_largest_split_sum

# Example Test Case 1:
# Input: nums = [7, 2, 5, 10, 8], m = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
print(Solution().splitArray([7, 2, 5, 10, 8], 2))  # Expected output: 18

# Example Test Case 2:
# Input: nums = [1, 2, 3, 4, 5], m = 2
# Output: 9
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
print(Solution().splitArray([1, 2, 3, 4, 5], 2))  # Expected output: 9

# Example Test Case 3:
# Input: nums = [1, 4, 4], m = 3
# Output: 4
# Explanation: Since m=3, we can split the array into [1], [4], [4] where the largest sum is 4.
print(Solution().splitArray([1, 4, 4], 3))  # Expected output: 4

"""
https://leetcode.com/problems/split-array-largest-sum/description/
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any
subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

#---------------------------------------------------------------------------------------#

Overview
We have an array of n non-negative integers which we must split into m subarrays. The goal is to split it in such a way
that the largest sum of a subarray among these m subarrays is minimized.

While dividing the array, we can observe that for each integer, there are two options: either add it to the current
subarray or start a new subarray with it (as long as the number of subarrays does not exceed m). The maximum number
of possible combinations is (m−1n−1) (because we must split the array at m−1 positions to obtain m subarrays, and
there are n−1 positions where the array can be split). The brute force approach is to enumerate every possible
combination and select the combination with the smallest maximum sum subarray. However, given the problem constraints,
the worst-case scenario will have (49 999) combinations, which is extraordinarily large. So let's try to find a
better-optimized approach.

There are two characteristics of this problem that we should take note of at this time. First, as we iterate over each
element, we must decide whether to add the element to the current subarray or to start a new subarray. This decision
will depend on the number of subarrays we have already made. In other words, each decision we make is affected by the
previous decisions we have made. Second, the problem is asking to minimize the largest sum of subarrays. These are two
common characteristics of dynamic programming problems, and as such we will first approach this problem using dynamic
programming.

Note: If you arrived at this conclusion before reading this article, then you have done well! The clues in the problem
description hint that we should consider using dynamic programming to solve this problem. However, what makes this
problem especially tricky is that the optimal solution does not use dynamic programming! This speaks to the importance
of taking a moment to consider other possible approaches, even after arriving at the first possible solution. Take a
moment to try to come up with another viable approach now, and we will discuss the optimal approach last.


"""
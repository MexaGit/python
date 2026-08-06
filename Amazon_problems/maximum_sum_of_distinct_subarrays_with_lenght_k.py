from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Return 0 if it's impossible to have a subarray of length k
        if n < k:
            return 0

        max_sum = 0
        current_sum = 0
        element_count = {}

        # Sliding window
        for i in range(n):
            # Add the current element to the window
            current_sum += nums[i]
            element_count[nums[i]] = element_count.get(nums[i], 0) + 1

            # If window size exceeds k, remove the oldest element
            if i >= k:
                current_sum -= nums[i - k]
                element_count[nums[i - k]] -= 1
                if element_count[nums[i - k]] == 0:
                    del element_count[nums[i - k]]

            # When the window size is exactly k, check if all elements are unique
            if i >= k - 1 and len(element_count) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum

"""
https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
"""

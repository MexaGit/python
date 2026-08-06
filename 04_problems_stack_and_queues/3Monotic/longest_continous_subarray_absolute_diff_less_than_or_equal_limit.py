from typing import List
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Deques to maintain the indices of the maximum and minimum elements in the current window
        increasing = deque()  # To keep track of the minimum elements
        decreasing = deque()  # To keep track of the maximum elements
        left = ans = 0  # Left pointer for the sliding window and the maximum length found

        for right in range(len(nums)):
            # Maintain the monotonic deques
            # Remove elements from the increasing deque if they are greater than the current element
            while increasing and increasing[-1] > nums[right]:
                increasing.pop()
            # Remove elements from the decreasing deque if they are less than the current element
            while decreasing and decreasing[-1] < nums[right]:
                decreasing.pop()

            # Append the current element to both deques
            increasing.append(nums[right])
            print(increasing, "in")
            decreasing.append(nums[right])
            print(decreasing, "de")

            # Maintain window property: the difference between max and min should not exceed limit
            while decreasing[0] - increasing[0] > limit:
                # If the leftmost element is the maximum, remove it from the decreasing deque
                if nums[left] == decreasing[0]:
                    decreasing.popleft()
                # If the leftmost element is the minimum, remove it from the increasing deque
                if nums[left] == increasing[0]:
                    increasing.popleft()
                # Move the left pointer to the right to shrink the window
                left += 1

            # Update the maximum length of subarray found
            ans = max(ans, right - left + 1)

        return ans

# Test case with mixed values and a larger limit
# Input: nums = [8, 2, 4, 7], limit = 4
# Expected Output: 4
# Explanation:
# Valid subarrays within limit:
# [8, 2, 4, 7] → max = 8, min = 2 → diff = 6 (not valid)
# [2, 4, 7] → max = 7, min = 2 → diff = 5 (not valid)
# [2, 4] → max = 4, min = 2 → diff = 2 (valid)
# [4, 7] → max = 7, min = 4 → diff = 3 (valid)
# Longest valid subarray: length 4

solution = Solution()
print(solution.longestSubarray([8, 2, 4, 7], 4))  # Output: 4

# Test case with the provided input
# Input: nums = [10, 1, 2, 4, 7, 2], limit = 5
# Expected Output: 4
# Explanation:
# Valid subarrays within limit:
# - [1, 2, 4, 7, 2]: max = 7, min = 1 → |7 - 1| = 6 (not valid)
# - [2, 4, 7, 2]: max = 7, min = 2 → |7 - 2| = 5 (valid)
# The longest valid subarray is [2, 4, 7, 2], which has length 4.

solution = Solution()
print(solution.longestSubarray([10, 1, 2, 4, 7, 2], 5))  # Output: 4

# Test case with the provided input
# Input: nums = [4, 2, 2, 2, 4, 4, 2, 2], limit = 0
# Expected Output: 3
# Explanation:
# Valid subarrays within limit:
# - [2, 2, 2]: max = 2, min = 2 → |2 - 2| = 0 (valid)
# The longest valid subarray is [2, 2, 2], which has length 3.

solution = Solution()
print(solution.longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0))  # Output: 3

"""
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray
such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Example 1:
Input: nums = [8,2,4,7], limit = 4
Output: 2

Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.

Example 2:
Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

Example 3:
Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
"""
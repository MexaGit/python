class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        # Dictionary to store the first occurrence of each count
        count_map = {0: -1}
        max_len = count = 0

        # Iterate through the array
        for i, num in enumerate(nums):
            # Increase count by 1 for 1s, decrease by 1 for 0s
            count += 1 if num == 1 else -1

            # If the count has been seen before, calculate the length of the subarray
            if count in count_map:
                max_len = max(max_len, i - count_map[count])
            else:
                # Store the first occurrence of the count
                count_map[count] = i

        return max_len

# Example usage:
solution = Solution()
input_nums = [0, 1, 0]
print(solution.findMaxLength(input_nums))  # Output: 2

"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2

Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2

Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""
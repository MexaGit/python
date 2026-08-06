from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0  # Left pointer for the sliding window
        sumOfCurrentWindow = 0  # Sum of the current window
        res = float('inf')  # Result initialized to infinity

        # Iterate with the right pointer through the array
        for right in range(len(nums)):
            sumOfCurrentWindow += nums[right]  # Add the current number to the window sum

            # While the current window sum is greater than or equal to the target
            while sumOfCurrentWindow >= target:
                # Update the result with the minimum length found
                res = min(res, right - left + 1)
                sumOfCurrentWindow -= nums[left]  # Remove the leftmost element from the sum
                left += 1  # Move the left pointer to the right
            print(right, left)

        # Return the result if a valid subarray was found, otherwise return 0
        return 0 if res == float('inf') else res

# Example usage
solution = Solution()
print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))  # Output: 2
print(solution.minSubArrayLen(11, [1,1,1,1,1,1]))  # Output: 0

"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2

Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Time Complexity of minSubArrayLen:

Iterating through the array:
The outer for loop iterates through each element in the list nums with a right pointer. This loop runs O(n) times, 
where n is the length of nums.

Sliding window adjustment:
The inner while loop adjusts the left pointer whenever the current window sum is greater than or equal to the target. 
In the worst case, each element in nums will be processed twice—once when added to the sum and once when removed. 
Thus, the total time spent in the inner loop across all iterations is also O(n).
Since both loops together contribute to a linear pass through the list, the overall time complexity is O(n).

Space Complexity of minSubArrayLen:

Space for variables:
The algorithm uses a fixed number of variables (left, sumOfCurrentWindow, res), which take constant space O(1).

Input list:
The input list nums is provided and not modified or duplicated. Thus, it does not contribute to additional space 
requirements.
Therefore, the overall space complexity is O(1), as the algorithm only uses a constant amount of extra space beyond 
the input.
"""
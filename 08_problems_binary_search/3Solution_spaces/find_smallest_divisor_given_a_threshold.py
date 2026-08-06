from typing import List
from math import ceil

class Solution:
    # Binary Search
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        # Helper function to calculate the sum of ceil(num / divisor) for each number in 'nums'
        def find_division_sum(divisor: int) -> int:
            result = 0
            for num in nums:
                # Add the division result for each number, rounded up (using ceil)
                result += ceil(num / divisor)
            return result

        # Initialize the binary search range
        low = 1  # The smallest possible divisor is 1
        high = max(nums)  # The largest divisor we might need to consider is the largest number in the list
        ans = -1  # This will store the final answer

        # Perform binary search
        while low <= high:
            mid = (low + high) // 2  # Find the midpoint divisor
            result = find_division_sum(mid)  # Calculate the sum for the current divisor

            # If the sum is less than or equal to the threshold, it could be a valid divisor
            if result <= threshold:
                ans = mid  # Store this as a potential answer
                high = mid - 1  # Try smaller divisors to find the minimum
            else:
                low = mid + 1  # Otherwise, try larger divisors to reduce the sum

        return ans

# Example Test Case 1:
# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: The smallest divisor is 5 since ceil([1/5, 2/5, 5/5, 9/5]) results in [1, 1, 1, 2] and the sum is 5
# which is <= 6.
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1.
# If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2).
print(Solution().smallestDivisor([1, 2, 5, 9], 6))  # Expected output: 5

# Example Test Case 2:
# Input: nums = [44, 22, 33, 11, 1], threshold = 5
# Output: 44
# Explanation: The smallest divisor is 44 since it gives the sum 5 (1, 1, 1, 1, 1) when dividing [44, 22, 33, 11, 1].
print(Solution().smallestDivisor([44, 22, 33, 11, 1], 5))  # Expected output: 44

# Example Test Case 3:
# Input: nums = [19, 29, 15], threshold = 8
# Output: 6
# Explanation: The smallest divisor is 6 since ceil([19/6, 29/6, 15/6]) results in [4, 5, 3] and the sum is 12 which
# is <= 8.
print(Solution().smallestDivisor([19, 29, 15], 8))  # Expected output: 6

"""
https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the
array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less
than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example:
7/3 = 3 and 10/2 = 5).

The test cases are generated so that there will be an answer.
"""
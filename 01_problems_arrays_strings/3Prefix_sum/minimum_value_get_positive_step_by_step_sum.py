from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        total = 0  # Initialize the running total
        min_sum = 0  # Initialize the minimum sum seen so far

        # Calculate the running sum and track the minimum sum
        for num in nums:
            total += num  # Update the running total
            print(total, end=" ")
            min_sum = min(min_sum, total)  # Update the minimum sum if the current total is lower
            # Uncomment the line below for debugging purposes
            # print(min_sum, total, num)

        # We need at least 1 to make the minimum sum positive, hence the +1.
        # return 1 - min_sum if min_sum < 0 else 1
        if min_sum < 0:
            # return 1 - (-4) = 5
            # return 1 - (1) = 1
            # return 1 - (-4) = 5
            return 1 - min_sum
        else:
            return 1


# Example usage
solution = Solution()
print(solution.minStartValue([-3, 2, -3, 4, 2]))  # Output: 5
print(solution.minStartValue([1, 2]))              # Output: 1
print(solution.minStartValue([1, -2, -3]))         # Output: 5

"""
Example 1:

Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
step by step sum
startValue = 4 | startValue = 5 | nums
  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
  (4 +2 ) = 6  | (5 +2 ) = 7    |   2
  
Time Complexity: O(n), where n is the length of nums (due to the single loop iterating through the list).
Space Complexity: O(1), as we are using a constant amount of extra space for variables.
"""
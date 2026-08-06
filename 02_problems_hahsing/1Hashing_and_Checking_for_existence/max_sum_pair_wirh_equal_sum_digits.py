from collections import defaultdict
from typing import List

class Solution:
    # This algorithm is inefficient due to the sorting, which can potentially cost O(n ⋅ log n)
    # if every number in the input has the same digit sum, where n is the length of the input array.
    def maximumSum(self, nums: List[int]) -> int:
        def get_digit_sum(num):
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10

            return digit_sum

        dic = defaultdict(list)
        for num in nums:
            digit_sum = get_digit_sum(num)
            dic[digit_sum].append(num)

        ans = -1
        for key in dic:
            curr = dic[key]
            if len(curr) > 1:
                curr.sort(reverse=True)
                ans = max(ans, curr[0] + curr[1])

        return ans

    def maximumSum1(self, nums: List[int]) -> int:
        def get_digit_sum(num):
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10

            return digit_sum

        dic = defaultdict(int)
        ans = -1
        for num in nums:
            digit_sum = get_digit_sum(num)
            if digit_sum in dic:
                ans = max(ans, num + dic[digit_sum])
            dic[digit_sum] = max(dic[digit_sum], num)

        return ans

solution = Solution()
print(solution.maximumSum([18,43,36,13,7]))

"""
You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j,
such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].
Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j
that satisfy the conditions.

Example 1:
Input: nums = [18,43,36,13,7]
Output: 54

Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.

Example 2:
Input: nums = [10,12,19,14]
Output: -1

Explanation: There are no two numbers that satisfy the conditions, so we return -1.
"""
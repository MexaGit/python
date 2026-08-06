from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        l, r = nums[i], nums[j]
        res = 0
        while i < j:
            if l < r:
                i += 1
                l += nums[i]
                res += 1
            elif l > r:
                j -= 1
                r += nums[j]
                res += 1
            else:
                i += 1
                l += nums[i]
                j -= 1
                r += nums[j]
        return res

"""
https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
Example 1:

Input: nums = [4,3,2,1,2,3,1]
Output: 2
Explanation: We can turn the array into a palindrome in 2 operations as follows:
- Apply the operation on the fourth and fifth element of the array, nums becomes equal to [4,3,2,3,3,1].
- Apply the operation on the fifth and sixth element of the array, nums becomes equal to [4,3,2,3,4].
The array [4,3,2,3,4] is a palindrome.
It can be shown that 2 is the minimum number of operations needed.
"""
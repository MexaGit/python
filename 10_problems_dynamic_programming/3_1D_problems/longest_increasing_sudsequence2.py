from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

# Test cases
sol = Solution()

# Test case 1: The longest increasing subsequence is [2, 3, 7, 101].
print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4

# Test case 2: The longest increasing subsequence is [0, 1, 2, 3].
print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))  # Output: 4
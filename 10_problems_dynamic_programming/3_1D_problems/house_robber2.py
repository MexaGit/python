from typing import List

class Solution:
    # bottom_up
    def rob(self, nums: List[int]) -> int:
        # To avoid out of bounds error from setting base case
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * n

        # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            # Recurrence relation
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]

# Test cases
sol = Solution()

# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
print(sol.rob([1, 2, 3, 1]))  # Output: 4 (rob houses 1 and 3)

# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
print(sol.rob([2, 7, 9, 3, 1]))  # Output: 12 (rob houses 2 and 4)

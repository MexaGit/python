from typing import List

class Solution:
    # This algorithm has the same time complexity, but an O(1) space complexity!
    def rob(self, nums: List[int]) -> int:
        # To avoid out of bounds error from setting base case
        if len(nums) == 1:
            return nums[0]

        n = len(nums)

        # Base cases
        back_two = nums[0]
        back_one = max(nums[0], nums[1])

        for i in range(2, n):
            # back_two becomes back_one, and back_one gets updated
            back_one, back_two = max(back_one, back_two + nums[i]), back_one

        return back_one

# Test cases
sol = Solution()

# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
print(sol.rob([1, 2, 3, 1]))  # Output: 4 (rob houses 1 and 3)

# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
print(sol.rob([2, 7, 9, 3, 1]))  # Output: 12 (rob houses 2 and 4)

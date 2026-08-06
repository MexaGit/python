from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dic:  # This operation is O(1)!
                return [i, dic[complement]]

            dic[num] = i

        return [-1, -1]

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
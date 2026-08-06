from typing import  List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # left is set to 1 because the first element is always unique.
        left = 1
        for right in range(1, len(nums)):
            # Found unique element
            if nums[right - 1] != nums[right]:
                # print(nums[right - 1], nums[right], " nums")
                # Updating left in our main array
                # unique elements are grouped together at the beginning of the array
                nums[left] = nums[right]
                # Incrementing left count by 1
                left += 1
        return left

solution = Solution()
print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(solution.removeDuplicates([0,0,1,5,5,1,1,2,2,4,4,3,3,2,2,4,4]))

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique 
element appears only once. The relative order of the elements should be kept the same. Then return the number of 
unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were 
present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""
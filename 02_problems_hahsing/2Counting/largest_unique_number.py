from collections import Counter, OrderedDict
from typing import List

class Solution:
    # Sorting
    def largestUniqueNumber(self, nums: List[int]) -> int:
        n = len(nums)

        # If there's only one element, it's unique by default
        if n == 1:
            return nums[0]

        nums.sort(reverse=True)

        # Start from the beginning (largest numbers)
        currentIndex = 0

        while currentIndex < n:
            # If it's the first element or different from the next one, it's unique
            if currentIndex == n - 1 or nums[currentIndex] != nums[currentIndex + 1]:
                return nums[currentIndex]
            # Skip duplicates
            while currentIndex < n - 1 and nums[currentIndex] == nums[currentIndex + 1]:
                currentIndex += 1
            # Move to the next unique number
            currentIndex += 1

        return -1

    #------------------------------------------------------------------------------------#
    # Sorted Map
    def largestUniqueNumber1(self, nums: List[int]) -> int:
        # Create a frequency map
        frequency_map = {}
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1

        # Create a sorted OrderedDict
        sorted_map = OrderedDict(sorted(frequency_map.items(), reverse=True))

        # Find the largest unique number
        for num, freq in sorted_map.items():
            if freq == 1:
                return num

        return -1

    # ------------------------------------------------------------------------------------#
    # Map
    def largestUniqueNumber2(self, nums: List[int]) -> int:
        # Use Counter to count frequencies of numbers
        frequency_map = Counter(nums)

        # Find the largest number with frequency 1, or -1 if none found
        return max((num for num, freq in frequency_map.items() if freq == 1), default=-1,)

solution = Solution()
print(solution.largestUniqueNumber([5,7,3,9,4,9,8,3,1]))
"""
Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.
Input: nums = [5,7,3,9,4,9,8,3,1]
Output: 8

Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, 
so it is the answer.
"""
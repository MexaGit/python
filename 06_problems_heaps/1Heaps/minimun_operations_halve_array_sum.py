import heapq
from typing import List

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        # Calculate the target sum, which is half of the total sum of the array.
        target = sum(nums) / 2

        # Create a max-heap by converting all numbers to negative.
        heap = [-num for num in nums]
        heapq.heapify(heap)  # Transform the list into a heap (min-heap but with negative values for max-heap behavior)

        ans = 0  # This will track the number of operations needed to halve the array sum.

        # While we still need to reduce the sum more (i.e., the remaining target is greater than zero)
        while target > 0:
            ans += 1  # Increment the number of operations

            # Pop the largest number (most negative value, representing the largest absolute value)
            x = heapq.heappop(heap)

            # Reduce the remaining target by half of the current largest value
            target += x / 2  # x is negative, so adding x / 2 actually reduces the target

            # Push half of the current largest value back into the heap for further reductions
            heapq.heappush(heap, x / 2)

        return ans

# Test case 1
# Explanation: The initial sum of nums is equal to 5 + 19 + 8 + 1 = 33.
# The following is one of the ways to reduce the sum by at least half:
# Pick the number 19 and reduce it to 9.5.
# Pick the number 9.5 and reduce it to 4.75.
# Pick the number 8 and reduce it to 4.
# The final array is [5, 4.75, 4, 1] with a total sum of 5 + 4.75 + 4 + 1 = 14.75.
# The sum of nums has been reduced by 33 - 14.75 = 18.25, which is at least half of the initial sum, 18.25 >= 33/2 = 16.5.
# Overall, 3 operations were used so we return 3.
# It can be shown that we cannot reduce the sum by at least half in less than 3 operations.
nums1 = [5, 19, 8, 1]
solution = Solution()
print(solution.halveArray(nums1))  # Expected output: 3
# Explanation: First reduce 19, then 9.5, then 5 -> Operations: 3

# Test case 2
# Explanation: The initial sum of nums is equal to 3 + 8 + 20 = 31.
# The following is one of the ways to reduce the sum by at least half:
# Pick the number 20 and reduce it to 10.
# Pick the number 10 and reduce it to 5.
# Pick the number 3 and reduce it to 1.5.
# The final array is [1.5, 8, 5] with a total sum of 1.5 + 8 + 5 = 14.5.
# The sum of nums has been reduced by 31 - 14.5 = 16.5, which is at least half of the initial sum, 16.5 >= 31/2 = 15.5.
# Overall, 3 operations were used so we return 3.
# It can be shown that we cannot reduce the sum by at least half in less than 3 operations.
nums2 = [3, 8, 20]
print(solution.halveArray(nums2))  # Expected output: 3
# Explanation: First reduce 20, then 10, then 8 -> Operations: 3

"""
You are given an array nums of positive integers. In one operation, you can choose any number from nums and reduce it
to exactly half the number. (Note that you may choose this reduced number in future operations.)

Return the minimum number of operations to reduce the sum of nums by at least half.

#-------------------------------------------------------------------------------------------------------#

This is another great example of when to use a heap - we need to find the max element repeatedly. 
Like in the previous example, it's not enough to just sort the input descending and go through the elements in order, 
because elements are added back in after being halved.

First, we convert the input into a heap. Then we define target as the sum of the elements divided by two - this is the 
amount of reduction we need to achieve.

Now, while target > 0, we need to reduce the sum. Remove the maximum element x from the heap (which is fast and easy). 
Reduce it to x / 2 by subtracting x / 2 from target, and then put x / 2 back into the heap.

The heap will always give us the maximum element in logarithmic time, even as we add elements back in.

A heap is an amazing data structure when you need to repeatedly find the maximum or minimum element. 
It can handle insertions and removals all while maintaining the max/min property, all in logarithmic time.
"""
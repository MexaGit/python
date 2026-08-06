from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize pointers to the start and end of the list
        left, right = 0, len(nums) - 1
        # Use binary search to find the target or the insert position
        while left <= right:
            pivot = (left + right) // 2  # Find the midpoint of the current range
            # If the target is found, return its index
            if nums[pivot] == target:
                return pivot
            # If the target is less than the pivot, search the left half
            if target < nums[pivot]:
                right = pivot - 1
            # Otherwise, search the right half
            else:
                left = pivot + 1

        # If target is not found, return the position where it should be inserted
        return left

# Example Test Case 1
# Input: nums = [1,3,5,6], target = 5
# Output: 2
print(Solution().searchInsert([1, 3, 5, 6], 5))  # Expected output: 2

# Example Test Case 2
# Input: nums = [1,3,5,6], target = 2
# Output: 1
print(Solution().searchInsert([1, 3, 5, 6], 2))  # Expected output: 1

"""
https://leetcode.com/problems/search-insert-position/description/
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return
the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

#-------------------------------------------------------------------------------------------------------#
Approach 1: Binary Search
Intuition

Based on the description of the problem, we can see that it could be a good match with the binary search algorithm.
    Binary search is a search algorithm that finds the position of a target value within a sorted array.

Usually, within binary search, we compare the target value to the middle element of the array at each iteration.
    If the target value is equal to the middle element, the job is done.
    If the target value is less than the middle element, continue to search on the left.
    If the target value is greater than the middle element, continue to search on the right.

To mark the search boundaries, one could use two pointers: left and right.

Starting from left = 0 and right = n - 1, we then move either of the pointers according to various situations:
    While left <= right:
        The pivot index is the one in the middle: pivot = (left + right) / 2. The pivot also divides the original array
        into two subarrays.
        If the target value is equal to the pivot element: target == nums[pivot], we're done.
        If the target value is less than the pivot element target < nums[pivot], continue to search on the left
        subarray by moving the right pointer right = pivot - 1.
        If the target value is greater than the pivot element target > nums[pivot], continue to search on the right
        subarray by moving the left pointer left = pivot + 1.
    What if the target value is not found?
In this case, the loop will be stopped at the moment when right < left and nums[right] < target < nums[left].

Integer Overflow
Let us now stress the fact that pivot = (left + right) // 2 works fine for Python3, which has arbitrary precision
integers, but it could cause some issues in Java and C++.

If left + right is greater than the maximum int value 231−1, it overflows to a negative value. In Java, it would
trigger an exception of ArrayIndexOutOfBoundsException, and in C++ it causes an illegal write, which leads to memory
corruption and unpredictable results.

Here is a simple way to fix it:
pivot = (left + right) // 2

and here is a bit more complicated but probably faster way using the bit shift operator.
pivot = (left + right) >> 1

Algorithm

Initialize the left and right pointers: left = 0, right = n - 1.
While left <= right:
    Compare middle element of the array nums[pivot] to the target value target.
        If the middle element is the target, i.e. target == nums[pivot]: return pivot.
        If the target is not here:
            If target < nums[pivot], continue to search on the left subarray. right = pivot - 1.
            Else continue to search on the right subarray. left = pivot + 1.
Return left.
"""
import heapq
from typing import List

class Solution:
    # Min-Heap
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        # Iterate through all numbers in the array
        for num in nums:
            # Push the current number to the min-heap
            heapq.heappush(heap, num)
            # If the heap exceeds size k, pop the smallest element
            if len(heap) > k:
                heapq.heappop(heap)

        # The top element of the heap will be the k-th largest
        return heap[0]

# Example usage
solution = Solution()

# Test case 1
nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
result1 = solution.findKthLargest(nums1, k1)
print(result1)  # Expected output: 5

# Test case 2
nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4
result2 = solution.findKthLargest(nums2, k2)
print(result2)  # Expected output: 4

"""
https://leetcode.com/problems/kth-largest-element-in-an-array/description/
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

#-------------------------------------------------------------------------------------#

Approach 2: Min-Heap
Intuition

A heap is a very powerful data structure that allows us to efficiently find the maximum or minimum value in a dynamic 
dataset.

If you are not familiar with heaps, we recommend checking out the Heap Explore Card.

The problem is asking for the kth largest element. Let's push all the elements onto a min-heap, but pop from the heap 
when the size exceeds k. When we pop, the smallest element is removed. By limiting the heap's size to k, after handling
all elements, the heap will contain exactly the k largest elements from the array.

It is impossible for one of the green elements to be popped because that would imply there are at least k elements in 
the array greater than it. This is because we only pop when the heap's size exceeds k, and popping removes the smallest
element.

After we handle all the elements, we can just check the top of the heap. Because the heap is holding the k largest 
elements and the top of the heap is the smallest element, the top of the heap would be the kth largest element, 
which is what the problem is asking for.

Algorithm

1. Initialize a min-heap heap.
2. Iterate over the input. For each num:
    Push num onto the heap.
    If the size of heap exceeds k, pop from heap.
3. Return the top of the heap.
"""
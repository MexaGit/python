import heapq
from collections import defaultdict
from typing import List

class Solution:
    # Two Heaps (Lazy Removal)
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def get_median():
            # Return the median depending on whether the window size k is odd or even
            if k % 2 == 1:
                return float(-lo[0])  # Return the max element from lo (max-heap)
            else:
                return (-lo[0] + hi[0]) / 2.0  # Return the average of tops of both heaps

        lo, hi = [], []  # lo is a max-heap (simulated using negatives), hi is a min-heap
        hash_table = defaultdict(int)  # For lazy deletion of elements
        medians = []

        # Initialize the heaps with the first `k` elements
        for i in range(k):
            heapq.heappush(lo, -nums[i])
        for _ in range(k // 2):
            heapq.heappush(hi, -heapq.heappop(lo))  # Balance the heaps

        # Process each sliding window
        for i in range(k, len(nums) + 1):
            medians.append(get_median())  # Append current median

            if i == len(nums):
                break  # Exit loop after processing all windows

            out_num = nums[i - k]  # Element leaving the window
            in_num = nums[i]  # Element entering the window
            balance = 0

            # Process the outgoing element
            if lo and out_num <= -lo[0]:  # Ensure heap is not empty before accessing
                balance -= 1  # Outgoing element was in the max heap
            else:
                balance += 1  # Outgoing element was in the min heap
            hash_table[out_num] += 1  # Mark the outgoing element for lazy deletion

            # Process the incoming element
            if lo and in_num <= -lo[0]:  # Ensure heap is not empty before accessing
                heapq.heappush(lo, -in_num)
                balance += 1  # Incoming element goes into max heap
            else:
                heapq.heappush(hi, in_num)
                balance -= 1  # Incoming element goes into min heap

            # Rebalance the heaps if necessary
            if balance < 0:  # Max heap has too many elements
                heapq.heappush(lo, -heapq.heappop(hi))
                balance += 1
            elif balance > 0:  # Min heap has too many elements
                heapq.heappush(hi, -heapq.heappop(lo))
                balance -= 1

            # Remove invalid elements from the top of the heaps
            while lo and hash_table[-lo[0]] > 0:
                hash_table[-lo[0]] -= 1
                heapq.heappop(lo)
            while hi and hash_table[hi[0]] > 0:
                hash_table[hi[0]] -= 1
                heapq.heappop(hi)

        return medians


# Example test cases
# Explanation:
# Window position                Median
# ---------------                -----
# [1  3  -1] -3  5  3  6  7        1
#  1 [3  -1  -3] 5  3  6  7       -1
#  1  3 [-1  -3  5] 3  6  7       -1
#  1  3  -1 [-3  5  3] 6  7        3
#  1  3  -1  -3 [5  3  6] 7        5
#  1  3  -1  -3  5 [3  6  7]       6
nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
k1 = 3
# Expected output: [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
print(Solution().medianSlidingWindow(nums1, k1))

nums2 = [1,2,3,4,2,3,1,4,2]
k2 = 3
# Expected output: [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0]
print(Solution().medianSlidingWindow(nums2, k2))

"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. 
So the median is the mean of the two middle values.
    For examples, if arr = [2,3,4], the median is 3.
    For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
    
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very
left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves
right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

#---------------------------------------------------------------------------------------------------#

Approach 2: Two Heaps (Lazy Removal)
Intuition

The idea is the same as Approach 3 from 295. Find Median From Data Stream. The only additional requirement is removing 
the outgoing elements from the window.

Since the window elements are stored in heaps, deleting elements that are not at the top of the heaps is a pain.

Some languages (like Java) provide implementations of the PriorityQueue class that allow for removing arbitrarily 
placed elements. Generally, using such features is not efficient nor is their portability assured.

Assuming that only the tops of heaps (and by extension the PriorityQueue class) are accessible, we need to find a way 
to efficiently invalidate and remove elements that are moving out of the sliding window.

At this point, an important thing to notice is the fact that if the two heaps are balanced, only the top of the heaps 
are actually needed to find the medians. This means that as long as we can somehow keep the heaps balanced, we could 
also keep some extraneous elements.

Thus, we can use hash-tables to keep track of invalidated elements. Once they reach the heap tops, we remove them from 
the heaps. This is the lazy removal technique.

An immediate challenge at this point is balancing the heaps while keeping extraneous elements. This is done by actually
moving some elements to the heap which has extraneous elements, from the other heap. This cancels out the effect of having extraneous elements and maintains the invariant that the heaps are balanced.

NOTE: When we talk about keeping the heaps balanced, we are not referring to the actual heap sizes. 
We are only concerned with valid elements and hence when we talk about balancing heaps, we are referring to count 
of such elements.

Algorithm

Two priority queues:
    A max-heap lo to store the smaller half of the numbers
    A min-heap hi to store the larger half of the numbers
    
A hash-map or hash-table hash_table for keeping track of invalid numbers. It holds the count of the occurrences of all
such numbers that have been invalidated and yet remain in the heaps.

The max-heap lo is allowed to store, at worst, one more element more than the min-heap hi. Hence if we have processed 
k elements:
    If k=2⋅n+1(∀n∈Z), then lo is allowed to hold n+1 elements, while hi can hold n elements.
    If k=2⋅n(∀n∈Z), then both heaps are balanced and hold n elements each.
    
This gives us the nice property that when the heaps are perfectly balanced, the median can be derived from the tops 
of both heaps. Otherwise, the top of the max-heap lo holds the legitimate median.

NOTE: As mentioned before, when we are talking about keeping the heaps balanced, the actual sizes of the heaps are 
irrelevant. Only the count of valid elements in both heaps matter.
    
    Keep a balance factor. It indicates three situations:
        balance =0: Both heaps are balanced or nearly balanced.
        balance <0: lo needs more valid elements. Elements from hi are moved to lo.
        balance >0: hi needs more valid elements. Elements from lo are moved to hi.
        
    Inserting an incoming number in_num:
        If in_num is less than or equal to the top element of lo, then it can be inserted to lo. 
        However this unbalances hi (hi has lesser valid elements now). Hence balance is incremented.
        Otherwise, in_num must be added to hi. Obviously, now lo is unbalanced. Hence balance is decremented.

    Lazy removal of an outgoing number out_num:
        If out_num is present in lo, then invalidating this occurrence will unbalance lo itself. Hence balance must be
        decremented.
        If out_num is present in hi, then invalidating this occurrence will unbalance hi itself. Hence balance must be
        incremented.
        We increment the count of this element in the hash_table table.
        Once an invalid element reaches either of the heap tops, we remove them and decrement their counts in the 
        hash_table table.
"""


from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element in nums
        counts = Counter(nums) # hashmap
        heap = []

        # Build a min-heap of size k
        for key, val in counts.items():
        # make sure when push the frequency comes first, heap make comparisons, checks elements left to right
            heapq.heappush(heap, (val, key))  # Push (frequency, element) onto the heap
            if len(heap) > k:
                heapq.heappop(heap)  # Remove the least frequent element if heap size exceeds k
        # Extract the elements from the heap and return them
        return [pair[1] for pair in heap]

# Example usage
solution = Solution()

# Test case 1
nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
result1 = solution.topKFrequent(nums1, k1)
print(result1)  # Expected output: [1, 2]

# Test case 2
nums2 = [1]
k2 = 1
result2 = solution.topKFrequent(nums2, k2)
print(result2)  # Expected output: [1]

# Test case 3
nums3 = [1, 2, 3, 1, 2, 4, 4, 4]
k3 = 2
result3 = solution.topKFrequent(nums3, k3)
print(result3)  # Expected output: [4, 1] or [1, 4], order may vary

"""
https://leetcode.com/problems/top-k-frequent-elements/description/
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any
order.

#--------------------------------------------------------------------------------#

Approach 1: Heap
Let's start from the simple heap approach with O(Nlogk) time complexity. To ensure that O(Nlogk) is always less than
O(NlogN), the particular case k=N could be considered separately and solved in O(N) time.

Algorithm
The first step is to build a hash map element -> its frequency. In Java, we use the data structure HashMap.
Python provides a dictionary subclass Counter to initialize the hash map we need directly from the input array.
This step takes O(N) time where N is a number of elements in the list.

The second step is to build a heap of size k using N elements. To add the first k elements takes a linear time O(k)
in the average case, and O(log1+log2+...+logk)=O(logk!)=O(klogk) in the worst case. It's equivalent to heapify
implementation in Python. After the first k elements we start to push and pop at each step, N - k steps in total.
The time complexity of heap push/pop is O(logk) and we do it N - k times which means O((N−k)logk) time complexity.
Adding both parts up, we get O(Nlogk) time complexity for the second step.

The third and last step is to convert the heap into an output array. That could be done in O(klogk) time.

In Python, library heapq provides a method nlargest, which combines the last two steps under the hood and has the same
O(Nlogk) time complexity.
"""
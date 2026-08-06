from heapq import heappush, heappop
from typing import List

class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        prefix = [False] * len(nums)
        pq = []
        for i, x in enumerate(nums):
            if len(pq) == k and -pq[0] < x: prefix[i] = True
            heappush(pq, -x)
            if len(pq) > k: heappop(pq)
        ans = 0
        pq = []
        for i, x in reversed(list(enumerate(nums))):
            if len(pq) == k and -pq[0] < x and prefix[i]: ans += 1
            heappush(pq, -x)
            if len(pq) > k: heappop(pq)
        return ans

"""
https://leetcode.com/problems/count-the-number-of-k-big-indices/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
Example 1:

Input: nums = [2,3,6,5,2,3], k = 2
Output: 2
Explanation: There are only two 2-big indices in nums:
- i = 2 --> There are two valid idx1: 0 and 1. There are three valid idx2: 2, 3, and 4.
- i = 3 --> There are two valid idx1: 0 and 1. There are two valid idx2: 3 and 4.
"""
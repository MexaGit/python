import heapq
from typing import List

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # Create a max heap by negating the values
        heap = [-num for num in piles]
        heapq.heapify(heap)  # Heapify the list to form a valid heap

        # Perform k operations
        for _ in range(k):
            # Pop the largest pile (negate to get the original value)
            curr = -heapq.heappop(heap)
            # Calculate the number of stones to remove (half the current pile)
            remove = curr // 2
            # Push the new pile size back into the heap
            heapq.heappush(heap, -(curr - remove))

        # Return the total sum of piles after k operations
        return -sum(heap)  # Negate again to get the original values


# Example test cases
solution = Solution()

# Test case 1
# Explanation: Steps of a possible scenario are:
# - Apply the operation on pile 2. The resulting piles are [5,4,5].
# - Apply the operation on pile 0. The resulting piles are [3,4,5].
# The total number of stones in [3,4,5] is 12.
piles1 = [5, 4, 9]
k1 = 2
result1 = solution.minStoneSum(piles1, k1)
print(result1)  # Expected output: 12 (after reducing the piles)

# Test case 2
# Explanation: Steps of a possible scenario are:
# - Apply the operation on pile 2. The resulting piles are [4,3,3,7].
# - Apply the operation on pile 3. The resulting piles are [4,3,3,4].
# - Apply the operation on pile 0. The resulting piles are [2,3,3,4].
# The total number of stones in [2,3,3,4] is 12.
piles2 = [4, 3, 6, 7]
k2 = 3
result2 = solution.minStoneSum(piles2, k2)
print(result2)  # Expected output: 8 (after reducing the piles)

"""
https://leetcode.com/problems/remove-stones-to-minimize-the-total/description/
You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile,
and an integer k. You should apply the following operation exactly k times:
    Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
    
Notice that you can apply the operation on the same pile more than once.
Return the minimum possible total number of stones remaining after applying the k operations.
floor(x) is the greatest integer that is smaller than or equal to x (i.e., rounds x down).

#--------------------------------------------------------------------------------------------#

Approach: Greedy + Max Heap
Intuition

At any given step, which number should we choose? We want to minimize the total number of stones remaining, which 
means we want to maximize the number of stones we remove at each step, so we should choose greedily choose the largest
 number at every step.

Every time we complete an operation, the data changes and we need to find the maximum number again. The best data 
structure for this would be a heap, as it allows us to update the data and always retrieve the maximum value in O(logn)
 time, compared to O(n) if we just used an array.

Algorithm
1. Initialize a max heap from piles.
2. Perform the following k times:
    Pop the maximum element from the heap, call it curr.
    Calculate how many stones remove should be removed from curr after performing the operation. 
    It is the floor of curr / 2.
    Push curr - remove onto the heap.
3. Return the sum of the elements in the heap.
"""
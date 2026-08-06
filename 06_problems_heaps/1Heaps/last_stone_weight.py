import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert all the stone weights to negative values because heapq in Python
        # is a min-heap by default, and we want to simulate a max-heap.
        stones = [-stone for stone in stones]

        # Transform the list into a heap. This operation is O(n).
        heapq.heapify(stones)

        # Keep processing the stones until one or no stones remain
        while len(stones) > 1:
            # Pop the two largest (most negative) stones
            first = abs(heapq.heappop(stones))  # the largest stone
            second = abs(heapq.heappop(stones))  # the second largest stone

            # If they are not the same, push the difference back as a new stone
            if first != second:
                heapq.heappush(stones, -abs(first - second))

        # If there's one stone left, return its weight, otherwise return 0
        return -stones[0] if stones else 0


# Test case 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
stones1 = [2, 7, 4, 1, 8, 1]
solution = Solution()
print(solution.lastStoneWeight(stones1))  # Expected output: 1

# Test case 2
stones2 = [10, 4, 2, 10]
print(solution.lastStoneWeight(stones2))  # Expected output: 2

"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

#---------------------------------------------------------------------------------------------#

To solve this problem, we can just simulate the process. The problem is, it could be expensive to repeatedly find the 
two heaviest stones. Just sorting the input descending and going through the elements in order wouldn't work because
often, a smash results in a new stone that is put back into the input.

With a heap, we can remove the two maximum elements in logarithmic time. After we perform the smash, if we have a 
leftover stone, we can add it back in logarithmic time. Note that logarithmic time is much faster than linear time, 
so this is a huge improvement over using a normal array.

So we put all the stones into a max heap. Then we just simulate the process until there are one or zero stones 
remaining. Pop the 2 max elements and then apply the rules in the problem description.

Don't focus on what's happening under the hood - just remember what a heap can do for you and how to use the operations.
"""
from typing import List
import heapq

class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        # Convert the list into a min-heap
        heapq.heapify(arr)
        apples = units = 0  # Initialize the count of apples and total weight

        # Process the apples while there are still apples in the heap
        # and the total weight does not exceed 5000
        while arr and units + arr[0] <= 5000:
            # Add the weight of the smallest apple to the total weight
            units += heapq.heappop(arr)
            # Increment the count of apples
            apples += 1

        return apples


# Example test case
# Input: arr = [100, 200, 150, 1000, 5000]
# Output: 4
# Explanation: All 4 apples can be carried by the basket since their sum of weights is 1450.
solution = Solution()
print(solution.maxNumberOfApples([100, 200, 150, 1000, 5000]))  # Expected output: 4

"""
https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/description/
You have some apples and a basket that can carry up to 5000 units of weight.
Given an integer array weight where weight[i] is the weight of the ith apple, return the maximum number of apples you
can put in the basket.

#--------------------------------------------------------------------------------------------#

Approach 2: Min-Heap
Intuition

Another approach to select the lightest apple at each time is using a min-heap.
We can transform the input array arr into a min-heap;
we then keep popping the first element from it, which is the lightest apple due to min-heap's nature.

Algorithm

Transform arr into a min-heap, and initialize two integer variables: apples to count the number of apples we have put 
in the basket and units to record the current weight of the basket.
Before units reaches 5000 and while there are remaining elements in the min-heap:
    increment apples by 1;
    increment units by the popped element from the min-heap;
    
Note: We will creat a heap using the heapify method. To create a heap using the heapify method requires O(N) time. 
More details can be found here.
"""
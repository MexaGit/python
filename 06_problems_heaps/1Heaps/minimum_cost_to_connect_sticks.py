import heapq
from typing import List

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        total_cost = 0
        # Create a min-heap from the list of sticks
        heapq.heapify(sticks)  # transforms the list into a heap in O(n) time

        # Combine two of the smallest sticks until only one remains
        while len(sticks) > 1:
            stick1 = heapq.heappop(sticks)  # Get the smallest stick
            stick2 = heapq.heappop(sticks)  # Get the second smallest stick

            cost = stick1 + stick2  # Cost to combine the two sticks
            total_cost += cost  # Add the cost to the total

            heapq.heappush(sticks, cost)  # Push the combined stick back into the heap

        return total_cost  # Return the total cost

# Example usage
solution = Solution()

# Test case 1
# Explanation: You start with sticks = [2,4,3].
# 1. Combine sticks 2 and 3 for a cost of 2 + 3 = 5. Now you have sticks = [5,4].
# 2. Combine sticks 5 and 4 for a cost of 5 + 4 = 9. Now you have sticks = [9].
# There is only one stick left, so you are done. The total cost is 5 + 9 = 14.
sticks1 = [2, 4, 3]
result1 = solution.connectSticks(sticks1)
print(result1)  # Expected output: 14

# Test case 2
# Explanation: You start with sticks = [1,8,3,5].
# 1. Combine sticks 1 and 3 for a cost of 1 + 3 = 4. Now you have sticks = [4,8,5].
# 2. Combine sticks 4 and 5 for a cost of 4 + 5 = 9. Now you have sticks = [9,8].
# 3. Combine sticks 9 and 8 for a cost of 9 + 8 = 17. Now you have sticks = [17].
# There is only one stick left, so you are done. The total cost is 4 + 9 + 17 = 30.
sticks2 = [1, 8, 3, 5]
result2 = solution.connectSticks(sticks2)
print(result2)  # Expected output: 30

"""
https://leetcode.com/problems/minimum-cost-to-connect-sticks/description/
You have some number of sticks with positive integer lengths. These lengths are given as an array sticks, where 
sticks[i] is the length of the ith stick.

You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. You must connect all the 
sticks until there is only one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.

#--------------------------------------------------------------------------------------------#

Approach 1: Greedy
Intuition and Algorithm

Always pick two of the smallest sticks to connect and continue doing this until you get only one stick. 
Let's see why this works.

Consider 4 sticks of the following lengths:
sticks=[a1,a2,a3,a4]

Let's try to connect them left to right.
After first merge, we will have:
sticks=[(a1+a 2),a3,a4],cost=(a1+a2)

After second merge, we will have:
sticks=[(a1+a2+a3),a4],cost=(a1+a2)+(a1+a2+a3)

And finally, last stick will look like:
sticks=[(a1+a2+a3+a4)],cost=)a1+a2)+(a1+a2+a3)+(a1+a2+a3+a4)

The final cost can be re-written as: cost=(3a1+3a2+2a3+a4)

As we can see, the sticks which are connected first are included in the final cost more than the ones that are picked 
later. Hence, it is optimal to pick smaller sticks first to get the smallest cost.

Let's try to figure out which data structure will be optimal to perform following tasks:
    Get two of the smallest sticks (stick1 and stick2) from the array.
    Add one stick (stick1 + stick2) back to the array.
    
We can use a min heap data structure (which is, generally, implemented as a PriorityQueue in most languages) which 
gives us O(logN) complexity for both the operations.
"""

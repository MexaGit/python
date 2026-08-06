from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper function to determine if Koko can eat all bananas
        # at speed 'k' within 'h' hours.
        def check(k):
            hours = 0
            # Calculate total hours needed to eat all piles at speed 'k'
            for bananas in piles:
                # Use ceil to account for partial hours (if bananas/k is not an integer)
                hours += ceil(bananas / k)
            # Return True if Koko can finish all bananas within 'h' hours
            return hours <= h

        # Initialize the binary search boundaries: the minimum possible speed is 1
        # and the maximum possible speed is the largest pile (since Koko can eat a pile per hour).
        left = 1
        right = max(piles)

        # Binary search to find the minimum eating speed
        while left <= right:
            mid = (left + right) // 2  # Try the middle speed
            if check(mid):
                right = mid - 1  # If it works, try smaller speeds
            else:
                left = mid + 1  # Otherwise, try larger speeds

        # 'left' is now the minimum eating speed that allows Koko to eat all bananas in 'h' hours
        return left


# Example Test Case 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Explanation:
# Koko can eat at speed 4 to finish all piles in exactly 8 hours.
print(Solution().minEatingSpeed([3, 6, 7, 11], 8))  # Expected output: 4

# Example Test Case 2:
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Explanation:
# Koko needs to eat at speed 30 to finish all piles within 5 hours.
print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 5))  # Expected output: 30

"""
https://leetcode.com/problems/koko-eating-bananas/description/
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and
will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas
from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas
during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

#-------------------------------------------------------------------------------------------------#

Overview
In the problem, Koko is given n piles of bananas, represented by an integer array of length n. She eats bananas at a 
constant speed, for example, x bananas per hour. The time taken to eat a pile of y bananas is y/x after rounding up to 
the closest integer. For example, if she eats 3 bananas per hour, it takes her 2 hours to eat a pile of 4 bananas.

The first constraint of the problem is that Koko has to eat all the piles within h hours, where h is no less than the 
number of piles. We can imagine that with a fast speed, Koko spends 1 hour on each pile, therefore, she can always 
finish all the piles within h hours. Let's call this kind of speed workable speed. Likewise, let any eating speed at 
which Koko can't eat all the piles be unworkable speed.

However, we have another constraint that Koko would like to eat as slow as possible, therefore, among all the workable 
eating speeds, we need to find out the minimum one.

"""
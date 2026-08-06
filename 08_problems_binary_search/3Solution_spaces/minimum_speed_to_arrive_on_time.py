from typing import List
from math import ceil

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # If the number of trips exceeds the ceiling of the available time, it's impossible to make it.
        if len(dist) > ceil(hour):
            return -1

        # Check if a given speed 'k' allows arriving on time
        def check(k):
            t = 0  # Initialize total time
            for d in dist:
                t = ceil(t)  # Round up the time after each segment, except the last one
                t += d / k  # Add time taken to travel distance 'd' at speed 'k'

            # Return True if the total time 't' is within the allowed hours
            return t <= hour

        # Binary search range for speed
        left = 1
        right = 10 ** 7  # Max possible speed

        # Perform binary search to find the minimum speed
        while left <= right:
            mid = (left + right) // 2
            if check(mid):  # If speed 'mid' is fast enough
                right = mid - 1  # Try lower speeds
            else:  # Otherwise, try higher speeds
                left = mid + 1

        return left  # 'left' now holds the minimum speed

# Example Test Case 1:
# Input: dist = [1, 3, 2], hour = 6
# Output: 1
# Explanation: At speed 1:
# - The first train ride takes 1/1 = 1 hour.
# - Since we are already at an integer hour, we depart immediately at the 1 hour mark. The second train takes 3/1 = 3 hours.
# - Since we are already at an integer hour, we depart immediately at the 4 hour mark. The third train takes 2/1 = 2 hours.
# - You will arrive at exactly the 6 hour mark.
print(Solution().minSpeedOnTime([1, 3, 2], 6))  # Expected output: 1

# Example Test Case 2:
# Input: dist = [1, 3, 2], hour = 2.7
# Output: 3
# Explanation: At speed 3:
# - The first train ride takes 1/3 = 0.33333 hours.
# - Since we are not at an integer hour, we wait until the 1 hour mark to depart. The second train ride takes 3/3 = 1 hour.
# - Since we are already at an integer hour, we depart immediately at the 2 hour mark. The third train takes 2/3 = 0.66667 hours.
# - You will arrive at the 2.66667 hour mark.
print(Solution().minSpeedOnTime([1, 3, 2], 2.7))  # Expected output: 3

# Example Test Case 3:
# Input: dist = [1, 3, 2], hour = 1.9
# Output: -1
# Explanation: It is impossible because the earliest the third train can depart is at the 2 hour mark.
print(Solution().minSpeedOnTime([1, 3, 2], 1.9))  # Expected output: -1

"""
https://leetcode.com/problems/minimum-speed-to-arrive-on-time/description/
You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute
to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where
dist[i] describes the distance (in kilometers) of the ith train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on
the 2nd train ride at the 2 hour mark.
Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach
the office on time, or -1 if it is impossible to be on time.

Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal
point.

#------------------------------------------------------------------------------------------#

Approach: Binary Search
Intuition

There are N trains that we need to take in order; the ith train will ride for dist[i] distance. We need to complete
this journey, i.e. ride all these trains within hour time; hour is a decimal number representing the amount of time we
have. We need to return the minimum positive speed integer that is required. One more constraint we have is that each
train will depart at an integer hour, so if we completed our 1st ride at, say 2.4 hours, then we can only start riding
the next train at 3rd hour.

One hint in the problem description is that the answer speed will not exceed 10'7. The first naive approach we can
apply is to do an exhaustive search over all the possible speeds we have. We can iterate from 1 to 10'7, and the first
number that can lead us to complete the journey within hour will be our answer. But how can we find out if some speed
can make us complete the journey within the constraint time? We can easily find the time required for individual rides
for each train, and then summing them up will give us the total time required. If this total time is less than hour
then it could be a possible answer; otherwise, not. This approach, as we can observe, is not efficient; we need to
iterate over the whole search space and then iterate over every train to find the total time.

Can we somehow reduce our search space? Let's say the time required with speed s is t; then it can be easily proved
that the time required with a speed greater than s will always be less than or equal to t. In other words, a higher
speed will always require less or equal time. This implies that if for a speed s the time required is less than the
time needed hour, then we don't need to look for the speeds greater than s as we need the smallest speed possible,
in this case, our search space should reduce down to left side of s, i.e. speeds less than s.
"""
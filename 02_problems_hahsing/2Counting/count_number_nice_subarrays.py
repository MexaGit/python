from collections import defaultdict
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in nums:
            # Increment 'curr' by 1 if 'num' is odd, else add 0
            curr += num % 2
            # Add to 'ans' the number of times the cumulative sum 'curr - k' has occurred
            ans += counts[curr - k]
            # Increment the count of the current cumulative sum of odd numbers
            counts[curr] += 1

        return ans

solution = Solution()
print(solution.numberOfSubarrays([1, 1, 2, 1, 1], 3))

"""
Valid Subarrays with Exactly 3 Odd Numbers
From the above enumeration, the valid subarrays are:

[1, 1, 2, 1] (Indices 0 to 3)
[1, 2, 1, 1] (Indices 1 to 4)

Given an array of positive integers nums and an integer k. Find the number of subarrays with exactly k odd numbers 
in them.
For example, given nums = [1, 1, 2, 1, 1], k = 3, the answer is 2. The subarrays with 3 odd numbers in them are
[1, 1, 2, 1, 1] and [1, 1, 2, 1, 1].

Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2

Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Visual Representation
Subarray	        Odd Count	Valid?
[1]	                1	        ❌
[1, 1]	            2	        ❌
[1, 1, 2]	        2	        ❌
[1, 1, 2, 1]	    3	        ✅
[1, 1, 2, 1, 1]	    4	        ❌
[1]	                1	        ❌
[1, 2]	            1	        ❌
[1, 2, 1]	        2	        ❌
[1, 2, 1, 1]	    3	        ✅
[2]	                0	        ❌
[2, 1]	            1	        ❌
[2, 1, 1]	        2	        ❌
[1]	                1	        ❌
[1, 1]	            2	        ❌
[1]	                1	        ❌
"""
from collections import defaultdict  # Importing defaultdict to handle default integer values
from typing import List  # Importing List for type hinting


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)  # Initialize a defaultdict to keep track of counts of cumulative sums
        counts[0] = 1  # This accounts for the case where the cumulative sum equals k itself
        ans = 0  # This will store the number of subarrays that sum to k
        curr = 0  # This variable will store the current cumulative sum
        print(counts)  # Initial state of counts: {0: 1}

        for num in nums:  # Iterate through each number in the input list
            curr += num  # Update the current cumulative sum
            # Example: If nums = [1, 2, 1, 2, 1], the values of curr will be:
            # After first iteration (num=1): curr = 1
            # After second iteration (num=2): curr = 3
            # After third iteration (num=1): curr = 4
            # After fourth iteration (num=2): curr = 6
            # After fifth iteration (num=1): curr = 7

            ans += counts[curr - k]  # Check how many times the (current sum - k) has occurred
            # This gives the number of valid subarrays ending at the current index that sum to k
            # For example, if curr = 3 and k = 3, we check counts[3 - 3] = counts[0] which is 1
            # This means there's one subarray [1, 2] summing to k
            # This count is added to ans

            counts[curr] += 1  # Update the count of the current cumulative sum
            # Example: counts becomes:
            # After first iteration (curr=1): counts = {0: 1, 1: 1}
            # After second iteration (curr=3): counts = {0: 1, 1: 1, 3: 1}
            # After third iteration (curr=4): counts = {0: 1, 1: 1, 3: 1, 4: 1}
            # After fourth iteration (curr=6): counts = {0: 1, 1: 1, 3: 1, 4: 1, 6: 1}
            # After fifth iteration (curr=7): counts = {0: 1, 1: 1, 3: 1, 4: 1, 6: 1, 7: 1}

        return ans  # Return the total count of subarrays that sum to k


solution = Solution()
# Calling the function with the example array and target sum
# Expected output: 2, because there are two subarrays that sum to 3: [1,2] and [2,1]
print(solution.subarraySum([1, 2, 1, 2, 1],3))

"""
Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1, 2, 1, 2, 1], k = 3
Output: 2

The prefix sum for this input, which is what curr represents during iteration, is [1, 3, 4, 6, 7].
You can see that there are three differences in this array of 3:   (4 - 1), (6 - 3), (7 - 4).

But we said that there are four valid subarrays? Recall that we need to initialize our hash map with 0: 1,
considering the empty prefix. This is because if there is a prefix with a sum equal to k, then without
initializing 0: 1, curr - k = 0 wouldn't show up in the hash map and we would "lose" this valid subarray.

So at indices 1, 2, 3, and 4, we find curr - k has been seen prior. The elements are all positive
so each value of curr - k only showed up once, and hence our answer is 4.

Visual Representation of counts Over Iterations
Iteration	num	curr  target (curr - k)	Counts Before Update	        Counts After Update	                  ans
0	        1	1	  -2	            {0: 1}	                        {0: 1, 1: 1}	                      0
1	        2	3	  0	                {0: 1, 1: 1}	                {0: 1, 1: 1, 3: 1}	                  1
2	        1	4	  1	                {0: 1, 1: 1, 3: 1}	            {0: 1, 1: 1, 3: 1, 4: 1}	          2
3	        2	6	  3	                {0: 1, 1: 1, 3: 1, 4: 1}	    {0: 1, 1: 1, 3: 1, 4: 1, 6: 1}	      3
4	        1	7	  4	                {0: 1, 1: 1, 3: 1, 4: 1, 6: 1}	{0: 1, 1: 1, 3: 1, 4: 1, 6: 1, 7: 1}  4
"""
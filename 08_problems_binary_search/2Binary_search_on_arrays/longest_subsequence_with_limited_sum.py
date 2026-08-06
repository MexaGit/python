from typing import List
import bisect

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # Sort the nums array to prepare for prefix sum calculations
        nums.sort()

        # Create the prefix sum array
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]  # Each element becomes the sum of all previous elements

        # Prepare a list to store the results for each query
        answer = []

        # For each query, find the maximum number of elements from nums that sum up to query
        for query in queries:
            # Use binary search to find the index of the largest prefix sum <= query
            index = bisect.bisect_right(nums, query)
            # Append the index as the result for this query
            answer.append(index)

        return answer

# Example Test Case 1
# Input: nums = [4,5,2,1], queries = [3,10,21]
# Output: [2,3,4]
# Explanation:
# 1st query: The sum of 1 and 2 is <= 3, so we can pick 2 numbers.
# 2nd query: The sum of 1, 2, and 4 is <= 10, so we can pick 3 numbers.
# 3rd query: All the numbers (1, 2, 4, 5) sum up to 12 which is <= 21, so we can pick all 4 numbers.
print(Solution().answerQueries([4, 5, 2, 1], [3, 10, 21]))  # Expected output: [2, 3, 4]

# Example Test Case 2
# Input: nums = [2,3,4,5], queries = [1]
# Output: [0]
# Explanation:
# 1st query: No number can be picked such that the sum <= 1, so we can pick 0 numbers.
print(Solution().answerQueries([2, 3, 4, 5], [1]))  # Expected output: [0]

"""
https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/
You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums
such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the
order of the remaining elements.

#--------------------------------------------------------------------------------------------------#

Approach 2: Prefix Sum + Binary Search
Intuition

Can we find the maximum size of a subsequence in a faster way than by adding up the numbers one by one?

We can take advantage of the prefix sum array presum of the sorted nums, each value presum[i] represents the sum of all 
numbers from nums[0] to nums[i]. Therefore, we can get the sum of the range from presum in constant time, rather than 
iterating over nums which requires O(n) time in the worst-case scenario.

To build the prefix sum array for an array nums, we start from an empty array presum:
    presum[0] = nums[0].
    presum[1] = nums[0] + nums[1], which equals presum[0] + nums[1].
    presum[2] = nums[0] + nums[1] + nums[2], which equals presum[1] + nums[2].
    ...
    
We can tell that all the terms presum[i] follow presum[i] = presum[i - 1] + nums[i] apart from the first term 
presum[0] = nums[0]. Therefore, we only need to iterate over nums once to build its prefix sum array presum. Moreover, 
since we don't need the original array nums once we have presum, thus we can build presum by modifying nums in-place 
to save some space:
    nums[0] = nums[0].
    nums[1] = nums[1] + nums[0].
    nums[2] = nums[2] + nums[1].
    nums[3] = nums[3] + nums[2].
    ...
The next subproblem is to find the maximum size of the subsequence of each query. Since the values in the prefix sum 
array presum are strictly increasing, thus we can use a binary search to find the insertion index of query to presum. 
Assume that the insertion index is index, it means the sum of the first index smallest numbers does not exceed query, 
thus index is the longest subsequence consists of the first index smallest numbers.

Algorithm
1. Sort nums and convert it into presum. We can re-use the nums array for this. Initialize an empty array answer.
2. Iterate over queries, for each query query, we use binary search to find its insertion index index and add index 
to answer.
3. Return answer when the iteration stops.
"""
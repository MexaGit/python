from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        # Sort the array to process elements in increasing order
        nums.sort()
        # Initialize the number of partitions (at least 1 partition is needed)
        ans = 1
        # Start with the first element of the sorted array as the base of the first partition
        x = nums[0]

        # Iterate through the rest of the elements
        for i in range(1, len(nums)):
            # If the difference between the current element and the base exceeds k,
            # start a new partition and set the new base to the current element
            if nums[i] - x > k:
                x = nums[i]
                ans += 1

        # Return the total number of partitions
        return ans

# Test cases

# Example 1:
# Input: nums = [3, 6, 1, 2, 5], k = 2
# Output: 2
# Explanation:
# We can partition nums into the two subsequences [3,1,2] and [6,5].
# The difference between the maximum and minimum value in the first subsequence is 3 - 1 = 2.
# The difference between the maximum and minimum value in the second subsequence is 6 - 5 = 1.
# Since two subsequences were created, we return 2. It can be shown that 2 is the minimum number of subsequences needed.
solution = Solution()
nums1 = [3, 6, 1, 2, 5]
k1 = 2
print(solution.partitionArray(nums1, k1))  # Output: 2

# Example 2:
# Input: nums = [5, 3, 6, 2, 8, 1], k = 1
# Output: 4
# Explanation:
# The array can be partitioned as [1, 2], [3], [5, 6], and [8].
nums3 = [5, 3, 6, 2, 8, 1]
k3 = 1
print(solution.partitionArray(nums3, k3))  # Output: 4

"""
You are given an integer array nums and an integer k. You may partition nums into one or more subsequences such that
each element in nums appears in exactly one of the subsequences.

Return the minimum number of subsequences needed such that the difference between the maximum and minimum values in
each subsequence is at most k.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing
the order of the remaining elements.

#-------------------------------------------------------------------------------------------#

Let's say we have nums = [3, 6, 1, 2, 5] and k = 2. The optimal subsequences are [3, 1, 2] and [6, 5]. What if we sort 
the input? Then we would have [1, 2, 3, 5, 6]. We completely messed up the order of the elements and the two optimal 
subsequences don't exist anymore.

Does it matter though? Is there any meaningful difference between [3, 1, 2] and a new subsequence that can be formed 
from the sorted input [1, 2, 3]? No, because in both, the only thing we are concerned about is the maximum and minimum 
element, which is independent of the order. Therefore, we can sort the input without worry.

The smallest element 1 must be in a group. We are allowed to put the 2 and 3 in the same group because they're within k.
 Should we? If we do, then we increment our answer by one, and then we have to solve the remaining problem [5, 6].

If we exclude the 3, then we need to increment our answer by one, and then we have to solve the remaining 
problem [3, 5, 6]. If we exclude both 2 and 3, then we need to increment our answer by one, and then we have to solve 
the remaining problem [2, 3, 5, 6].

In all 3 cases, we increment our answer by one. Therefore, we may as well choose the case where the remaining problem 
is the smallest since we want to minimize the answer. We can conclude that the optimal strategy is to greedily take as 
many numbers as we can per group, which is easy to do once we sort the input.

"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Backtracking function to generate subsets
        def backtrack(curr, i):
            # Base condition: if 'i' exceeds the length of nums, return
            if i > len(nums):
                return

            # Append a copy of the current subset (curr) to the answer list
            ans.append(curr[:])

            # Try adding every element starting from index 'i' to form subsets
            for j in range(i, len(nums)):
                curr.append(nums[j])  # Add the element to the current subset
                backtrack(curr, j + 1)  # Recurse to generate further subsets
                curr.pop()  # Backtrack to explore other subsets

        ans = []  # List to store all subsets
        backtrack([], 0)  # Start backtracking with an empty subset and index 0
        return ans

# Test Case 1:
# Input: nums = [1, 2, 3]
# Output: All subsets of [1, 2, 3]
print(Solution().subsets([1, 2, 3]))
# Expected output: [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]

# Test Case 2:
# Input: nums = [0]
# Output: All subsets of [0]
print(Solution().subsets([0]))
# Expected output: [[], [0]]

# Test Case 3:
# Input: nums = [1, 2]
# Output: All subsets of [1, 2]
print(Solution().subsets([1, 2]))
# Expected output: [[], [1], [1,2], [2]]

"""
https://leetcode.com/problems/subsets/description/
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

#----------------------------------------------------------------------------------------#

We can use the same process as in the previous approach to generate the backtracking tree.

The first important thing to understand is what the argument i represents. In the previous problem, we iterated over
the entire input at each node. We cannot do that here, as it would produce duplicate subsets. For example, if we have
nums = [1, 2, 3], then we would at one point have curr = [1, 2]. When we finish the subtree with 1 at the first
position, we would try 2 at the first position next. If we considered all numbers at each node, we would end up with
curr = [2, 1], which is a duplicate of [1, 2] since the order doesn't matter here.

As such, when we add an element to curr, we only want to consider elements that come after that element for the entire
subtree. We use an argument i that tells us where to start iterating from at each node. If we add an element at
index j, we pass j + 1 to the next call.

Now that we understand what i does, let's talk about the differences in implementation between this problem and the
previous one. In the previous problem, the answer nodes were the leaf nodes (as the leaf nodes represented curr having
a length of n). In this problem, a subset can have any length, so every node is an answer (even the root, as the root
represents the empty subset []). Therefore, the first thing we will do at each node is add curr to the answer.

The only other difference is that we will iterate over the input starting from i instead of iterating over the entire
input. As mentioned above, this will ensure that we don't have duplicates in our answer.
"""
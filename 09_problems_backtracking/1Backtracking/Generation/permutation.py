from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Backtracking function to generate permutations
        def backtrack(curr):
            # If the current list has all elements, it's a valid permutation
            if len(curr) == len(nums):
                ans.append(curr[:])  # Add a copy of the current list to results
                return

            # Try each number in 'nums' that is not already in 'curr'
            for num in nums:
                if num not in curr:
                    curr.append(num)  # Choose the number
                    backtrack(curr)  # Recurse with the updated list
                    curr.pop()  # Undo the choice (backtrack)

        ans = []  # List to store all permutations
        backtrack([])  # Start the backtracking process with an empty list
        return ans

# Test Case 1:
# Input: nums = [1, 2, 3]
# Output: All possible permutations of [1, 2, 3]
print(Solution().permute([1, 2, 3]))  # Expected output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

# Test Case 2:
# Input: nums = [0, 1]
# Output: All possible permutations of [0, 1]
print(Solution().permute([0, 1]))  # Expected output: [[0, 1], [1, 0]]

# Test Case 3:
# Input: nums = [1]
# Output: Only one permutation is possible: [1]
print(Solution().permute([1]))  # Expected output: [[1]]

"""
https://leetcode.com/problems/permutations/description/
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
#-----------------------------------------------------------------------------------------------#

First, to generate all permutations, we need to put every number in the first position. For each number in the first
position, we need to try all other numbers in the second position, and so on.

We will model the backtracking with a tree. Every node in the tree represents a function call. For a given function
call, the argument curr represents the current permutation we are buiding.

When we add an element to curr, we make another call to backtrack. This is equivalent to moving to a child. The root
node represents an empty array, and the path from the root to any given node represents curr.

To generate/traverse this tree, we start by calling backtrack with curr = []. Then, we put the first number in the
first position and call backtrack again. In the second call, we can't put the first number in the second position
because we already used the first number, so we put the second number instead and call backtrack again.

Eventually, curr will have the same length as nums which indicates that we have used all numbers (since duplicates
aren't allowed) and we have a valid permutation. This is a leaf node/base case - we add curr to the answer, and then
return.

Every time we return, exactly like in DFS, we are moving back up the tree. Remember: the path from the root to a given
node represents curr. When we return, we are removing the last node in the path. This means we also need to remove the
last element from curr.

After we have tried all possibilities with the first number being in the first position, we try the second number in
the first position and go through a subtree again. In general, in each call to backtrack, we iterate over the input
and if we find a number is not in curr, we add it to curr and go through the subtree.

Approach: Backtracking
Intuition

We are given that n <= 6. Typically, problems that ask you to find all of something with low bounds can be solved with
backtracking.

In backtracking, we generate all solutions one element at a time. This problem is asking us to generate all possible
permutations, so we will generate permutations one element at a time.

To generate a permutation one element at a time, we will use an array curr that represents the current permutation we
are building. To start, we add the first element in nums. We have curr = [nums[0]]. We are locking in this first value
and we will now find all permutations that start with nums[0].

To find all permutations that start with nums[0], we start by adding the next element, which is nums[1]. We now have
curr = [nums[0], nums[1]]. We are locking in this second element and we will now find all permutations that start with
nums[0], nums[1].

This continues until we use all elements, i.e. curr.length == nums.length. Let's say that we have finished finding all
permutations that start with [nums[0], nums[1]]. Now what? We backtrack by removing the nums[1], and we have
curr = [nums[0]] again. Now, we add the second element that comes after nums[0], which is nums[2]. We have
curr = [nums[0], nums[2]], and now we need to find all permutations that start with [nums[0], nums[2]].

Once we find all the permutations that start with [nums[0]], we backtrack by removing nums[0] from curr and adding the
next element. We have curr = [nums[1]], and now we need to find all permutations that start with nums[1].

This process is very recursive in nature. Each time we add an element, we solve a new version of the problem (find all
permutations that start with curr). The initial version of the problem is to find all permutations that start with [],
which represents all possible permutations.

To summarize: try all numbers in the first position. For each number in the first position, try all other numbers in
the second position. For each pair of numbers in the first and second positions, try all other numbers in the third
position, and so on.

Trees

The best way to think about the backtracking process is by modeling it as a tree. You can imagine the solution space as
a tree, with each node representing a version of curr. Label each node with a number that represents the last number
in curr. Moving to a child is like adding the child's label to curr.

A permutation uses each element exactly once. A node should only have children with labels representing elements that
haven't been used yet in the current path.

Given nums = [1, 2, 3], here is the backtracking tree:
"""
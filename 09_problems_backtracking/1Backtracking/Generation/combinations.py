from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Backtracking function to generate combinations
        def backtrack(curr, i):
            # If the current combination has reached length 'k', add it to the result
            if len(curr) == k:
                ans.append(curr[:])
                return

            # Iterate through the range from 'i' to 'n'
            for num in range(i, n + 1):
                curr.append(num)  # Add the number to the current combination
                backtrack(curr, num + 1)  # Recurse with the next number
                curr.pop()  # Backtrack to try other combinations

        ans = []  # List to store all combinations
        backtrack([], 1)  # Start backtracking with an empty combination and start from 1
        return ans

# Test Case 1:
# Input: n = 4, k = 2
# Output: All combinations of 2 numbers from [1, 2, 3, 4]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
print(Solution().combine(4, 2))
# Expected output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

# Test Case 2:
# Input: n = 5, k = 3
# Output: All combinations of 3 numbers from [1, 2, 3, 4, 5]
print(Solution().combine(5, 3))
# Expected output: [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5],
# [3, 4, 5]]

# Test Case 3:
# Input: n = 3, k = 1
# Output: All combinations of 1 number from [1, 2, 3]
print(Solution().combine(3, 1))
# Expected output: [[1], [2], [3]]

"""
https://leetcode.com/problems/combinations/description/
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Notice that for combinations, duplicates are also not allowed. For example, [1, 2] and [2, 1] are the same. We can use 
this observation to deduce that we need to find all subsets of length k.

As such, we can essentially copy paste our code from the previous problem and make some minor modifications. First, 
we have a new base case of curr.length = k. We don't need to continue adding numbers to curr after this because we 
don't care about combinations with a longer length. Like in the first example, the leaves represent the base case and 
are also our answer nodes. So we will add curr to the answer only at a leaf instead of at every node.

In the previous two problems, we iterated over an array and added elements from the array. In this problem, we are 
dealing with the numbers in the range [1, n]. One option to solving this problem would be to create an array 
[1, 2, ..., n] and then just applying the same algorithm on this array. However, we can save some space by just using 
the for loop's iteration variable.

We still make use of the i argument. Initially, i = 1 indicates we are considering 1 and all numbers after it. We 
iterate with a for loop variable num from i to n. For each num, we add it to curr and then pass num + 1 to the next 
backtrack call.

#----------------------------------------------------------------------------------#

Approach: Backtracking
Intuition

We are given that n <= 20. Typically, problems that ask you to find all of something with low bounds can be solved
with backtracking.

In backtracking, we generate all solutions one element at a time. This problem is asking us to generate all possible
combinations, so we will generate combinations one element at a time.

The range of elements we are working with is [1, n]. To generate a combination one element at a time, we will use an
array curr that represents the current combination we are building.

To start, we add the first element 1, so we have curr = [1]. We are locking in this 1 and we will now find all
combinations that start with 1.

To find all combinations that start with 1, we start by adding the first element after 1, which is 2. We now have
curr = [1, 2]. We are locking in this 2 and we will now find all combinations that start with 1, 2.

This continues until we reach the target length k. Let's say that we have finished finding all combinations that start
with [1, 2]. Now what? We backtrack by removing the 2, and we have curr = [1] again. Now, we add the second element
that comes after 1, which is 3. We have curr = [1, 3], and now we need to find all combinations that start with [1, 3].

Once we find all the combinations that start with [1], we backtrack by removing the 1 from curr and adding the next
element. We have curr = [2], and now we need to find all combinations that start with 2.

This process is very recursive in nature. Each time we add an element, we solve a new version of the problem (find all
combinations that start with curr). The initial version of the problem is to find all combinations that start with [],
which represents all possible combinations.

Trees

The best way to think about the backtracking process is by modeling it as a tree. You can imagine the solution space
as a tree, with each node representing a version of curr. Label each node with a number that represents the last number
in curr. Moving to a child is like adding the child's label to curr.

To prevent duplicate combinations like [1, 2] and [2, 1], a node only has children with labels greater than its own.

Given n = 4 and k = 2, here is the backtracking tree:

The root node represents an empty []. From the root, every node's curr represents the path taken from the root. The
nodes at depth k represent the answer combinations (highlighted in green).

Solving this problem is equivalent to "traversing" this tree. The easiest way to perform the traversal is by using
recursion and passing curr as an argument.

Think of each call to the recursive function as being a node in the tree. In each call, we need to iterate over the
numbers greater than the label of the current node. We can pass an argument firstNum representing the first number we
should start iterating from.

For each num in [firstNum, n], we add it to curr and then make a recursive call passing curr and num + 1 as firstNum.
This ensures that we only consider numbers greater than the ones we have already added. Modifying curr and making a
recursive call is equivalent to "traversing" to a child node in the tree.

When we return from a function call, it's equivalent to moving back up the tree (exactly like in a DFS). When we moved
from a parent to a child, we added an element to curr. When we move from a child back to its parent, we need to remove
the element we added from curr. This is the "backtracking" step.

The following is an implementation of this backtrack function, which is essentially performing a DFS on the solution
space tree.
"""
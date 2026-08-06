from typing import List

class Solution:
    # top-down solution
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 1. A recursive function that computes the minimum cost to reach the top from step 'i'.
        def dp(i):
            # 3. Base case: If i is 0 or 1, it means we are at the bottom or first step, so cost is 0.
            if i <= 1:
                return 0

            # If the result for step 'i' is already computed, return it from the memoization dictionary.
            if i in memo:
                return memo[i]

            # 2. Recurrence relation: The cost to reach step 'i' is the minimum of:
            #    - Coming from step i-1 plus the cost of step i-1
            #    - Coming from step i-2 plus the cost of step i-2
            memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
            return memo[i]

        # Memoization dictionary to store the minimum cost to reach each step.
        memo = {}
        # Return the minimum cost to reach the top, which is at the length of the cost list.
        return dp(len(cost))


# Test cases
sol = Solution()

# Test case 1: You can either step on [10, 15] or step on [15, 10], both cost 15.
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
print(sol.minCostClimbingStairs([10, 15, 20]))  # Output: 15

# Test case 2: The best way is to take the steps with the least cost [1, 100, 1, 1, 1, 100, 1, 1].
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # Output: 6

"""
https://leetcode.com/problems/min-cost-climbing-stairs/description/
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you
can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

#--------------------------------------------------------------------------------------------#

Overview
We can make two important observations about this problem. First, we need to find the maximum or minimum of something.
Second, we have to make decisions that might look different depending on decisions we made previously. These
characteristics are typical of a dynamic programming problem. In this case, we need to make decisions about either
taking 1 step or 2 steps at a time, and our goal is to minimize the overall cost.

If you're new to dynamic programming, this question may seem more like a medium. Don't worry though, this is a great
problem for getting started with dynamic programming. Generally, there are two main ways to implement a dynamic
programming algorithm - top-down and bottom-up. In this article, we will take a look at both.

Before we begin, let's clear up some of the confusion surrounding the problem statement.

The "top of the floor" does not refer to the final index of costs. We actually need to "arrive" beyond the array's
bounds.

"""
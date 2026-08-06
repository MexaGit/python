from typing import List

class Solution:
    # Recursion with Memoization
    def climbStairs(self, n: int) -> int:
        # Initialize a memoization list to store the number of ways to climb to each step
        memo = [0] * (n + 1)
        # Start climbing from the 0th step
        return self.climb_Stairs(0, n, memo)

    def climb_Stairs(self, i: int, n: int, memo: List[int]) -> int:
        # If the current index exceeds the number of steps, return 0 (invalid path)
        if i > n:
            return 0

        # If we have reached the top step, return 1 (valid path)
        if i == n:
            return 1

        # If the value has already been computed, return the cached value
        if memo[i] > 0:
            return memo[i]

        # Calculate the number of ways to climb to the next step (i + 1)
        # and the step after next (i + 2), and store the result in the memo
        memo[i] = self.climb_Stairs(i + 1, n, memo) + self.climb_Stairs(i + 2, n, memo)

        return memo[i]

# Test cases
solution = Solution()

# Test case 1: Climbing 2 steps
n1 = 2
# There are 2 ways to climb 2 steps: (1+1) or (2)
print(solution.climbStairs(n1))  # Output: 2

# Test case 2: Climbing 3 steps
n2 = 3
# There are 3 ways to climb 3 steps: (1+1+1), (1+2), (2+1)
print(solution.climbStairs(n2))  # Output: 3

"""
https://leetcode.com/problems/climbing-stairs/description/
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#-------------------------------------------------------------------------------------------#

Solution

Approach 2: Recursion with Memoization
Algorithm
In the previous approach we are redundantly calculating the result for every step. Instead, we can store the result at
each step in memo array and directly returning the result from the memo array whenever that function is called again.

In this way we are pruning recursion tree with the help of memo array and reducing the size of recursion tree upto n.
"""
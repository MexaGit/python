# Python3
class Solution:
    # Dynamic Programming
    def climbStairs(self, n: int) -> int:
        # Base case: If there is only one step, there is only one way to climb it
        if n == 1:
            return 1

        # Create a list to store the number of ways to reach each step
        dp = [0 for _ in range(n + 1)]

        # Base cases
        dp[1] = 1  # There is 1 way to climb to the first step
        dp[2] = 2  # There are 2 ways to climb to the second step: (1+1) or (2)

        # Fill the dp array for steps from 3 to n
        for i in range(3, n + 1):
            # The number of ways to reach step i is the sum of the ways to reach
            # the previous step (i-1) and the step before that (i-2)
            dp[i] = dp[i - 1] + dp[i - 2]

        # The answer is the number of ways to reach the nth step
        return dp[n]

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
Approach 3: Dynamic Programming
Algorithm
As we can see this problem can be broken into subproblems, and it contains the optimal substructure property i.e. 
its optimal solution can be constructed efficiently from optimal solutions of its subproblems, we can use dynamic 
programming to solve this problem.

One can reach i'th step in one of the two ways:
    Taking a single step from (i−1)th step.
    Taking a step of 2 from (i−2)th step.

So, the total number of ways to reach i'th is equal to sum of ways of reaching (i−1)th step and ways of reaching 
(i−2)th step.

Let dp[i] denotes the number of ways to reach on i'th step:
dp[i]=dp[i−1]+dp[i−2]
"""


from typing import List

class Solution:
    # bottom-up solution
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # Step 2: Create a DP array of size n+1 to store the minimum cost to reach each step.
        # dp[i] represents the minimum cost to reach the i-th step.
        dp = [0] * (n + 1)

        # Step 3: Base cases are implicitly handled.
        # dp[0] and dp[1] are initialized as 0 since it costs nothing to start from either step 0 or 1.

        # Step 4: Start filling the dp array from step 2 onwards (since dp[0] and dp[1] are already 0).
        for i in range(2, n + 1):
            # Step 5: The minimum cost to reach the i-th step is the minimum of:
            # - Coming from the (i-1)-th step plus the cost of the (i-1)-th step.
            # - Coming from the (i-2)-th step plus the cost of the (i-2)-th step.
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        # Step 6: The result is stored in dp[n], which gives the minimum cost to reach the top.
        return dp[n]


# Test cases
sol = Solution()

# Test case 1: You can either step on [10, 15] or step on [15, 10], both cost 15.
print(sol.minCostClimbingStairs([10, 15, 20]))  # Output: 15

# Test case 2: The best way is to take the steps with the least cost [1, 100, 1, 1, 1, 100, 1, 1].
print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # Output: 6


"""
Converting a top-down solution to a bottom-up one
As discussed in the previous article, there are some benefits of using bottom-up instead of top-down. Sometimes, 
an interviewer may ask for both approaches. The following is a general method for converting a top-down recursive 
solution to a bottom-up iterative one.

1. Start by implementing the top-down approach.

2. Initialize an array dp that is sized according to the state variables. For example, let's say the input to the 
problem was an array nums and an integer k that represents the maximum number of actions allowed. Your array dp would 
be 2D with one dimension of length nums.length and the other of length k. In the top-down approach, we had a function 
dp. We want these two to be equivalent. For example, the value of dp(4, 6) can now be found in dp[4][6].

3. Set your base cases, same as the ones you are using in your top-down function. In the example we just looked at, we 
had dp(0) = dp(1) = 0. We can initialize our dp array values to 0 to implicitly set this base case. As you'll see soon, 
other problems will have more complicated base cases.

4. Write a for-loop(s) that iterate over your state variables. If you have multiple state variables, you will need nested 
for-loops. These loops should start iterating from the base cases and end at the answer state.

5. Now, each iteration of the inner-most loop represents a given state, and is equivalent to a function call to the same 
state in top-down. Copy-paste the logic from your function into the for-loop and change the function calls to accessing 
your array. All dp(...) changes into dp[...].

6. We're done! dp is now an array populated with the answer to the original problem for all possible states. Return the 
answer to the original problem, by changing return dp(...) to return dp[...].

"""